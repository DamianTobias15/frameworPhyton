# tests/test_module.py
from selenium import webdriver

def test_example():
    print("Iniciando la prueba...")
    driver = webdriver.Chrome()
    print("Abriendo el navegador...")
    driver.get("https://www.example.com")
    print("Navegando a www.example.com...")
    assert "Example" in driver.title
    print("Título verificado exitosamente.")
    driver.quit()
    print("Cerrando el navegador...")