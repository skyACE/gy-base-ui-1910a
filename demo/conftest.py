#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
from time import sleep

import pytest
from selenium import webdriver





@pytest.fixture(scope='session')
def driver():
    # 打开浏览器
    driver = webdriver.Chrome(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../chrome_driver_v78/chromedriver.exe'))
    # 调整浏览器窗口大小
    driver.maximize_window()
    driver.implicitly_wait(10) # 设置等待时长5秒
    # 浏览器全局设置，一般在浏览器启动之后设置一次，终生有效
    yield driver
    driver.quit()