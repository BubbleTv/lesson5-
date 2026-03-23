from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()

try:

    driver.get("http://the-internet.herokuapp.com/login")
    

    time.sleep(1)
    

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")
    print("Введен username: tomsmith")
    
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    print("Введен password: SuperSecretPassword!")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    print("Кнопка Login нажата")
    
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
    )
    print(f"\nТекст с зеленой плашки:\n{success_message.text}")
    

    time.sleep(2)
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    driver.quit()