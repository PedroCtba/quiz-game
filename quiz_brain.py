# make class quiz brain with 2 atributes, the number of the question, and the list of questions
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0 # this always initialize as 0
        self.score = 0 # this always initialize as 0
        self.question_list = question_list
        

    def ask(self):
        current_q = self.question_number
        reply = input(f'{self.question_list[current_q].text} (True/False): ')
        self.check(reply, self.question_list[current_q].answer)
        self.question_number += 1
        

    def keep_asking(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print(f'You finished the quiz, your score was ({self.score}/{self.question_number})')
            return False


    def check(self, reply, current_a):
        if reply.lower() == current_a.lower():
            self.score += 1
            print(f'You are right! Your current score is {self.score}/{self.question_number + 1}')
            return True
        else:
            print(f'Sorry that"s wrong! Your current score is {self.score}/{self.question_number + 1}')
            return False