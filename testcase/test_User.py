import time
import allure
import pytest
from page.user_page import UserPage
from config.assert_utils import assert_compare
# from utils.mysql_util import db
from config.read import read_yaml

@allure.epic("大方法") #标记当前测试类/方法属于某大类
@allure.feature("子模块") #定义子模块
@pytest.mark.run(order=1) #用例顺序
class TestUser:
    @allure.title("用户登录") # 设置当前测试用例标题为"用户登录"
    @pytest.mark.skip("跳过用例")
    @pytest.mark.parametrize('data', read_yaml()['user_login'])
    def test_user_login(self, driver_project, data):
        username, password = str(data['username']), str(data['password'])
        page = UserPage(driver_project)
        page.get_url('https://www.baidu.com/?tn=85070231_12_hao_pg')
        # page.refresh()
        page.send_keys(page.login_account, username)
        page.send_keys(page.login_password, password)
        time.sleep(10)
        page.click(page.login_btn)
        time.sleep(3)
        assert "百度一下，你就知道" in page.get_title()  # 断言登录后标题
