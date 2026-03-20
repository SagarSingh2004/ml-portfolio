import streamlit as st
import pandas as pd
import joblib
import os

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #e3f2fd, #ffffff);
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Page Config (MUST BE FIRST)
# -------------------------
st.set_page_config(
    page_title="Income Prediction App",
    page_icon="💼",
    layout="centered"
)

# -------------------------
# Custom CSS
# -------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
h1 {
    text-align: center;
}
.stButton>button {
    width: 100%;
    height: 50px;
    border-radius: 10px;
    font-size: 18px;
    background-color: #4CAF50;
    color: white;
}
.result-box {
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}
.success-box {
    background-color: #d4edda;
    color: #155724;
}
.info-box {
    background-color: #d1ecf1;
    color: #0c5460;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("📌 About")
st.sidebar.info(
    "This app predicts whether a person earns more than 50K based on demographic features."
)

# -------------------------
# Load Model
# -------------------------
@st.cache_resource
def load():
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "final_best_model.pkl")
    return joblib.load(path)

model = load()

# -------------------------
# Title
# -------------------------
st.title("💼 Income Classification App")
st.markdown("### Predict whether income is **>50K or ≤50K**")

# -------------------------
# Input Section
# -------------------------
st.markdown("## 📝 Enter User Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 90, 30)
    workclass = st.selectbox("Workclass", [
        "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov",
        "Local-gov", "State-gov", "Without-pay", "Never-worked"
    ])
    education = st.selectbox("Education", [
        "Bachelors", "Some-college", "11th", "HS-grad", "Prof-school",
        "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th",
        "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"
    ])
    marital_status = st.selectbox("Marital Status", [
        "Married-civ-spouse", "Divorced", "Never-married", "Separated",
        "Widowed", "Married-spouse-absent", "Married-AF-spouse"
    ])
    occupation = st.selectbox("Occupation", [
        "Tech-support", "Craft-repair", "Other-service", "Sales",
        "Exec-managerial", "Prof-specialty", "Handlers-cleaners",
        "Machine-op-inspct", "Adm-clerical", "Farming-fishing",
        "Transport-moving", "Priv-house-serv", "Protective-serv",
        "Armed-Forces"
    ])

with col2:
    fnlwgt = st.number_input("Final Weight", 10000, 1000000, 200000)
    education_num = st.slider("Education Number", 1, 16, 10)
    relationship = st.selectbox("Relationship", [
        "Wife", "Own-child", "Husband", "Not-in-family",
        "Other-relative", "Unmarried"
    ])
    race = st.selectbox("Race", [
        "White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"
    ])
    sex = st.selectbox("Sex", ["Male", "Female"])

# Additional Features
st.markdown("### ⚙️ Additional Details")

col3, col4 = st.columns(2)

with col3:
    capital_gain = st.number_input("Capital Gain", 0, 100000, 0)
    hours_per_week = st.slider("Hours per Week", 1, 100, 40)

with col4:
    capital_loss = st.number_input("Capital Loss", 0, 5000, 0)
    native_country = st.selectbox("Native Country", [
        "United-States", "India", "Mexico", "Philippines", "Germany",
        "Canada", "England", "China", "Cuba", "Japan", "Other"
    ])

# -------------------------
# Prediction Button
# -------------------------
st.markdown("")

if st.button("🔍 Predict Income"):

    input_data = pd.DataFrame([{
        "age": age,
        "workclass": workclass,
        "fnlwgt": fnlwgt,
        "education": education,
        "education_num": education_num,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "sex": sex,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }])

    prediction = model.predict(input_data)[0]

    # -------------------------
    # Result Display
    # -------------------------
    st.markdown("## 📊 Prediction Result")

    if prediction == 1:
        st.markdown('<div class="result-box success-box">💰 Income > 50K</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-box info-box">💼 Income ≤ 50K</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("👨‍💻 Built by Sagar | Data Science Project")