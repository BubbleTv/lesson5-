from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/classattr")
    

    time.sleep(1)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary.btn-test"))
    )
    
    # Кликнуть на синюю кнопку
    button.click()
    
    print("Клик по синей кнопке выполнен успешно")
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    time.sleep(1)
    driver.quit()