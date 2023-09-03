class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.user_score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)

    def still_has_questions(self):
        return len(self.questions_list) > self.question_number

    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is {self.user_score}/{self.question_number}")
        print("\n")
