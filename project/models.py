from project import db  # pragma: no cover
from project import bcrypt  # pragma: no cover

from sqlalchemy import ForeignKey  # pragma: no cover
from sqlalchemy.orm import relationship   # pragma: no cover


class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, description, author_id):
        self.title = title
        self.description = description
        self.author_id = author_id

    def __repr__(self):
        return '<title {}>'.format(self.title)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<name: {}>'.format(self.name)

class Kickoff(db.Model):

    __tablename__ = "kickoff"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)
    papresults = relationship("PapResults", backref="kickoff")

    def __init__(self, location, date):
        self.location = location
        self.date = date

    def __repr__(self):
        return '<location: {}'.format(self.location), '<date: {}'.format(self.date)



class PapResults(db.Model):

    __tablename__ = "papresults"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    patientNumber = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    lmp = db.Column(db.String, nullable=True)
    adequateSample = db.Column(db.Integer, nullable=False)
    cellCount = db.Column(db.String, nullable=False)
    endocervicalCells = db.Column(db.Integer, nullable=False)
    metaplasticCells = db.Column(db.Integer, nullable=True)
    #How come the above works when the other "boolean" values below are OK with a "0" as the data even though they are nullable=False)?
    backgroundInflammation = db.Column(db.String, nullable=False)
    fungal = db.Column(db.Integer, nullable=False)
    trich = db.Column(db.Integer, nullable=False)
    hpv = db.Column(db.Integer, nullable=False)
    bacteria = db.Column(db.Integer, nullable=False)
    hsv = db.Column(db.Integer, nullable=False)
    impression = db.Column(db.String, nullable=False)
    advice = db.Column(db.String, nullable=False)
    doctor = db.Column(db.String, nullable=False)
    disposition = db.Column(db.String, nullable=False)
    kickoff_id = db.Column(db.Integer, ForeignKey('kickoff.id'))

    def __init__(self, name, age, patientNumber, phone, address, lmp, adequateSample, cellCount, endocervicalCells, metaplasticCells, backgroundInflammation, fungal, trich, hpv, bacteria, hsv, impression, advice, doctor, disposition, kickoff_id):
        self.name = name
        self.age = age
        self.patientNumber = patientNumber
        self.phone = phone
        self.address = address
        self.lmp = lmp
        self.adequateSample = adequateSample
        self.cellCount = cellCount
        self.endocervicalCells = endocervicalCells
        self.metaplastiCells = metaplasticCells
        self.backgroundInflammation = backgroundInflammation
        self.fungal = fungal
        self.trich = trich
        self.hpv = hpv
        self.bacteria = bacteria
        self.hsv = hsv
        self.impression = impression
        self.advice = advice
        self.doctor = doctor
        self.disposition = disposition
        self.kickoff_id = kickoff_id

    def __repr__(self):
        return '<name: {}>'.format(self.name)
