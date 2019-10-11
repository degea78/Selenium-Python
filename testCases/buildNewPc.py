import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("F://Python/Selenium-Python")	
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class LoginTest(unittest.TestCase):
    baseURL = "https://www.pcgarage.ro/"
    driver = webdriver.Chrome(executable_path = "F:/Python/Selenium-Python/drivers/chromedriver.exe")

    

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
            
    def test_graphics(self):
        wait = WebDriverWait(self.driver, 15) 
        actions = ActionChains(self.driver)        
                       
        self.assertEqual("PC Garage | Notebook, calculatoare, sisteme, periferice si componente PC", self.driver.title) 
        mainBtn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cat-nav-tab'][text()='Componente']"))) 
        mainBtn.click()
        # Buy Procesor 
        procesoare = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.pcgarage.ro/procesoare/']"))).click()
        procHeader = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[text()='Procesoare']"))).text
        self.assertTrue(procHeader == "Procesoare")        
        procSel = self.driver.find_element_by_xpath("//p[text()='Producator']//following-sibling::p[@class='lc-filter-char']//span[@class='visuallyhidden']").click()

        intelProc = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.pcgarage.ro/procesoare/intel/']"))).click()

        drpElement=self.driver.find_element_by_id("sortsel")
        drp=Select(drpElement)
        drp.select_by_visible_text("Pret descrescator")
        time.sleep(1)
        intelProcHeader = wait.until(EC.presence_of_element_located((By.XPATH, "//b[text()='Procesoare Intel']"))).text
        self.assertTrue(intelProcHeader == "Procesoare Intel") 

        intelProcSel = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.pcgarage.ro/procesoare/intel/coffee-lake-core-i9-9900k-360ghz-box/']"))).click()

        intelProcSelHeader = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Procesor Intel Coffee Lake, Core i9 9900K 3.6GHz box']"))).text
        self.assertTrue(intelProcSelHeader == "Procesor Intel Coffee Lake, Core i9 9900K 3.6GHz box")

        cosProcIntel = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit'][@aria-label='Adauga Intel Coffee Lake, Core i9 9900K 3.6GHz box in cos']"))).click()
        cosMeuDeCump = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Cosul tau de cumparaturi']"))).text
        self.assertTrue(cosMeuDeCump == "Cosul tau de cumparaturi")
        procCosDeCump = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Procesor Intel Coffee Lake, Core i9 9900K 3.6GHz box']")))
        self.assertIsNotNone(procCosDeCump)

        # Buy Motherboard
        time.sleep(2)
        # mainBtn.click()
        # mbSel = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.pcgarage.ro/placi-de-baza/']"))).click()



        # self.assertEqual("Procesoare", procHeader)


        # actions.move_to_element(pcMenuBtn).move_to_element(componenteBtn).click().perform()
        
  

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Selenium-Python\\reports'))