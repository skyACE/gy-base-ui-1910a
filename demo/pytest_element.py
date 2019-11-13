from time import sleep
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
    slider = driver.find_element_by_xpath("//*[@id='form']/form/div[5]/div/div/div/div[2]/div")
    # 点击拖拽功能的
    actions =ActionChains(driver)
    actions.drag_and_drop_by_offset(slider,0,-200).perform()
    sleep(2)

















