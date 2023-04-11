from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, BankAccountForm, CreditCardForm, MedicalRecordsForm
from werkzeug.security import generate_password_hash, check_password_hash
from . import db    ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import inspect
from datetime import datetime



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if len(email) < 8:
            flash('Please enter a valid password, try again.', category='error')
        elif "@" not in email:
            flash('Please enter a valid password, try again.', category='error')
        else:
            return redirect(url_for('auth.forms'))

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('sign_up.html', user=current_user)


#Bank Account Form
@auth.route('/bankaccountform',  methods=['GET', 'POST'])
def bankaccountform():
    flash(request.method)
    if request.method == 'POST':
        inspector = inspect(db.engine)
        if inspector.has_table('BankAccountForm'):
            flash("bankaccount table exists", category='success')
        else:
            flash("bankaccount table does not exist", category='error')

        account_number = request.form.get('account_num')
        owner_first_name = request.form.get('owner_fname')
        owner_middle_initial = request.form.get('owner_mid_initial')
        owner_last_name = request.form.get('owner_lname')
        joint_owner_first_name = request.form.get('joint_owner_fname')
        joint_owner_middle_initial = request.form.get('joint_owner_mid_initial')
        joint_owner_last_name = request.form.get('joint_owner_lname')
        party_name = request.form.get('company_name')
        auth_person = request.form.get('authorized_person_name')
        other_auth_person = request.form.get('other_authorized_person_name')
        annual_income = request.form.getlist('annual_income')
        liquid_net_worth = request.form.get('liquid_net_worth')
        total_net_worth = request.form.get('total_net_worth')
        owner_signature_1 = request.form.get('owner_signature1')
        date_1 = request.form.get('get_date_1')
        owner_signature_2 = request.form.get('owner_signature2')
        date_2 = request.form.get('get_date_2')
        last_updated_ts = datetime.utcnow()

        if not all([account_number, owner_first_name, owner_last_name, joint_owner_first_name, joint_owner_last_name,
                    annual_income, liquid_net_worth, total_net_worth, owner_signature_1, date_1]):
            flash('account number and the first_name and last_name of both parties cannot be blank.'
                  'Account information cannot be left blank', category='error')
        elif date_1 == '' or date_2 == '':
            flash('dates cannot be blank. please use today\'s date for both dates otherwise.', category='error')
        else:
            new_form = BankAccountForm(form_type="Vanguard Bank Account Form",
                                       account_number=account_number,
                                       owner_first_name=owner_first_name,
                                       owner_middle_initial=owner_middle_initial,
                                       owner_last_name=owner_last_name,
                                       joint_owner_first_name=joint_owner_first_name,
                                       joint_owner_middle_initial=joint_owner_middle_initial,
                                       joint_owner_last_name=joint_owner_last_name,
                                       party_name=party_name,
                                       auth_person=auth_person,
                                       other_auth_person=other_auth_person,
                                       annual_income=annual_income,
                                       liquid_net_worth=liquid_net_worth,
                                       total_net_worth=total_net_worth,
                                       owner_signature_1=owner_signature_1,
                                       date_1=date_1,
                                       owner_signature_2=owner_signature_2,
                                       date_2=date_2,
                                       last_updated_ts=last_updated_ts)

            db.session.add(new_form)  # adding the note to the database
            db.session.commit()
            flash('Form added!', category='success')
            return redirect(url_for('auth.records'))
    else:
        flash('Problem request.method', category='error')
    return render_template('AccountForm.html', user=current_user)


#Credit Card Form
@auth.route('/CreditCardForm',  methods=['GET', 'POST'])
def creditcardform():
    #flash('first_name, last_name, email, and account number cannot be blank', category='error')
    flash(request.method)
    if request.method == 'POST':
        inspector = inspect(db.engine)
        if inspector.has_table('CreditCardForm'):
            flash("creditform table exists", category='success')
        else:
            flash("creditform table does not exist", category='error')

        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        account_number = request.form.get('account_num')
        phone = request.form.get('phone')
        payment_option = request.form.get('credit_auth')
        checking_acc_num = request.form.get('checking_acc_num')
        checking_aba_num = request.form.get('checking_aba_num')
        checking_start = request.form.get('checking_start_month')
        savings_acc_num = request.form.get('saving_acc_num')
        savings_aba_num = request.form.get('saving_aba_num')
        savings_start = request.form.get('saving_start_month')
        payment_amount = request.form.get('amount')
        signature = request.form.get('signature')
        payment_date = request.form.get('get_date')
        auth_type = request.form.get('payments')
        last_updated_ts = datetime.utcnow()

        if not all([first_name, last_name, email, account_number]):
            flash('first_name, last_name, email, and account number cannot be blank', category='error')
        elif not all([auth_type, payment_amount, payment_date]):
            flash('authentication, payment and account number cannot be left blank', category='error')
        #elif not all([checking_acc_num, checking_aba_num, savings_aba_num, savings_acc_num]):
        #    flash('checking and savings numbers cannot be left blank. please leave a \'0\' if n/a', category='error')
        else:
            new_form = CreditCardForm(form_type="FirstTech Credit Card Form",
                                      first_name=first_name,
                                      last_name=last_name,
                                      email=email,
                                      account_number=account_number,
                                      phone=phone,
                                      payment_option=payment_option,
                                      checking_acc_num=checking_acc_num,
                                      checking_aba_num=checking_aba_num,
                                      checking_start=checking_start,
                                      savings_acc_num=savings_acc_num,
                                      savings_aba_num=savings_aba_num,
                                      savings_start=savings_start,
                                      payment_amount=payment_amount,
                                      signature=signature,
                                      payment_date=payment_date,
                                      auth_type=auth_type,
                                      last_updated_ts=last_updated_ts)

            db.session.add(new_form)  # adding the note to the database
            db.session.commit()
            flash('Form added!', category='success')
            return redirect(url_for('auth.records'))

    return render_template('CreditCardForm.html', user=current_user)


#Medical Records Form
@auth.route('/medicalrecordform', methods=['GET', 'POST'])
def medicalrecordsform():
    flash(request.method)
    if request.method == 'POST':
        inspector = inspect(db.engine)
        if inspector.has_table('MedicalRecordsForm'):
            flash("medicalrecords table exists", category='success')
        else:
            flash("medicalrecords table does not exist", category='error')

        first_name = request.form.get('fname')
        middle_initial = request.form.get('mid_initial')
        last_name = request.form.get('lname')
        email = request.form.get('email')
        phone = request.form.get('phone')
        mailing_address = request.form.get('mail_address')
        city = request.form.get('city')
        state = request.form.get('state')
        zip_code = request.form.get('zip_code')
        birthday = request.form.get('birthday')
        last_appointment = request.form.get('last_appt')
        location = request.form.getlist('Question2')
        record_format = request.form.get('Question4')
        information = request.form.get('Question6')
        other_party = request.form.get('end_name')
        relationship = request.form.get('end_relationship')
        other_address = request.form.get('end_address')
        other_city = request.form.get('end_city')
        other_state = request.form.get('end_state')
        other_zip = request.form.get('end_zip')
        other_fax = request.form.get('end_fax')
        other_phone = request.form.get('end_phone')
        other_email = request.form.get('end_email')
        status = request.form.get('Question7')
        signature_1 = request.form.get('signature_1')
        sign_date_1 = request.form.get('current_date_1')
        other_relationship = request.form.get('other_relationship')
        signature_2 = request.form.get('signature_2')
        sign_date_2 = request.form.get('current_date_2')
        last_updated_ts = datetime.utcnow()

        if not all([first_name, last_name, email, phone, mailing_address, city, state, zip_code, signature_1, sign_date_1]):
            flash('first_name, last_name, email, mailing_address, city, state, zip_code, signature or date cannot be blank', category='error')
        else:
            new_form = MedicalRecordsForm(form_type="Legacy Health medical Record Form",
                                          first_name=first_name,
                                          middle_initial=middle_initial,
                                          last_name=last_name,
                                          email=email,
                                          phone=phone,
                                          mailing_address=mailing_address,
                                          city=city,
                                          state=state,
                                          zip_code=zip_code,
                                          birthday=birthday,
                                          last_appointment=last_appointment,
                                          location=location,
                                          record_format=record_format,
                                          information=information,
                                          other_party=other_party,
                                          relationship=relationship,
                                          other_address=other_address,
                                          other_city=other_city,
                                          other_state=other_state,
                                          other_zip=other_zip,
                                          other_phone=other_phone,
                                          other_fax=other_fax,
                                          age_status=status,
                                          other_email=other_email,
                                          other_relationship=other_relationship,
                                          signature_1=signature_1,
                                          sign_date_1=sign_date_1,
                                          signature_2=signature_2,
                                          sign_date_2=sign_date_2,
                                          last_updated_ts=last_updated_ts)

            db.session.add(new_form)  # adding the form to the database
            db.session.commit()
            flash('Note added!', category='success')
            return redirect(url_for('auth.records'))
    else:
        return redirect(url_for('auth.medicalrecordsform'))
    return render_template('MedicalRecordsForm.html', user=current_user)


#Form Option Page
@auth.route('/forms',  methods=['GET', 'POST'])
def forms():
    flash(request.method)
    return render_template('OptionsForm.html', user=current_user)

#Place where records are stored:
@auth.route('/records',  methods=['GET', 'POST'])
def records():
    bank_item = BankAccountForm.query.order_by(BankAccountForm.last_updated_ts.desc()).first()
    credit_item = CreditCardForm.query.order_by(CreditCardForm.last_updated_ts.desc()).first()
    medical_item = MedicalRecordsForm.query.order_by(MedicalRecordsForm.last_updated_ts.desc()).first()
    return render_template('records.html', user=current_user, bank_item=bank_item, credit_item=credit_item, medical_item=medical_item)
