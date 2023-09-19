from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import chromedriver_autoinstaller
                    
def Desktop_Function(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chromedriver_autoinstaller.install(True)
    self.driver = webdriver.Chrome(options=chrome_options)

def xpathClick(target, wait):
    wait.until(EC.element_to_be_clickable((By.XPATH,target))).click()

def xpathCheck(target, wait):
    wait.until(EC.element_to_be_clickable((By.XPATH,target)))

def time_check():
    now = datetime.now()
    nowDatetime = now.strftime('실행시간: %Y-%m-%d %H:%M:%S')
    print(nowDatetime)





