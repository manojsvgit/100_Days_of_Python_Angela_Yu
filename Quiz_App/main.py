from pyfiglet import figlet_format
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

logo="Q u i z z "
print(figlet_format(logo))

question_bank=[]

for question in question_data:
    qtext=question["text"]
    qanswer=question["answer"]
    new_question=Question(qtext,qanswer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz ")
print(f"Your final score was : {quiz.score}/{len(question_bank)}")