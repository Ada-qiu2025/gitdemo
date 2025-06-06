import allure
import pytest
from page.loginPage import LoginPage as loginPage

@allure.feature("用户登录模块")
class TestLogin:
    @allure.story("验证成功登录")
    def test_valid_login(self,driver_project):
        login_page = loginPage(driver_project)
        login_page.driver.get("https://www.baidu.com/?tn=85070231_12_hao_pg")  # 替换为实际登录页URL
        login_page.login("18382411899", "baidumima")
        assert "百度一下，你就知道" in login_page.get_title()  # 断言登录后标题

    # @allure.story("验证错误密码登录")
    # def test_invalid_password(self,driver_project):
    #     login_page = loginPage(driver_project)
    #     login_page.driver.get("https://wefine.cdfortis.com/e-hosp-dongying/routing/login.pg")
    #     login_page.login("admin", "wrong_password")
    #     assert "无效的用户名或密码" in login_page.get_error_message()
