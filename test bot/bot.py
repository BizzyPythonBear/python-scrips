from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

activate = True

driver = webdriver.Chrome()
driver.get('https://hackertyper.net/')

#def there_is_a_reason_to_break(i):
    #return not there_is_a_reason_to_break(i)

while (activate):
        actions = ActionChains(driver)
        actions.send_keys("I'm trying to make a bot to see how far I can get in hackertyper")
        actions.perform()
        while (activate):
            ActionChains(driver).move_to_element(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='main']//pre//span[@id='cursor']")))).send_keys("I'm trying to make a bot to see how far I can get in hackertyper").perform()
        #if there_is_a_reason_to_break(i):
            #break;