#!/bin/env bash

echo "--------------------------"

# reset db
mariadb -uroot -p$MARIADB_ROOT_PASSWORD -e "DROP DATABASE IF EXISTS pa25; CREATE DATABASE pa25;"

for file in $(ls *.sql); do

	# mariadb -uroot -p$MARIADB_ROOT_PASSWORD "$DB_NAME" < "$file"
	mariadb -uroot -p$MARIADB_ROOT_PASSWORD pa25 < "$file"

	if [[ $? -ne 0 ]]; then
		echo "db-init ERROR: executing '$file' has returned :"
		echo "$cmd"
		exit 1
	fi

	echo "db-init: Success for '$file'"
done
