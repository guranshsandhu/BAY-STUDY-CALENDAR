"""Check starter files and proposed utility without third-party dependencies."""
import json
from pathlib import Path
from src.bayes_model import VARIABLES, EDGES
from src.planner import ACTIONS, utility, days_until_exam
from datetime import date
root = Path(__file__).parent
assert len(VARIABLES) == 9
assert len(ACTIONS) == 3
assert all(a in VARIABLES and b in VARIABLES for a,b in EDGES)
assert utility(True, False) == 100
assert utility(True, True) == 70
assert days_until_exam("2026-11-10", date(2026,11,1)) == 9
scenarios=json.loads((root / "data/scenarios.json").read_text())
for s in scenarios:
    assert all(value in VARIABLES[key] for key,value in s['evidence'].items())
assert len(scenarios) == 3
print("Week 8 setup check passed: 9 variables, 3 actions, 3 valid scenarios.")
print("CPTs, inference, action selection, and calendar writes remain planned work.")
