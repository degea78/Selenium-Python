class LoginPage():



    def __init__(self, driver):
        self.driver = driver
    def clickMainBth(self):
        self.driver.find_element_by_xpath("//a[@class='cat-nav-tab'][text()='Componente']").click()
    def searchPb(self):
        self.driver.find_element_by_xpath( "//input[@name = 'search'][@id ='searchac']").send_keys("ASUS TUF Z390-PRO GAMING")
        self.driver.find_element_by_id("sbbt").click()
    def pbClick(self):
        self.driver.find_element_by_xpath("//a[text()='Placa de baza '][@title='Placa de baza ASUS TUF Z390-PRO GAMING']").click()
    def pbCosClick(self):
        self.driver.find_element_by_xpath("//button[@type ='submit'][@aria-label='Adauga ASUS TUF Z390-PRO GAMING in cos']").click()
    def memClick(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.pcgarage.ro/memorii/'][text()='Memorii']").click()
    def memSelClick(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.pcgarage.ro/memorii/gskill/trident-z-rgb-64gb-ddr4-3000mhz-cl14-135v-dual-channel-kit/']").click()
    def memCosClick(self):
        self.driver.find_element_by_xpath("//div[@class='ps-addtocart']//button[@type='submit']").click()
    def vcClick(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.pcgarage.ro/placi-video/'][text()='Placi video']").click()
    def vcSelClick(self):
        self.driver.find_element_by_xpath("//a[@href='https://www.pcgarage.ro/placi-video/inno3d/geforce-rtx-2080-super-twin-x2-oc-8gb-gddr6-256-bit/']").click()
    def vcCosClick(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Adauga Inno3D GeForce RTX 2080 SUPER Twin X2 OC 8GB GDDR6 256-bit in cos']").click()
        
