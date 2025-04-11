from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_enlace_recuperar():
    driver = setup_driver()
    driver.get("https://plataformavirtual.itla.edu.do/login/index.php")

    link = driver.find_element(By.LINK_TEXT, "¿Olvidó su nombre de usuario o contraseña?")
    assert link.is_displayed()

    driver.save_screenshot("screenshots/enlace_recuperar.png")
    driver.quit()
