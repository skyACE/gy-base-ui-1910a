from time import sleep

import autoit
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


def test_input(driver):
    driver.get('http://ui.yansl.com/#/input')
    sleep(2)

    input = driver.find_element_by_xpath("//input[@name='t1']")
    # 清空
    input.clear()
    # 输入内容
    input.send_keys("我是谁？我在哪？我该干什么?")
    sleep(2)

def test_radio(driver):
    driver.get('http://ui.yansl.com/#/radio')
    sleep(2)

    radio = driver.find_element_by_xpath("//input[@name='sex'][2]")
    # 点击
    radio.click()
    sleep(2)

def test_checkbox(driver):
    driver.get('http://ui.yansl.com/#/checkbox')
    sleep(1)
    # 点击页面单选元素
    checkbox = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/label[1]/span[1]")
    attribute = checkbox.get_attribute("class")
    #判断单选按钮是否被点击，没被点击点击一下，点击了就不点击
    if not attribute == 'el-checkbox__input is-checked':
        checkbox.click()
        sleep(3)
    #判断单选按钮是否被点击，没被点击点击一下，点击了就不点击
    checkbox = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/label[1]/span[1]")
    attribute = checkbox.get_attribute("class")
    if not attribute == 'el-checkbox__input is-checked':
        checkbox.click()
        sleep(2)



def test_select(driver):
    driver.get('http://ui.yansl.com/#/select')
    sleep(2)
    # 定位下拉框
    select = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div/input")
    # 点击下拉框
    select.click()
    sleep(2)
    #模拟鼠标点击，选中下拉框里的“双皮奶”元素的位置
    option =driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions =ActionChains(driver)
    #组合鼠标和选中按键，actions，move_to_element,执行为perform()
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)



def test_slider(driver):
    driver.get('http://ui.yansl.com/#/slider')
    sleep(2)
    # 定位下拉框
    slider = driver.find_element_by_xpath("(//div[@class='el-tooltip el-slider__button'])[6]")
    # 点击拖拽功能的
    actions =ActionChains(driver)
    actions.drag_and_drop_by_offset(slider,0,-200).perform()
    sleep(2)


def test_time(driver):
    driver.get('http://ui.yansl.com/#/dateTime')
    sleep(2)
    # 定义按键位置
    t1 = driver.find_element_by_xpath("//*[@id='form']/form/div[1]/div[2]/div/div/input")
    # 点击
    t1.clear()
    # 输入内容时间
    t1.send_keys("10:50:20")
    sleep(2)


def test_file(driver):
    driver.get('http://ui.yansl.com/#/upload')
    sleep(2)
    # 定义按键位置
    file = driver.find_element_by_xpath("//input[@type='file']")
    # 点击
    file.clear()
    # 输入文件路径
    file.send_keys("C:\\Users\\guoya\\Desktop\\mall-admin-2019-10-31.log")
    sleep(2)

def test_file1(driver):
    driver.get('http://ui.yansl.com/#/upload')
    sleep(2)
    # 定义按键位置
    file1 = driver.find_element_by_xpath("//*[@id='form']/form/div[2]/div/div/div[1]/button/span")
    file1.click()
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(1)
    # file.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "‪C:\\Users\\guoya\\Desktop\\美女.jpg")
    sleep(2)
    autoit.control_click("打开", "Button1")

    sleep(3)



def test_button(driver):
    driver.get('http://192.168.1.128:8082/xuepl/demo.html')
    sleep(2)

    button = driver.find_element_by_xpath("/html/body/table/tbody/tr[6]/td[2]/input")
    button.click()
    sleep(2)
    alert = driver.switch_to.alert
    alert.send_keys("saasd")
    alert.accept()
    sleep(2)












