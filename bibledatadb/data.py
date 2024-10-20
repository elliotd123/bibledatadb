#!/usr/bin/env python3

from bibledatadb import db
import csv
from sqlalchemy.orm import Session

rootFolder = 'bible-data/'

def populate_data():

    session = Session(db.engine)

    # Reference table
    with open(rootFolder + 'BibleData-Reference.csv', 'r') as csvfile:
        referenceReader = csv.reader(csvfile)
        fielse = next(referenceReader)
        for row in referenceReader:
            reference = db.Reference()
            reference.ReferenceID = row[0]
            reference.BookID = int(row[1])
            reference.USXCode = row[2]
            reference.Chapter = int(row[3])
            reference.Verse = int(row[4])
            reference.VerseSequence = int(row[5])
            session.add(reference)
        session.commit()

    # Person table
    with open(rootFolder + 'BibleData-Person.csv', 'r') as csvfile:
        personReader = csv.reader(csvfile)
        fields = next(personReader)
        for row in personReader:
            person = db.Person()
            person.PersonID = row[0]
            person.PersonName = row[1]
            person.Surname = row[2]
            person.UniqueAttribute = row[3]
            person.Sex = row[4]
            person.Tribe = row[5]
            person.PersonNotes = row[6]
            person.NameInstance = int(row[7])
            person.PersonSequence = int(row[8])
            session.add(person)
        session.commit()

    # Person Label table
    with open(rootFolder + 'BibleData-PersonLabel.csv', 'r') as csvfile:
        labelReader = csv.reader(csvfile)
        fields = next(labelReader)
        for row in labelReader:
            label = db.PersonLabel()
            label.PersonLabelID = row[0]
            label.PersonID = row[1]
            label.EnglishLabel = row[2]
            label.HebrewLabel = row[3]
            label.HebrewLabelTransliterated = row[4]
            label.HebrewLabelMeaning = row[5]
            label.HebrewStrongsNumber = row[6]
            label.GreekLabel = row[7]
            label.GreekLabelTransliterated = row[8]
            label.GreekLabelMeaning = row[9]
            label.GreekStrongsNumber = row[10]
            label.LabelReferenceID = row[11]
            label.LabelType = row[12]
            label.LabelGivenByGod = row[13]
            label.LabelNotes = row[14]
            label.PersonLabelCount = int(row[15])
            label.LabelSequence = int(row[16])
            #label.UnknownColumnR = int(row[17])
            #label.UnknownColumnS = int(row[18])
            #label.UnknownColumnT = int(row[19])
            session.add(label)
        session.commit()

    # Person Verse table
    with open(rootFolder + 'BibleData-PersonVerse.csv', 'r') as csvfile:
        personVerseReader = csv.reader(csvfile)
        fields = next(personVerseReader)
        for row in personVerseReader:
            personVerse = db.PersonVerse()
            personVerse.PersonVerseID = row[0]
            personVerse.ReferenceID = row[1]
            personVerse.PersonLabelID = row[2]
            personVerse.PersonID = row[3]
            personVerse.PersonLabel = row[4]
            try:
                personVerse.PersonLabelCount = int(row[5])
            except:
                personVerse.PersonLabelCount = 0
            personVerse.PersonVerseSequence = int(row[6])
            personVerse.PersonVerseNotes = row[7]
            session.add(personVerse)
        session.commit()

    #Place table
    with open(rootFolder + 'BibleData-Place.csv', 'r') as csvfile:
        placeReader = csv.reader(csvfile)
        fields = next(placeReader)
        for row in placeReader:
            place = db.Place()
            place.PlaceID = row[0]
            place.PlaceName = row[1]
            place.PlaceType = row[2]
            place.ModernEquivalent = row[3]
            place.PlaceNotes = row[4]
            place.OpenBibleID = row[5]
            place.OpenBibleURL = row[6]
            place.NameInstance = int(row[7])
            place.PlaceSequence = int(row[8])
            session.add(place)
        session.commit()

    # Commandments Table
    with open(rootFolder + 'BibleData-Commandments.csv', 'r') as csvfile:
        commandmentReader = csv.reader(csvfile)
        fields = next(commandmentReader)
        for row in commandmentReader:
            commandment = db.Commandment()
            commandment.CommandmentNumber = int(row[0])
            commandment.CommandmentConcept = row[1]
            commandment.CommandmentPolarity = row[2]
            commandment.ReferenceID = row[3]
            commandment.ScriptureEnglish = row[4]
            commandment.ScriptureHebrew = row[5]
            commandment.ScriptureGreek = row[6]
            commandment.ScriptureParashah = row[7]
            commandment.SeferHachinuchNumber = row[8]
            commandment.MishnehTorahBookNumber = int(row[9])
            commandment.MishnehTorahBookName = row[10]
            commandment.MishnehTorahCategory = row[11]
            commandment.P119FCategory = row[12]
            #commandment.UnknownColumnN = row[13]
            session.add(commandment)
        session.commit()

    session.close()
