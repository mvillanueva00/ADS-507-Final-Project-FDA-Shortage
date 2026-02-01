
# Monitoring
This folder do monitoring checks for the FDA pipiline.

Monitoring is executed automatically in Github Actions after the pipeline.
A report is generatd at runtime and uploaded as an artifact.

Monitoring focuses on pipeline health and data quality. Business analytics are handled separately through SQL analysis queries and the Streamlit dashboard.

Purpose of monitoring is to analyse:
Did the pipeline run?
Did tables load?
Did the join work?
Is data missing or broken?

pipeline_health.sql file checks row counts and confirms pipeline ran end to end
Eg-raw_ndc rows > 0
raw_drug_shortages rows > 0
shortages_with_ndc exists

data_quality_checks.sql file Checks missing key fields,Ensures data isn’t broken


