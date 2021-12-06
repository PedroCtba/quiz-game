# importing data with qiestios and object to construct questions
from question_model import Question
from data import question_data


questions = [(Question(dic['text'], dic['answer'])) for dic in question_data]