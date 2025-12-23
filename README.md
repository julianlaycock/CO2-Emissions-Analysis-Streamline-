# CO₂ Emissions Analysis – Streamlit App

An interactive web application built with **Streamlit** to explore historical **CO₂ emissions per capita** for selected countries.

The app lets you:

- **Select a country** and **year range**
- View **CO₂ emissions per capita over time**
- Switch between **absolute levels** and **year-over-year percentage change**
- See **summary metrics** (latest value, change over time, period covered)
- Compare countries using a **bar chart**
- **Download** the filtered dataset as CSV

---

## 🔧 Features

**1. Interactive controls**

- **Country selector** in the sidebar  
- **Year range slider** to focus on specific periods  

**2. Summary metrics**

For the selected country and period, the app shows:

- **Latest CO₂ per capita** (tonnes per person)  
- **Change vs first year in the selected range** (absolute and percentage, where possible)  
- **Period covered** (start year – end year)

**3. Trend visualisation**

- Line chart of **CO₂ emissions per capita** over time  
- Toggle to switch between:
  - **CO₂ per capita**
  - **Year-over-year change (%)**

**4. Country comparison**

- Bar chart comparing countries by:
  - **Average CO₂ per capita**, or  
  - **Latest available CO₂ per capita**

**5. Data table and download**

- Filtered data table for the selected country and period  
- **Download button** to export the filtered data as a CSV file

---

## 📦 Installation Clone the repository: 

```bash git clone git@github.com:julianlaycock/CO2-Emissions-Analysis-Streamline-.git cd CO2-Emissions-Analysis-Streamline-

---

## 📁 Project structure

```text
.
├── app.py               # Streamlit app
├── co2_emissions.csv    # Source data (CO₂ emissions per capita)
└── README.md            # Project documentation

