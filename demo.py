from selenium import webdriver


def test():
    driver = None
    try:
        driver = webdriver.Remote(command_executor='http://192.168.3.48:4444/wd/hub',
                                  desired_capabilities={'browserName': 'chrome'})

        driver.get('https://www.baidu.com')
        driver.implicitly_wait(15)
        driver.get_screenshot_as_file("./baidu_img.png")
        print("OK")
    finally:
        if driver is not None:
            driver.quit()


def test1():
    driver = None
    try:
        driver = webdriver.Remote(command_executor='http://192.168.3.48:4444/wd/hub',
                                  desired_capabilities={'browserName': 'chrome'})

        driver.get('https://www.baidu.com')
        driver.implicitly_wait(15)
        driver.get_screenshot_as_file("./baidu1_img.png")
        print("OK")
    finally:
        if driver is not None:
            driver.quit()


if __name__ == '__main__':
    pass