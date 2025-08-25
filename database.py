import sqlite3
from datetime import date
import pandas as pd # <--- THIS IS THE FIX

def init_db():
    """Initializes the database and creates tables if they don't exist."""
    conn = sqlite3.connect('wellness_data.db')
    cursor = conn.cursor()

    # Table for daily tracking metrics
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_tracking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        track_date DATE UNIQUE,
        total_work_seconds INTEGER DEFAULT 0,
        total_breaks INTEGER DEFAULT 0
    )
    ''')

    # Table for storing burnout assessment results
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        assessment_date DATE,
        risk_label INTEGER,
        risk_score REAL,
        sentiment_score REAL
    )
    ''')
    conn.commit()
    conn.close()

def get_or_create_today_tracking():
    """Gets today's tracking data or creates a new entry for today."""
    conn = sqlite3.connect('wellness_data.db')
    cursor = conn.cursor()
    today = date.today()
    cursor.execute("SELECT * FROM daily_tracking WHERE track_date = ?", (today,))
    today_data = cursor.fetchone()

    if today_data is None:
        cursor.execute("INSERT INTO daily_tracking (track_date) VALUES (?)", (today,))
        conn.commit()
        cursor.execute("SELECT * FROM daily_tracking WHERE track_date = ?", (today,))
        today_data = cursor.fetchone()

    conn.close()
    # Return as a dictionary for easier access
    return {"id": today_data[0], "date": today_data[1], "work_seconds": today_data[2], "breaks": today_data[3]}


def update_tracking_data(work_seconds, total_breaks):
    """Updates the work time and break count for today."""
    conn = sqlite3.connect('wellness_data.db')
    cursor = conn.cursor()
    today = date.today()
    cursor.execute("""
    UPDATE daily_tracking
    SET total_work_seconds = ?, total_breaks = ?
    WHERE track_date = ?
    """, (work_seconds, total_breaks, today))
    conn.commit()
    conn.close()

def save_assessment(risk_label, risk_score, sentiment_score):
    """Saves a new assessment result to the database."""
    conn = sqlite3.connect('wellness_data.db')
    cursor = conn.cursor()
    today = date.today()
    cursor.execute("""
    INSERT INTO assessments (assessment_date, risk_label, risk_score, sentiment_score)
    VALUES (?, ?, ?, ?)
    """, (today, risk_label, risk_score, sentiment_score))
    conn.commit()
    conn.close()

def get_assessment_history():
    """Retrieves historical assessment data for charts."""
    conn = sqlite3.connect('wellness_data.db')
    query = "SELECT assessment_date, risk_score FROM assessments ORDER BY assessment_date DESC LIMIT 30"
    # This line now works because pd is defined
    df = pd.read_sql_query(query, conn) 
    conn.close()
    return df

def get_latest_assessment():
    """Gets the most recent assessment from the database."""
    conn = sqlite3.connect('wellness_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assessments ORDER BY id DESC LIMIT 1")
    assessment = cursor.fetchone()
    conn.close()
    if assessment:
        return {"id": assessment[0], "date": assessment[1], "label": assessment[2], "score": assessment[3]}
    return None