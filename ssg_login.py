from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from typing import Any
from func_path import Elements as elements
import unittest, sys, os
import func_set, func_set
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def xpath_click(target: str, wait: Any) -> None:
    func_set.xpath_click(target, wait)

def xpath_check(target: str, wait: Any) -> None:
    func_set.xpath_check(target, wait)

class LoginSSG(unittest.TestCase):
    """Login SSG mall"""
    test_failed = False

    def setUp(self) -> None:
        """Unittest setUp"""
        func_set.desktop_function(self)

    def test_login(self) -> None:
        """Test Login"""
        elems = elements()
        driver = self.driver
        driver.get("https://www.ssg.com/")
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 5)

        print ('[신세계몰 로그인 테스트]')
        func_set.time_check()

        # 헤더 로그인 버튼 클릭 > 로그인 팝업창 > 이메일&비밀번호 입력 > 로그인 클릭
        xpath_click(elems.header_login_btn, wait)
        driver.switch_to.window(driver.window_handles[1])
        xpath_check(elems.wait_login_page, wait)
        elem_id =  driver.find_element(*elems.id_input)
        elem_id.send_keys("id")
        elem_pw = driver.find_element(*elems.pw_input)
        elem_pw.send_keys("pw")
        xpath_click(elems.login_btn, wait)

        # 헤더 고객명 클릭 > 마이페이지 노출 여부로 로그인 성공 확인
        driver.switch_to.window(driver.window_handles[0])
        xpath_click(elems.header_mypage_btn, wait)
        elem_mypage = driver.find_element(*elems.wait_mypage)
        if elem_mypage:
            print ('▶ 로그인 케이스 결과 : PASS')
            pass
        else:
            raise Exception("ERROR: 로그인 실패")
        
    def tearDown(self) -> None:
        """Make Screenshot"""
        if self.test_failed == False:
            self.driver.save_screenshot('./screenshots/screenshot.png')
        else:
            pass
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'])

