#encoding=utf-8

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# project/
# ├── base/             # 基础封装层（基类）
# │   └── base_page.py  # 封装通用方法（如元素定位、显式等待）
# ├── pages/            # 页面对象层
# │   ├── login_page.py  # 登录页面的元素定位及操作
# │   └── home_page.py   # 主页面的操作封装
# ├── testcases/        # 测试用例层
# │   └── test_login.py  # 调用页面对象编写测试逻辑
# ├── utils/            # 工具类
# │   ├── log_util.py    # 日志管理
# │   └── config_util.py # 配置文件解析
# ├── conftest.py       # Pytest全局Fixture配置（浏览器驱动管理）:ml-citation{ref="5,6" data="citationList"}
# └── allure-results/   # Allure报告生成目录（自动创建）
# pytest.main() 启动
#   → 加载 conftest.py 中的 Fixture（初始化浏览器）
#   → 执行测试用例（调用 selenium 操作）
#   → Allure 收集测试步骤、结果、附件
#   → Fixture 清理浏览器资源
#   → 生成 Allure 原始数据到 report/ 目录
#   → allure generate 生成 HTML 报告

import pytest
import os

if __name__ == '__main__':
    # 1.执行测试用例
    pytest.main()
    os.system("copy environment.properties  .\\report")
    # 2.生成报告
    os.system("allure generate report -o allure-report --clean")
    # 3.打开报告
    os.system("allure open allure-report")

