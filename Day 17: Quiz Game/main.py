#This Python script sets up a quiz using data from a question_data list stored in a separate module. 
#It imports the Question class from question_model.py, the question_data list from data.py, and the QuizBrain class from quiz_brain.py. 
#The script then creates a list Question_Bank by extracting question text and answers from question_data and using them to instantiate Question objects, which are added to the Question_Bank. A QuizBrain object called quiz is initialized with the Question_Bank. 
#The script then runs a loop to ask each question, get user answers, and update the score accordingly using the methods in the QuizBrain class. 
#Once all questions have been asked, it prints the completion message along with the final score. 
#The inner workings of the Question, QuizBrain, and question_data classes are not detailed in this code snippet.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = []
for question in question_data:
    question_text = question["text"]
    question_answer= question["answer"]
    new_question= Question(question_text, question_answer)
    Question_Bank.append(new_question)

quiz = QuizBrain(Question_Bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
