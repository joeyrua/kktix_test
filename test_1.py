import undetected_chromedriver as uc
import selenium.webdriver.support.ui as ui
import time
URL = uc.Chrome("C:\\Users\\Administrator\\chromedriver")
wait = ui.WebDriverWait(URL, 10)
URL.get("https://kktix.com/users/sign_in?back_to=https%3A%2F%2Fkktix.com%2F")  # kktix

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div/div[2]/form/div[1]/div/input"))
account = URL.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div/div[2]/form/div[1]/div/input")
account.send_keys("yellow145258789@gmail.com")
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div/div[2]/form/div[2]/div/input"))
password = URL.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div/div[2]/form/div[2]/div/input")
time.sleep(2)
password.send_keys("juan145258789")
password.send_keys(u'\ue007')

time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div/div[2]/div[2]/section[1]/div/div/div[1]/ul/li[9]"))
search_activity = URL.find_element(
    "xpath", "/html/body/div[3]/div[2]/div/div/div[2]/div[2]/section[1]/div/div/div[1]/ul/li[9]").click()
js = "var q=document.documentElement.scrollTop=100000"
URL.execute_script(js)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[2]/div[2]/div/div[8]/a"))
next = URL.find_element(
    "xpath", "/html/body/div[2]/div[2]/div/div[8]/a").click()
time.sleep(2)
js = "var q=document.documentElement.scrollTop=100000"
URL.execute_script(js)
time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div[4]/div/div/div[5]/div[1]/div[3]/div/div/div/span[3]/button[2]"))
add = URL.find_element(
    "xpath", "/html/body/div[3]/div[4]/div/div/div[5]/div[1]/div[3]/div/div/div/span[3]/button[2]")
for i in range(4):
    add.click()  # 連續按四次
time.sleep(2)
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div[4]/div/div/div[5]/div[3]/label/input"))
check = URL.find_element(
    "xpath", "/html/body/div[3]/div[4]/div/div/div[5]/div[3]/label/input").click()
wait.until(lambda driver: driver.find_element(
    "xpath", "/html/body/div[3]/div[4]/div/div/div[5]/div[4]/button"))
next_2 = URL.find_element(
    "xpath", "/html/body/div[3]/div[4]/div/div/div[5]/div[4]/button").click()
