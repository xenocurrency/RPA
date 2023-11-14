"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class TwitterBot:
    def __init__(self):
        self.options = Options()
        # 옵션에 헤드리스를 명시합니다. 주석을 해제하면 헤드리스로 작업이 수행됩니다.
        #self.options.add_argument("--headless=new")
        # 옵션에 해상도를 입력합니다.
        self.options.add_argument("--window-size=1440,980")
        # 옵션을 입력해서 크롬 웹드라이버를 불러옵니다.
        self.driver = webdriver.Chrome()
        #self.driver = webdriver.Chrome(options=self.options)
        # 트윗할 메시지들을 저장할 공간을 만듭니다.
        self.contents = []

    # 크롤러를 종료하는 메서드입니다.
    # 굳이 한줄짜리 코드를 함수로 만든 데에는 여러 이유가 있습니다만,
    # 쉽게 설명하자면 클래스 외부에서 클래스 내부 자료에 너무 깊게 관여하는 상황을 원하지 않기 때문입니다.
    def kill(self):
        self.driver.quit()

    # 크롬드라이버를 껐다가 다시 켜는 2차원 매서드입니다.
    def reload_browser(self):
        # 드라이버를 끕니다.
        self.kill()
        # 옵션을 입력해서 크롬 웹드라이버를 불러옵니다.
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    # 로그인을 수행하는 메서드입니다.
    def login(self, id, ps):
        # 트위터 로그인창으로 들어갑니다.
        self.driver.get("https://twitter.com/i/flow/login")
        # 로딩이 오래 걸릴 수 있으니 잠시 대기합니다.
        time.sleep(5)
        # 아이디를 입력하기 위해 아이디 입력창 요소를 찾아옵니다.
        # 아이디 입력창 xapth 복사 후 입력. selenium버젼때문에 기존과는 코드가 약간 다름
        id_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        # id를 입력합니다.
        id_input.send_keys(id)
        #엔터 입력
        id_input.send_keys(Keys.RETURN)

        # 비번창으로 전환. 로딩이 오래 걸릴 수 있으니 잠시 대기합니다.
        time.sleep(5)
        # 비밀번호를 입력합니다.
        # 비밀번호 입력창 xapth 복사 후 입력. selenium버젼때문에 기존과는 코드가 약간 다름
        ps_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        ps_input.send_keys(ps)
        ps_input.send_keys(Keys.RETURN)

    # 파일을 읽어와 트윗할 메시지를 정리하는 메서드입니다.
    def prepare_contents(self, filename):
        # 인코딩이 utf8이 아닐 경우 변경해주세요.
        file = open(filename, encoding="utf8")
        self.contents = file.read().split("\n")

    # 메시지를 입력받아 트윗하는 매서드입니다.
    def tweet(self, string):
        # 트윗 멘션을 쉽게 입력할 수 있게 전용 페이지로 이동합니다.
        self.driver.get("https://twitter.com/intent/tweet")
        time.sleep(5)
        # 메시지 입력창 요소를 찾습니다. xpath를 복사합니다.
        board = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        # 메시지 입력창에 메시지를 보냅니다.
        board.send_keys(string)
        # Ctrl + Enter를 눌러 메시지를 게시합니다.
        board.send_keys(Keys.CONTROL + Keys.RETURN)

    # self.contents에 저장된 모든 메시지를 하나씩 트윗하는 2차원 매서드입니다.
    def tweet_all(self, interval):
        # for문을 사용해 모든 메시지를 하나씩 접근합니다.
        for el in self.contents:
            # 메시지를 하나씩 트윗합니다.
            self.tweet(el)
            # 로딩에 좀 걸릴 수 있으므로 기다려줍니다.
            time.sleep(interval)

    # 파일을 읽어온 다음, 모두 트윗하는 3차원 매서드입니다.
    def twitter_jungdok(self, filename, interval=10):
        self.prepare_contents(filename)
        time.sleep(5)
        self.tweet_all(interval)

    def save_screenshot(self):
        self.driver.save_screenshot("test.png")
