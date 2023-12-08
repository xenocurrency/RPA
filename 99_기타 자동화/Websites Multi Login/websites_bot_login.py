#-*-coding:utf-8
"""
programmer : Juhyun Kim
GitHub : https://github.com/xenocurrency
Last Modification : 2023.12.02.
"""

try:
    import pyexcel as px
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'pyexcel'])
    pip.main(['install', 'pyexcel-xlsx'])
    try:
        import pyexcel as px
    except ModuleNotFoundError:
        time.sleep(2)
        import pyexcel as px
# If pyexcel has problem, please enter below 2 commands in git bash sequentially.
# pip uninstall openpyxl
# pip install openpyxl==3.0.10

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pyw
import time

# LoginBot 클래스 목적 : 여러 웹사이트 로그인 후 창을 유지함
class LoginBot:
    def __init__(self,websites_info_filename):
        self.data_array = px.get_array(file_name=websites_info_filename)  # 웹사이트 로그인 정보 엑셀파일을 리스트로 불러옴

        self.header = self.data_array[0]        # 헤더 리스트 분리
        self.contents = self.data_array[1:]     # 내용 리스트 분리
        self.websites_qty = len(self.contents)      # 로그인 할 웹사이트 개수

        self.URL = []
        self.ID = []
        self.PW = []
        self.tab_for_ID = []
        self.tab_for_PW = []
        self.landing_page = []

        for i in range(self.websites_qty):
            self.URL.append(self.contents[i][0])      # 로그인 url
            self.ID.append(self.contents[i][1])
            self.PW.append(self.contents[i][2])
            self.tab_for_ID.append(self.contents[i][3])       # URL 생성 이후 ID 입력창에 가기 위해 눌러야 하는 TAB 회수
            self.tab_for_PW.append(self.contents[i][4])       # ID 입력 이후 PW 입력창에 가기 위해 눌러야 하는 TAB 회수
            self.landing_page.append(self.contents[i][5])       # 랜딩페이지. 로그인 후 최초접속 url


        self.options = Options()
        self.options.add_argument("--window-size=1024,768")
        self.driver = webdriver.Chrome()        #크롬 실행


    def kill(self):
        self.driver.quit()      #크롬 닫기


    def login(self):
        for i in range(self.websites_qty):
            self.driver.execute_script("window.open('');")      #새창 열기
            self.new_tab = self.driver.window_handles[-1]
            self.driver.switch_to.window(self.new_tab)      #새창으로 전환
            self.driver.get(self.URL[i])        #새창에서 로그인 url로 이동
            time.sleep(2)
            for j in range(self.tab_for_ID[i]):
                pyw.key_press_once("tab")       # TAB을 지정횟수만큼 눌러 ID 입력창으로 이동
            pyw.typing(self.ID[i])     # ID입력
            for j in range(self.tab_for_PW[i]):
                pyw.key_press_once("tab")       # TAB을 지정횟수만큼 눌러 PW 입력창으로 이동
            pyw.typing(self.PW[i])     # PW입력
            pyw.key_press_once("enter")     # 엔터쳐서 로그인이 안되는 사이트라면 로그인불가(이런 일이 거의 없어서 무시한다)
            time.sleep(5)
            if len(self.landing_page[i]) == 0:
                continue        #랜딩페이지가 공백이면 생략
            self.driver.get(self.landing_page[i])       #랜딩페이지로 이동


    def print(self):        #프린트.테스트용
        print(self.header)
        print(self.contents)
        print("websites Q'ty = "+ str(len(self.contents)))
        print(self.URL)



