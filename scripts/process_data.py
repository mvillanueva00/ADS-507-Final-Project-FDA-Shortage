"""
FDA Data Processing Script
Cleans and normalizes the downloaded FDA datasets into structured CSV tables
"""

import pandas as pd
import json
import os

print("Starting data processing...")

# ============================================
# Process NDC Dataset
# ============================================
print("\n1. Processing NDC dataset...")

try:
    # Load the NDC JSON file
    with open('data/drug-ndc-0001-of-0001.json', 'r') as f:
        ndc_data = json.load(f)
    
    # Extract results into DataFrame
    df_ndc = pd.DataFrame(ndc_data['results'])
    print(f"   Loaded {len(df_ndc)} NDC records")
    
    # Create core NDC products table
    ndc_core_columns = [
        'product_ndc', 'generic_name', 'labeler_name', 'brand_name',
        'finished', 'marketing_category', 'dosage_form', 'route',
        'product_type', 'marketing_start_date', 'application_number'
    ]
    
    # Only keep columns that exist
    available_columns = [col for col in ndc_core_columns if col in df_ndc.columns]
    ndc_core = df_ndc[available_columns].copy()
    
    # Save core NDC table
    ndc_core.to_csv('data/ndc_core.csv', index=False)
    print(f"   ✓ Created ndc_core.csv ({len(ndc_core)} products)")
    
    # Extract packaging information (one-to-many relationship)
    packaging_records = []
    for idx, row in df_ndc.iterrows():
        product_ndc = row.get('product_ndc')
        packaging_list = row.get('packaging', [])
        
        if isinstance(packaging_list, list):
            for pkg in packaging_list:
                packaging_records.append({
                    'product_ndc': product_ndc,
                    'package_ndc': pkg.get('package_ndc'),
                    'description': pkg.get('description'),
                    'marketing_start_date': pkg.get('marketing_start_date')
                })
    
    ndc_packaging = pd.DataFrame(packaging_records)
    ndc_packaging.to_csv('data/ndc_packaging.csv', index=False)
    print(f"   ✓ Created ndc_packaging.csv ({len(ndc_packaging)} packages)")
    
except Exception as e:
    print(f"   ✗ Error processing NDC dataset: {e}")

# ============================================
# Process Drug Shortages Dataset
# ============================================
print("\n2. Processing Drug Shortages dataset...")

try:
    # Note: This is a placeholder - you'll need to get actual drug shortage data
    # from FDA's drug shortage database at:
    # https://www.accessdata.fda.gov/scripts/drugshortages/default.cfm
    
    # For now, create a simple structure that matches what you'll need
    print("   Note: Using placeholder for drug shortage data")
    print("   You'll need to download actual shortage data from FDA drug shortage database")
    
    # Create empty template
    shortage_template = pd.DataFrame(columns=[
        'package_ndc', 'generic_name', 'company_name', 'status',
        'therapeutic_category', 'initial_posting_date', 'update_date',
        'dosage_form', 'reason'
    ])
    
    shortage_template.to_csv('data/drug_shortages_core.csv', index=False)
    print("   ✓ Created drug_shortages_core.csv template")
    
    # Create contacts template
    contacts_template = pd.DataFrame(columns=['package_ndc', 'contact_info'])
    contacts_template.to_csv('data/shortage_contacts.csv', index=False)
    print("   ✓ Created shortage_contacts.csv template")
    
except Exception as e:
    print(f"   ✗ Error processing Drug Shortages dataset: {e}")

print("\n✓ Data processing complete!")
print("\nGenerated files in data/ directory:")
print("  - ndc_core.csv")
print("  - ndc_packaging.csv")
print("  - drug_shortages_core.csv")
print("  - shortage_contacts.csv")
print("\nNext step: Load these CSV files into MySQL")
