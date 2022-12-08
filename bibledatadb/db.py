#!/usr/bin/env python3

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

metadata_obj = MetaData()

Base = declarative_base(metadata=metadata_obj)
engine = create_engine("sqlite:///bible-data.db")

class Reference(Base):
    """BibleData-Reference table definition"""
    __tablename__ = 'reference'
    ID = Column(Integer, primary_key=True)
    ReferenceID = Column(String(256), index=True)
    BookID = Column(Integer, index=True)
    USXCode = Column(String(8))
    Chapter = Column(Integer)
    Verse = Column(Integer)
    VerseSequence = Column(Integer)

class Person(Base):
    """BibleData-Person table definition"""
    __tablename__ = 'person'
    ID = Column(Integer, primary_key=True)
    PersonID = Column(String(256), index=True)
    PersonName = Column(String(256), index=True)
    Surname = Column(String(256))
    UniqueAttribute = Column(String(2048))
    Sex = Column(String(16))
    Tribe = Column(String(256))
    PersonNotes = Column(String(2048))
    NameInstance = Column(Integer)
    PersonSequence = Column(Integer)

class PersonLabel(Base):
    """BibleData-PersonLabel table definition"""
    __tablename__ = 'person_label'
    ID = Column(Integer, primary_key=True)
    PersonLabelID = Column(String(256), index=True)
    PersonID = Column(String(256), index=True)
    EnglishLabel = Column(String(256))
    HebrewLabel = Column(String(256))
    HebrewLabelTransliterated = Column(String(256))
    HebrewLabelMeaning = Column(String(2048))
    HebrewStrongsNumber = Column(String(256))
    GreekLabel = Column(String(256))
    GreekLabelTransliterated = Column(String(256))
    GreekLabelMeaning = Column(String(2048))
    GreekStrongsNumber = Column(String(256))
    LabelReferenceID = Column(String(64), index=True)
    LabelType = Column(String(64))
    LabelGivenByGod = Column(String(64))
    LabelNotes = Column(String(2048))
    PersonLabelCount = Column(Integer)
    LabelSequence = Column(Integer)
    #UnknownColumnR = Column(Integer)
    #UnknownColumnS = Column(Integer)
    #UnknownColumnT = Column(Integer)

class Commandment(Base):
    """BibleData-Commandments table definition"""
    __tablename__ = 'commandment'
    ID = Column(Integer, primary_key=True)
    CommandmentNumber = Column(Integer)
    CommandmentConcept = Column(String(1024))
    CommandmentPolarity = Column(String(1))
    ReferenceID = Column(String(32), index=True)
    ScriptureEnglish = Column(String(2048))
    ScriptureHebrew = Column(String(2048))
    ScriptureGreek = Column(String(2048))
    ScriptureParashah = Column(String(1024))
    SeferHachinuchNumber = Column(String(64))
    MishnehTorahBookNumber = Column(Integer)
    MishnehTorahBookName = Column(String(64))
    MishnehTorahCategory = Column(String(128))
    P119FCategory = Column(String(128))
    #UnknownColumnN = Column(String(64))


def create_database():
    metadata_obj.create_all(engine)
