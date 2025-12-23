import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------- Load and prepare data ----------
@st.cache_data
def load_data():
    df = pd.read_csv("co2_emissions.csv")

    df = df.rename(columns={
        "Entity": "Country",
        "Year": "Year",
        "Annual CO₂ emissions (per capita)": "CO2"
    })

    df = df[["Country", "Year", "CO2"]]

    countries = ["Germany", "United States", "China", "India", "Australia"]
    df_filtered = df[df["Country"].isin(countries)].copy()

    df_filtered = df_filtered.sort_values(["Country", "Year"])
    df_filtered["CO2_change_pct"] = df_filtered.groupby("Country")["CO2"].pct_change() * 100

    return df_filtered

df_filtered = load_data()

# ---------- Sidebar controls (frontend) ----------
st.sidebar.title("CO₂ Explorer")

country = st.sidebar.selectbox(
    "Select a country",
    sorted(df_filtered["Country"].unique())
)

years = df_filtered["Year"].unique()
min_year = int(years.min())
max_year = int(years.max())

year_range = st.sidebar.slider(
    "Select year range",
    min_year,
    max_year,
    (min_year, max_year)
)

# ---------- Filter data (backend logic) ----------
mask = (
    (df_filtered["Country"] == country) &
    (df_filtered["Year"] >= year_range[0]) &
    (df_filtered["Year"] <= year_range[1])
)
df_country = df_filtered[mask]

# ---------- Main page ----------
st.title("CO₂ Emissions Per Capita")
st.subheader(f"{country} — {year_range[0]} to {year_range[1]}")

# Text summary
if not df_country.empty:
    latest_row = df_country.sort_values("Year").iloc[-1]
    latest_year = int(latest_row["Year"])
    latest_co2 = latest_row["CO2"]

    st.markdown(
        f"- Latest available year: **{latest_year}**  \n"
        f"- CO₂ emissions per capita: **{latest_co2:.2f} tonnes**"
    )
else:
    st.warning("No data available for this selection.")

# Line chart: CO₂ over time
if not df_country.empty:
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df_country["Year"], df_country["CO2"], marker="o")
    ax.set_xlabel("Year")
    ax.set_ylabel("CO₂ per capita (tonnes)")
    ax.set_title(f"CO₂ emissions per capita — {country}")
    ax.grid(alpha=0.3)
    st.pyplot(fig)

# Optional: show raw data
st.markdown("### Data")
st.dataframe(df_country.reset_index(drop=True))
