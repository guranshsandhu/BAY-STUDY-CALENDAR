"""Action definitions and proposed outcome utility; no recommendation engine yet."""
from datetime import date
ACTIONS = {
    "intensive": {"hours": 5, "label": "Intensive study"},
    "review": {"hours": 1, "label": "Light review"},
    "rest": {"hours": 0, "label": "Rest day"},
}

def days_until_exam(exam_date, today=None):
    return (date.fromisoformat(exam_date) - (today or date.today())).days

def utility(exam_success, high_stress):
    # Proposed weights; review and justify during model development.
    return (100 if exam_success else 0) - (30 if high_stress else 0)

def choose_action(evidence):
    raise NotImplementedError("Expected utilities require the completed Bayesian model.")
