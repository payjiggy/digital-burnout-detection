import streamlit as st
from datetime import datetime  # <--- THIS IS THE FIX
from modules.emotion_analyzer import EmotionAnalyzer
from modules.prediction_engine import PredictionEngine
from modules.recommendation_system import RecommendationSystem

# --- Page Configuration ---
st.set_page_config(page_title="AI Burnout Detection System", layout="wide", page_icon="🛡️")


# --- Custom CSS Loader ---
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Please ensure 'static/style.css' exists.")

# --- Load AI Models (with Streamlit's caching for efficiency) ---
@st.cache_resource
def load_models():
    """Loads and returns all the AI model classes only once."""
    print("INFO: Loading AI models...")
    emotion_engine = EmotionAnalyzer()
    prediction_engine = PredictionEngine(model_path='models/burnout_model.pkl', scaler_path='models/scaler.pkl')
    recommender = RecommendationSystem()
    print("INFO: AI models loaded successfully.")
    return emotion_engine, prediction_engine, recommender

# Load custom styles and AI models
load_css("static/style.css")
emotion_engine, prediction_engine, recommender = load_models()

# =============================================================================
# --- USER INTERFACE (UI) ---
# =============================================================================

st.title("🛡️ AI-Powered Burnout Detection System")
st.write("""
This application serves as an interactive demonstration of an AI model for the early detection of digital burnout.
It fulfills the project's research objectives by integrating behavioral and interactional data to provide a comprehensive risk assessment.
""")

# --- Instructions Expander ---
with st.expander("ℹ️ How to Use This Tool"):
    st.markdown("""
    1.  **Adjust the sliders** in the *Behavioral Data* section to reflect your recent work patterns.
    2.  **Enter a message** in the *Emotion Analysis* section that captures your current work-related feelings.
    3.  **Click the 'Analyze Burnout Risk' button** to process the data and view your AI-generated report.
    """)

st.divider()

# Create two columns for a clean input layout
input_col, empty_col = st.columns([2, 1])

with input_col:
    # --- Objective 1: Behavioral Data Input ---
    st.header("📊 Behavioral Data Input")
    st.caption("Simulate the Behavioral Tracking Module by providing your recent work patterns.")

    avg_work_hours = st.slider(
        "Average Daily Work Hours",
        min_value=4.0, max_value=16.0, value=9.5, step=0.5,
        help="How many hours do you typically work on an average day?"
    )
    avg_breaks = st.slider(
        "Average Number of Breaks Per Day",
        min_value=0, max_value=15, value=3,
        help="How many short breaks (5-15 mins) do you take daily?"
    )
    task_completion_rate = st.slider(
        "Task Completion Rate",
        min_value=0.0, max_value=1.0, value=0.75, step=0.05,
        help="What percentage of tasks are you completing on time? (e.g., 0.7 = 70%)"
    )

    # Convert breaks to minutes for the model
    avg_break_minutes = avg_breaks * 10

    # --- Objective 2: Interactional Data Input ---
    st.header("✍️ Emotion Analysis Input")
    st.caption("Simulate the Emotion Analysis Engine by providing a recent work-related communication.")
    user_text = st.text_area(
        "Enter a message that reflects your current feelings about work:",
        height=120,
        placeholder="e.g., 'The workload has been overwhelming lately, and I'm struggling to keep up with the constant deadlines.'"
    )
st.divider()

# --- Main "Run Analysis" Button ---
if st.button("Analyze My Burnout Risk", type="primary", use_container_width=True):
    if user_text:
        with st.spinner("Analyzing data and generating report..."):
            # 1. Analyze sentiment (Fulfills Objective 2)
            sentiment_score = emotion_engine.analyze_sentiment(user_text)

            # Assemble data for prediction
            behavioral_data = {
                'avg_work_hours_per_day': avg_work_hours,
                'avg_break_time_minutes': avg_break_minutes,
                'meeting_hours_per_week': 10.0,  # Using a fixed placeholder for simplicity
            }
            productivity_data = {'task_completion_rate': task_completion_rate}

            # 2. Predict burnout (Fulfills Objective 3)
            risk_label, risk_score = prediction_engine.get_burnout_risk_score(
                behavioral_data, productivity_data, sentiment_score
            )

            # 3. Generate recommendation (Fulfills Objective 4)
            recommendation = recommender.generate_recommendation(
                risk_label, risk_score, behavioral_data
            )

            # --- Display Results in a Professional Report Container ---
            st.markdown('<div class="report-container">', unsafe_allow_html=True)
            st.header("AI Wellness Report")
            # This line will now work because 'datetime' has been imported
            st.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            st.divider()

            # Display key metrics side-by-side
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.subheader("Emotion Analysis")
                st.metric("Sentiment Score", f"{sentiment_score:.2f}")
                st.caption("From -1.0 (Negative) to 1.0 (Positive).")
            with res_col2:
                st.subheader("Burnout Risk")
                st.metric("Calculated Risk Score", f"{risk_score:.2f}")
                st.caption("From 0.0 (Low Risk) to 1.0 (High Risk).")

            st.divider()

            # Display Recommendation
            st.subheader("Personalized Recommendation")
            if recommendation['risk_level'] == 'Low':
                st.success(f"**{recommendation['risk_level']} Risk:** {recommendation['message']}", icon="✅")
            elif recommendation['risk_level'] in ['Medium', 'High']:
                 st.warning(f"**{recommendation['risk_level']} Risk:** {recommendation['message']}", icon="⚠️")
            elif recommendation['risk_level'] == 'Critical':
                 st.error(f"**{recommendation['risk_level']} Risk:** {recommendation['message']}", icon="🚨")

            st.info(f"**Actionable Suggestion:** {recommendation['suggestion']}")
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.error("⚠️ Please enter some text in the message box to perform an analysis.")