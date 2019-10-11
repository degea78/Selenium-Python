import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("C://Users/Pavel/Desktop/Python/Proiect")	
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class LoginTest(unittest.TestCase):
    baseURL = "http://emag.ro"
    driver = webdriver.Chrome(executable_path = "C:/Users/Pavel/Desktop/Python/Proiect/drivers/chromedriver.exe")

    

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
            
    def test_graphics(self):
        wait = WebDriverWait(self.driver, 10) 
        actions = ActionChains(self.driver)

        mainBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class ='navbar-aux-content__departments']"))).click()                
        self.assertEqual("eMAG.ro - Libertate în fiecare zi", self.driver.title) 

        pcMenuBtn = self.driver.find_element_by_xpath("//a[@class ='js-megamenu-list-department-link gtm_31vgamc'][@href='javascript:void(0)']")        
        componenteBtn = self.driver.find_element_by_xpath("//a[text()='Componente PC']")
        actions.move_to_element(pcMenuBtn).move_to_element(componenteBtn).click().perform()
        
    

        




        time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__== "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\reports'))