
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
URL = "https://www.wildberries.ru/catalog/169234407/detail.aspx"

try:
    driver.get(URL)
    wait = WebDriverWait(driver, 20)
    
    button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Все характеристики и описание')]")))
    sleep(5)
    button.click()
    
    popup = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'popup__content')))
    
    result_dict = {}
    operating_system_key = popup.find_element(By.XPATH, "//span[contains(text(), 'Серия ноутбуков')]").text.strip()
    operating_system_value = popup.find_element(By.XPATH, "//span[contains(text(), 'Серия ноутбуков')]/following::td[1]/span").text.strip()
    
    result_dict['Операционная система Windows'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Операционная система')]/following::td[1]/span").text.strip()
    result_dict['Диагональ экрана'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Диагональ экрана')]/following::td[1]/span").text.strip()
    result_dict['Тип матрицы'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Тип матрицы')]/following::td[1]/span").text.strip()
    result_dict['Разрешение экрана'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Разрешение экрана')]/following::td[1]/span").text.strip()
    result_dict['Тип оперативной памяти'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Тип оперативной памяти')]/following::td[1]/span").text.strip()
    result_dict['Объем оперативной памяти (Гб)'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Объем оперативной памяти')]/following::td[1]/span").text.strip()
    result_dict['Ёмкость аккумулятора'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Емкость аккумулятора')]/following::td[1]/span").text.strip()
    result_dict['Линейка процессоров'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Линейка процессоров')]/following::td[1]/span").text.strip()
    result_dict['Процессор'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Процессор')]/following::td[1]/span").text.strip()
    result_dict['Количество ядер процессора'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Количество ядер процессора')]/following::td[1]/span").text.strip()
    result_dict['Тактовая частота процессора'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Тактовая частота процессора')]/following::td[1]/span").text.strip()    
    result_dict['Разъем HDMI'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Разъем HDMI')]/following::td[1]/span").text.strip()
    result_dict['Разъем для наушников/микрофона'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Разъем для науш')]/following::td[1]/span").text.strip()
    result_dict['Разъем карт памяти'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Разъем карт памяти')]/following::td[1]/span").text.strip()
    result_dict['Тип накопителя'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Тип накопителя')]/following::td[1]/span").text.strip()
    result_dict['Объем накопителя'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Объем накопителя')]/following::td[1]/span").text.strip()
    result_dict['Количество динамиков'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Количество динамиков')]/following::td[1]/span").text.strip()
    result_dict['Материал корпуса'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Материал корпуса')]/following::td[1]/span").text.strip()
    result_dict['Комплектация'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Комплектация')]/following::td[1]/span").text.strip()
    result_dict['Страна производства'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Страна производства')]/following::td[1]/span").text.strip()
    result_dict['Вес без упаковки (кг)'] = popup.find_element(By.XPATH, "//span[contains(text(), 'Вес без упаковки')]/following::td[1]/span").text.strip()
    
    thickness = popup.find_element(By.XPATH, "//span[contains(text(), 'Толщина')]/following::td[1]/span").text.strip()
    depth = popup.find_element(By.XPATH, "//span[contains(text(), 'Глубина')]/following::td[1]/span").text.strip()
    width = popup.find_element(By.XPATH, "//span[contains(text(), 'Ширина')]/following::td[1]/span").text.strip()
    result_dict['Габариты ноутбука (Т*Г*Ш)'] = f'{thickness} x {depth} x {width}'

    print(json.dumps(result_dict))
    
    with open ('Wildberries_Selenium.json', 'w', encoding='utf-8') as f:
        json.dump(result_dict, f)
    
    
except Exception as ex:
  print("Произошла ошибка:", ex)
  driver.quit()

finally:
  driver.quit()
