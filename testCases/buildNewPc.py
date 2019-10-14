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
from pageObjects.LoginPage import LoginPage


# This test make you(buy) the best computer, prepare your wallet!
class LoginTest(unittest.TestCase):
    baseURL = "https://www.pcgarage.ro/"
    driver = webdriver.Chrome(executable_path = "F:/Python/Selenium-Python/drivers/chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
            
    def test_graphics(self):
        lp=LoginPage(self.driver)
        wait = WebDriverWait(self.driver, 15) 
        action = ActionChains(self.driver)
        self.driver.implicitly_wait(10)
                       
        self.assertEqual("PC Garage | Notebook, calculatoare, sisteme, periferice si componente PC", self.driver.title) 
        lp.clickMainBth()
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
        lp.clickMainBth()                
        lp.searchPb()
        lp.pbClick()
        lp.pbCosClick()
        pbCosDeCump = self.driver.find_element_by_xpath ("//td[@class='ct-name']//a[@href='https://www.pcgarage.ro/placi-de-baza/asus/tuf-z390-pro-gaming/']")
        self.assertTrue(cosMeuDeCump == "Cosul tau de cumparaturi")
        self.assertIsNotNone(procCosDeCump)
        self.assertIsNotNone(pbCosDeCump)
        
        # Buy Ram
        lp.clickMainBth() 
        lp.memClick()
        memHeader = wait.until(EC.presence_of_element_located((By.XPATH, "//b[text()='Memorii']"))).text
        self.assertTrue(memHeader == "Memorii")        
        lp.memSelClick()
        memBuyHeader = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Memorie G.Skill Trident Z RGB 64GB DDR4 3000MHz CL14 1.35v Dual Channel Kit']"))).text
        self.assertTrue(memBuyHeader == "Memorie G.Skill Trident Z RGB 64GB DDR4 3000MHz CL14 1.35v Dual Channel Kit")
        lp.memCosClick() 
        memCosDeCump = self.driver.find_element_by_xpath("//a[@href='https://www.pcgarage.ro/memorii/gskill/trident-z-rgb-64gb-ddr4-3000mhz-cl14-135v-dual-channel-kit/']")
        self.assertTrue(cosMeuDeCump == "Cosul tau de cumparaturi")
        self.assertIsNotNone(procCosDeCump)
        self.assertIsNotNone(pbCosDeCump)
        self.assertIsNotNone(memCosDeCump) 

        # Buy Video Card
        lp.clickMainBth()
        lp.vcClick()
        cvHeader = wait.until(EC.presence_of_element_located((By.XPATH, "//b[text()='Placi video']"))).text
        self.assertTrue(cvHeader == "Placi video")
        lp.vcSelClick()
        lp.vcCosClick()
        vcCosDeCump = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='https://www.pcgarage.ro/placi-video/inno3d/geforce-rtx-2080-super-twin-x2-oc-8gb-gddr6-256-bit/']"))).text
        self.assertTrue(cosMeuDeCump == "Cosul tau de cumparaturi")
        self.assertIsNotNone(procCosDeCump)
        self.assertIsNotNone(pbCosDeCump)
        self.assertIsNotNone(memCosDeCump)
        self.assertIsNotNone(vcCosDeCump)

        # Buy SSD
        lp.clickMainBth()
        lp.ssdClick()
         
        



      

        time.sleep(5)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__== "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Selenium-Python\\reports'))