import random


class Pycon2014:
    """Pycon 2014 GUIDO VAN ROSSUM

    When Guido Van Rossum take a stage in Pycon 2014
    He had multiple important topics to tell, so he pick some topics randomly
    with sample script, pick_question wich use a liste of questions from
    a txt file (questions.txt), each line represent a question
    """

    GUIDO_VAN_ROSSUM = "python author and inventor"

    questions = []

    @classmethod
    def pick_question_legacy(cls):
        """Guido V.Rossum used read with splitlines in this stage"""
        questions = open(".\\ressources\\questions.txt", "r").read().splitlines()
        question = random.choice(questions)
        print("Guido Van Rossum - lagacy -")
        print(question)

    @classmethod
    def set_questions(cls):
        """Here I'm using the with operator """

        with open(".\\ressources\\questions.txt") as question_file:
            for question in question_file:
                cls.questions.append(question)

    @classmethod
    def pick_question(cls):
        '''Pick a question from question list using choice'''
        if not cls.questions:
            cls.set_questions()

        random_question = random.choice(cls.questions)
        print("Q: {}".format(random_question.rstrip()))

    @classmethod
    def run(cls):
        cls.pick_question_legacy()
