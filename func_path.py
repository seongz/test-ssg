from selenium.webdriver.common.by import By

class Elements():
    def __init__(self):
        self.header_login_btn = "//div[@id='header']//li[@id='loginBtn']"
        self.wait_login_page = "//div[@id='memberLogin']"

        self.id_input = [By.XPATH, "//input[@id='mem_id']"]
        self.pw_input = [By.XPATH, "//input[@id='mem_pw']"]

        self.login_btn = "//button[@id='loginBtn']"
        self.header_mypage_btn = "//div[@id='header']//li[@id='gnbUserInfoArea']"
        self.wait_mypage = [By.XPATH, "//div[@id='divCmmyssgSecOrder']"]


