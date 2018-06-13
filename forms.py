from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, StringField, FileField, RadioField, BooleanField, SelectField


class SupaPlayaMaka(FlaskForm):
    amount = IntegerField('How many files to input?')
    submit = SubmitField('Submit')
    filename = StringField('Enter file name')
    videofile = FileField('Select files', render_kw={'multiple': True})
    entryid = StringField('Entry ID')
    playerchoice = RadioField('Player Type', choices=[('standardplayer','Standard Player'),('audioplayer','Audio Player')], default='standardplayer')
    slidefile = FileField('Select files', render_kw={'multiple': True})
    slidefolder = FileField('Select folder')
    width = StringField('Width', render_kw={"placeholder": "Width"})
    height = StringField('Height', render_kw={"placeholder": "Height"})
    fadeopt = BooleanField('Fade transition?')
    captionfile = FileField('Select files', render_kw={'multiple': True})
    sendmetadata = SubmitField('Populate video ids')
    folderpath = FileField('Select file')
    continuetonext = SubmitField('Continue')
    slideshowfolder = StringField('Slideshow folder', render_kw={"placeholder": "Slideshow folder"})
    college = SelectField(
    'College',
    choices=[('CAS', 'CAS'), ('CFA', 'CFA'), ('COM', 'COM'), ('ENG', 'ENG'), ('GMS', 'GMS'), ('LAW', 'LAW'), ('MET/AR', 'MET/AR'),
    ('MET/CIS', 'MET/CIS'), ('MET/CJ', 'MET/CJ'), ('CET/CPE', 'MET/CPE'), ('MET/HCOM', 'MET/HCOM'), ('MET/MS_M', 'MET/MS_M'), ('MET/ODE', 'MET/ODE'), ('MET/UDCP', 'MET/UDCP'), ('PUBLIC', 'PUBLIC'),
    ('SAR', 'SAR'), ('SED', 'SED'), ('SMG', 'SMG'), ('SSW/IGSW', 'SSW/IGSW'), ('SSW/MSW', 'SSW/MSW'), ('STH', 'STH')]
    )
    course = StringField('Course number', render_kw={"placeholder": "Course"})
