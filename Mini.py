from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
import HtmlTestRunner
import time


class SeleniumTesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/shubh/Desktop/chromedriver_win32/chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_buying_product(self):
        driver = self.driver
        driver.get("http://www.nasindia.co")
        driver.find_element_by_xpath("//a[@class='buttons'][contains(text(),'Cricket')]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//li[14]//div[1]//div[1]").click()
        time.sleep(4)
        driver.find_element_by_xpath(
            "//li[@class='ajax_block_product last_item item clearfix']//div[@class='center_block']//img").click()
        time.sleep(4)
        driver.find_element_by_name("Submit").click()
        time.sleep(4)
        driver.find_element_by_xpath("//img[@class='logo']").click()
        time.sleep(4)

    def test_signup_form_invalid_input(self):
        driver = self.driver
        driver.get("http://www.nasindia.co")
        driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
        driver.find_element_by_xpath("//input[@id='email_create']").send_keys("shubhamgadiwan96@gmail.com")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='SubmitCreate']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//label[contains(text(),'Mr.')]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//input[@id='customer_firstname']").send_keys("Shubh123")
        driver.find_element_by_xpath("//input[@id='customer_lastname']").send_keys("Gadiwan345")
        driver.find_element_by_xpath("//input[@id='passwd']").send_keys("pass?*word37")
        drp1 = Select(driver.find_element_by_xpath("//select[@id='days']"))
        drp1.select_by_index(20)
        time.sleep(2)
        drp2 = Select(driver.find_element_by_xpath("//select[@id='months']"))
        drp2.select_by_index(12)
        time.sleep(2)
        drp3 = Select(driver.find_element_by_xpath("//select[@id='years']"))
        drp3.select_by_value('19a5')
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id='submitAccount']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//img[@class='logo']").click()
        time.sleep(5)

    def test_signup_form(self):
        driver = self.driver
        driver.get("http://www.nasindia.co")
        driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
        driver.find_element_by_xpath("//input[@id='email_create']").send_keys("shubhamgadiwan96@gmail.com")
        time.sleep(4)
        driver.find_element_by_xpath("//input[@id='SubmitCreate']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//label[contains(text(),'Mr.')]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//input[@id='customer_firstname']").send_keys("Shubham")
        driver.find_element_by_xpath("//input[@id='customer_lastname']").send_keys("Gadiwan")
        driver.find_element_by_xpath("//input[@id='passwd']").send_keys("pass_word37")
        drp1 = Select(driver.find_element_by_xpath("//select[@id='days']"))
        drp1.select_by_index(20)
        time.sleep(2)
        drp2 = Select(driver.find_element_by_xpath("//select[@id='months']"))
        drp2.select_by_index(12)
        time.sleep(2)
        drp3 = Select(driver.find_element_by_xpath("//select[@id='years']"))
        drp3.select_by_value('1995')
        time.sleep(2)
        driver.find_element_by_xpath("//img[@class='logo']").click()
        time.sleep(5)

    def test_mail_right_input(self):
        driver = self.driver
        driver.get("http://www.nasindia.co")
        driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
        driver.find_element_by_xpath("//input[@id='email_create']").send_keys("shubhamgadiwan96@gmail.com")
        time.sleep(2)
        driver.find_element_by_xpath("//img[@class='logo']").click()
        time.sleep(5)

    def test_mail_wrong_input(self):
        driver = self.driver
        driver.get("http://www.nasindia.co")
        driver.find_element_by_xpath("//a[contains(text(),'Login')]").click()
        driver.find_element_by_xpath("//input[@id='email_create']").send_keys("shubhamgadiwan96gmail.com")
        driver.find_element_by_xpath("//input[@id='SubmitCreate']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//img[@class='logo']").click()
        time.sleep(5)

    def test_scroll_down_button(self):
        driver = self.driver
        driver.get("http://www.nasindia.co")
        driver.find_element_by_xpath("//body/div[@id='page']/div[@id='columns']/div[@id='left_column']/div["
                                     "@id='categories_block_left']/div[1]/ul[1]/li[1]/span[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//body/div[@id='page']/div[@id='columns']/div[@id='left_column']/div["
                                     "@id='categories_block_left']/div[1]/ul[1]/li[1]/ul[1]/li[1]/a[1]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//input[@id='as4c_12_170']").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
        print("Test Completed")
