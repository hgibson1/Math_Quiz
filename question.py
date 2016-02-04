import datetime


class Question(object):
    text = None
    answer = None
    starttime = None
    endtime = None
    
    def start(self):
        self.starttime = datetime.datetime.now()

    def stop(self):
        self.endtime = datetime.datetime.now() 


class Add(Question):
    def __init__(self, num1,  num2):
        """
  
        >>> add = Add(1, 3)
        >>> add.answer
        4.0

        """
        self.text = "{} + {}".format(num1, num2)
        self.answer = round(float(num1) + float(num2), 3) 


class Multiply(Question):
    def __init__(self, num1, num2):
        """

        >>> mult = Multiply(1, 3)
        >>> mult.answer
        3.0

        """
        self.text = "{} * {}".format(num1, num2)
        self.answer = round(float(num1) * float(num2), 3)


class Subtract(Question):
    def __init__(self, num1, num2):
        """

        >>> sub = Subtract(3, 1)
        >>> sub.answer
        2.0

        """
        self.text = "{} - {}".format(num1, num2)
        self.answer = round(float(num1) - float(num2), 3)


class Divide(Question):
    def __init__(self, num1, num2):
        """

        >>> div = Divide(3, 1)
        >>> div.answer
        3.0

        """
        self.text = "{} / {}".format(num1, num2)
        self.answer = round(float(num1) / float(num2), 3)

