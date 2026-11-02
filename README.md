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
