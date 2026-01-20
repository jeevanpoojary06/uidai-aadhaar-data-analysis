# 📊 UIDAI Aadhaar Data Analysis & Prediction (Age 5–17)

This project analyzes UIDAI Aadhaar update data to identify trends, relationships, and future demand for Aadhaar updates in the **age group 5–17**.  
The goal is to help authorities and policymakers understand update patterns and plan service delivery more efficiently.

---

## 🚀 Project Overview

Government UIDAI data is large and complex, making it difficult to extract meaningful insights.  
This project transforms raw UIDAI datasets into a **clean, unified dataset**, performs detailed analysis, and predicts future Aadhaar update demand using **trend-based forecasting**.

An **interactive Streamlit dashboard** is also developed to visualize insights clearly.

---

## 🧩 Problem Statement

There is no simple way to understand:

- Aadhaar update trends over time  
- High-demand age groups  
- Regions requiring more Aadhaar update services  

This project addresses these challenges by analyzing historical UIDAI data and predicting future update demand for the **5–17 age group**.

---

## 🎯 Objectives

- Merge multiple UIDAI datasets into a single dataset  
- Clean and preprocess government data  
- Perform column-to-column and correlation analysis  
- Identify Aadhaar update trends  
- Predict future Aadhaar update volume  
- Visualize insights using Streamlit  

---

## 📁 Datasets Used

Three official UIDAI datasets were used:

### 1. Biometric Updates Dataset
- `bio_age_5_17`
- `bio_age_17_`

### 2. Demographic Updates Dataset
- `demo_age_5_17`
- `demo_age_17_`

### 3. Age-wise Aadhaar Dataset
- `age_0_5`
- `age_5_17`
- `age_18_greater`

### Common Merge Keys
date, state, district, pincode


## ⚙️ Methodology

### 1. Data Merging
- Combined three datasets using common columns

### 2. Data Cleaning
- Removed duplicates  
- Handled missing values  
- Fixed date formats  
- Removed negative values  
- Standardized column names  

### 3. Feature Engineering
- Created a new feature:
total_5_17 = bio_age_5_17 + demo_age_5_17


### 4. Analysis
- Column-to-column analysis  
- Correlation analysis  
- State-wise and time-wise trend analysis  

### 5. Prediction
- Applied trend-based moving average forecasting  
- Predicted future Aadhaar update volume (Age 5–17)  

### 6. Visualization
- Built an interactive Streamlit dashboard  

---

## 📊 Results & Insights

- Strong correlation between biometric and demographic updates  
- Age group **5–17** shows higher update activity  
- Clear temporal trends observed  
- Forecast highlights future high-demand periods  

---

## 🖥️ Streamlit Dashboard

The Streamlit app includes:

- Dataset preview  
- State-wise analysis  
- Correlation table  
- Trend prediction graph  

### Run Locally
```bash
streamlit run app.py
