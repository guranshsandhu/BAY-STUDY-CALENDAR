"""Week 8 interface preview: displays inputs without simulated predictions."""
import json
from pathlib import Path
import streamlit as st
from src.planner import ACTIONS
st.title("Bayesian Study Planner")
st.info("Week 8 setup: Bayesian predictions and calendar integration are not implemented yet.")
st.date_input("Upcoming exam date")
for n in range(1, 4):
    st.selectbox(f"Concept {n} difficulty", ["easy", "hard"])
st.selectbox("Current mastery", ["low", "high"])
st.selectbox("Current stress", ["low", "high"])
st.subheader("Planned actions")
for a in ACTIONS.values():
    st.write(f"{a['label']}: {a['hours']} hours")
st.subheader("Demonstration scenarios")
st.json(json.loads((Path(__file__).parent / "data/scenarios.json").read_text()))
