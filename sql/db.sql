------------------------------------------------------------------
-- 1) TABLE: subscription_plan_table
------------------------------------------------------------------
CREATE TABLE subscription_plan_table(
    subscription_plan_id BYTE,
    max_size SMALLINT NOT NULL,
    default_consultation SMALLINT NOT NULL,
    chatbot_access SMALLINT NOT NULL,
    activities VARCHAR(50) NOT NULL,
    contract_id VARCHAR(46),
    PRIMARY KEY(subscription_plan_id)
	FOREIGN KEY contract_id REFERENCES contracts_table(contract_id)
);

------------------------------------------------------------------
-- 2) TABLE: administrator_table
------------------------------------------------------------------
CREATE TABLE administrator_table(
    administrator_id VARCHAR(50),
    email VARCHAR(255) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    password CHAR(128) NOT NULL,
    PRIMARY KEY(administrator_id),
    UNIQUE(email)
);

------------------------------------------------------------------
-- 3) TABLE: contracts_table 
------------------------------------------------------------------
CREATE TABLE contracts_table(
    contract_id VARCHAR(46),
    sign_at DATETIME NOT NULL,
    file VARCHAR(255) NOT NULL,
    company_id VARCHAR(43),
    PRIMARY KEY(contract_id),
    UNIQUE(file)
	FOREIGN KEY (company_id) REFERENCES company_table(company_id)
);

------------------------------------------------------------------
-- 4) TABLE: estimates_table (ex-estimates)
------------------------------------------------------------------
CREATE TABLE estimates_table(
    estimate_id VARCHAR(46),
    made_at DATETIME NOT NULL,
    file VARCHAR(255) NOT NULL,
    status BOOLEAN NOT NULL,
    company_id VARCHAR(43),
    PRIMARY KEY(estimate_id),
    UNIQUE(file)
	FOREIGN KEY (company_id) REFERENCES company_table(company_id)
);

------------------------------------------------------------------
-- 5) TABLE: bill_table
------------------------------------------------------------------
CREATE TABLE bill_table(
    bill_id VARCHAR(41),
    payed_at DATETIME NOT NULL,
    file VARCHAR(255) NOT NULL,
    company_id VARCHAR(43),
    PRIMARY KEY(bill_id),
    UNIQUE(file)
	FOREIGN KEY (company_id) REFERENCES company_table(company_id)
);

------------------------------------------------------------------
-- 6) TABLE: categories_table
------------------------------------------------------------------
CREATE TABLE categories_table(
    category_id VARCHAR(47),
    title VARCHAR(255) NOT NULL,
    PRIMARY KEY(category_id),
    UNIQUE(title)
);

------------------------------------------------------------------
-- 7) TABLE: ngo_table
------------------------------------------------------------------
CREATE TABLE ngo_table(
    ngo_id VARCHAR(40),
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    country VARCHAR(50) NOT NULL,
    type VARCHAR(255) NOT NULL,
    website VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    administrator_id VARCHAR(50),
    PRIMARY KEY(ngo_id),
    FOREIGN KEY(administrator_id) REFERENCES administrator_table(administrator_id)
);

------------------------------------------------------------------
-- 8) TABLE: company_table
------------------------------------------------------------------
CREATE TABLE company_table(
    company_id VARCHAR(43),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    registration_number VARCHAR(50) NOT NULL,
    registration_date DATE NOT NULL,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(50) NOT NULL,
    inscription_date DATETIME NOT NULL,
    revenue BIGINT NOT NULL,
    size BIGINT NOT NULL,
    password CHAR(128) NOT NULL,
    administrator_id VARCHAR(50),
    PRIMARY KEY(company_id),
    UNIQUE(name),
    UNIQUE(email),
    UNIQUE(registration_number),
    FOREIGN KEY(administrator_id) REFERENCES administrator_table(administrator_id)
);

------------------------------------------------------------------
-- 9) TABLE: contractor_table
------------------------------------------------------------------
CREATE TABLE contractor_table(
    contractor_id VARCHAR(47),
    registration_number VARCHAR(50) NOT NULL,
    registration_date DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    service VARCHAR(255) NOT NULL,
    service_price INT NOT NULL,
    password CHAR(128) NOT NULL,
    street VARCHAR(255) NOT NULL,
    city VARCHAR(255),
    country VARCHAR(50) NOT NULL,
    inscription_date DATETIME NOT NULL,
    administrator_id VARCHAR(50),
    PRIMARY KEY(contractor_id),
    UNIQUE(registration_number),
    UNIQUE(email),
    UNIQUE(phone),
    FOREIGN KEY(administrator_id) REFERENCES administrator_table(administrator_id)
);

------------------------------------------------------------------
-- 10) TABLE: event_table
------------------------------------------------------------------
CREATE TABLE event_table(
    event_id VARCHAR(42),
    created_at DATETIME NOT NULL,
    begin_at DATETIME NOT NULL,
    end_at DATETIME NOT NULL,
    place VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    ngo_id VARCHAR(40),
    administrator_id VARCHAR(50),
    PRIMARY KEY(event_id),
    FOREIGN KEY(ngo_id) REFERENCES ngo_table(ngo_id),
    FOREIGN KEY(administrator_id) REFERENCES administrator_table(administrator_id)
);

------------------------------------------------------------------
-- 11) TABLE: subject_table
------------------------------------------------------------------
CREATE TABLE subject_table(
    subject_id CHAR(43),
    subject_title CHAR(255) NOT NULL,
    category_id VARCHAR(47) NOT NULL,
    PRIMARY KEY(subject_id),
    UNIQUE(subject_title),
    FOREIGN KEY(category_id) REFERENCES categories_table(category_id)
);

------------------------------------------------------------------
-- 12) TABLE: collaborator_table
------------------------------------------------------------------
CREATE TABLE collaborator_table(
    collaborator_id CHAR(49),
    email VARCHAR(255) NOT NULL,
    birthday DATE NOT NULL,
    role VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    password CHAR(128) NOT NULL,
    company_id VARCHAR(43) NOT NULL,
    PRIMARY KEY(collaborator_id),
    UNIQUE(email),
    FOREIGN KEY(company_id) REFERENCES company_table(company_id)
);

------------------------------------------------------------------
-- 13) TABLE: posts_table
------------------------------------------------------------------
CREATE TABLE posts_table(
    post_id CHAR(42),
    post_title VARCHAR(255) NOT NULL,
    text TEXT NOT NULL,
    parent_id CHAR(42) NOT NULL,
    created_at DATETIME NOT NULL,
    collaborator_id CHAR(49) NOT NULL,
    subject_id CHAR(43) NOT NULL,
    PRIMARY KEY(post_id),
    FOREIGN KEY(collaborator_id) REFERENCES collaborator_table(collaborator_id),
    FOREIGN KEY(subject_id) REFERENCES subject_table(subject_id)
);

------------------------------------------------------------------
-- 15) TABLE: appointment_table
------------------------------------------------------------------
CREATE TABLE appointment_table(
    collaborator_id CHAR(49),
    contractor_id VARCHAR(47),
    appointment_date DATETIME NOT NULL,
    took DATETIME NOT NULL,
    note BYTE,
    appointment_bill VARCHAR(255),
    PRIMARY KEY(collaborator_id, contractor_id),
    FOREIGN KEY(collaborator_id) REFERENCES collaborator_table(collaborator_id),
    FOREIGN KEY(contractor_id) REFERENCES contractor_table(contractor_id)
);

------------------------------------------------------------------
-- 16) TABLE: book_event_table (ex-book_event)
------------------------------------------------------------------
CREATE TABLE book_event_table(
    collaborator_id CHAR(49),
    event_id VARCHAR(42),
    book_at DATETIME NOT NULL,
    PRIMARY KEY(collaborator_id, event_id),
    FOREIGN KEY(collaborator_id) REFERENCES collaborator_table(collaborator_id),
    FOREIGN KEY(event_id) REFERENCES event_table(event_id)
);

------------------------------------------------------------------
-- 17) TABLE: likes_table (ex-likes)
------------------------------------------------------------------
CREATE TABLE likes_table(
    collaborator_id CHAR(49),
    post_id CHAR(42),
    likes_at DATETIME NOT NULL,
    PRIMARY KEY(collaborator_id, post_id),
    FOREIGN KEY(collaborator_id) REFERENCES collaborator_table(collaborator_id),
    FOREIGN KEY(post_id) REFERENCES posts_table(post_id)
);

------------------------------------------------------------------
-- 18) TABLE: reports_table
------------------------------------------------------------------
CREATE TABLE reports_table(
    contractor_id VARCHAR(47),
    post_id CHAR(42),
    reports_at DATETIME NOT NULL,
    PRIMARY KEY(contractor_id, post_id),
    FOREIGN KEY(contractor_id) REFERENCES contractor_table(contractor_id),
    FOREIGN KEY(post_id) REFERENCES posts_table(post_id)
);

------------------------------------------------------------------
-- 19) TABLE: give_table (ex-give)
------------------------------------------------------------------
CREATE TABLE give_table(
    contractor_id VARCHAR(47),
    ngo_id VARCHAR(40),
    amount INT NOT NULL,
    give_at DATETIME NOT NULL,
    bill VARCHAR(255) NOT NULL,
    PRIMARY KEY(collaborator_table, ngo_id),
    FOREIGN KEY(collaborator_table) REFERENCES collaborator_table(collaborator_id),
    FOREIGN KEY(ngo_id) REFERENCES ngo_table(ngo_id)
);
