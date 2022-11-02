-- Convert a given database to UTF8 encoding(utf8mb4, collate utf8mb4_unicode_ci)
USE hbtn_0c_0;
ALTER TABLE first_table MODIFY name VARCHAR(256) COLLATE utf8mb4_unicode_ci;
ALTER TABLE firts_table COLLATE utf8mb4_unicode_ci;
