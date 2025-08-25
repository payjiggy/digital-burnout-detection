# AI-Powered Early Detection System for Digital Burnout

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)
![Libraries](https://img.shields.io/badge/Libraries-Scikit--learn%20%7C%20Transformers-orange.svg)

This repository contains the practical implementation of the research project: "An AI-Powered Early Detection System for Digital Burnout in Remote Workers Using Behavioral and Interactional Data."

The application is an interactive web-based dashboard that allows users to monitor their work habits in real-time and receive AI-driven assessments and recommendations to mitigate the risks of digital burnout.

## 📜 Project Motivation

This project was built to satisfy the core aim and objectives of the accompanying research paper. It serves as a proof-of-concept demonstrating how modern AI techniques can be leveraged to create proactive wellness tools.

The system is designed to fulfill the following research objectives:

- **Behavioral Tracking Module**: To design a module that can monitor work patterns and identify overworking signals. The app's Activity tab implements a real-time work session tracker.
- **Emotion Analysis Engine**: To develop an engine that determines emotional signs of burnout from communications. The Assessment tab uses a pre-trained BERT-based NLP model from Hugging Face to analyze user-submitted text.
- **Machine Learning Burnout Scoring Model**: To create a model that generates real-time risk ratings. A pre-trained Random Forest Classifier integrates behavioral and emotional data to produce a burnout risk score.
- **Embedded Recommendation System**: To provide personalized, evidence-based interventions. The Recommendations tab generates intelligent alerts and actionable suggestions based on the user's latest assessment.

## ✨ Key Features

- **Real-Time Activity Tracking**: Start, stop, and time your work sessions. Track your total work hours and the number of breaks you take each day. All data is saved persistently.
- **AI-Powered Burnout Assessment**: Submit a work-related message to have its sentiment analyzed by an NLP model. The app combines this with your daily work data to calculate a burnout risk score.
- **Historical Trend Analysis**: Visualize your burnout risk score over time with an interactive line chart, helping you identify patterns and trends in your wellbeing.
- **Personalized Recommendations**: Receive actionable, evidence-based advice tailored to your current risk level to help you maintain a healthy work-life balance.

## 🛠️ Technology Stack & Architecture

- **Frontend**: Streamlit (for the interactive web dashboard)
- **Backend & Machine Learning**:
  - Python 3.9+
  - Scikit-learn: For training the Random Forest prediction model
  - Hugging Face Transformers: For the pre-trained sentiment analysis NLP model (distilbert-base-uncased)
  - Pandas: For data manipulation
- **Database**: SQLite (for persistent storage of tracking and assessment data)

## 📂 Project Structure

```
/digital_burnout_detection
├── /models
│   ├── burnout_model.pkl       # Pre-trained Scikit-learn classification model
│   └── scaler.pkl              # Pre-trained feature scaler
│
├── /modules
│   ├── __init__.py
│   ├── behavioral_tracker.py   # Simulates behavioral data collection
│   ├── emotion_analyzer.py     # Class for sentiment analysis using Transformers
│   ├── prediction_engine.py    # Class to run the burnout prediction model
│   └── recommendation_system.py  # Class to generate personalized advice
│
├── /static
│   └── style.css               # Custom CSS for styling the Streamlit UI
│
├── app.py                      # The main Streamlit application script
├── database.py                 # Handles all SQLite database operations
├── requirements.txt            # All required Python libraries
└── README.md                   # This file
```

## 🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

### Prerequisites

- Python 3.9 or newer installed
- Git for cloning the repository
- An internet connection is required for the initial setup to download the NLP model

### 1. Clone the Repository

Open your terminal or command prompt and clone the repository:

```bash
git clone <your-repository-url>
cd digital_burnout_detection
```

### 2. Create a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies

Install all the required Python libraries from the requirements.txt file:

```bash
pip install -r requirements.txt
```

> **Note**: The transformers and torch libraries are quite large and may take a few minutes to install.

## ▶️ Running the Application

Once the setup is complete, you can run the Streamlit application with a single command:

```bash
streamlit run app.py
```

Your default web browser will automatically open a new tab with the Digital Wellness Monitor running locally.

> **Important**: The first time you run the app, the transformers library will download the pre-trained sentiment analysis model (~268MB). This is a one-time process and requires an internet connection.

## 🧠 How the Modules Work

- **database.py**: Manages a simple SQLite database (`wellness_data.db`) that stores daily work metrics and historical assessment scores, ensuring your data persists between sessions.

- **emotion_analyzer.py**: When you submit text for an assessment, this module uses a powerful, pre-trained NLP model to determine if the sentiment is positive or negative and assigns it a numerical score.

- **prediction_engine.py**: This module takes your real-time behavioral data (work hours, breaks) and the sentiment score as input, scales them, and feeds them into the trained `burnout_model.pkl` to calculate your final burnout risk score.

- **recommendation_system.py**: Based on your risk score and specific data points (like long work hours), this module generates a tailored, helpful suggestion to guide you toward better work habits.