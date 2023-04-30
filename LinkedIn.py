import time
from selenium import webdriver
driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3348298644&distance=25&f_AL=true&geoId=115884833&keywords=Python%20Flask&refresh=true")
# job = driver.find_element("xpath", '//*[@id="ember629"]')
time.sleep(3)
login = driver.find_element("link text", "Sign in")
login.click()
username = driver.find_element("id", "username")
username.send_keys("pushpenderrajputsp@gmail.com")
username.submit()
password = driver.find_element("id", "password")
password.send_keys("Pushpender@21")
password.submit()
apply = driver.find_element("xpath", '//*[@id="ember313"]/span')
time.sleep(3)
apply.click()
nexxt = driver.find_element("xpath", '//*[@id="ember345"]')
nexxt.click()
new_next = driver.find_element(
    "xpath", '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span')
new_next.click()
skipexp = driver.find_element(
    "xpath", '//html/body/div[3]/div/div/div[2]/div/div[2]/form/div[1]/div/div[2]/button[1]/span')
skipexp.click()
nownext = driver.find_element(
    "xpath", '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span')
nownext.click()
review = driver.find_element(
    "xpath", '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span')
review.click()
submitapplication = driver.find_element(
    "xpath", '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]/span')
submitapplication.click()
time.sleep(10)
driver.quit()
