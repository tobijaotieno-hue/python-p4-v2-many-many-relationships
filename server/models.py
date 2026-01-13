# server/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Naming convention for Alembic migrations
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

# Association table for many-to-many relationship
employee_meetings = db.Table(
    'employees_meetings',
    metadata,
    db.Column('employee_id', db.Integer, db.ForeignKey('employees.id'), primary_key=True),
    db.Column('meeting_id', db.Integer, db.ForeignKey('meetings.id'), primary_key=True)
)

# Employee model
class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    hire_date = db.Column(db.Date)

    # Many-to-many relationship with Meeting
    meetings = db.relationship(
        'Meeting',
        secondary=employee_meetings,
        back_populates='employees'
    )

    def __repr__(self):
        return f'<Employee {self.id}, {self.name}, {self.hire_date}>'

# Meeting model
class Meeting(db.Model):
    __tablename__ = 'meetings'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String)
    scheduled_time = db.Column(db.DateTime)
    location = db.Column(db.String)
    
    # Many-to-many relationship with Employee
    employees = db.relationship(
        'Employee',
        secondary=employee_meetings,
        back_populates='meetings'
    )

    def __repr__(self):
        return f'<Meeting {self.id}, {self.topic}, {self.scheduled_time}, {self.location}>'

# Project model
class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    budget = db.Column(db.Integer)

    def __repr__(self):
        return f'<Project {self.id}, {self.title}, {self.budget}>'
