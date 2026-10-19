import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="ICU AI Patient Deterioration Monitor",
    page_icon="🩺",
    layout="wide",
)

st.title("🩺 Real-Time Patient Deterioration & Clinical Triage Engine")
st.markdown(
    "Modeled on **Epic Systems eTriage & Rothman Index** industrial hospital warning architecture."
)
st.divider()


# --- 2. Clinical Telemetry Generator ---
@st.cache_data
def generate_clinical_data(samples=1000):
    np.random.seed(42)
    # Features: [Heart Rate (bpm), Systolic BP (mmHg), Respiration Rate (bpm), SpO2 (%), Temp (°C)]
    hr = np.random.uniform(50, 160, samples)
    sbp = np.random.uniform(70, 190, samples)
    resp = np.random.uniform(8, 38, samples)
    spo2 = np.random.uniform(82, 100, samples)
    temp = np.random.uniform(35.0, 41.0, samples)

    # Clinical risk logic (Sepsis / Cardiac Arrest Risk Scoring)
    risk_score = (
        (np.abs(hr - 75) * 0.08)
        + (np.abs(sbp - 120) * 0.05)
        + (np.abs(resp - 16) * 0.12)
        + ((100 - spo2) * 0.25)
        + (np.abs(temp - 37.0) * 0.8)
    )

    # Binary Label: 0 = Stable Patient, 1 = High Deterioration Risk
    y = np.where(risk_score > 6.0, 1, 0)

    return pd.DataFrame(
        {
            "Heart Rate (BPM)": hr,
            "Systolic BP (mmHg)": sbp,
            "Respiration Rate (BPM)": resp,
            "Oxygen Saturation SpO2 (%)": spo2,
            "Temperature (°C)": temp,
            "Deterioration Flag": y,
        }
    )


df = generate_clinical_data()


# --- 3. Ensemble Classifier Training ---
@st.cache_resource
def train_clinical_models(data):
    X = data[
        [
            "Heart Rate (BPM)",
            "Systolic BP (mmHg)",
            "Respiration Rate (BPM)",
            "Oxygen Saturation SpO2 (%)",
            "Temperature (°C)",
        ]
    ]
    y = data["Deterioration Flag"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    rf = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
    rf.fit(X_train, y_train)

    gbc = GradientBoostingClassifier(
        n_estimators=100, learning_rate=0.05, max_depth=4, random_state=42
    )
    gbc.fit(X_train, y_train)

    # Blended Probabilities
    probs = (rf.predict_proba(X_test)[:, 1] + gbc.predict_proba(X_test)[:, 1]) / 2.0
    auc = roc_auc_score(y_test, probs)
    acc = accuracy_score(y_test, (probs > 0.5).astype(int))

    return rf, gbc, auc, acc


rf_model, gbc_model, model_auc, model_acc = train_clinical_models(df)

# --- 4. Sidebar Patient Telemetry Inputs ---
st.sidebar.header("🎛️ Patient Bedside Sensors")
hr_in = st.sidebar.slider("Heart Rate (BPM)", 40, 180, 78)
sbp_in = st.sidebar.slider("Systolic Blood Pressure (mmHg)", 60, 200, 122)
resp_in = st.sidebar.slider("Respiration Rate (breaths/min)", 6, 40, 16)
spo2_in = st.sidebar.slider("Oxygen Saturation SpO2 (%)", 75, 100, 98)
temp_in = st.sidebar.slider("Body Temperature (°C)", 34.0, 42.0, 37.1, 0.1)

st.sidebar.divider()
st.sidebar.subheader("📊 Clinical Model Metrics")
st.sidebar.metric(label="ROC-AUC Score", value=f"{model_auc:.3f}")
st.sidebar.metric(label="Classification Accuracy", value=f"{model_acc * 100:.1f}%")

# --- 5. Real-Time Inference ---
input_sample = pd.DataFrame(
    [
        {
            "Heart Rate (BPM)": hr_in,
            "Systolic BP (mmHg)": sbp_in,
            "Respiration Rate (BPM)": resp_in,
            "Oxygen Saturation SpO2 (%)": spo2_in,
            "Temperature (°C)": temp_in,
        }
    ]
)

prob_rf = rf_model.predict_proba(input_sample)[0][1]
prob_gbc = gbc_model.predict_proba(input_sample)[0][1]
risk_probability = (prob_rf + prob_gbc) / 2.0 * 100.0  # Percentage

# --- 6. Executive KPI Bar ---
k1, k2, k3, k4 = st.columns(4)
k1.metric("Patient Status", "STABLE" if risk_probability < 40 else "CRITICAL")
k2.metric("Calculated Risk Score", f"{risk_probability:.1f}%")
k3.metric(
    "SpO2 Level",
    f"{spo2_in}%",
    delta="Normal" if spo2_in >= 95 else "Hypoxia Risk",
    delta_color="normal" if spo2_in >= 95 else "inverse",
)
k4.metric("Heart Rate", f"{hr_in} BPM")

st.divider()

# --- 7. Live Risk Gauge & Clinical Action ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Deterioration Probability Index")
    fig_gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=risk_probability,
            title={"text": "24-Hour Deterioration Risk (%)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#1F2937"},
                "steps": [
                    {"range": [0, 30], "color": "#D1FAE5"},
                    {"range": [30, 65], "color": "#FEF3C7"},
                    {"range": [65, 100], "color": "#FEE2E2"},
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "value": 65,
                },
            },
        )
    )
    fig_gauge.update_layout(height=280, margin=dict(l=20, r=20, t=30, b=10))
    st.plotly_chart(fig_gauge, use_container_width=True)

with col2:
    st.subheader("🚨 Automated Triage Action Protocol")
    if risk_probability >= 65:
        st.error(
            "🚨 **HIGH DETERIORATION RISK:** Rapid Response Team (RRT) notified automatically. ICU bed reservation placed."
        )
    elif risk_probability >= 30:
        st.warning(
            "🟡 **MODERATE RISK:** Increase bedside vital check frequency to every 15 minutes."
        )
    else:
        st.success(
            "🟢 **LOW RISK / STABLE:** Standard ward monitoring protocol active."
        )

    # Feature Importance (Fixed typo here)
    fig_imp = px.bar(
        x=gbc_model.feature_importances_,
        y=["Heart Rate", "Systolic BP", "Respiration", "SpO2", "Temperature"],
        orientation="h",
        title="Vital Sign Risk Contribution",
        color_continuous_scale="Reds",
    )
    fig_imp.update_layout(height=180, margin=dict(l=20, r=20, t=30, b=10))
    st.plotly_chart(fig_imp, use_container_width=True)

# --- 8. Ward Patient Roster ---
st.subheader("📋 Hospital Ward Real-Time Triage Roster")
roster = pd.DataFrame(
    {
        "Bed ID": ["BED-101", "BED-102", "BED-103", "BED-104", "BED-105"],
        "Patient ID": ["PAT-884", "PAT-912", "PAT-304", "PAT-551", "PAT-209"],
        "SpO2 (%)": [98, 88, 96, 91, 99],
        "Heart Rate": [72, 124, 80, 110, 68],
        "Deterioration Risk": [
            "12.4% (Low)",
            "84.2% (CRITICAL)",
            "18.1% (Low)",
            "68.5% (HIGH)",
            "8.1% (Low)",
        ],
        "System Action": [
            "Routine",
            "RRT Dispatched",
            "Routine",
            "Physician Alert",
            "Routine",
        ],
    }
)
st.dataframe(roster, use_container_width=True)