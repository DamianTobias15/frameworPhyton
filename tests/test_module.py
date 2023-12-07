# tests/test_module.py
import unittest
from selenium import webdriver

class TestExample(unittest.TestCase):
    def setUp(self):
        print("Iniciando la prueba...")
        self.driver = webdriver.Chrome()
        print("Abriendo el navegador...")

    def test_example(self):
        self.driver.get("https://www.example.com")
        print("Navegando a www.example.com...")
        self.assertIn("Example", self.driver.title, "El título no contiene 'Example'")
        print("Título verificado exitosamente.")

    def tearDown(self):
        self.driver.quit()
        print("Cerrando el navegador...")

if __name__ == "__main__":
    unittest.main()
