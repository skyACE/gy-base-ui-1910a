from time import sleep

from selenium import webdriver

# 打开浏览器
def test_browser(driver):
    driver = webdriver.Chrome('../chrome_driver_v78/chromedriver.exe')

    sleep(1)
    driver.maximize_window()
    sleep(1)

    #打开网址
    driver.get("http://www.baidu.com")
    sleep(1)
    driver.get("https://www.runoob.com/")
    sleep(1)
    # 后退

    driver.back()
    sleep(1)

    # 前进
    driver.forward()
    sleep(1)

    # 刷新
    driver.refresh()
    sleep(1)



    # 关闭浏览器,而不退出driver
    #driver.close()

    # 关闭浏览器,并退出driver
    driver.quit()







