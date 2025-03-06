CREATE TABLE users (
  user_id CHAR(36),
  firstname VARCHAR(50) NOT NULL,
  lastname VARCHAR(50) NOT NULL,
  dob DATE NOT NULL,
  phone VARCHAR(50) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password CHAR(128) NOT NULL,
  role VARCHAR(50),
  country VARCHAR(255) NOT NULL,
  city VARCHAR(255) NOT NULL,
  street VARCHAR(255) NOT NULL,
  pc VARCHAR(10) NOT NULL,
  inscription_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  verified BOOLEAN NOT NULL,
  stripe_id VARCHAR(255),
  PRIMARY KEY(user_id),
  UNIQUE(phone),
  UNIQUE(email),
  UNIQUE(stripe_id)
);

CREATE TABLE administrators(
   admin_id CHAR(36),
   PRIMARY KEY(admin_id),
   FOREIGN KEY(admin_id) REFERENCES users(user_id)
);

CREATE TABLE categories(
   category_id CHAR(36),
   title VARCHAR(255) NOT NULL,
   admin_id CHAR(36),
   PRIMARY KEY(category_id),
   UNIQUE(title),
   FOREIGN KEY(admin_id) REFERENCES administrators(admin_id)
);

CREATE TABLE ngo(
   ngo_id CHAR(36),
   name VARCHAR(255) NOT NULL,
   registration_number VARCHAR(50) NOT NULL,
   registration_date DATETIME NOT NULL,
   address VARCHAR(255) NOT NULL,
   country VARCHAR(50) NOT NULL,
   type VARCHAR(255) NOT NULL,
   presentation TEXT NOT NULL,
   website VARCHAR(255) NOT NULL,
   phone VARCHAR(50) NOT NULL,
   stripe_id VARCHAR(50),
   admin_id CHAR(36),
   PRIMARY KEY(ngo_id),
   UNIQUE(name),
   UNIQUE(registration_number),
   UNIQUE(stripe_id),
   FOREIGN KEY(admin_id) REFERENCES administrators(admin_id)
);

CREATE TABLE packs (
   pack_id CHAR(36),
   name VARCHAR(50) NOT NULL,
   creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
   activity_number INT NOT NULL,
   annual_collaborator_price SMALLINT NOT NULL,
   bonus_consultation_price SMALLINT NOT NULL,
   default_consultation_number SMALLINT NOT NULL,
   chatbot_messages_number SMALLINT,
   admin_id CHAR(36) NOT NULL,
   PRIMARY KEY(pack_id),
   FOREIGN KEY(admin_id) REFERENCES administrators(admin_id)
);

CREATE TABLE tickets (
     ticket_id CHAR(36),
     title VARCHAR(255) NOT NULL,
     text TEXT NOT NULL,
     open_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
     close_date DATETIME,
     user_id CHAR(36) NOT NULL,
     admin_id CHAR(36),
     PRIMARY KEY(ticket_id),
     FOREIGN KEY(user_id) REFERENCES users(user_id),
     FOREIGN KEY(admin_id) REFERENCES administrators(admin_id)
);

CREATE TABLE messages (
  ticket_id CHAR(36),
  messages_id CHAR(36),
  text TEXT NOT NULL,
  creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  user_id CHAR(36),
  admin_id CHAR(36),
  PRIMARY KEY(ticket_id, messages_id),
  FOREIGN KEY(ticket_id) REFERENCES tickets(ticket_id),
  FOREIGN KEY(admin_id) REFERENCES administrators(admin_id),
  FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE companies(
   company_id CHAR(36),
   name VARCHAR(255) NOT NULL,
   website VARCHAR(255),
   registration_number VARCHAR(50) NOT NULL,
   registration_date DATE NOT NULL,
   industry VARCHAR(50) NOT NULL,
   revenue INT NOT NULL,
   size INT NOT NULL,
   admin_id CHAR(36),
   PRIMARY KEY(company_id),
   UNIQUE(name),
   UNIQUE(website),
   UNIQUE(registration_number),
   FOREIGN KEY(company_id) REFERENCES users(user_id),
   FOREIGN KEY(admin_id) REFERENCES administrators(admin_id)
);

CREATE TABLE contractors(
   contractor_id CHAR(36),
   registration_number VARCHAR(50) NOT NULL,
   registration_date DATE NOT NULL,
   contract_file VARCHAR(50),
   sign_date VARCHAR(50),
   service VARCHAR(255) NOT NULL,
   service_price INT NOT NULL,
   website VARCHAR(255),
   intervention VARCHAR(50) NOT NULL,
   admin_id CHAR(36),
   PRIMARY KEY(contractor_id),
   UNIQUE(registration_number),
   UNIQUE(contract_file),
   FOREIGN KEY(contractor_id) REFERENCES users(user_id),
   FOREIGN KEY(admin_id) REFERENCES administrators(admin_id)
);

CREATE TABLE events(
   event_id CHAR(36),
   created_at DATETIME NOT NULL,
   begin_at DATETIME NOT NULL,
   end_at DATETIME NOT NULL,
   place VARCHAR(255) NOT NULL,
   title VARCHAR(255) NOT NULL,
   capacity INT NOT NULL,
   ngo_id CHAR(36),
   admin_id CHAR(36),
   PRIMARY KEY(event_id),
   FOREIGN KEY(ngo_id) REFERENCES ngo(ngo_id),
   FOREIGN KEY(admin_id) REFERENCES administrators(admin_id)
);

CREATE TABLE collaborators(
    collaborator_id CHAR(36),
    company_id CHAR(36) NOT NULL,
    PRIMARY KEY(collaborator_id),
    FOREIGN KEY(collaborator_id) REFERENCES users(user_id),
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

CREATE TABLE subjects(
    subject_id CHAR(36),
    collaborator_id CHAR(36) NOT NULL,
    title CHAR(255) NOT NULL,
    creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    category_id CHAR(36) NOT NULL,
    PRIMARY KEY(subject_id),
    UNIQUE(title),
    FOREIGN KEY(category_id) REFERENCES categories(category_id),
    FOREIGN KEY(collaborator_id) REFERENCES collaborators(collaborator_id)
);

CREATE TABLE calendars(
   contractor_id CHAR(36),
   calendar_id CHAR(36),
   unvailable_begin_date DATETIME NOT NULL,
   unvailable_end_date DATETIME NOT NULL,
   PRIMARY KEY(contractor_id, calendar_id),
   FOREIGN KEY(contractor_id) REFERENCES contractors(contractor_id)
);

CREATE TABLE company_subscriptions(
   company_id CHAR(36),
   company_subscription_id CHAR(36),
   bonus_consultation_number SMALLINT NOT NULL,
   billing_plan VARCHAR(10) NOT NULL,
   status VARCHAR(50),
   pack_id CHAR(36) NOT NULL,
   PRIMARY KEY(company_id, company_subscription_id),
   FOREIGN KEY(company_id) REFERENCES companies(company_id),
   FOREIGN KEY(pack_id) REFERENCES packs(pack_id)
);

CREATE TABLE estimates (
   company_id CHAR(36),
   company_subscription_id CHAR(36),
   file VARCHAR(255) NOT NULL,
   creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
   signature_date DATETIME,
   PRIMARY KEY(company_id, company_subscription_id),
   UNIQUE(file),
   FOREIGN KEY(company_id, company_subscription_id) REFERENCES company_subscriptions(company_id, company_subscription_id)
);

CREATE TABLE bills(
   company_id CHAR(36),
   company_subscription_id CHAR(36),
   bill_id CHAR(36),
   file VARCHAR(255) NOT NULL,
   begin_billing_perdiode_date DATETIME NOT NULL,
   end_billing_perdiode_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
   payed BOOLEAN NOT NULL DEFAULT FALSE,
   PRIMARY KEY(company_id, company_subscription_id, bill_id),
   UNIQUE(file),
   FOREIGN KEY(company_id, company_subscription_id) REFERENCES company_subscriptions(company_id, company_subscription_id)
);

CREATE TABLE contracts (
   company_id CHAR(36),
   company_subscription_id CHAR(36),
   file VARCHAR(255) NOT NULL,
   creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
   signature_date DATETIME,
   PRIMARY KEY(company_id, company_subscription_id),
   UNIQUE(file),
   FOREIGN KEY(company_id, company_subscription_id) REFERENCES company_subscriptions(company_id, company_subscription_id)
);

CREATE TABLE posts(
    post_id CHAR(36),
    text TEXT NOT NULL,
    creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    parent_post_id CHAR(36),
    subject_id CHAR(36) NOT NULL,
    PRIMARY KEY(post_id),
    FOREIGN KEY(parent_post_id) REFERENCES posts(post_id),
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
);

CREATE TABLE booked_events(
    event_id CHAR(36),
    collaborator_id CHAR(36),
    creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(event_id, collaborator_id),
    FOREIGN KEY(event_id) REFERENCES events(event_id),
    FOREIGN KEY(collaborator_id) REFERENCES collaborators(collaborator_id)
);

CREATE TABLE appointments(
    appointment_id CHAR(36),
    contractor_id CHAR(36),
    collaborator_id CHAR(36),
    appointment_date DATETIME NOT NULL,
    creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50),
    bill_file VARCHAR(255) NOT NULL,
    place VARCHAR(6) NOT NULL,
    note SMALLINT,
    PRIMARY KEY(appointment_id),
    UNIQUE(bill_file),
    FOREIGN KEY(contractor_id) REFERENCES contractors(contractor_id),
    FOREIGN KEY(collaborator_id) REFERENCES collaborators(collaborator_id)
);

CREATE TABLE reports(
    report_id CHAR(36),
    collaborator_id CHAR(36),
    title VARCHAR(255) NOT NULL,
    creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    post_id CHAR(36),
    subject_id CHAR(36),
    appointment_id CHAR(36),
    PRIMARY KEY(report_id),
    FOREIGN KEY(collaborator_id) REFERENCES collaborators(collaborator_id),
    FOREIGN KEY(post_id) REFERENCES posts(post_id),
    FOREIGN KEY(appointment_id) REFERENCES appointments(appointment_id),
    FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
);

CREATE TABLE donations(
   collaborator_id CHAR(36),
   ngo_id CHAR(36),
   bill_file VARCHAR(255) NOT NULL,
   creation_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
   amount INT NOT NULL,
   PRIMARY KEY(collaborator_id, ngo_id),
   UNIQUE(bill_file),
   FOREIGN KEY(collaborator_id) REFERENCES collaborators(collaborator_id),
   FOREIGN KEY(ngo_id) REFERENCES ngo(ngo_id)
);


-- ==================================================
-- 1) TABLE : users
-- ==================================================
INSERT INTO users (
    user_id,
    firstname,
    lastname,
    dob,
    phone,
    email,
    password,
    role,
    country,
    city,
    street,
    pc,
    verified
)
VALUES
-- Admin User
('11111111-1111-1111-1111-111111111111',
 'Jean',
 'Dupont',
 '1980-01-01',
 '+33000000001',
 'admin@example.com',
 'df6b9fb15cfdbb7527be5a8a6e39f39e572c8ddb943fbc79a943438e9d3d85ebfc2ccf9e0eccd9346026c0b6876e0e01556fe56f135582c05fbdbb505d46755a',
 'ADMIN',
 'France',
 'Paris',
 '1 Rue Principale',
 '75001',
 1
),
-- Collaborator
('22222222-2222-2222-2222-222222222222',
 'Marie',
 'Martin',
 '1990-05-10',
 '+33000000002',
 'collabo@example.com',
 'df6b9fb15cfdbb7527be5a8a6e39f39e572c8ddb943fbc79a943438e9d3d85ebfc2ccf9e0eccd9346026c0b6876e0e01556fe56f135582c05fbdbb505d46755a',
 'COLLABORATOR',
 'France',
 'Lyon',
 '2 Rue Secondaire',
 '69000',
 1
),
-- Contractor
('33333333-3333-3333-3333-333333333333',
 'Robert',
 'Cotier',
 '1985-09-15',
 '+33000000003',
 'contractor@example.com',
 'df6b9fb15cfdbb7527be5a8a6e39f39e572c8ddb943fbc79a943438e9d3d85ebfc2ccf9e0eccd9346026c0b6876e0e01556fe56f135582c05fbdbb505d46755a',
 'CONTRACTOR',
 'France',
 'Marseille',
 '3 Rue Principale',
 '13000',
 1
),
-- Company User
('44444444-4444-4444-4444-444444444444',
 'Sophie',
 'Entreprise',
 '1987-07-07',
 '+33000000004',
 'company@example.com',
 'df6b9fb15cfdbb7527be5a8a6e39f39e572c8ddb943fbc79a943438e9d3d85ebfc2ccf9e0eccd9346026c0b6876e0e01556fe56f135582c05fbdbb505d46755a',
 'COMPANY',
 'France',
 'Toulouse',
 '4 Rue Principale',
 '31000',
 1
);

-- ==================================================
-- 2) TABLE : administrators
-- ==================================================
INSERT INTO administrators (admin_id)
VALUES
    ('11111111-1111-1111-1111-111111111111');

-- ==================================================
-- 3) TABLE : categories
-- ==================================================
INSERT INTO categories (category_id, title, admin_id)
VALUES
    ('55555555-5555-5555-5555-555555555555', 'Catégorie 1', '11111111-1111-1111-1111-111111111111'),
    ('55555555-5555-5555-5555-666666666666', 'Catégorie 2', '11111111-1111-1111-1111-111111111111');

-- ==================================================
-- 4) TABLE : ngo
-- ==================================================
INSERT INTO ngo (
    ngo_id,
    name,
    registration_number,
    registration_date,
    address,
    country,
    type,
    presentation,
    website,
    phone,
    admin_id
)
VALUES
    ('66666666-6666-6666-6666-666666666666',
     'ONG Exemple',
     'REG-123456',
     '2021-01-01',
     '1 Rue Humanitaire, Paris',
     'France',
     'Humanitaire',
     'Présentation de l’ONG...',
     'https://ong-exemple.fr',
     '+33000000005',
     '11111111-1111-1111-1111-111111111111');

-- ==================================================
-- 5) TABLE : packs
-- ==================================================
INSERT INTO packs (
    pack_id,
    name,
    activity_number,
    annual_collaborator_price,
    bonus_consultation_price,
    default_consultation_number,
    chatbot_messages_number,
    admin_id
)
VALUES
    ('77777777-7777-7777-7777-777777777777',
     'Pack Basic',
     10,
     100,
     50,
     5,
     100,
     '11111111-1111-1111-1111-111111111111');

-- ==================================================
-- 6) TABLE : tickets
-- ==================================================
INSERT INTO tickets (
    ticket_id,
    title,
    text,
    user_id,
    admin_id
)
VALUES
    ('88888888-8888-8888-8888-888888888888',
     'Ticket 1',
     'Mon problème est le suivant...',
     '22222222-2222-2222-2222-222222222222',
     '11111111-1111-1111-1111-111111111111');

-- ==================================================
-- 7) TABLE : messages
-- ==================================================
INSERT INTO messages (
    ticket_id,
    messages_id,
    text,
    user_id
)
VALUES
    ('88888888-8888-8888-8888-888888888888',
     '99999999-9999-9999-9999-999999999999',
     'Pouvez-vous préciser ?',
     '22222222-2222-2222-2222-222222222222');

-- ==================================================
-- 8) TABLE : companies
-- ==================================================
INSERT INTO companies (
    company_id,
    name,
    registration_number,
    registration_date,
    industry,
    revenue,
    size,
    admin_id
)
VALUES
    ('44444444-4444-4444-4444-444444444444',
     'Entreprise Exemple',
     'REG-987654',
     '2020-05-20',
     'Services',
     300000,
     50,
     '11111111-1111-1111-1111-111111111111');

-- ==================================================
-- 9) TABLE : contractors
-- ==================================================
INSERT INTO contractors (
    contractor_id,
    registration_number,
    registration_date,
    service,
    service_price,
    intervention,
    admin_id
)
VALUES
    ('33333333-3333-3333-3333-333333333333',
     'REG-456789',
     '2022-03-15',
     'Consultation',
     1000,
     'France',
     '11111111-1111-1111-1111-111111111111');

-- ==================================================
-- 10) TABLE : events
-- ==================================================
INSERT INTO events (
    event_id,
    created_at,
    begin_at,
    end_at,
    place,
    title,
    capacity,
    ngo_id,
    admin_id
)
VALUES
    ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
     '2023-01-01 10:00:00',
     '2023-01-05 09:00:00',
     '2023-01-05 18:00:00',
     'Salle de conférence, Paris',
     'Conférence bénévole',
     100,
     '66666666-6666-6666-6666-666666666666',
     '11111111-1111-1111-1111-111111111111');

-- ==================================================
-- 11) TABLE : collaborators
-- ==================================================
INSERT INTO collaborators (
    collaborator_id,
    company_id
)
VALUES
    ('22222222-2222-2222-2222-222222222222',  -- Correspond à l'utilisateur Collaborator
     '44444444-4444-4444-4444-444444444444');   -- Correspond à l'utilisateur Company

-- ==================================================
-- 12) TABLE : subjects
-- ==================================================
INSERT INTO subjects (
    subject_id,
    collaborator_id,
    title,
    category_id
)
VALUES
    ('bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
     '22222222-2222-2222-2222-222222222222',
     'Sujet Important',
     '55555555-5555-5555-5555-555555555555');

-- ==================================================
-- 13) TABLE : calendar
-- ==================================================
INSERT INTO calendar (
    contractor_id,
    calendar_id,
    unvailable_begin_date,
    unvailable_end_date
)
VALUES
    ('33333333-3333-3333-3333-333333333333',
     'cccccccc-cccc-cccc-cccc-cccccccccccc',
     '2023-11-01 08:00:00',
     '2023-11-01 17:00:00');

-- ==================================================
-- 14) TABLE : company_subscriptions
-- ==================================================
INSERT INTO company_subscriptions (
    company_id,
    company_subscription_id,
    bonus_consultation_number,
    billing_plan,
    status,
    pack_id
)
VALUES
    ('44444444-4444-4444-4444-444444444444',
     'dddddddd-dddd-dddd-dddd-dddddddddddd',
     10,
     'STANDARD',
     'ACTIVE',
     '77777777-7777-7777-7777-777777777777');

-- ==================================================
-- 15) TABLE : estimates
-- ==================================================
INSERT INTO estimates (
    company_id,
    company_subscription_id,
    file,
    creation_date
)
VALUES
    ('44444444-4444-4444-4444-444444444444',
     'dddddddd-dddd-dddd-dddd-dddddddddddd',
     'devis_entreprise.pdf',
     '2023-10-01 09:00:00');

-- ==================================================
-- 16) TABLE : bills
-- ==================================================
INSERT INTO bills (
    company_id,
    company_subscription_id,
    bill_id,
    file,
    begin_billing_perdiode_date,
    end_billing_perdiode_date,
    payed
)
VALUES
    ('44444444-4444-4444-4444-444444444444',
     'dddddddd-dddd-dddd-dddd-dddddddddddd',
     'eeeeeeee-eeee-eeee-eeee-eeeeeeeeeeee',
     'facture_octobre.pdf',
     '2023-10-01 00:00:00',
     '2023-10-31 23:59:59',
     TRUE);

-- ==================================================
-- 17) TABLE : contracts
-- ==================================================
INSERT INTO contracts (
    company_id,
    company_subscription_id,
    file,
    creation_date
)
VALUES
    ('44444444-4444-4444-4444-444444444444',
     'dddddddd-dddd-dddd-dddd-dddddddddddd',
     'contrat_standard.pdf',
     '2023-09-01 12:00:00');

-- ==================================================
-- 18) TABLE : posts
-- ==================================================
INSERT INTO posts (
    post_id,
    text,
    creation_date,
    parent_post_id,
    subject_id
)
VALUES
    ('ffffffff-ffff-ffff-ffff-ffffffffffff',
     'Voici un texte intéressant lié au sujet',
     '2023-10-15 10:00:00',
     NULL,
     'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb');

-- ==================================================
-- 19) TABLE : booked_events
-- ==================================================
INSERT INTO booked_events (
    event_id,
    collaborator_id,
    creation_date
)
VALUES
    ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa',
     '22222222-2222-2222-2222-222222222222',
     '2023-11-07 09:00:00');

-- ==================================================
-- 20) TABLE : appointments
-- ==================================================
INSERT INTO appointments (
    appointment_id,
    contractor_id,
    collaborator_id,
    appointment_date,
    creation_date,
    status,
    bill_file,
    place,
    note
)
VALUES
    ('99999999-9999-9999-9999-999999999999',
     '33333333-3333-3333-3333-333333333333',
     '22222222-2222-2222-2222-222222222222',
     '2023-12-01 15:00:00',
     '2023-11-30 12:00:00',
     'CONFIRMED',
     'facture_consultation.pdf',
     'Bureau',
     5);

-- ==================================================
-- 21) TABLE : reports
-- ==================================================
INSERT INTO reports (
    report_id,
    collaborator_id,
    title,
    creation_date,
    post_id,
    subject_id,
    appointment_id
)
VALUES
    ('aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaabbbb',
     '22222222-2222-2222-2222-222222222222',
     'pas bien',
 '2023-12-02 18:00:00',
 'ffffffff-ffff-ffff-ffff-ffffffffffff',
 'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb',
 '99999999-9999-9999-9999-999999999999');

-- ==================================================
-- 22) TABLE : donations
-- ==================================================
INSERT INTO donations (
    collaborator_id,
    ngo_id,
    bill_file,
    creation_date,
    amount
)
VALUES
('22222222-2222-2222-2222-222222222222',
 '66666666-6666-6666-6666-666666666666',
 'donation_receipt.pdf',
 '2023-11-25 14:00:00',
 200);

-- =============================================================================
-- FIN DU SCRIPT
-- =============================================================================
