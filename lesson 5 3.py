
driver = webdriver.Firefox()

try:

    driver.get("http://the-internet.herokuapp.com/inputs")
    

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    

    input_field.send_keys("12345")
    print("Введен текст: 12345")
    time.sleep(1)
    input_field.clear()
    print("Поле очищено")
    time.sleep(1)
    
    input_field.send_keys("54321")
    print("Введен текст: 54321")
    time.sleep(1)
    
except Exception as e:
    print(f"Произошла ошибка: {e}")
    
finally:
    driver.quit()