from twilio.rest import Client

from decouple import config

import random

import string

def sending_sms(phone_num,otp) :

    
    account_sid = config('account_sid')

    auth_token = config('auth_token')

    client = Client(account_sid, auth_token)

    message = client.messages.create(

        from_='+12314686462',
        to=f'{phone_num}',
        body= f'Your OTP for Verification : {otp}'
)

def get_otp():

    otp = ''.join(random.choices(string.digits,k=4))

    return otp 