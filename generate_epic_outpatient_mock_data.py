import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define parameters
num_records = 100  # You can change this
departments = ['Primary Care', 'Cardiology', 'Endocrinology', 'Neurology']
providers = ['Dr. Smith', 'Dr. Johnson', 'Dr. Patel', 'Dr. Lee']
visit_types = ['Follow-up', 'New Patient', 'Consultation']

# Initialize storage
data = []

# Base date for generating realistic visit dates
start_date = datetime.today().replace(hour=8, minute=0, second=0, microsecond=0)

# Loop to generate mock rows
for i in range(num_records):
    patient_id = f"P{i+1:04d}"
    department = random.choice(departments)
    provider = random.choice(providers)
    visit_type = random.choice(visit_types)
    
    # Generate timestamps
    visit_day = start_date + timedelta(days=random.randint(0, 30))
    check_in = visit_day + timedelta(minutes=random.randint(0, 20))
    provider_sign_in = check_in + timedelta(minutes=random.randint(5, 15))
    order_entry = provider_sign_in + timedelta(minutes=random.randint(2, 8))
    chart_close = provider_sign_in + timedelta(minutes=random.randint(15, 45))
    discharge = chart_close + timedelta(minutes=random.randint(1, 10))

    # Append to list
    data.append([
        patient_id, department, provider, visit_type,
        check_in, provider_sign_in, order_entry, chart_close, discharge
    ])

# Create DataFrame
columns = ['PatientID', 'Department', 'Provider', 'VisitType',
           'CheckInTime', 'ProviderSignIn', 'OrderEntry', 'ChartClose', 'Discharge']
df = pd.DataFrame(data, columns=columns)

# Export to CSV
df.to_csv("epic_outpatient_mock_data.csv", index=False)
print("Mock data generated and saved to 'epic_outpatient_mock_data.csv'")
