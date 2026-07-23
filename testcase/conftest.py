import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.get_filepath import get_screen_shot_path
from selenium.webdriver.chrome.options import Options

# 浏览器配置
options = Options()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# options.add_argument("--headless=new")
options.add_argument("--disable-dev-shm-usage")

# 手动指定本地驱动，彻底禁用SeleniumManager自动联网
service = Service(r'E:\pydemo\seleniumDemo\venv\chromedriver.exe')

driver = None

@pytest.fixture(scope="session")
def driver_project():
    global driver
    driver = webdriver.Chrome(service=service, options=options)
    print("打开浏览器")
    yield driver
    print("关闭浏览器")
    if driver:
        driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    print("=========================")
    out = yield
    report = out.get_result()

    print(f"测试报告：{report}")
    print(f"步骤：{report.when}")
    print(f"nodeid：{report.nodeid}")
    print(f"运行结果：{report.outcome}")

    # 仅用例执行失败时截图
    if report.when == 'call' and report.failed:
        driver.save_screenshot(get_screen_shot_path())
        allure.attach(driver.get_screenshot_as_png(), "用例执行失败截图", allure.attachment_type.PNG)