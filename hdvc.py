import unittest
import time
from selenium import webdriver
file = open("login.txt","w")
import json
with open("new.json") as f:
    data = json.load(f)

class Meetingsuccessfully(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = "/home/shubham/chromedriver"
        cls.driver = webdriver.Chrome(executable_path=path)
    def test_alogin(self):
        #for login
        self.driver.get("https://hdvc.truringsoftek.co.in/login")
        self.driver.maximize_window()
        self.driver.find_element_by_id("email").send_keys("puneet.singh@truringsoftek.com")
        self.driver.find_element_by_id("password").send_keys("Test@5321")
        self.driver.find_element_by_xpath(data["signin"]).click() #signin
        time.sleep(2)
        self.driver.find_element_by_xpath(data["my meeting"]).click()
        self.driver.find_element_by_xpath(data["my scheduled"]).click()
        self.driver.find_element_by_xpath(data["title"]).send_keys("Test")
        self.driver.find_element_by_xpath(data["description"]).send_keys("explanation")
        self.driver.find_element_by_xpath(data["time"]).send_keys(20)
        self.driver.find_element_by_xpath(data["hour"]).send_keys( 30)
        self.driver.find_element_by_xpath(data["participants"]).send_keys("colours23@gmail.com")
        self.driver.find_element_by_xpath(data["add participants"]).click()
        time.sleep(2)
    def test_btime(self):
        self.driver.find_element_by_xpath(data["recurring_meeting"]).click()
        self.driver.find_element_by_xpath(data["daily"]).click() #daily
        self.driver.find_element_by_xpath(data["date"]).send_keys()
        self.driver.find_element_by_xpath(data["scheduled"]).click()#scheduled
        time.sleep(2)
        lists = self.driver.find_elements_by_xpath(data["meeting successfully scheduled"])
        self.assertEqual(0, len(lists))
        print('login pass')
        file.write("test_alogin = Pass")
    def test_cmonthly(self):
        self.setUpClass()
        self.test_alogin()
        time.sleep(2)
        self.driver.find_element_by_xpath(data["recurring_meeting"]).click()
        self.driver.find_element_by_xpath(data["monthly"]).click()
        self.driver.find_element_by_xpath(data["mday"]).click()
        self.driver.find_element_by_xpath(data["scheduled"]).click()#scheduled
        time.sleep(2)
        lists = self.driver.find_elements_by_xpath(data["meeting successfully scheduled"])
        self.assertEqual(0, len(lists))
        print('monthly pass')
        file.write(" \n test_cmonthly = Pass")
    def test_cweekly(self):
        self.setUpClass()
        self.test_alogin()
        time.sleep(2)

        self.driver.find_element_by_xpath(data["recurring_meeting"]).click()
        self.driver.find_element_by_xpath(data["weekly"]).click()
        self.driver.find_element_by_xpath(data["wday"]).click()
        self.driver.find_element_by_xpath(data["scheduled"]).click()#scheduled
        time.sleep(2)
        lists = self.driver.find_elements_by_xpath(data["meeting successfully scheduled"])
        self.assertEqual(0, len(lists))
        print('weekly pass')
        file.write("\n test_cweekly = Pass")
    def test_dview(self):
        self.setUpClass()
        self.test_alogin()
        time.sleep(2)
        self.driver.find_element_by_xpath(data["speaker"]).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(data["scheduled"]).click()#scheduled
        lists = self.driver.find_elements_by_xpath(data["meeting successfully scheduled"])
        self.assertEqual(0, len(lists))
        print('view pass')
        file.write("\n test_dview = Pass")
    def test_eview(self):
        self.setUpClass()
        self.test_alogin()
        time.sleep(2)
        self.driver.find_element_by_xpath(data["grid"]).click()
        self.driver.find_element_by_xpath(data["scheduled"]).click()#scheduled
        time.sleep(2)
        lists = self.driver.find_elements_by_xpath(data["meeting successfully scheduled"])
        self.assertEqual(0, len(lists))
        print('Grid pass')
        file.write("\n test_eview = Pass")
    def test_fon(self):
        self.test_dview()
        self.driver.find_element_by_xpath(data["audiooff"]).click()#on
        time.sleep(2)
        lists = self.driver.find_elements_by_xpath(data["meeting successfully scheduled"])
        self.assertEqual(0, len(lists))
        print('on pass')
        file.write("\n test_fon = Pass")
    def test_gon(self):
        self.test_dview()
        self.driver.find_element_by_xpath(data["videooff"]).click()#on
        time.sleep(2)
        lists = self.driver.find_elements_by_xpath(data["meeting successfully scheduled"])
        self.assertEqual(0, len(lists))
        print('off pass')
        file.write("\n test_gon = Pass")
    def test_second_Meetingsuccessfully(self):
        print("verify title....")
        lists = self.driver.find_elements_by_xpath(data["meeting successfully scheduled"])
        self.assertEqual(0, len(lists))
        print('pass')
        file.write("\n test_second_Meetingsuccessfully = Pass")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        file.close()
if __name__=='__main__':
    unittest.main()
    
    
    
    
    
    from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from apscheduler.schedulers.blocking import BlockingScheduler

import time


def play_youtube_video():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
    dt_string = dt_string + "  Process Started\n"
    f = open("youtube.log", "a")
    f.write(dt_string)
    CHROMEDRIVER_PATH = '/root/chromedriver'
    WINDOW_SIZE = "1920,1080"
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.binary_location = "/usr/bin/google-chrome"
    # chrome_options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                              options=options
                              )
    time.sleep(10)
    try:
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        presence = EC.presence_of_element_located
        visible = EC.visibility_of_element_located
        i = 0
        while i < 6:
            i += 1
            driver.get("https://www.youtube.com/results?search_query=" + str("Attack on Titan IN 9 MINUTES"))
            print(driver.title)
            time.sleep(3)
            wait.until(visible((By.ID, "video-title")))
            time.sleep(3)
            driver.find_element_by_id("video-title").click()
            time.sleep(574)
            # now = datetime.now()
            # dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
            # dt_string = dt_string + "  Video Played " + str(i) + "\n"
            # f = open("playVideo.log", "a")
            # f.write(dt_string)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
        dt_string = dt_string + "  ~1 Hour Played " + str(i) + "\n"
        f = open("youtube.log", "a")
        f.write(dt_string)
        time.sleep(3)
        driver.close()
        time.sleep(2)
        play_youtube_video()
    except Exception as e:
        print("Error: ", e.args)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
        dt_string = dt_string + "  Error: " + str(e.args) + "\n"
        f = open("youtube.log", "a")
        f.write(dt_string)
        play_youtube_video()
    finally:
        driver.close()
        f.close()

play_youtube_video()













#!/usr/bin/env python3
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from apscheduler.schedulers.blocking import BlockingScheduler

import time


def play_youtube_video():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
    dt_string = dt_string + "  Process Started\n"
    f = open("akamai.log", "a")
    f.write(dt_string)
    CHROMEDRIVER_PATH = '/root/chromedriver'
    WINDOW_SIZE = "1920,1080"
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless")
    options.binary_location = "/usr/bin/google-chrome"
    # chrome_options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--window-size=%s" % WINDOW_SIZE)
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                              options=options
                              )
    time.sleep(10)
    try:
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        presence = EC.presence_of_element_located
        visible = EC.visibility_of_element_located
        i = 0
        while i < 180:
            i += 1
            driver.get("https://www.akamai.com/us/en/akamai-free-trials.jsp")
            print(driver.title)
            time.sleep(3)
            # wait.until(visible((By.ID, "video-title")))
            # time.sleep(3)
            # driver.find_element_by_id("video-title").click()
            time.sleep(17)
            # now = datetime.now()
            # dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
            # dt_string = dt_string + "  Video Played " + str(i) + "\n"
            # f = open("playVideo.log", "a")
            # f.write(dt_string)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
        dt_string = dt_string + "  ~1 Hour Played " + str(i) + "\n"
        f = open("akamai.log", "a")
        f.write(dt_string)
        time.sleep(3)
        driver.close()
        time.sleep(2)
        play_youtube_video()
    except Exception as e:
        print("Error: ", e.args)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y  %H:%M:%S")
        dt_string = dt_string + "  Error: " + str(e.args) + "\n"
        f = open("akamai.log", "a")
        f.write(dt_string)
        play_youtube_video()
    finally:
        driver.close()
        f.close()

play_youtube_video()

