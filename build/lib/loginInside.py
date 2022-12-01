import time
import pyotp
import schedule
import smtplib
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime

print("Nhap ma Inside: ")
user = input()
pw = getpass.getpass('Pass: ')
print("Nhap link OTP: ")
linkOTP = input()
print("Ok toi bat dau hoat dong")

today = datetime.today()

class Browser:
    browser, service = None, None;

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)
    
    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def get_OTP(s):
        otp_uri = linkOTP
        otp     = pyotp.parse_uri( otp_uri )
        s = str(otp.now())
        return s

    def login_Inside(self, username: str, password: str, otp: str):
        self.add_input(by=By.ID, value='mat-input-3', text=username)
        self.add_input(by=By.ID, value='mat-input-4', text=password)
        self.add_input(by=By.ID, value='mat-input-5', text = otp)
        self.click_button(by=By.CLASS_NAME, value='kt-login__btn-primary')

    def click_In(self):
        self.click_button(by=By.ID, value='imgcheckout')


def job(t):
    if today.weekday() != 6 :
        print ("I'm working...", t)
        browser = Browser('../chromedriver')

        # open Tab
        browser.open_page('https://inside.fptshop.com.vn/')
        time.sleep(3)

        # get OTP
        s = ""
        s = Browser.get_OTP(s)

        # login
        browser.login_Inside(username=user, password=pw,otp= s)
        time.sleep(10)

        #click button in -> out
        browser.click_In()

        time.sleep(10)

        browser.close_browser()

        email = 'botinside001@gmail.com'
        password = 'agwojtoqjdryawqw'
        email_receive = 'phucndah2002@gmail.com'

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(email, password)

        mail_content = ''' Hom nay toi da cham cong cho ban '''
        session.sendmail(email, email_receive, mail_content)
        print('Da cham cong thanh cong')
    else:
        print("Hom nay la chu nhat ban khong can phai cham cong")
        email = 'botinside001@gmail.com'
        password = 'agwojtoqjdryawqw'
        email_receive = 'phucndah2002@gmail.com'

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(email, password)

        mail_content = '''Hom nay la chu nhat ban khong can phai cham cong'''
        session.sendmail(email, email_receive, mail_content)
    return


if __name__ == '__main__':
    schedule.every().day.at("08:15").do(job,'')
    while True:
        schedule.run_pending()
