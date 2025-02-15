-- 1) subscription_plan_table
CREATE TABLE subscription_plan_table (
    subscription_plan_id     CHAR(54),  -- "subscription_plan-UUID"
    max_size                 SMALLINT NOT NULL,
    default_consultation     SMALLINT NOT NULL,
    chatbot_access           SMALLINT NOT NULL,
    activities               VARCHAR(50) NOT NULL,
    PRIMARY KEY (subscription_plan_id)
);

-- 2) administrator_table
CREATE TABLE administrator_table (
    administrator_id   CHAR(50),  -- "administrator-UUID"
    email              VARCHAR(255) NOT NULL,
    lastname           VARCHAR(50)  NOT NULL,
    firstname          VARCHAR(50)  NOT NULL,
    password           CHAR(128)    NOT NULL,
    PRIMARY KEY (administrator_id),
    UNIQUE(email)
);

-- 3) subject_table
CREATE TABLE subject_table (
    subject_id         CHAR(44),  -- "subject-UUID"
    subject_title      CHAR(255) NOT NULL,
    PRIMARY KEY (subject_id),
    UNIQUE(subject_title)
);

-- 4) company_table
CREATE TABLE company_table (
    company_id             CHAR(44),       -- "company-UUID"
    name                   VARCHAR(255) NOT NULL,
    email                  VARCHAR(255) NOT NULL,
    phone                  VARCHAR(50)  NOT NULL,
    registration_number    VARCHAR(50)  NOT NULL,
    registration_date      DATE         NOT NULL,
    street                 VARCHAR(255) NOT NULL,
    city                   VARCHAR(255) NOT NULL,
    postal_code            VARCHAR(20)  NOT NULL,
    country                VARCHAR(50)  NOT NULL,
    inscription_date       DATETIME     NOT NULL,
    revenue                BIGINT       NOT NULL,
    size                   BIGINT       NOT NULL,
    password               CHAR(128)    NOT NULL,

    administrator_id       CHAR(50),     -- FK -> administrator_table

    PRIMARY KEY (company_id),
    UNIQUE (name),
    UNIQUE (email),
    UNIQUE (registration_number),

    FOREIGN KEY (administrator_id)
        REFERENCES administrator_table(administrator_id)
);

-- 5) contractor_table
CREATE TABLE contractor_table (
    contractor_id        CHAR(46),  -- "contractor-UUID"
    registration_number  VARCHAR(50)  NOT NULL,
    registration_date    DATE         NOT NULL,
    email                VARCHAR(255) NOT NULL,
    phone                VARCHAR(50)  NOT NULL,
    service              VARCHAR(255) NOT NULL,
    service_price        INT          NOT NULL,
    password             CHAR(128)    NOT NULL,
    street               VARCHAR(255) NOT NULL,
    city                 VARCHAR(255),
    country              VARCHAR(50)  NOT NULL,
    inscription_date     DATETIME     NOT NULL,

    administrator_id     CHAR(50),    -- FK -> administrator_table

    PRIMARY KEY (contractor_id),
    UNIQUE (registration_number),
    UNIQUE (email),
    UNIQUE (phone),

    FOREIGN KEY (administrator_id)
        REFERENCES administrator_table(administrator_id)
);

-- 6) event_table
CREATE TABLE event_table (
    event_id            CHAR(42),   -- "event-UUID"
    created_at          DATETIME NOT NULL,
    begin_at            DATETIME NOT NULL,
    end_at              DATETIME NOT NULL,
    place               VARCHAR(255) NOT NULL,
    title               VARCHAR(255) NOT NULL,

    administrator_id    CHAR(50),   -- FK -> administrator_table

    PRIMARY KEY (event_id),

    FOREIGN KEY (administrator_id)
        REFERENCES administrator_table(administrator_id)
);

-- 7) collaborator_table
CREATE TABLE collaborator_table (
    collaborator_id   CHAR(48),  -- "collaborator-UUID"
    email            VARCHAR(255) NOT NULL,
    birthday         DATE         NOT NULL,
    role             VARCHAR(50)  NOT NULL,
    firstname        VARCHAR(50)  NOT NULL,
    lastname         VARCHAR(50)  NOT NULL,
    password         CHAR(128)    NOT NULL,

    company_id       CHAR(44) NOT NULL,  -- FK -> company_table

    PRIMARY KEY (collaborator_id),
    UNIQUE(email),

    FOREIGN KEY (company_id)
        REFERENCES company_table(company_id)
);

-- 8) posts_table
CREATE TABLE posts_table (
    posts_id            CHAR(42),   -- "posts-UUID"
    post_title          VARCHAR(255) NOT NULL,
    text                TEXT         NOT NULL,
    parent_id           CHAR(42)     NOT NULL,
    created_at          DATETIME     NOT NULL,
    reports             INT,

    collaborator_id     CHAR(48) NOT NULL,  -- FK -> collaborator_table
    subject_id          CHAR(44) NOT NULL,  -- FK -> subject_table

    PRIMARY KEY (posts_id),

    FOREIGN KEY (collaborator_id)
        REFERENCES collaborator_table(collaborator_id),

    FOREIGN KEY (subject_id)
        REFERENCES subject_table(subject_id)
);

-- 9) company_subscription_table
CREATE TABLE company_subscription_table (
    company_subscription_id   CHAR(57),   -- "company_subscription-UUID"

    company_id                CHAR(44) NOT NULL,  -- FK -> company_table
    subscription_plan_id      CHAR(54) NOT NULL,  -- FK -> subscription_plan_table

    bonus_consultation        INT       NOT NULL,
    company_subscription_bill VARCHAR(255) NOT NULL,
    contract                  VARCHAR(255) NOT NULL,

    PRIMARY KEY (company_subscription_id),

    FOREIGN KEY (company_id)
        REFERENCES company_table(company_id),

    FOREIGN KEY (subscription_plan_id)
        REFERENCES subscription_plan_table(subscription_plan_id)
);

-- 10) appointment_table
CREATE TABLE appointment_table (
    collaborator_id   CHAR(48),  -- FK -> collaborator_table
    contractor_id     CHAR(46),  -- FK -> contractor_table

    appointment_date  DATETIME NOT NULL,
    took              DATETIME NOT NULL,
    note              TINYINT,
    appointment_bill  VARCHAR(255),

    PRIMARY KEY (collaborator_id, contractor_id),

    FOREIGN KEY (collaborator_id) REFERENCES collaborator_table(collaborator_id),
    FOREIGN KEY (contractor_id)   REFERENCES contractor_table(contractor_id)
);

-- 11) book_event_table
CREATE TABLE book_event_table (
    collaborator_id   CHAR(48),  -- FK -> collaborator_table
    event_id          CHAR(42),  -- FK -> event_table
    book_at           DATETIME NOT NULL,

    PRIMARY KEY (collaborator_id, event_id),

    FOREIGN KEY (collaborator_id) REFERENCES collaborator_table(collaborator_id),
    FOREIGN KEY (event_id)        REFERENCES event_table(event_id)
);

-- 12) likes_table
CREATE TABLE likes_table (
    collaborator_id   CHAR(48),  -- FK -> collaborator_table
    posts_id          CHAR(42),  -- FK -> posts_table
    likes_at          DATETIME NOT NULL,

    PRIMARY KEY (collaborator_id, posts_id),

    FOREIGN KEY (collaborator_id) REFERENCES collaborator_table(collaborator_id),
    FOREIGN KEY (posts_id)        REFERENCES posts_table(posts_id)
);
