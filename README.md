# 📊 COVID-19 Data Cleaning & Visualization Project

This project demonstrates data cleaning, transformation, and visual analysis of global COVID-19 trends using a sample from the OWID (Our World in Data) dataset. The project is written in Python using `pandas`, `NumPy`, and `matplotlib`.

---

## 🧾 Project Overview

The goals of this project include:

- Handling missing values
- Generating smoothed trends using rolling averages
- Aggregating data by country
- Visualizing:
  - 📈 Total COVID-19 cases over time
  - 🧱 Top 10 countries by total deaths
  - 🥧 Vaccine distribution among the top 10 countries

---

## 📁 Files Included

| File Name                     | Description                                                |
|------------------------------|------------------------------------------------------------|
| [`covid_data_cleaning.py`](covid%20data%20cleaning.py) | Main Python script for data analysis and plotting           |
| [`sample_owid_covid_data.csv`](sample_owid_covid_data.csv) | Sample COVID-19 dataset containing global data by OWID      |

---

## 📈 Key Steps Performed

- **Data Cleaning**
  - Checked for and printed missing values
  - Converted `date` column to datetime format
  - Sorted data by country and date

- **Feature Engineering**
  - Created `daily_vaccinations` column using `.diff()`
  - Computed a 5-day rolling mean for vaccination trends

- **Visualizations**
  - Line chart: Total cases over time
  - Bar chart: Top 10 countries by total deaths
  - Pie chart: Vaccine distribution among the top 10 countries

---

## 🔧 Tools & Libraries Used

- Python 3
- pandas
- NumPy
- matplotlib

---

## 📚 Dataset Source

This project uses a sample based on the full dataset from:

📌 [Our World in Data – COVID-19](https://ourworldindata.org/covid-deaths)  
Original full dataset:  
📎 [`owid-covid-data.csv`](https://covid.ourworldindata.org/data/owid-covid-data.csv)

---

## 💡 Future Improvements

- Add more advanced time-series smoothing
- Compare trends between continents
- Deploy charts on a Streamlit or Flask app
- Automate updates with live data from OWID

---

## 🤝 Contribution & Licensing

This project is educational and open-source. Feel free to fork and improve it!

---

