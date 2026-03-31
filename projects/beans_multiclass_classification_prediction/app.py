import streamlit as st
import pandas as pd
import joblib
import os

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Bean Classifier",
    page_icon="🫘",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_pipeline():
    current_dir = os.path.dirname(__file__)
    pipeline_path = os.path.join(current_dir, 'model.pkl')
    return joblib.load(pipeline_path)

pipeline = load_pipeline()

# -----------------------------
# Global Styles
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0F1A0E;
    font-family: 'DM Sans', sans-serif;
}
[data-testid="stAppViewContainer"] {
    background-image:
        radial-gradient(ellipse 80% 60% at 10% 0%, rgba(52,90,40,0.35) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 90% 100%, rgba(30,70,25,0.3) 0%, transparent 55%);
}
[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #0d1f0c 0%, #162214 60%, #1a2e18 100%);
    border-right: 1px solid rgba(120,180,80,0.15);
}
[data-testid="stSidebar"] * { color: #c8dfc0 !important; }
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #a8d878 !important;
    font-family: 'Playfair Display', serif !important;
}
.sidebar-divider {
    border: none;
    border-top: 1px solid rgba(120,180,80,0.2);
    margin: 16px 0;
}

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #1a3a14 0%, #243d1c 50%, #1e3518 100%);
    border: 1px solid rgba(140,200,90,0.2);
    border-radius: 20px;
    padding: 40px 48px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    gap: 32px;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 280px; height: 280px;
    background: radial-gradient(circle, rgba(120,200,60,0.12) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 30%;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(80,160,40,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-text h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.6rem;
    font-weight: 700;
    color: #d4f0a0;
    margin: 0 0 10px 0;
    line-height: 1.15;
    letter-spacing: -0.5px;
}
.hero-text p {
    font-size: 1.05rem;
    color: #88b870;
    margin: 0;
    font-weight: 300;
}
.hero-icon {
    font-size: 5.5rem;
    line-height: 1;
    filter: drop-shadow(0 4px 16px rgba(120,200,60,0.3));
    flex-shrink: 0;
}

/* ── Stats Strip ── */
.stats-strip {
    display: flex;
    gap: 16px;
    margin-bottom: 28px;
}
.stat-card {
    background: rgba(30,55,20,0.6);
    border: 1px solid rgba(120,180,80,0.18);
    border-radius: 14px;
    padding: 18px 24px;
    flex: 1;
    text-align: center;
    backdrop-filter: blur(4px);
}
.stat-card .stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #a8e060;
    line-height: 1;
}
.stat-card .stat-label {
    font-size: 0.78rem;
    color: #7aab60;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-top: 4px;
}

/* ── Section heading ── */
.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    color: #c0e890;
    margin: 0 0 18px 0;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* ── Form card ── */
.form-card {
    background: rgba(20,40,15,0.7);
    border: 1px solid rgba(100,160,70,0.2);
    border-radius: 18px;
    padding: 32px 36px 8px;
    backdrop-filter: blur(6px);
    margin-bottom: 4px;
}

/* ── Number inputs ── */
[data-testid="stNumberInput"] label {
    color: #90c878 !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.5px !important;
    text-transform: uppercase !important;
}
[data-testid="stNumberInput"] input {
    background: rgba(10,25,8,0.8) !important;
    border: 1px solid rgba(100,160,70,0.3) !important;
    border-radius: 10px !important;
    color: #d4f0a0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.97rem !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: rgba(140,210,80,0.6) !important;
    box-shadow: 0 0 0 3px rgba(120,200,60,0.1) !important;
}
[data-testid="stNumberInput"] button {
    background: rgba(30,55,20,0.9) !important;
    border-color: rgba(100,160,70,0.3) !important;
    color: #a8d878 !important;
}

/* ── Predict button ── */
[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #3a7a20 0%, #4e9a28 50%, #3a7a20 100%) !important;
    color: #e8f8d0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 500 !important;
    letter-spacing: 1px !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 48px !important;
    width: 100% !important;
    margin-top: 10px !important;
    box-shadow: 0 4px 20px rgba(60,130,30,0.35) !important;
    transition: all 0.25s ease !important;
}
[data-testid="stFormSubmitButton"] button:hover {
    background: linear-gradient(135deg, #4a9a28 0%, #5eb830 50%, #4a9a28 100%) !important;
    box-shadow: 0 6px 28px rgba(80,160,40,0.5) !important;
    transform: translateY(-1px) !important;
}

/* ── Result Card ── */
.result-card {
    background: linear-gradient(135deg, #1c3d14 0%, #254d1a 100%);
    border: 1px solid rgba(140,210,80,0.4);
    border-radius: 18px;
    padding: 36px 40px;
    margin-top: 28px;
    text-align: center;
    box-shadow: 0 8px 32px rgba(60,130,30,0.25);
    animation: fadeSlideUp 0.5s ease forwards;
}
.result-card .result-label {
    font-size: 0.85rem;
    color: #80b060;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
}
.result-card .result-bean {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 700;
    color: #c0f070;
    letter-spacing: -0.5px;
    text-shadow: 0 0 30px rgba(160,230,80,0.4);
}
.result-card .result-icon { font-size: 2.5rem; margin-bottom: 8px; }

@keyframes fadeSlideUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0d1a0c; }
::-webkit-scrollbar-thumb { background: #3a6a20; border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.markdown("""
<div style="text-align:center; padding: 10px 0 20px;">
    <div style="font-size:4rem; margin-bottom:8px;">🌿</div>
    <div style="font-family:'Playfair Display',serif; font-size:1.4rem; color:#a8d878; font-weight:700;">Bean Classifier</div>
    <div style="font-size:0.78rem; color:#5a8a48; letter-spacing:1.5px; text-transform:uppercase; margin-top:4px;">ML · SVM · 94% Accuracy</div>
</div>
<hr class="sidebar-divider"/>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
### 📋 How to Use
1. Enter the bean's morphological measurements
2. Click **Predict Bean Type**
3. See the classification result instantly

<hr class="sidebar-divider"/>

### 🫘 Bean Varieties
- **SEKER** — Small, round & smooth
- **BARBUNYA** — Spotted, medium size
- **BOMBAY** — Large, elongated
- **CALI** — Medium-large, oval
- **HOROZ** — Elongated, pointed tip
- **SIRA** — Small to medium
- **DERMASON** — Tiny, round

<hr class="sidebar-divider"/>

### 📐 About Features
16 geometric & shape descriptors extracted from bean seed images via image processing techniques.
""", unsafe_allow_html=True)

# -----------------------------
# Hero Banner
# -----------------------------
st.markdown("""
<div class="hero-banner">
    <div class="hero-icon">🫘</div>
    <div class="hero-text">
        <h1>Dry Bean<br>Classification</h1>
        <p>Identify 7 varieties of dry beans from morphological measurements<br>using an SVM trained on 13,000+ labelled seed samples.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Stats Strip
st.markdown("""
<div class="stats-strip">
    <div class="stat-card">
        <div class="stat-number">13,611</div>
        <div class="stat-label">Training Samples</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">7</div>
        <div class="stat-label">Bean Varieties</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">16</div>
        <div class="stat-label">Shape Features</div>
    </div>
    <div class="stat-card">
        <div class="stat-number">94%</div>
        <div class="stat-label">Model Accuracy</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Feature Names & Defaults
# -----------------------------
feature_names = [
    'area', 'perimeter', 'major_axis_length', 'minor_axis_length',
    'aspect_ratio', 'eccentricity', 'convex_area', 'equiv_diameter',
    'extent', 'solidity', 'roundness', 'compactness',
    'shape_factor_1', 'shape_factor_2', 'shape_factor_3', 'shape_factor_4'
]

feature_defaults = {
    'area': 44652.0,
    'perimeter': 794.941,
    'major_axis_length': 296.883,
    'minor_axis_length': 192.432,
    'aspect_ratio': 1.5511,
    'eccentricity': 0.7644,
    'convex_area': 45178.0,
    'equiv_diameter': 238.438,
    'extent': 0.7599,
    'solidity': 0.9883,
    'roundness': 0.8832,
    'compactness': 0.8013,
    'shape_factor_1': 0.006645,
    'shape_factor_2': 0.001694,
    'shape_factor_3': 0.6420,
    'shape_factor_4': 0.9964,
}

# -----------------------------
# Input Form
# -----------------------------
st.markdown('<p class="section-heading">📐 &nbsp;Morphological Measurements</p>', unsafe_allow_html=True)
st.markdown('<div class="form-card">', unsafe_allow_html=True)

with st.form("input_form"):
    user_input = {}
    col1, col2 = st.columns(2, gap="large")

    for i, feat in enumerate(feature_names):
        val = float(feature_defaults[feat])
        if i % 2 == 0:
            user_input[feat] = col1.number_input(
                feat.replace('_', ' ').title(),
                min_value=0.0,
                value=val,
                format="%.6f"
            )
        else:
            user_input[feat] = col2.number_input(
                feat.replace('_', ' ').title(),
                min_value=0.0,
                value=val,
                format="%.6f"
            )

    st.markdown("<br>", unsafe_allow_html=True)
    submitted = st.form_submit_button("🔍  Predict Bean Type")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Prediction Result
# -----------------------------
if submitted:
    try:
        input_df = pd.DataFrame([user_input])
        prediction = pipeline.predict(input_df)[0]

        bean_icons = {
            'SEKER': '🟤', 'BARBUNYA': '🫘', 'BOMBAY': '🟫',
            'CALI': '🌰', 'HOROZ': '🫛', 'SIRA': '⚪', 'DERMASON': '🟡'
        }
        icon = bean_icons.get(prediction, '🫘')

        st.markdown(f"""
        <div class="result-card">
            <div class="result-icon">{icon}</div>
            <div class="result-label">Predicted Bean Variety</div>
            <div class="result-bean">{prediction}</div>
        </div>
        """, unsafe_allow_html=True)

        st.balloons()

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

st.markdown("---")
st.markdown("👨‍💻 Built by Sagar | Data Science Project")