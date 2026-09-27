import streamlit as st
import requests

# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AQI Predictor",
    page_icon="🌍",
    layout="centered"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🌍 AQI Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict Air Quality Index using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

st.divider()


# --------------------------------------------------
# Input section
# --------------------------------------------------

st.header("Enter Pollutant AQI Values")

col1, col2 = st.columns(2)

with col1:

    co_aqi_value = st.number_input(
        "CO AQI Value",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

    ozone_aqi_value = st.number_input(
        "Ozone AQI Value",
        min_value=0.0,
        value=20.0,
        step=1.0
    )


with col2:

    no2_aqi_value = st.number_input(
        "NO₂ AQI Value",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

    pm2_5_aqi_value = st.number_input(
        "PM2.5 AQI Value",
        min_value=0.0,
        value=50.0,
        step=1.0
    )


st.divider()


# --------------------------------------------------
# Prediction button
# --------------------------------------------------

if st.button(
    "🔮 Predict AQI",
    use_container_width=True
):

    # Data sent to FastAPI
    payload = {
        "co_aqi_value": co_aqi_value,
        "ozone_aqi_value": ozone_aqi_value,
        "no2_aqi_value": no2_aqi_value,
        "pm2_5_aqi_value": pm2_5_aqi_value
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=10
        )

        # ------------------------------------------
        # Successful response
        # ------------------------------------------

        if response.status_code == 200:

            result = response.json()

            predicted_aqi = result["predicted_aqi"]

            st.success("Prediction successful!")

            st.metric(
                label="Predicted AQI",
                value=f"{predicted_aqi:.2f}"
            )

            # --------------------------------------
            # AQI category
            # --------------------------------------

            if predicted_aqi <= 50:
                category = "Good"
                message = "Air quality is considered good."

            elif predicted_aqi <= 100:
                category = "Moderate"
                message = "Air quality is acceptable."

            elif predicted_aqi <= 150:
                category = "Unhealthy for Sensitive Groups"
                message = "Sensitive people should consider reducing prolonged outdoor activity."

            elif predicted_aqi <= 200:
                category = "Unhealthy"
                message = "Everyone may begin to experience health effects."

            elif predicted_aqi <= 300:
                category = "Very Unhealthy"
                message = "Health alert: increased risk of health effects."

            else:
                category = "Hazardous"
                message = "Health warning: emergency conditions."

            st.subheader(f"Category: {category}")
            st.info(message)

        # ------------------------------------------
        # API error
        # ------------------------------------------

        else:

            try:
                error_detail = response.json().get(
                    "detail",
                    "Unknown API error"
                )
            except Exception:
                error_detail = response.text

            st.error(
                f"API Error ({response.status_code}): "
                f"{error_detail}"
            )

    # ----------------------------------------------
    # FastAPI not running
    # ----------------------------------------------

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Could not connect to FastAPI.\n\n"
            "Make sure your FastAPI backend is running "
            "on http://127.0.0.1:8000"
        )

    # ----------------------------------------------
    # Timeout
    # ----------------------------------------------

    except requests.exceptions.Timeout:

        st.error("❌ The request timed out.")

    # ----------------------------------------------
    # Other error
    # ----------------------------------------------

    except Exception as e:

        st.error(f"❌ Unexpected error: {e}")