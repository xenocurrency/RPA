"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class LoginBot:
    def __init__(self):
        # 셀레늄 웹드라이버에 입력할 옵션을 지정합니다.
        self.options = Options()
        # 옵션에 해상도를 입력합니다.
        self.options.add_argument("--window-size=1024,768")
        # 옵션에 헤드리스를 명시합니다. 주석을 해제하면 헤드리스로 작업이 수행됩니다.
        # self.options.add_argument("headless")
        # 옵션을 입력해서 크롬 웹드라이버를 불러옵니다.
        self.driver = webdriver.Chrome()

    # 크롤러를 종료하는 메서드입니다.
    # 굳이 한줄짜리 코드를 함수로 만든 데에는 여러 이유가 있습니다만,
    # 쉽게 설명하자면 클래스 외부에서 클래스 내부 자료에 너무 깊게 관여하는 상황을 원하지 않기 때문입니다.
    def kill(self):
        self.driver.quit()

    # 로그인을 수행하는 메서드입니다.
    def login(self, id, ps):
        # 트위터 로그인창으로 들어갑니다.
        self.driver.get("https://twitter.com/login")
        # 로딩이 오래 걸릴 수 있으니 잠시 대기합니다.
        time.sleep(3)
        # 아이디를 입력하기 위해 아이디 입력창 요소를 찾아옵니다.
        # 아이디 입력창 xapth 복사 후 입력. selenium버젼때문에 기존과는 코드가 약간 다름
        id_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        # id를 입력합니다.
        id_input.send_keys(id)
        #엔터 입력
        id_input.send_keys(Keys.RETURN)

        # 비번창으로 전환. 로딩이 오래 걸릴 수 있으니 잠시 대기합니다.
        time.sleep(3)
        # 비밀번호를 입력합니다.
        # 비밀번호 입력창 xapth 복사 후 입력. selenium버젼때문에 기존과는 코드가 약간 다름
        ps_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        ps_input.send_keys(ps)
        ps_input.send_keys(Keys.RETURN)

    def save_screenshot(self):
        self.driver.save_screenshot("test.png")
