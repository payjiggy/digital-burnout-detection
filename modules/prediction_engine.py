import joblib
import pandas as pd

class PredictionEngine:
    """
    (Objective 3) Creates a burnout scoring model for real-time risk ratings.
    This engine uses the pre-trained ensemble model to generate predictions.
    """
    def __init__(self, model_path, scaler_path):
        print("INFO: Initializing Prediction Engine...")
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        print("INFO: Prediction Engine loaded successfully.")

    def get_burnout_risk_score(self, behavioral_data, productivity_data, sentiment_score):
        """
        Generates a real-time burnout risk score from integrated data streams.
        """
        # Create a single-row DataFrame matching the model's training columns
        input_data = pd.DataFrame({
            'avg_work_hours_per_day': [behavioral_data['avg_work_hours_per_day']],
            'avg_break_time_minutes': [behavioral_data['avg_break_time_minutes']],
            'meeting_hours_per_week': [behavioral_data['meeting_hours_per_week']],
            'sentiment_score': [sentiment_score],
            'task_completion_rate': [productivity_data['task_completion_rate']]
        })

        # Scale the input data using the loaded scaler
        input_data_scaled = self.scaler.transform(input_data)

        # Predict the binary label and the probability (risk score)
        prediction_label = self.model.predict(input_data_scaled)[0]
        prediction_score = self.model.predict_proba(input_data_scaled)[0][1] # Probability of class '1'

        return prediction_label, round(prediction_score, 4)