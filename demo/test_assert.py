from time import sleep

#那展示文本做断言
def test_text(driver):
    driver.get("http://ui.yansl.com/#/message")
    # 使用 find_elements_by_xpath 定位元素为列表[]
    buttons = driver.find_elements_by_xpath("//label[contains(text(),'自动关闭提示')]/..//span[1]")
    buttons[0].click()
    message = driver.find_element_by_xpath("//div[@role='alert']/p")
    text = message.text
    print(text)
    # 断言 后面加条件 返回值为 true 和 false
    assert "这是一条消息" in text
    sleep(2)


# 页面元素是否相同，判断页面是否跳转
def test_page_source(driver):
    driver.get("http://ui.yansl.com")
    driver.find_element_by_xpath("//*[@id='app']/section/section/aside/ul/li[3]/div").click()
    driver.find_element_by_xpath("//li[contains(text(),'消息提示')]").click()
    source = driver.page_source
    print(source)
    assert "手工关闭提示" in source
    sleep(2)










