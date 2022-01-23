from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas
import datetime as dt

CHROME_DRIVER_PATH ="C:\development\chromedriver.exe"

#Gets the Username and Password for login to the Instagram

USERNAME = input('Enter instagram handle: ')
PASSWORD = input('Enter password: ')


class Automated_Message:
    def __init__(self, CHROME_DRIVER_PATH):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(5)

    def login(self, ig_handle, login_password):
        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        username.send_keys(ig_handle)
        password.send_keys(login_password)
        log_in = self.driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
        log_in.click()
        sleep(5)

    def check_birthday(self):
        try:
            now = dt.datetime.today()
            content = pandas.read_csv('birthday.csv')
            today_date = now.day
            today_month = now.month
            birth_date = content['day']

            content_dict = content.to_dict()  # converting to dictionary
            birthdate_day_list = birth_date.to_list()
            birthdate_month_list = content['month'].to_list()

            content_df = content[(content['day'] == today_date) & (content['month'] == today_month)]

            birthday_person = str(content_df.iloc[0]['name'])
            print(birthday_person)
            birthday_acc = str(content_df.iloc[0]['email'])
            print(birthday_acc)
            MESSAGE = 'Happy Birthday'
        except:
            MESSAGE = 'No birthdays today'
            birthday_acc = 'jernic_roy'
        msg = self.driver.find_element_by_css_selector('.xWeGp svg')
        msg.click()
        print('step 1')
        sleep(5)
        not_now = self.driver.find_element_by_css_selector('button.aOOlW.HoLwm ')
        not_now.click()
        sleep(5)
        send = self.driver.find_element_by_css_selector('button.sqdOP.L3NKy.y3zKF')
        send.click()
        print('step 2')
        text = self.driver.find_element_by_name('queryBox')
        text.send_keys(birthday_acc)
        print('step 3')
        sleep(3)
        choose = self.driver.find_element_by_css_selector('button.dCJp8 span')
        choose.click()
        print('step 4')

        next = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div')
        next.click()
        sleep(4)
        message = self.driver.find_element_by_css_selector('textarea')
        message.send_keys(MESSAGE)
        message.send_keys(Keys.ENTER)



#Execution of the Function through Function call one by one

bot = Automated_Message(CHROME_DRIVER_PATH)
bot.login(USERNAME, PASSWORD)
bot.check_birthday()
