# BAY-STUDY-CALENDAR

## Overview
A personalized study planning system that uses Bayesian inference and
the Google Calendar API to schedule sessions before upcoming exams.

## Planned Model
The Bayesian network will model the difficulty of at least three course
concepts, student mastery, current stress, and days remaining until an
exam. The network will contain approximately 10 variables or fewer.

Model variables and handcrafted conditional probability tables will
be documented with explanations of their parameters.

## Decision Making
The system will compare three actions:
- Schedule an intensive 5-hour study block.
- Schedule a light 1-hour review session.
- Recommend a rest day without adding a study session.

For each action, built-in Bayesian inference will predict exam success
and stress. A utility function will balance these outcomes, and the
system will choose the action with the highest expected utility.

## Planned Technologies
- Python
- pgmpy
- Google Calendar API
- google-api-python-client
- google-auth-oauthlib
- Streamlit

## Timeline
- Week 8: Repository setup, scope, and initial project structure.
- Week 9: Network design and handcrafted CPTs.
- Week 10: Light review and preparation of test scenarios.
- Week 11: Inference, utility calculations, and calendar integration.
- Week 12: Minimal interface, scenario testing, and essential fixes.
- Week 13: Presentation video and demonstration.
- Week 14: Final documentation and deliverables.

## Current Status
Week 8: Initial project setup. Implementation is not yet complete.

## Planned Demonstration
Compare struggling and advanced students, along with a student
experiencing high stress, to demonstrate different scheduling decisions.

## Week 8 implementation and setup

Project structure, nine-variable model specification, action definitions,
three sample scenarios, proposed utility, setup checker and interface preview
are implemented. CPTs, Bayesian inference, expected utility action selection,
OAuth and calendar writes are not implemented. No prediction results are claimed.

## Setup on Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe setup_check.py
.\.venv\Scripts\python.exe -m streamlit run app.py
```
Activation is optional; these commands avoid PowerShell activation-policy issues.
Use Python 3.11 or 3.12 for a straightforward dependency setup.

## macOS/Linux
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python setup_check.py
.venv/bin/python -m streamlit run app.py
```
The setup check uses only Python's standard library. The interface needs Streamlit.

## Files
- src/bayes_model.py: proposed variables/edges and explicit model placeholder.
- src/planner.py: three actions, date helper and proposed utility.
- src/calendar_client.py: explicit Calendar integration placeholder.
- app.py: Week 8 input/interface preview.
- data/scenarios.json: struggling, advanced and highly stressed scenarios.
- docs/model-plan.md: inference task, action semantics and expected utility design.
- docs/calendar-setup.md: Google account configuration steps.
- docs/timeline.md: Weeks 8-14 milestones.
- setup_check.py: verifies starter structure and valid scenario states.
- requirements.txt: dependency ranges; exact versions can be locked after local installation.

## Known limitations
This is a Week 8 scaffold, not a functioning scheduling system. The UI shows
inputs and scenarios only; inputs are not yet used for recommendations.
Review and refine the model, weights and implementation as the project develops.

##AI assistance: 
I used ChatGPT to help prepare the initial Week 8 project structure, starter code, and documentation. Bayesian inference and calendar integration are not yet implemented. I will review, test, and develop this foundation as the project progresses.

## Credential handling
credentials.json, token.json, .env and .venv are ignored by Git.
Use a dedicated test calendar; keep credentials out of uploads.
