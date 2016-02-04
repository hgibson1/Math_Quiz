import question
import datetime
import random


class Quiz(object):
    questions = []
    answers = []
    start = None
    end = None 
 
    def __init__(self):
        #generates 10 random questions
        types = (
            question.Add, 
            question.Multiply,
            question.Subtract,
            question.Divide
        )
        for _ in range(10):
            #underscore = throw away value
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            problem = random.choice(types)(num1, num2)
            self.questions.append(problem) 
                         
    def take(self):
        #log start time
        #ask all questions
        #log user answers
        #log time to complete
        #show summary
        self.start = datetime.datetime.now() 
        for question in self.questions:
            self.ask(question)        
        self.end = datetime.datetime.now()

    def ask(self, question):
        #log start time
        #capture answer
        #checks answer + store in answers
        #send elapsed time
        question.start()
        answer = None
        while answer is None:
            answer = raw_input("What is {}? ".format(question.text))
            try:
                #converts input to float with 3 decimal places
                answer = round(float(answer), 3) 
            except ValueError:
                print "Not a vaild answer"
                answer = None
        question.stop()
        self.answers.append(answer == question.answer) 
        print "You answered {}, answer was {}".format(answer, question.answer)
        print "You answered the question in {} seconds".format((question.endtime - question.starttime).seconds) 

    def summary(self):
        #print correct/incorrect user answers
        #print elapsed time
        trues = [answer for answer in self.answers if answer]
        print "{} out of {} correct".format(len(trues), len(self.answers))
        print "it took {} seconds to complete the test".format((self.end - self.start).seconds)

        
if __name__ == "__main__":
   quiz = Quiz() 
   quiz.take() 
   quiz.summary()
            
