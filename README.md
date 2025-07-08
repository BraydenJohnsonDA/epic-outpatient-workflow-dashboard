# Epic Outpatient Workflow Dashboard

This project was developed by Brayden Johnson as a technical demonstration for the Epic Outpatient Clinical System Analyst interview at Freeman Health System. It simulates how an Epic analyst might support outpatient operations by identifying workflow delays and proposing system-level improvements based on mock data.

## Project Purpose

The goal of this project is to showcase how outpatient visit data can be used to uncover inefficiencies in provider workflows, chart closure times, and order entry delays. It demonstrates how data modeling, dashboard design, and Epic-specific thinking can support operational performance in a healthcare environment.

## Tools and Technologies

- **Python**: Used to generate realistic mock outpatient data
- **Power BI**: Used for data modeling and dashboard creation
- **DAX (Data Analysis Expressions)**: Used to calculate time-based performance metrics
- **GitHub**: Used for version control and professional documentation

## Files Included

| File Name                                       | Description                                                                 |
|------------------------------------------------|-----------------------------------------------------------------------------|
| `generate_epic_outpatient_mock_data.py`        | Python script that generates mock outpatient visit data                     |
| `epic_outpatient_mock_data.csv`                | Simulated dataset used in the Power BI dashboard                           |
| `Brayden_Johnson_Outpatient_Workflow_Dashboard.pdf` | One-page executive summary used for the interview presentation             |
| `outpatient_dashboard_screenshot.png`          | Screenshot of the final Power BI dashboard                                 |
| `epic_outpatient_analyst_dashboard.pbix`       | (Optional) Power BI file with all visuals and data model                   |

## Project Overview

The dataset includes timestamped events for check-in, provider sign-in, order entry, chart closure, and discharge for 100 outpatient visits across multiple departments and providers. Key performance indicators (KPIs) were calculated using DAX, including:

- Time from check-in to discharge
- Time from provider sign-in to chart closure
- Time from provider sign-in to order entry
- Flags for delayed charting (greater than 30 minutes)

The Power BI dashboard includes:

- KPI cards summarizing average visit duration, chart closure time, and order entry delay
- Department-level and provider-level bar charts for performance comparison
- A time-series line chart to observe trends in chart closure time
- A donut chart highlighting the ratio of delayed versus on-time charting

## How to Use This Project

1. Run the Python script to generate mock data, or use the included CSV file
2. Load the CSV into Power BI Desktop
3. Use the DAX calculations described in the PDF to create new columns and measures
4. Rebuild or explore the included visuals for workflow insight and performance analysis

## Summary

This project represents how a system analyst can use data to identify workflow inefficiencies, support clinical users, and contribute to system-level improvements within the Epic environment. It reflects the analytical, operational, and communication skills required for success in a clinical systems analyst role.
