from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os

os.makedirs("screenshots", exist_ok=True)


def setup_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_campos_visibles():
    driver = setup_driver()
    driver.get("https://plataformavirtual.itla.edu.do/login/index.php")

    assert driver.find_element(By.ID, "username").is_displayed()
    assert driver.find_element(By.ID, "password").is_displayed()
    assert driver.find_element(By.ID, "loginbtn").is_displayed()

    driver.save_screenshot("screenshots/campos_visibles.png")
    driver.quit()
