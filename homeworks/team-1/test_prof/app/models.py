from test_prof.app.__init__ import db


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_test = db.Column(db.String(120))
    questions = db.relationship('Questions', backref='test', lazy='dynamic')

    def __init__(self, name):
        self.name_test = name


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200))
    direction_id = db.Column(db.Integer, db.ForeignKey('directions.id'))
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'))
    answers = db.relationship('Answers', backref='questions', lazy='dynamic')

    def __init__(self, question, direction_id, test_id):
        self.question = question
        self.direction_id = direction_id
        self.test_id = test_id


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(120))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    direction_id = db.Column(db.Integer, db.ForeignKey('directions.id'))

    def __init__(self, answer, question_id, direction_id):
        self.answer = answer
        self.question_id = question_id
        self.direction_id = direction_id


class Directions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_direction = db.Column(db.String(50))

    def __init__(self, name):
        self.name_direction = name