from selenium import webdriver
browser = webdriver.Chrome()
url = "www.baidu.com"
browser.get(url)
input = browser.find_element_by_css_selector("#kw")
input.clear()
input.send_keys("机器学习")
