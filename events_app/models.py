"""Create database models to represent tables."""
from events_app import db
from sqlalchemy.orm import backref
from enum import Enum

guest_event_table = db.Table('events_guests',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('guest_id', db.Integer, db.ForeignKey('guest.id'), primary_key=True)
)
class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    events_attending = db.relationship('Event', secondary=guest_event_table, backref=db.backref('guest_attending', lazy='dynamic'))

class EventType(Enum):
    PARTY = 'Party'
    STUDY = 'Study'
    NETWORKING = 'Networking'

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    date_and_time = db.Column(db.DateTime)
    event_type = db.Column(db.Enum(EventType))
    guests = db.relationship('Guest', secondary=guest_event_table, backref=db.backref('events', lazy='dynamic'))
