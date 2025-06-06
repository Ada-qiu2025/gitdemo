# pages/login_page.py
import time

from base.base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    username_input = (By.ID, "TANGRAM__PSP_11__userName")
    password_input = (By.ID, "TANGRAM__PSP_11__password")
    submit_button = (By.ID, "TANGRAM__PSP_11__submit")
    ddd=(By.ID,"s-top-loginbtn")
    agree=(By.ID,"TANGRAM__PSP_11__isAgree")



    def login(self, username, password):
        self.click(self.ddd)
        time.sleep(1)
        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        time.sleep(2)
        self.click(self.agree)
        time.sleep(1)
        self.click(self.submit_button)  # 操作链封装:ml-citation{ref="4,5" data="citationList"}
