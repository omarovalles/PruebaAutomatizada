import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv

load_dotenv()

def setup_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_login_exitoso():
    driver = setup_driver()
    driver.get("https://plataformavirtual.itla.edu.do/login/index.php")
    driver.maximize_window()

    driver.find_element(By.ID, "username").send_keys(os.getenv("ITLA_USER"))
    driver.find_element(By.ID, "password").send_keys(os.getenv("ITLA_PASS"))
    driver.find_element(By.ID, "loginbtn").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page-header")) 
    )

    assert "my" in driver.current_url or "dashboard" in driver.current_url

    # Guardamos la captura
    driver.save_screenshot("screenshots/login_exitoso.png")
    driver.quit()
