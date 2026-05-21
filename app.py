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

encoders = joblib.load("encoders.pkl")


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


# TITLE

st.title("CO₂ Emissions Prediction App")

st.write("Helping protect the Amazon Rainforest")


# RANDOM DEFAULT VALUES

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

# INPUT

col1, col2 = st.columns(2)

with col1:

    year = st.number_input(
        "Year",
        value=st.session_state.year
    )

    selected_state = st.selectbox(
        "State of Production",
        encoders["state_of_production"].classes_
    )
    state_of_production = encoders["state_of_production"].transform([selected_state])[0]

    selected_municipality = st.selectbox(
        "Municipality of Production",
        encoders["municipality_of_production"].classes_
    )
    municipality_of_production = encoders["municipality_of_production"].transform([selected_municipality])[0]

    selected_logistics_hub = st.selectbox(
        "Logistics Hub",
        encoders["logistics_hub"].classes_
    )
    logistics_hub = encoders["logistics_hub"].transform([selected_logistics_hub])[0]

    selected_product_type = st.selectbox(
        "Product Type",
        encoders["product_type"].classes_
    )
    product_type = encoders["product_type"].transform([selected_product_type])[0]

    selected_port = st.selectbox(
        "Port of Export",
        encoders["port_of_export"].classes_
    )
    port_of_export = encoders["port_of_export"].transform([selected_port])[0]

    selected_exporter = st.selectbox(
        "Exporter",
        encoders["exporter"].classes_
    )
    exporter = encoders["exporter"].transform([selected_exporter])[0]

    selected_exporter_group = st.selectbox(
        "Exporter Group",
        encoders["exporter_group"].classes_
    )
    exporter_group = encoders["exporter_group"].transform([selected_exporter_group])[0]

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

    selected_importer = st.selectbox(
        "Importer",
        encoders["importer"].classes_
    )
    importer = encoders["importer"].transform([selected_importer])[0]

    selected_country = st.selectbox(
        "Country of Destination",
        encoders["country_of_destination"].classes_
    )
    country_of_destination = encoders["country_of_destination"].transform([selected_country])[0]

    selected_economic_bloc = st.selectbox(
        "Economic Bloc",
        encoders["economic_bloc"].classes_
    )
    economic_bloc = encoders["economic_bloc"].transform([selected_economic_bloc])[0]

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


# PREDICTION

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