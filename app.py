import streamlit as st
import joblib
import numpy as np
import random
import base64


# PAGE CONFIG

st.set_page_config(
    page_title="CO2 Prediction",
    layout="wide"
)


# LOAD MODEL

model = joblib.load("model.pkl")

# BACKGROUND IMAGE
def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_image = get_base64("amazon_forest.jpg")

page_bg = f"""
<style>

[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

.main {{
    background-color: rgba(0,0,0,0.55);
    padding: 20px;
    border-radius: 15px;
}}

h1, h2, h3, p, label {{
    color: white !important;
}}

.stButton>button {{
    background-color: green;
    color: white;
    font-size: 20px;
    border-radius: 10px;
    padding: 10px 20px;
}}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.title("CO₂ Emissions Prediction App")

st.write("Helping protect the Amazon Rainforest")

# -----------------------------
# RANDOM DEFAULT VALUES
# -----------------------------
if "loaded" not in st.session_state:

    st.session_state.year = random.randint(2010, 2025)
    st.session_state.state_of_production = random.randint(0, 30)
    st.session_state.municipality_of_production = random.randint(0, 500)
    st.session_state.logistics_hub = random.randint(0, 50)
    st.session_state.product_type = random.randint(0, 10)
    st.session_state.port_of_export = random.randint(0, 30)
    st.session_state.exporter = random.randint(0, 100)
    st.session_state.exporter_group = random.randint(0, 20)
    st.session_state.zero_deforestation_brazil_beef = random.randint(0, 1)
    st.session_state.forest_500_beef = random.randint(0, 1)
    st.session_state.importer = random.randint(0, 100)
    st.session_state.country_of_destination = random.randint(0, 100)
    st.session_state.economic_bloc = random.randint(0, 20)
    st.session_state.country_of_destination_trase_id = random.randint(0, 100)

    st.session_state.cattle_deforestation_5_year_total_exposure = random.uniform(0, 10000)

    st.session_state.co2_net_emissions_cattle_deforestation_5_year_total_exposure = random.uniform(0, 100000)

    st.session_state.land_use = random.uniform(0, 10000)
    st.session_state.volume = random.uniform(0, 10000)
    st.session_state.fob = random.uniform(0, 100000)

    st.session_state.loaded = True


# INPUT

col1, col2 = st.columns(2)

with col1:

    year = st.number_input(
        "Year",
        value=st.session_state.year
    )

    state_of_production = st.number_input(
        "State of Production",
        value=st.session_state.state_of_production
    )

    municipality_of_production = st.number_input(
        "Municipality of Production",
        value=st.session_state.municipality_of_production
    )

    logistics_hub = st.number_input(
        "Logistics Hub",
        value=st.session_state.logistics_hub
    )

    product_type = st.number_input(
        "Product Type",
        value=st.session_state.product_type
    )

    port_of_export = st.number_input(
        "Port of Export",
        value=st.session_state.port_of_export
    )

    exporter = st.number_input(
        "Exporter",
        value=st.session_state.exporter
    )

    exporter_group = st.number_input(
        "Exporter Group",
        value=st.session_state.exporter_group
    )

    zero_deforestation_brazil_beef = st.selectbox(
        "Zero Deforestation Brazil Beef",
        [0, 1],
        index=st.session_state.zero_deforestation_brazil_beef
    )

with col2:

    forest_500_beef = st.selectbox(
        "Forest 500 Beef",
        [0, 1],
        index=st.session_state.forest_500_beef
    )

    importer = st.number_input(
        "Importer",
        value=st.session_state.importer
    )

    country_of_destination = st.number_input(
        "Country of Destination",
        value=st.session_state.country_of_destination
    )

    economic_bloc = st.number_input(
        "Economic Bloc",
        value=st.session_state.economic_bloc
    )

    country_of_destination_trase_id = st.number_input(
        "Country Destination Trase ID",
        value=st.session_state.country_of_destination_trase_id
    )

    cattle_deforestation_5_year_total_exposure = st.number_input(
        "Cattle Deforestation Exposure",
        value=st.session_state.cattle_deforestation_5_year_total_exposure
    )

    co2_net_emissions_cattle_deforestation_5_year_total_exposure = st.number_input(
        "CO2 Net Emissions",
        value=st.session_state.co2_net_emissions_cattle_deforestation_5_year_total_exposure
    )

    land_use = st.number_input(
        "Land Use",
        value=st.session_state.land_use
    )

    volume = st.number_input(
        "Volume",
        value=st.session_state.volume
    )

    fob = st.number_input(
        "FOB",
        value=st.session_state.fob
    )

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("Predict CO₂"):

    features = np.array([[
        year,
        state_of_production,
        municipality_of_production,
        logistics_hub,
        product_type,
        port_of_export,
        exporter,
        exporter_group,
        zero_deforestation_brazil_beef,
        forest_500_beef,
        importer,
        country_of_destination,
        economic_bloc,
        country_of_destination_trase_id,
        cattle_deforestation_5_year_total_exposure,
        co2_net_emissions_cattle_deforestation_5_year_total_exposure,
        land_use,
        volume,
        fob
    ]])

    prediction = model.predict(features)

    st.success(
        f"Predicted CO₂ Emissions: {prediction[0]:,.2f}"
    )


# FOOTER

st.markdown(
    "<div style='position:fixed; bottom:10px; left:10px; color:white;'>By Carlos & Suelen</div>",
    unsafe_allow_html=True
)