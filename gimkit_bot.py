from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from credentials import USER, GIMKITPASS

PATH = "/Users/misterrobot/Documents/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH)

driver.get("https://gimkit.com/login")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Email address...']"))).send_keys(USER + Keys.ENTER)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Password']"))).send_keys(GIMKITPASS + Keys.ENTER)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-bcXHqe gDMAfV']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[2]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='sc-jNJNQp heYHTs'])[2]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-ipEyDJ esZnCW flex-center']"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@role='spinbutton']"))).send_keys(Keys.BACKSPACE + Keys.BACKSPACE)
driver.find_element(By.XPATH, "//input[@role='spinbutton']").send_keys("15")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-ipEyDJ esZnCW flex-center']"))).click()
time.sleep(.5)
driver.close()
driver.switch_to.window(driver.window_handles[0])
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='sc-iDJXoU erEfXI']")))
CODE = driver.find_element(By.XPATH, "//div[@class='sc-iDJXoU erEfXI']").text
print(CODE)

driver.switch_to.new_window("tab")
driver.get("https://gimkit.com/join")

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Game Code']"))).send_keys(CODE + Keys.ENTER)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Your Name']"))).send_keys("nico" + Keys.ENTER)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-pushable']")))

driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)
driver.find_elements(By.XPATH, "//button[@class='btn-pushable']")[4].click()

# driver.switch_to.window(driver.window_handles[1])


WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button']")))

ActionChains(driver)\
    .key_down(Keys.ESCAPE)\
    .key_up(Keys.ESCAPE)\
    .perform()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn-pushable'])[5]"))).click()

for x in range(0, 500):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@style='height: 100%; width: 100%; display: flex; justify-content: center; align-items: center; padding: 7px 6%; box-sizing: border-box; font-weight: 900; font-size: 25px;']")))
    A = driver.find_elements(By.XPATH, "//span[@class='notranslate lang-en']")[1].text
    B = driver.find_elements(By.XPATH, "//span[@class='notranslate lang-en']")[2].text
    C = driver.find_elements(By.XPATH, "//span[@class='notranslate lang-en']")[3].text
    D = driver.find_elements(By.XPATH, "//span[@class='notranslate lang-en']")[4].text
    if A in ["a", "b", "c", "d"]:
        ActionChains(driver) \
            .key_down("1") \
            .key_up("1") \
            .perform()
    elif B in ["a", "b", "c", "d"]:
        ActionChains(driver) \
            .key_down("2") \
            .key_up("2") \
            .perform()
    elif C in ["a", "b", "c", "d"]:
        ActionChains(driver) \
            .key_down("3") \
            .key_up("3") \
            .perform()
    else:
        ActionChains(driver) \
            .key_down("4") \
            .key_up("4") \
            .perform()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@style='height: 100%; width: 100%; display: flex; justify-content: center; align-items: center; padding: 15px 6%; box-sizing: border-box; font-weight: 900; font-size: 40px;']")))
    ActionChains(driver) \
        .key_down(Keys.ENTER) \
        .key_up(Keys.ENTER) \
        .perform()
    print(x)
    time.sleep(.35)
print("The Deed Is Done")
driver.quit()
