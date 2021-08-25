from selenium import webdriver

chrome_driver_path = "/home/jasminele/Downloads/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element_by_name('fName')
first_name.send_keys('Thu')
last_name = driver.find_element_by_name('lName')
last_name.send_keys('Le')
email = driver.find_element_by_name('email')
email.send_keys('leanhthunk@gmail.com')

submit = driver.find_element_by_css_selector('form button')
submit.click()
