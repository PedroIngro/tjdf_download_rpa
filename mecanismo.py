from rpa_precatorio import rpa_precatorio as rpa
import config

import time
from datetime import datetime, timedelta
from pyautogui import press, typewrite, hotkey

def rpa_process_function():
    driver = rpa.driver()

    driver.get(config.url)
    driver.maximize_window()

    rpa.wait_element(driver, config.full_body)

    dia_atual = datetime.now()
    dia_anterior = dia_atual + timedelta(days = -1)

    rpa.escrever(dia_anterior.strftime("%d/%m/%Y"), driver, config.de_xpath)
    rpa.escrever(dia_atual.strftime("%d/%m/%Y"), driver, config.ate_xpath)


    rpa.clicar(driver, config.pesquisar_xpath)
    rpa.timeout(driver, config.tabela_xpath)

    # linhas da tabela
    x = 1

    for pag in range(5, 14):
        for arquivos in range(1, 3):
            try:
                linha_arquivo = f"/html/body/div[5]/div/div/div/div[2]/form/div[2]/div/table/tbody/tr[{arquivos}]/td[1]"
                button_tj = rpa.wait_element(driver, linha_arquivo)
                button_tj = rpa.tag_finder(button_tj, "a")
                button_tj.click()
                driver.switch_to.window(driver.window_handles[1])
                print_button = rpa.wait_element(driver, config.link_button)
                print_button = rpa.tag_finder(print_button, "input")
                print_button.click()
                time.sleep(1)
                driver.switch_to.window(driver.window_handles[2])

                hotkey('ctrl', 's')
                time.sleep(1)
                typewrite(f"processo_{x}_{arquivos}.pdf")
                press('enter')
                
                rpa.close_window_and_switcher(driver)
                rpa.wait_element(driver, config.full_body)

            except Exception as e:
                rpa.close_window_and_switcher(driver)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        path_pag = f"/html/body/div[5]/div/div/div/div[2]/form/div[2]/div/table/tfoot/tr/td/div/div[1]/div/table/tbody/tr/td[{pag}]"
        rpa.clicar(driver, path_pag)
        print('aqui estamos')
        x = x + 1
        time.sleep(10)

        

    time.sleep(30)
    rpa.close(driver)
