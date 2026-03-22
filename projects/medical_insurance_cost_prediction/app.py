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
    page_title="Medical Insurance Cost Prediction App",
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
    "This app predicts the price of Medical Insurance based on demographic, health, and lifestyle indicators."
)

# -------------------------
# Load Model
# -------------------------
@st.cache_resource
def load():
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, "model.pkl")
    return joblib.load(path)

model = load()

# -------------------------
# Title
# -------------------------
st.title("Medical Insurance Cost Prediction App")
st.markdown("### Predict the price of Medical Insurance**")

# -------------------------
# Input Section
# -------------------------
st.markdown("## 📝 Enter Individual Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 90, 30)
    sex = st.selectbox("sex", [
        "male", "female"
    ])
    smoker = st.selectbox("smoker", [
        "yes", "no"
    ])

with col2:
    children = st.slider("children", 0, 10, 2)
    bmi = st.number_input("bmi", 1.00, 100.00, 10.00)
    region = st.selectbox("region", [
        "southwest", "southeast", "northwest", "northeast"
    ])


# -------------------------
# Prediction Button
# -------------------------
st.markdown("")

if st.button("🔍 Predict Price"):

    input_data = pd.DataFrame([{
        "age":age,
        "sex":sex,
        "smoker":smoker,
        "children":children,
        "bmi":bmi,
        "region":region
    }])

    prediction = model.predict(input_data)[0]

    # -------------------------
    # Result Display
    # -------------------------
    st.markdown("## 📊 Prediction Result")
    st.success(f'🎉 **Predicted Medical Insurance Price:** {prediction:.2f} $')
    st.balloons()


st.markdown("---")
st.markdown("👨‍💻 Built by Sagar | Data Science Project")