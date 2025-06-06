import allure
from selenium.webdriver.common.by import By
from base.base import BasePage
from config.assert_utils import assert_compare

"""
后台登录商户余额审核
"""


class UserPage(BasePage):
    # 选择城市
    login_city = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[2]/button/span')
    # 选择全部取消
    click_all = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[6]/div/div[2]/form/div/div/div[2]/label/span[1]/span')
    # 选择自营深圳
    click_sz = (By.XPATH,
                '//*[@id="app"]/div/div[2]/div/div/div[6]/div/div[2]/form/div/div/div[3]/div[1]/div/div/div/label[7]/span[1]/span')
    # 点击确认
    click_confir = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div[6]/div/div[3]/div/button[2]/span')
    # 用户列表-手机号搜索
    phone_serch = (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div[1]/div/div[1]/form/div[2]/div/div/input')

    login_account = (By.ID, "userName")
    login_password = (By.ID, "passWord")
    login_btn = (By.ID, "onsubmit")

    def login(self):
        self.get_url("https://wefine.cdfortis.com/e-hosp-dongying/routing/login.pg")
        self.send_keys(self.login_account, "admin")
        self.send_keys(self.login_password, "123456")
        self.send_keys(self.login_code, 1)
        self.click(self.login_btn)
