from time import sleep

import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    #定义启动项 “webdriver ”和启动路径（..）
    driver = webdriver.Chrome('../chrome_driver_v78/chromedriver.exe')
    #窗口最大化
    driver.maximize_window()
    driver.implicitly_wait(5)  #  隐视等待设置等待时间长5秒

    #追加执行
    yield driver
    #退出driver
    driver.quit()

    #
    # #打开网址
    # driver.get("http://www.baidu.com")
    # sleep(1)
    # driver.get("https://www.runoob.com/")
    # sleep(1)
    # # 后退
    #
    # driver.back()
    # sleep(1)
    #
    # # 前进
    # driver.forward()
    # sleep(1)
    #
    # # 刷新
    # driver.refresh()
    # sleep(1)

