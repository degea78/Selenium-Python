import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("C://Users/Pavel/Desktop/Python/Proiect/Selenium-Python")	
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class LoginTest(unittest.TestCase):
    baseURL = "https://www.pcgarage.ro/"
    driver = webdriver.Chrome(executable_path = "C:/Users/Pavel/Desktop/Python/Proiect/Selenium-Python/drivers/chromedriver.exe")

    

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
            
    def test_graphics(self):
        wait = WebDriverWait(self.driver, 10) 
        actions = ActionChains(self.driver)        
                       
        self.assertEqual("PC Garage | Notebook, calculatoare, sisteme, periferice si componente PC", self.driver.title) 
        mainBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cat-nav-tab'][text()='Componente']"))).click() 

        procesoare = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.pcgarage.ro/procesoare/']"))).click()
        procHeader = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Procesoare']"))).text
        self.assertTrue(procHeader == "Procesoare")        
        procSel = self.driver.find_element_by_xpath("//p[text()='Producator']//following-sibling::p[@class='lc-filter-char']//span[@class='visuallyhidden']").click()

        intelProc = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.pcgarage.ro/procesoare/intel/']"))).click()

        drpElement=self.driver.find_element_by_id("sortsel")
        drp=Select(drpElement)
        drp.select_by_visible_text("Pret descrescator")

        intelProcHeader = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Procesoare Intel']"))).text
        self.assertTrue(intelProcHeader == "Procesoare Intel") 

        intelProcSel = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.pcgarage.ro/procesoare/intel/coffee-lake-core-i9-9900k-360ghz-box/']"))).click()

        intelProcSelHeader = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Procesor Intel Coffee Lake, Core i9 9900K 3.6GHz box']"))).text
        self.assertTrue(intelProcSelHeader == "Procesor Intel Coffee Lake, Core i9 9900K 3.6GHz box")

        # cosProcIntel = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Adauga in cos']"))).click()

        # self.assertEqual("Procesoare", procHeader)

        # pcMenuBtn = self.driver.find_element_by_xpath("//a[@class ='js-megamenu-list-department-link gtm_31vgamc'][@href='javascript:void(0)']")        
        # componenteBtn = self.driver.find_element_by_xpath("//a[@class='cat-nav-tab'][text()='Componente']")
        # actions.move_to_element(pcMenuBtn).move_to_element(componenteBtn).click().perform()
        
        # titluComp = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Componente PC']")))

        # self.assertEqual("Componente PC", titluComp)
        # self.driver.send_keys(Keys.HOME)
        # self.driver.execute_script('window.scrollTo(0, 100*document.body.scrollHeight);')
        # procesoare = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Procesoare']")))
        # procesoare.click()



        time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__== "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Pavel/Desktop/Python/Proiect/Selenium-Python/reports'))