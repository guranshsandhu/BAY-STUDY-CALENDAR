# Week 8 model plan

Status: design proposal; parameters and outputs are not yet validated.

Nine variables: Concept1Difficulty, Concept2Difficulty, Concept3Difficulty
(each easy/hard); Mastery (low/high); CurrentStress (low/high);
DaysRemaining (near/far); StudyAction (intensive/review/rest);
ExamSuccess (false/true); ResultingStress (low/high).

Use the input exam date to calculate days remaining. Proposed near/far split:
near means 0-7 days, far means 8+ days. Reject past exam dates in the final app.
Mastery initially represents overall mastery across the three concepts.

Each concept difficulty, Mastery, DaysRemaining and StudyAction points to
ExamSuccess. CurrentStress, DaysRemaining and StudyAction point to ResultingStress.
This retains distinct difficulty variables for at least three concepts.
All input roots and CPTs will be handcrafted and explained in Week 9.
To manage the 96 parent combinations of ExamSuccess, generate the table from
a documented monotonic rule and review its values; do not hand-enter it blindly.

Inference: for each candidate action a, query the joint distribution
P(ExamSuccess, ResultingStress | observed inputs, StudyAction=a)
using pgmpy VariableElimination. Treat StudyAction as a controlled root with
no incoming edges; its prior is bookkeeping, not a learned user preference.

Proposed utility: U(success, stress) = 100*I(success) - 30*I(high stress).
Compute EU(a)=sum over success/stress states of P(states|evidence,a)*U(states).
Select the maximum expected utility, breaking ties toward fewer study hours.
The utility weights and action effects need justification and scenario testing.
No decision should be hardcoded to match an expected scenario.

Actions: intensive = 5-hour block today; review = 1-hour session today;
rest = no new study session, and remove only planner-owned study events if
rest-day clearing is later implemented. Never delete unrelated calendar events.
Use a separate test calendar and label events created by this application.

Recompute when mastery, difficulty, stress or exam timing changes. Initial
version can use a manual refresh button rather than background automation.
Test differing scenario choices after CPTs are implemented; predictions are
not known yet. Check sensitivity to stress weights and time remaining.
