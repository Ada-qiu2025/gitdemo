import allure
import pytest
from selenium import webdriver
# 删掉 from selenium.webdriver.chrome.service import Service 不再手动指定驱动
from config.get_filepath import get_screen_shot_path
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

# 浏览器配置
options = Options()
# 指定chrome浏览器路径（保留原有配置）
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# options.add_argument("--headless=new")  #无头模式，没有页面
options.add_argument("--disable-dev-shm-usage")

# 全局driver
driver = None

'''
scope="session" 该 fixture 将在整个测试会话期间被创建一次，并在所有测试完成后销毁。
适合跨多个测试用例共享浏览器实例
'''
@pytest.fixture(scope="session")
def driver_project():
    global driver
    # ✅ 重点：不再传入service，selenium自动下载匹配版本chromedriver
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    # driver.get("https://wefine.cdfortis.com/e-hosp-dongying/routing/login.pg")
    # print(driver.page_source)
    print("打开浏览器")
    yield driver
    print("关闭浏览器")
    # quit() 关闭浏览器+驱动进程，不需要额外close()
    if driver:
        driver.quit()


# 钩子函数，捕获用例执行结果
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """
    :param item: 代表测试函数或方法，包含测试相关的信心，比如名称，位置，标记
    :param call: 包含测试函数执行的详细信息，比如结果，执行时间
    when = setup:前置
    when = call:执行测试用例
    when = teardown:后置
    """
    print("=========================")
    # 获取钩子函数的结果
    out = yield
    # 获取测试报告
    report = out.get_result()

    print(f"测试报告：{report}")
    print(f"步骤：{report.when}")
    print(f"nodeid：{report.nodeid}")
    print(f"运行结果：{report.outcome}")
    # 失败测试用例截图（仅用例执行阶段失败才截图）
    if report.when == 'call' and report.failed:
        # 保存到本地
        driver.save_screenshot(get_screen_shot_path())
        # 截图二进制数据附加到allure报告
        allure.attach(driver.get_screenshot_as_png(), "用例执行失败截图", allure.attachment_type.PNG)