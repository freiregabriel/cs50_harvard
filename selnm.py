from selenium import webdriver
browser = webdriver.Chrome('C:/chromedriver.exe')
browser.fullscreen_window()
browser.get("http://www.gabrielfreire.com.br")
browser.implicitly_wait(2)
element = browser.find_element_by_css_selector('#app > div.application--wrap > nav > div > div:nth-child(3) > a:nth-child(4)')
if element:
    element.click()
    print("clicked!")

# element.send_keys("type")
# element.submit()