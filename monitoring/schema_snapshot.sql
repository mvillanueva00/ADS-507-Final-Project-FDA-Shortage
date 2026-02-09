-- This output will be captured into the monitoring report artifact.
-- Schema snapshot: tables, columns, and views

-- List tables
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE()
  AND table_type = 'BASE TABLE'
ORDER BY table_name;

-- List columns
SELECT table_name, column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_schema = DATABASE()
ORDER BY table_name, ordinal_position;

-- List views 
SELECT table_name AS view_name
FROM information_schema.views
WHERE table_schema = DATABASE()
ORDER BY table_name;

-- Show create view statements for key views
SHOW CREATE VIEW current_package_shortages;
SHOW CREATE VIEW multi_package_shortages;
SHOW CREATE VIEW manufacturer_risk_analysis;
SHOW CREATE VIEW current_manufacturer_risk;

-- Show create table statements for key tables
SHOW CREATE TABLE raw_ndc;
SHOW CREATE TABLE raw_ndc_packaging;
SHOW CREATE TABLE raw_drug_shortages;
SHOW CREATE TABLE shortages_with_ndc;