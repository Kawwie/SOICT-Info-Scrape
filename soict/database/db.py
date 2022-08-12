
from lib2to3.pgen2.token import STRING
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
engine = create_engine("sqlite:///db.sqlite", echo=True)
base = declarative_base()

class Teacher(base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key = True)
    name = Column(String)
    designation = Column(String)
    career = Column(String)
    link = Column(String)

    pub = relationship("Publication")
    prop = relationship("Proprietary")
    def __init__(self, teacher_id, name, designation, career, link):
        self.teacher_id = teacher_id
        self.name = name
        self.designation = designation
        self.career = career
        self.link = link
class Publication(base):
    __tablename__ = 'pub'
    pub_id = Column(Integer, primary_key = True)
    title = Column(String)
    author = Column(String)
    other_info = Column(String)
    publisher = Column(String)
    publication_year = Column(Integer)
    journal = Column(String)

    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))

    def __init__(self, pub_id, title, author, other_info, publisher, publication_year, journal, teacher_id):
        self.pub_id = pub_id
        self.title = title
        self.author = author
        self.other_info = other_info
        self.publisher = publisher
        self.publication_year = publication_year
        self.journal = journal
        self.teacher_id = teacher_id

class Proprietary(base):
    __tablename__ = 'proprietary'
    prop_id = Column(Integer, primary_key = True)
    title = Column(String)
    year = Column(Integer)

    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))

    def __init__(self,prop_id, title, year, teacher_id):
        self.prop_id = prop_id
        self.title = title
        self.year = year
        self.teacher_id = teacher_id

base.metadata.create_all(engine)
