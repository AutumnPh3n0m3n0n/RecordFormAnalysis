from flask import Blueprint, Flask, redirect, url_for, render_template, request, PyPDF2
from datetime import datetime

MedicalRecordsForm = Blueprint('MedicalRecordsForm', __name__)

@MedicalRecordsForm.route('/medicalrecordform', methods=['GET', 'POST'])

def MedicalRecordsForm():
    if request.method == 'POST':
        first_name = request.form['fname']
        middle_initial = request.form['mid_initial']
        last_name = request.form['lname']
        email = request.form['email']
        phone = request.form['phone']
        mailing_address = request.form['mail_address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip_code']
        phone_number = request.form['phone_number']
        birthday = datetime.datetime.strptime(request.form['birthday'], '%m-%d-%Y')
        last_appointment = datetime.datetime.strptime(request.form['last_appt'], '%m-%d-%Y')
        location = request.form.getlist('Question2')
        record_format = request.form.getlist('Question4')
        information = request.form.getlist('Question6')
        other_party = request.form['end_name']
        relationship = request.form['end_relationship']
        other_address = request.form['end_address']
        other_city = request.form['end_city']
        other_state = request.form['end_state']
        other_zip = request.form['end_zip']
        other_fax = request.form['end_fax']
        other_phone = request.form['end_phone']
        other_email = request.form['end_email']
        signature_1 = request.form['signature_1']
        sign_date_1 = datetime.datetime.strptime(request.form['current_date_1'], '%m-%d-%Y')
        signature_2 = request.form['signature_2']
        sign_date_2 = datetime.datetime.strptime(request.form['current_date_2'], '%m-%d-%Y')

        return render_template("MedicalRecordsForm.html")
