from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')


class BankAccountForm(db.Model):
    form_type = db.Column(db.String(50))
    owner_first_name = db.Column(db.String(50), nullable=False)
    owner_middle_initial = db.Column(db.String(2))
    owner_last_name = db.Column(db.String(50), nullable=False)
    account_number = db.Column(db.Integer, primary_key=True)
    joint_owner_first_name = db.Column(db.String(50))
    joint_owner_middle_initial = db.Column(db.String(2))
    joint_owner_last_name = db.Column(db.String(50))
    party_name = db.Column(db.String(100))
    auth_person = db.Column(db.String(100))
    other_auth_person = db.Column(db.String(100))
    annual_income = db.Column(db.String(50))
    liquid_net_worth = db.Column(db.String(50))
    total_net_worth = db.Column(db.String(50))
    owner_signature_1 = db.Column(db.String(100))
    date_1 = db.Column(db.String(50))
    owner_signature_2 = db.Column(db.String(100))
    date_2 = db.Column(db.String(50))
    last_updated_ts = db.Column(db.DateTime, default=datetime.utcnow)


class CreditCardForm(db.Model):
    form_type = db.Column(db.String(50))
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    account_number = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    payment_option = db.Column(db.String(100))
    checking_acc_num = db.Column(db.String(20))
    checking_aba_num = db.Column(db.String(20))
    checking_start = db.Column(db.String(20))
    savings_acc_num = db.Column(db.String(20))
    savings_aba_num = db.Column(db.String(20))
    savings_start = db.Column(db.String(20))
    payment_amount = db.Column(db.Integer)
    signature = db.Column(db.String(100))
    payment_date = db.Column(db.String(20))
    auth_type = db.Column(db.String(100))
    last_updated_ts = db.Column(db.DateTime, default=datetime.utcnow)


class MedicalRecordsForm(db.Model):
    form_type = db.Column(db.String(50))
    first_name = db.Column(db.String(50), nullable=False)
    middle_initial = db.Column(db.String(2))
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), primary_key=True)
    phone = db.Column(db.String(20), nullable=False)
    mailing_address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip_code = db.Column(db.String(10), nullable=False)
    birthday = db.Column(db.String(50), nullable=False)
    last_appointment = db.Column(db.String(100))
    location = db.Column(db.String(200))
    record_format = db.Column(db.String(100))
    information = db.Column(db.String(100))
    other_party = db.Column(db.String(100))
    relationship = db.Column(db.String(100))
    other_address = db.Column(db.String(100))
    other_city = db.Column(db.String(50))
    other_state = db.Column(db.String(50))
    other_zip = db.Column(db.String(10))
    other_fax = db.Column(db.String(50))
    other_phone = db.Column(db.String(20))
    other_email = db.Column(db.String(100))
    age_status = db.Column(db.String(20))
    other_relationship = db.Column(db.String(50))
    signature_1 = db.Column(db.String(100))
    sign_date_1 = db.Column(db.String(50))
    signature_2 = db.Column(db.String(100))
    sign_date_2 = db.Column(db.String(50))
    last_updated_ts = db.Column(db.DateTime, default=datetime.utcnow)
