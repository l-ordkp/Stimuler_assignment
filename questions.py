class QuestionnaireManager:
    def __init__(self, questions):
        self.questions = questions

    def get_next_question(self, asked_questions):
        for question in self.questions:
            if question not in asked_questions:
                return question
        return None  # No more questions available
