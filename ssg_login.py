from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest, sys, os
import func_set, func_set
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def xpathClick(target, wait):
    func_set.xpathClick(target, wait)

def xpathCheck(target, wait):
    func_set.xpathCheck(target, wait)

class Login_ssg(unittest.TestCase):
    test_failed = False

    def setUp(self):
        func_set.Desktop_Function(self)

    def test_login(self):
        driver = self.driver
        driver.get("https://www.ssg.com/")
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)

        print ('[신세계몰 로그인 테스트]')
        func_set.time_check()

        # 로그인 클릭 > 로그인 팝업창 > 이메일&비밀번호 입력 > 로그인 클릭
        xpathClick("//div[@id='header']//li[@id='loginBtn']", wait)
        driver.switch_to.window(driver.window_handles[1])
        xpathCheck("//div[@id='memberLogin']", wait)
        elem_id =  driver.find_element(By.XPATH, "//input[@id='mem_id']")
        elem_id.send_keys("id")
        elem_pw = driver.find_element(By.XPATH, "//input[@id='mem_pw']")
        elem_pw.send_keys("pw")
        xpathClick("//button[@id='loginBtn']", wait)

        # 헤더 고객명 클릭 > 마이페이지 노출 여부로 로그인 성공 확인
        driver.switch_to.window(driver.window_handles[0])
        xpathClick("//div[@id='header']//li[@id='gnbUserInfoArea']", wait)
        elem_mypage = driver.find_element(By.XPATH, "//div[@id='divCmmyssgSecOrder']")
        if elem_mypage:
            print ('▶ 로그인 케이스 결과 : PASS')
            pass
        else:
            raise Exception("ERROR: 로그인 실패")
        
    def tearDown(self):
        if self.test_failed == False:
            self.driver.save_screenshot('./screenshots/screenshot.png')
        else:
            pass
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'])

