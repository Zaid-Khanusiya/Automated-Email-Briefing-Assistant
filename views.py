from flask_restful import Resource
from utils import *
import time

MAIN_API_SLEEP_TIME = 5 # this time is in seconds

class Home(Resource):
    def get(self):
        return {'msg':'This is home page!'}

class MainAPI(Resource):
    def get(self):
        while True:
            print("IN WHILE")
            try:
                new_mail_list = read_new_mails()
                print("New messages:",len(new_mail_list))
                if len(new_mail_list) > 0:
                    summary_of_emails = summarise_email_list(emails_list=new_mail_list)
                    slack_status = forward_to_slack_channel(content=summary_of_emails)
                    if slack_status == True:
                        print('Message sent to slack successfully!')
                    else:
                        print('An error occurred while sending message to slack!')
            except Exception as e:
                print('---------------\n',e)
            time.sleep(MAIN_API_SLEEP_TIME)
        return True