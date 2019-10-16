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
