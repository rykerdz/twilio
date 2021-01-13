import twilio.rest
from rando_m import generate
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "your auth token"
client = Client(account_sid, auth_token)
def send_msg(auth_num, phone_num):
    message = client.messages.create(
        to= phone_num, 
        from_="+17328128935",
        body= "Your Authentication number is: "+ auth_num)
def get_num():
    return int(input("Enter The Authentication number we sent to your phone: "))
def check(auth_num):
    ver_code = get_num()
    if int(ver_code) == int(auth_num):
        print("you have completed your registration , you can login now.")
    else:
        answer = input("wrong activation number (0) to renter the the activation number (1) to resend: ")
        if answer == "0":
            check(auth_num)
        elif answer == "1":
            auth_num = generate()
            send_msg(auth_num, phone_num)
            ver_code = get_num()
            check(auth_num)
        else:
            return 0

phone_num = input("Enter your phone number to complete your registration(include +country code):")
auth_num = generate()
send_msg(auth_num, phone_num)
check(auth_num)

