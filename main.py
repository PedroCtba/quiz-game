# importing data with qiestios and object to construct questions
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# making a question bank
question_bank = [(Question(dic['text'], dic['answer'])) for dic in question_data]

# init quiz brain
quiz = QuizBrain(question_bank)

while quiz.keep_asking():
  quiz.ask()