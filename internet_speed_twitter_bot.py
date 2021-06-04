from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "Your Driver Path"
twitter_username = "Your Twitter Username or Email"
twitter_pwd = "Your Twitter Password"

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.promised_upload = 10
        self.promised_download = 200

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        run_test = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()

        # Delay for 50 seconds
        sleep(50)
        self.actual_download = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]').text
        self.actual_upload = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]').text
        print(f"Download: {self.actual_download}")
        print(f"Upload: {self.actual_upload}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        msg = f"Testing: Hey Internet Provider, why is my internet speed {self.actual_download}down/{self.actual_upload}up when I pay for {self.promised_download}down/{self.promised_upload}up?"
        print(msg)

        sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys(twitter_username)

        pwd = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pwd.send_keys(twitter_pwd)
        login = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()

        sleep(2)
        tweet_msg = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_msg.send_keys(msg)

        send_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        sleep(2)
        send_tweet.click()