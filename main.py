
import streamlit as st
import pandas as pd
import joblib
import os


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Water Potability Predictor",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# Load Model
# =========================================================

model = joblib.load("PipeLineTwo.pkl")


# =========================================================
# Custom CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   Main App
===================================================== */

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(14, 165, 233, 0.10),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            rgba(6, 182, 212, 0.10),
            transparent 30%
        ),
        #0b1120;
}


/* =====================================================
   Main Container
===================================================== */

.block-container {
    max-width: 1200px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}


/* =====================================================
   Header
===================================================== */

.main-title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;

    margin-bottom: 8px;

    background: linear-gradient(
        90deg,
        #22d3ee,
        #38bdf8,
        #60a5fa
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    letter-spacing: -1px;
}


.subtitle {
    text-align: center;

    font-size: 18px;

    color: #94a3b8;

    margin-bottom: 35px;
}


/* =====================================================
   Section Titles
===================================================== */

h2,
h3 {
    color: #e2e8f0 !important;
}


/* =====================================================
   Input Labels
===================================================== */

.stNumberInput label {
    color: #cbd5e1 !important;

    font-weight: 600 !important;

    font-size: 14px !important;
}


/* =====================================================
   Number Inputs
===================================================== */

.stNumberInput > div > div {

    background-color: #111827 !important;

    border: 1px solid #263449 !important;

    border-radius: 12px !important;

    transition: all 0.25s ease;
}


.stNumberInput > div > div:focus-within {

    border-color: #06b6d4 !important;

    box-shadow:
        0 0 0 1px rgba(6, 182, 212, 0.25);
}


.stNumberInput input {

    color: #f8fafc !important;
}


/* =====================================================
   Predict Button
===================================================== */

.stButton > button {

    width: 100%;

    min-height: 55px;

    border-radius: 14px;

    border: none;

    background: linear-gradient(
        90deg,
        #0891b2,
        #0284c7,
        #2563eb
    );

    color: white;

    font-size: 17px;

    font-weight: 700;

    letter-spacing: 0.3px;

    transition: all 0.25s ease;

    box-shadow:
        0 8px 25px rgba(6, 182, 212, 0.25);
}


.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 12px 30px rgba(14, 165, 233, 0.40);

    border: none;
}


.stButton > button:active {

    transform: translateY(0px);
}


/* =====================================================
   Prediction Card
===================================================== */

.prediction-box {

    margin-top: 30px;

    padding: 35px 25px;

    border-radius: 22px;

    text-align: center;

    background:
        linear-gradient(
            145deg,
            rgba(30, 41, 59, 0.95),
            rgba(15, 23, 42, 0.98)
        );

    border: 1px solid rgba(
        34,
        211,
        238,
        0.20
    );

    box-shadow:
        0 20px 50px rgba(0, 0, 0, 0.35),
        inset 0 1px 0 rgba(
            255,
            255,
            255,
            0.05
        );

    position: relative;

    overflow: hidden;
}


/* =====================================================
   Prediction Glow
===================================================== */

.prediction-box::before {

    content: "";

    position: absolute;

    top: -80px;

    left: 50%;

    width: 250px;

    height: 150px;

    transform: translateX(-50%);

    background: rgba(
        6,
        182,
        212,
        0.18
    );

    filter: blur(60px);
}


/* =====================================================
   Prediction Label
===================================================== */

.prediction-label {

    position: relative;

    color: #94a3b8;

    font-size: 15px;

    font-weight: 600;

    text-transform: uppercase;

    letter-spacing: 2px;

    margin-bottom: 10px;
}


/* =====================================================
   Result
===================================================== */

.result {

    position: relative;

    font-size: 42px;

    font-weight: 800;

    margin-top: 5px;

    letter-spacing: -1px;
}


/* =====================================================
   Prediction Note
===================================================== */

.prediction-note {

    position: relative;

    margin-top: 12px;

    color: #64748b;

    font-size: 13px;

    font-weight: 500;

    letter-spacing: 0.3px;
}


/* =====================================================
   Footer
===================================================== */

.footer {

    text-align: center;

    margin-top: 45px;

    padding-top: 20px;

    border-top: 1px solid rgba(
        148,
        163,
        184,
        0.12
    );

    color: #64748b;

    font-size: 14px;
}


/* =====================================================
   Divider
===================================================== */

hr {

    border-color: rgba(
        148,
        163,
        184,
        0.12
    ) !important;
}


/* =====================================================
   Alerts
===================================================== */

.stAlert {

    border-radius: 12px !important;
}


/* =====================================================
   Responsive Design
===================================================== */

@media (max-width: 768px) {

    .main-title {
        font-size: 36px;
    }

    .subtitle {
        font-size: 16px;
    }

    .result {
        font-size: 32px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# Header
# =========================================================

st.markdown(
    '<div class="main-title">💧 Water Potability Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered water quality classification using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# =========================================================
# Input Section
# =========================================================

st.subheader("🧪 Water Quality Specifications")


col1, col2, col3 = st.columns(3)


# =========================================================
# Column 1
# =========================================================

with col1:

    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=14.0,
        value=7.2,
        step=0.1
    )


    Hardness = st.number_input(
        "Hardness (mg/L)",
        min_value=0.0,
        value=180.5,
        step=0.1
    )


    Solids = st.number_input(
        "Solids (mg/L)",
        min_value=0.0,
        value=12000.0,
        step=100.0
    )


# =========================================================
# Column 2
# =========================================================

with col2:

    Chloramines = st.number_input(
        "Chloramines (mg/L)",
        min_value=0.0,
        value=7.0,
        step=0.1
    )


    Sulfate = st.number_input(
        "Sulfate (mg/L)",
        min_value=0.0,
        value=330.0,
        step=1.0
    )


    Conductivity = st.number_input(
        "Conductivity (µS/cm)",
        min_value=0.0,
        value=420.0,
        step=1.0
    )


# =========================================================
# Column 3
# =========================================================

with col3:

    Organic_carbon = st.number_input(
        "Organic Carbon (mg/L)",
        min_value=0.0,
        value=14.5,
        step=0.1
    )


    Trihalomethanes = st.number_input(
        "Trihalomethanes (µg/L)",
        min_value=0.0,
        value=65.0,
        step=0.1
    )


    Turbidity = st.number_input(
        "Turbidity (NTU)",
        min_value=0.0,
        value=4.0,
        step=0.1
    )
# =========================================================
# Prediction
# =========================================================

st.divider()


predict_button = st.button(
    "🚀 Predict Water Potability",
    use_container_width=True
)


if predict_button:

    # -----------------------------------------------------
    # Create Input DataFrame
    # -----------------------------------------------------

    input_data = pd.DataFrame([{

        "ph": ph,

        "Hardness": Hardness,

        "Solids": Solids,

        "Chloramines": Chloramines,

        "Sulfate": Sulfate,

        "Conductivity": Conductivity,

        "Organic_carbon": Organic_carbon,

        "Trihalomethanes": Trihalomethanes,

        "Turbidity": Turbidity

    }])


    # -----------------------------------------------------
    # Prediction
    # -----------------------------------------------------

    try:

        prediction = model.predict(input_data)[0]
        # -------------------------------------------------
        # Display Result
        # -------------------------------------------------
        if prediction == 1:
            st.markdown(
                """<div class="prediction-box">
                    <div class="prediction-label">💧 Water Quality Result</div>
                    <div class="result">✅ Water is Potable</div>
                    <div class="prediction-note">The model predicts that this water is suitable for drinking.</div>
                </div>""",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """<div class="prediction-box">
                    <div class="prediction-label">💧 Water Quality Result</div>
                    <div class="result">❌ Water is Not Potable</div>
                    <div class="prediction-note">The model predicts that this water is not suitable for drinking.</div>
                </div>""",
                unsafe_allow_html=True,
            )
    except Exception as e:
        st.error(
            f"Prediction Error: {e}"
        )
# =========================================================
# Footer
# =========================================================

st.markdown(
    """
    <div class="footer">
        💧 Water Potability Prediction • Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)

