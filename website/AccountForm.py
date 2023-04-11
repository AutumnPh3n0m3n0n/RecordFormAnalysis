from flask import Blueprint, Flask, redirect, url_for, render_template, request
from datetime import datetime

AccountForm = Blueprint('AccountForm', __name__)

@AccountForm.route('/accountform', methods=['GET', 'POST'])

def AccountForm():
    if request.method == 'POST':
        account_number = request.form['account_num']
        owner_first_name = request.form['owner_fname']
        owner_middle_initial = request.form['owner_name']
        owner_last_name = request.form['owner_lname']
        joint_owner_first_name = request.form['joint_owner_fname']
        joint_owner_middle_initial = request.form['joint_owner_mid_initial']
        joint_owner_last_name = request.form['joint_owner_lname']
        party_name = request.form['company_name']
        auth_person = request.form['authorized_person_name']
        other_auth_person = request.form['other_authorized_person_name']
        annual_income = request.form.getlist('annual_income')
        liquid_net_worth = request.form.getlist('liquid_net_worth')
        total_net_worth = request.form.getlist('total_net_worth')
        owner_signature_1 = request.form['owner_signature1']
        date_1 = datetime.datetime.strptime(request.form['get_date_1'], '%m-%d-%Y')
        owner_signature_2 = request.form['owner_signature2']
        date_2 = datetime.datetime.strptime(request.form['get_date_2'], '%m-%d-%Y')

        return render_template("AccountForm.html")