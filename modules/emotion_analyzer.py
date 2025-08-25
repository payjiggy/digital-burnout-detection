from transformers import pipeline

class EmotionAnalyzer:
    """
    (Objective 2) An emotion analysis engine using a pre-trained NLP model.
    This fulfills the requirement of using NLP techniques to determine
    emotional signs from communications.
    """
    def __init__(self):
        try:
            # Load a lightweight, pre-trained sentiment analysis model
            print("INFO: Initializing Emotion Analysis Engine...")
            self.sentiment_pipeline = pipeline(
                "sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )
            print("INFO: Emotion Analysis Engine loaded successfully.")
        except Exception as e:
            print(f"ERROR: Could not load sentiment model. Please ensure an internet connection. Details: {e}")
            self.sentiment_pipeline = None

    def analyze_sentiment(self, text):
        """
        Analyzes a piece of text and returns a sentiment score.
        Score ranges from -1 (very negative) to 1 (very positive).
        """
        if not self.sentiment_pipeline:
            print("WARN: Sentiment pipeline not available. Returning neutral score.")
            return 0.0

        print(f"INFO: Analyzing sentiment for text: '{text[:30]}...'")
        results = self.sentiment_pipeline(text)[0]
        score = results['score']
        # If the label is negative, make the score negative
        if results['label'] == 'NEGATIVE':
            score = -score
        return round(score, 4)