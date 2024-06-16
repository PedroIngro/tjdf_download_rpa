from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class rpa_precatorio:
    def driver():
        return webdriver.Chrome()

    def clicar(driver, xpath):
        elemento = driver.find_element("xpath", xpath)
        elemento.click()

    def escrever(texto, driver, xpath):
        elemento = driver.find_element("xpath", xpath)
        elemento.send_keys(texto)
    
    def wait_element(driver, xpath):
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    
    def tag_finder(element, tag):
        return element.find_element(By.TAG_NAME, tag)
    
    def element_process(driver, xpath, tag_name):
            elemento = rpa_precatorio.esperar_elemento(driver, xpath)
            return rpa_precatorio.tag_finder(elemento, tag_name)

    def close_window_and_switcher(driver):
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


    def close(driver):
        driver.quit()

    def timeout(driver, xpath):
        exist = 0
        while exist < 60:
            teste = driver.find_element("xpath", xpath)
            print(teste)
            if teste is not None:
                exist = 100
            else:
                time.sleep(1)
    