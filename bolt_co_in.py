import os

import xmlrunner as xmlrunner
from selenium import webdriver
import unittest, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import HtmlTestRunner
fromaddr = "mohit********"
toaddr = "msmohit*******"


def index(var):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Subject of the Mail"
    body = "Failed test "+var+" report"
    msg.attach(MIMEText(body, 'plain'))
    filename = "image1.png"
    attachment = open("image1.png", "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "Password")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome(executable_path="D:/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver.get("URL*****")
        self.driver.maximize_window()

    def test_search0_home_botton(self):
        try:
            self.driver.find_element(By.ID,"mat-input-0").send_keys("Website Username")
            self.driver.find_element(By.ID,"mat-input-1").send_keys("Website Password")
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']").click()
            time.sleep(5)

            print("login_success :-", self.driver.current_url)
        except:
            print("Login Failed Check Cridentials:-", self.driver.current_url)
            var = "Login Failed Check Cridentials"+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-drawer-inner-container ng-tns-c35-2']//mat-nav-list//a[1]").click()
            time.sleep(5)
            print("success Home button:-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Loading Home failed :-", self.driver.current_url)
            var = "Loading Home failed"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-drawer-inner-container ng-tns-c35-2']//mat-nav-list//a[1]").click()
            time.sleep(5)
            print("success Home button:-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Loading Home failed :-", self.driver.current_url)
            var = "Loading Home failed"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)


    def test_search1_dashboard_button(self):
        try:
            self.driver.find_element(By.ID, "mat-input-0").send_keys("******")
            self.driver.find_element(By.ID, "mat-input-1").send_keys("*******")
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']").click()
            time.sleep(5)
            print("login_success :-", self.driver.current_url)
        except:
            print("Login Failed Check Cridentials :-", self.driver.current_url)
            var = "Login Failed Check Cridentials"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-drawer-inner-container ng-tns-c35-2']//mat-nav-list//a[2]").click()
            print("success Dashboard :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("failed to load Dashboard :-", self.driver.current_url)
            var = " load Dashboard"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-tab-link-container']//div//div//a[2]").click()
            print("success Dashboard(Criticality) button:-", self.driver.current_url)
            time.sleep(3)
        except:
            print("failed to load Dashboard(Criticality) :-", self.driver.current_url)
            var = " load Dashboard(Criticality)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-link-container']//div//div//a[3]").click()
            print("success Dashboard(Compare Board) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("failed to load Dashboard(Compare Board) :-", self.driver.current_url)
            var = " load Dashboard(Compare Board)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)


    def test_search3_reports_button(self):
        try:
            self.driver.find_element(By.ID, "mat-input-0").send_keys("*******")
            self.driver.find_element(By.ID, "mat-input-1").send_keys("*******")
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']").click()
            time.sleep(5)
            print("login_success :-", self.driver.current_url)
        except:
            print("Login Failed Check Cridentials :-", self.driver.current_url)
            var = "Login Failed Check Cridentials"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-drawer-inner-container ng-tns-c35-2']//mat-nav-list//a[3]").click()
            print("success Reports :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Reports :-", self.driver.current_url)
            var = " load Reports"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[1]//figure//mat-card").click()
            print("success Reports(summary) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Reports(Summary) :-", self.driver.current_url)
            var = " load Reports(Summary)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            print("success back load  from Reports(Summary) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to back load from Reports(Summary) :-", self.driver.current_url)
            var = " back load from Reports(Summary)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[2]//figure//mat-card").click()
            print("success Reports(Events):-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Reports(Events) :-", self.driver.current_url)
            var = " load Reports(Events)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            print("success back load  from Reports(Events):-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to back load from Reports(Events) :-", self.driver.current_url)
            var = " back load from Reports(Events)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[3]//figure//mat-card").click()
            print("success Reports(Positions) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Reports(Positions) :-", self.driver.current_url)
            var = " load Reports(Positions)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            print("success back load  from Reports(Positions):-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to back load from Reports(positions) :-", self.driver.current_url)
            var = " back load from Reports(Positions)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        # try:
        #     self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[4]//figure//mat-card").click()
        #     print("success Reports(Testing):-", self.driver.current_url)
        #     time.sleep(3)
        # except:
        #     print("Failed to load Reports(Testing) :-", self.driver.current_url)
        #     var = " load Reports(Testing)"+" "+ self.driver.current_url
        #     self.driver.save_screenshot("image1.png")
        #     time.sleep(3)
        #     index(var)
        #
        # try:
        #     self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
        #     print("success back load  from Reports(Testing):-", self.driver.current_url)
        #     time.sleep(3)
        # except:
        #     print("Failed to back load from Reports(Testing) :-", self.driver.current_url)
        #     var = " back load from Reports(Testing)"+" "+ self.driver.current_url
        #     self.driver.save_screenshot("image1.png")
        #     time.sleep(3)
        #     index(var)


        # try:
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[5]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[6]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[7]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[8]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[9]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[10]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[11]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[12]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[13]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[14]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[15]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[16]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[17]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[18]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[19]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[20]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[21]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[22]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[23]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[24]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[25]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[26]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[27]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[28]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[29]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[30]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[31]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[32]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[33]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[34]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[35]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[36]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[37]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[38]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator primary_color mat-raised-button mat-button-base ng-star-inserted']").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)
            # self.driver.find_element(By.XPATH,"//mat-grid-list[@class='mat-grid-list']//div//mat-grid-tile[39]//figure//mat-card").click()
            # print("success on url:-", self.driver.current_url)
            # time.sleep(3)

        # except:
        #     print("Failed:-", self.driver.current_url)
        #     var = self.driver.current_url
        #     self.driver.save_screenshot("image1.png")
        #     index(var)
        #     time.sleep(10)

    def test_search4_streaming_button(self):
        try:
            self.driver.find_element(By.ID, "mat-input-0").send_keys("*******")
            self.driver.find_element(By.ID, "mat-input-1").send_keys("*******")
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']").click()
            time.sleep(5)
            print("login_success :-", self.driver.current_url)
        except:
            print("Login Failed Check Cridentials :-", self.driver.current_url)
            var = "Login Failed Check Cridentials"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-drawer-inner-container ng-tns-c35-2']//mat-nav-list//a[4]").click()
            print("success Steaming:-", self.driver.current_url)
            time.sleep(3)

        except:
            print("Failed to load Streaming :-", self.driver.current_url)
            var = " load Streaming"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)



    def test_search5_setting_button(self):
        try:
            self.driver.find_element(By.ID, "mat-input-0").send_keys("*******")
            self.driver.find_element(By.ID, "mat-input-1").send_keys("*******")
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']").click()
            time.sleep(5)
            print("login_success :-", self.driver.current_url)
        except:
            print("Login Failed Check Cridentials :-", self.driver.current_url)
            var = "Login Failed Check Cridentials"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-drawer-inner-container ng-tns-c35-2']//mat-nav-list//div//a[1]").click()
            print("success Setting:-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Setting :-", self.driver.current_url)
            var = " load Setting"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[1]").click()
            print("success Setting(Update Profile) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Setting(Update Profile) :-", self.driver.current_url)
            var = " load Setting(Update Profile)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[2]").click()
            print("success Setting(Device Documents) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Setting(Device Documents) :-", self.driver.current_url)
            var = " load Setting(Device Documents)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[3]").click()
            print("success Setting(Notification Types & Devices):-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Setting(Notification Types & Devices) :-", self.driver.current_url)
            var = " load Setting(Notification Types & Devices)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)
        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[4]").click()
            print("success Setting(Notification Receivers) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load (Notification Receivers) :-", self.driver.current_url)
            var = " load (Notification Receivers)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[5]").click()
            print("success Setting(Push Api) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load (Push Api) :-", self.driver.current_url)
            var = " load (Push Api)" + " " + self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)


    def test_search6_admin_button(self):
        try:
            self.driver.find_element(By.ID, "mat-input-0").send_keys("*******")
            self.driver.find_element(By.ID, "mat-input-1").send_keys("*******")
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']").click()
            time.sleep(5)
            print("login_success :-", self.driver.current_url)
        except:
            print("Login Failed Check Cridentials :-", self.driver.current_url)
            var = "Login Failed Check Cridentials"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-drawer-inner-container ng-tns-c35-2']//mat-nav-list//div//a[2]").click()
            print("success Admin:-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Admin :-", self.driver.current_url)
            var = " load Admin"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-tab-list']//div//a[1]").click()
            print("success Admin(Manager Users & Device):-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Admin(Manager Users & Device) :-", self.driver.current_url)
            var = " load Admin(Manager Users & Device)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[2]").click()
            print("success Admin(Stock Manage) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Admin(Stock Manage) :-", self.driver.current_url)
            var = " load Admin(Stock Manage)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[3]").click()
            print("success Admin(Sim Manage) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Admin(Sim Manage) :-", self.driver.current_url)
            var = " load Admin(Sim Manage)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[4]").click()
            print("success Admin(Activation Codes) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Admin(Activation Codes) :-", self.driver.current_url)
            var = " load Admin(Activation Codes)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH, "//div[@class='mat-tab-list']//div//a[5]").click()
            print("success Admin(Company Admin) :-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Failed to load Admin(Company Admin) :-", self.driver.current_url)
            var = " load Admin(Company Admin)"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)


    def test_search7_logout(self):
        try:
            self.driver.find_element(By.ID, "mat-input-0").send_keys("*******")
            self.driver.find_element(By.ID, "mat-input-1").send_keys("*******")
            self.driver.find_element(By.XPATH,"//button[@class='mat-focus-indicator mat-raised-button mat-button-base mat-primary']").click()
            time.sleep(5)
            print("login_success :-", self.driver.current_url)
        except:
            print("Login Failed Check Cridentials :-", self.driver.current_url)
            var = "Login Failed Check Cridentials"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)

        try:
            self.driver.find_element(By.XPATH,"//div[@class='mat-drawer-inner-container ng-tns-c35-2']//mat-nav-list//div//a[3]").click()
            print("logout_success:-", self.driver.current_url)
            time.sleep(3)
        except:
            print("Logout Failed :-",self.driver.current_url)
            var = "Logout Failed"+" "+ self.driver.current_url
            self.driver.save_screenshot("image1.png")
            time.sleep(3)
            index(var)



    def tearDown(self):
        self.driver.close()


if __name__=='__main__':
    unittest.main()
