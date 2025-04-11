from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_login_fallido():
    driver = setup_driver()
    try:
        driver.get("https://plataformavirtual.itla.edu.do/login/index.php")
        driver.maximize_window()

        driver.find_element(By.ID, "username").send_keys("usuariofalso")
        driver.find_element(By.ID, "password").send_keys("contrasenafalsa")
        driver.find_element(By.ID, "loginbtn").click()

        error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )

        print("Texto del error:", error.text.strip())

        assert "Acceso inválido" in error.text

        driver.save_screenshot("screenshots/login_fallido.png")
    
    finally:
        driver.quit()
