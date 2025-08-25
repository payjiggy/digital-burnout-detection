class RecommendationSystem:
    """
    (Objective 4) Provides personalized, evidence-based interventions.
    This system generates intelligent alerts based on the burnout risk score
    and the data that contributed to it.
    """
    def generate_recommendation(self, risk_label, risk_score, behavioral_data):
        """
        Generates a dynamic recommendation.
        """
        if risk_label == 0:
            return {
                "risk_level": "Low",
                "message": "Current work patterns appear healthy.",
                "suggestion": f"Keep up the great work! Your current risk score is low ({risk_score}). Continue prioritizing a healthy work-life balance."
            }

        # --- High Risk Detected ---
        if risk_score > 0.85:
            risk_level = "Critical"
            message = "Immediate attention is strongly recommended."
            suggestion = "Consider speaking with a manager or HR about workload. It is highly advised to take some time off to disconnect and recharge."
        elif risk_score > 0.7:
            risk_level = "High"
            message = "A high risk of burnout has been detected."
            suggestion = "Actively schedule 'no-meeting' blocks in your calendar and ensure you are taking your full breaks. Try to disconnect completely after work."
        else:
            risk_level = "Medium"
            message = "Early warning signs of potential burnout detected."
            suggestion = "Review your daily schedule. Small changes like a 10-minute walk or a short mindfulness exercise can make a big difference."

        # Make the alert more "intelligent" by referencing specific data
        if behavioral_data['avg_work_hours_per_day'] > 10:
            suggestion += f" Your average of {behavioral_data['avg_work_hours_per_day']:.1f} work hours/day is a major contributing factor."

        return {
            "risk_level": risk_level,
            "message": message,
            "suggestion": suggestion
        }