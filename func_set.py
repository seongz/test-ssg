from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from typing import Any
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
                    
def desktop_function(self: Any) -> None:
    """Desktop Function"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--start-maximized')
    service = Service(ChromeDriverManager().install())
    self.driver = webdriver.Chrome(service=service, options=chrome_options)

def xpath_click(target: Any, wait: Any) -> None:
    """XPATH Click"""
    wait.until(EC.element_to_be_clickable((By.XPATH,target))).click()

def xpath_check(target: Any, wait: Any) -> None:
    """XPATH Check"""
    wait.until(EC.element_to_be_clickable((By.XPATH,target)))

def time_check() -> None:
    """Time Check"""
    now = datetime.now()
    nowDatetime = now.strftime('실행시간: %Y-%m-%d %H:%M:%S')
    print(nowDatetime)





