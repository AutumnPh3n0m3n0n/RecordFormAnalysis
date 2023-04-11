from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime

CreditCardForm = Blueprint('CreditCardForm', __name__)

@CreditCardForm.route('/creditcardform', methods=['GET', 'POST'])

def CreditCardForm():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        account_number = request.form['account_num']
        phone = request.form['phone']
        checking_acc_num = request.form['checking_acc_num']
        checking_aba_num = request.form['checking_aba_num']
        checking_start = request.form['checking_start_month']
        savings_acc_num = request.form['saving_acc_num']
        savings_aba_num = request.form['saving_aba_num']
        savings_start = request.form['saving_start_month']
        payment_amount = request.form('amount')
        signature = request.form('signature')
        payment_date = datetime.datetime.strptime(request.form['get_date'], '%m-%d-%Y')
        auth_type = request.form.getlist('credit_auth')

        return render_template("CreditCardForm.html")

