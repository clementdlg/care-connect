#!/bin/env bash

echo "--------------------------"

files=$(ls /sql/*.sql)
if [[ -z "$files" ]]; then
		printf "%s\n%s\n" "db-init ERROR: No '.sql' files found at /sql" "db-init HINT: This container must be run using a bindmount like '-v ./sql:/sql'"
		exit 1
fi

# reset db
mariadb -uroot -p$MARIADB_ROOT_PASSWORD -e "DROP DATABASE IF EXISTS $DB_NAME; CREATE DATABASE $DB_NAME;"

for file in $(ls /sql/*.sql); do

	cmd=$(mariadb -uroot -p$MARIADB_ROOT_PASSWORD $DB_NAME < "$file" 2>&1)

	if [[ $? -ne 0 ]]; then
		echo "db-init ERROR: executing '$file' has returned :"
		echo "$cmd"
		exit 1
	fi

	echo "db-init: Success for '$file'"
done
echo "db-init: Success. All the sql files have been executed"
echo "--------------------------"
