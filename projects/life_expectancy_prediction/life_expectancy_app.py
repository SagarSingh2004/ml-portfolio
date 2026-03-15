import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained pipeline
@st.cache_resource
def load_pipeline():
    return joblib.load('life_expectancy_pipeline.pkl')
pipeline = load_pipeline()


# --- Sidebar ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/616/616494.png", width=80)
st.sidebar.title('Life Expectancy Predictor')
st.sidebar.markdown('''
**Instructions:**
- Enter the required features in the main panel.
- Click **Predict** to see the estimated life expectancy.
''')

# --- Main Panel ---
st.title('🌍 Life Expectancy Prediction')
st.markdown('''
This app uses a machine learning pipeline to predict life expectancy based on various health, economic, and demographic features.
''')

# Example feature names (replace with actual features from your pipeline)
feature_names = [
    'year', 'adult_mortality', 'infant_deaths', 'alcohol',
    'percentage_expenditure', 'hepatitis_b', 'measles', 'bmi',
    'under_five_deaths', 'polio', 'total_expenditure', 'diphtheria',
    'hiv_aids', 'gdp', 'population', 'thinness_1_19_years',
    'thinness_5_9_years', 'income_composition_of_resources', 'schooling',
    'status_Developing'  # If categorical, handle accordingly
]


# --- Input Form ---
with st.form("input_form"):
    st.subheader("Enter Features:")
    user_input = {}
    for feat in feature_names:
        if feat.startswith('status_'):
            user_input[feat] = st.selectbox(feat.replace('_', ' ').capitalize(), ['Developing', 'Developed'])
        else:
            user_input[feat] = st.number_input(feat.replace('_', ' ').capitalize(), value=0.0)
    submitted = st.form_submit_button("Predict")



# Convert categorical to numeric as expected by the pipeline
input_data = user_input.copy()
for feat in feature_names:
    if feat.startswith('status_'):
        # 1 for Developing, 0 for Developed
        input_data[feat] = 1 if user_input[feat] == 'Developing' else 0

# Prepare input for prediction
input_df = pd.DataFrame([input_data])

if submitted:
    try:
        prediction = pipeline.predict(input_df)[0]
        st.success(f'🎉 **Predicted Life Expectancy:** {prediction:.2f} years')
        st.balloons()
    except Exception as e:
        st.error(f'Prediction failed: {e}')
