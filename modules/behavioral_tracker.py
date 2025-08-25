import numpy as np

class BehavioralTracker:
    """
    (Objective 1) A module to track employee behavioral data.
    This class simulates fetching data that would otherwise come from
    system monitoring APIs (e.g., Google Calendar, Slack, Jira, RescueTime).
    """
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def get_work_patterns(self):
        """
        Simulates fetching work hour and break data.
        - In a real app, this could analyze calendar events or active window time.
        """
        print(f"INFO: Tracking work patterns for employee {self.employee_id}...")
        # Simulate a user who is slightly overworked
        simulated_data = {
            'avg_work_hours_per_day': np.random.normal(9.5, 1.5),
            'avg_break_time_minutes': np.random.normal(30, 10),
            'meeting_hours_per_week': np.random.normal(12, 4)
        }
        return simulated_data

    def get_productivity_metrics(self):
        """
        Simulates fetching productivity data.
        - In a real app, this could connect to a project management tool's API (e.g., Jira).
        """
        print(f"INFO: Tracking productivity for employee {self.employee_id}...")
        # Simulate a slightly decreasing task completion rate
        simulated_data = {
            'task_completion_rate': np.random.normal(0.75, 0.1)
        }
        return simulated_data