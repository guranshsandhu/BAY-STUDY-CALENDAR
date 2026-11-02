"""Week 8 model specification. CPTs and inference are planned for Week 9-11."""
VARIABLES = {
    "Concept1Difficulty": ["easy", "hard"],
    "Concept2Difficulty": ["easy", "hard"],
    "Concept3Difficulty": ["easy", "hard"],
    "Mastery": ["low", "high"],
    "CurrentStress": ["low", "high"],
    "DaysRemaining": ["near", "far"],
    "StudyAction": ["intensive", "review", "rest"],
    "ExamSuccess": ["false", "true"],
    "ResultingStress": ["low", "high"],
}
EDGES = [(v, "ExamSuccess") for v in
         ["Concept1Difficulty", "Concept2Difficulty", "Concept3Difficulty",
          "Mastery", "DaysRemaining", "StudyAction"]] + [
         (v, "ResultingStress") for v in
         ["CurrentStress", "DaysRemaining", "StudyAction"]]

def build_model():
    raise NotImplementedError("Week 8 scaffold: CPTs and inference are not implemented yet.")
