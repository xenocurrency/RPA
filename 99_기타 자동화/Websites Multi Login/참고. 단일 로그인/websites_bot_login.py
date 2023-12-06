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
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pywinmacro as pyw

# LoginBot 클래스 목적 : 여러 웹사이트 로그인 후 창을 유지함
class LoginBot:
    def __init__(self,websites_info_filename):
        self.data_array = px.get_array(file_name=websites_info_filename)  # 웹사이트 로그인 정보 엑셀파일을 리스트로 불러옴

        self.header = self.data_array[0]        # 헤더 리스트 분리
        self.contents = self.data_array[1:]     # 내용 리스트 분리

        self.URL = self.contents[0][0]      # 로그인 url
        self.ID = self.contents[0][1]
        self.PW = self.contents[0][2]
        self.tab_for_ID = self.contents[0][3]       # URL 생성 이후 ID 입력창에 가기 위해 눌러야 하는 TAB 회수
        self.tab_for_PW = self.contents[0][4]       # ID 입력 이후 PW 입력창에 가기 위해 눌러야 하는 TAB 회수

        self.options = Options()
        self.options.add_argument("--window-size=1024,768")
        self.driver = webdriver.Chrome()        #크롬 실행


    def kill(self):
        self.driver.quit()      #크롬 닫기


    def login(self):
        self.driver.get(self.URL)
        for i in range(self.tab_for_ID):
            pyw.key_press_once("tab")       # TAB을 지정횟수만큼 눌러 ID 입력창으로 이동
        pyw.typing(self.ID)     # ID입력
        for i in range(self.tab_for_PW):
            pyw.key_press_once("tab")       # TAB을 지정횟수만큼 눌러 PW 입력창으로 이동
        pyw.typing(self.PW)     # PW입력
        pyw.key_press_once("enter")     # 엔터쳐서 로그인이 안되는 사이트라면 로그인불가(이런 일이 거의 없어서 무시한다)


    def print(self):
        print(self.header)
        print(self.contents)
        print("websites Q'ty = "+ str(len(self.contents)))
        print(self.ID)
        print(self.PW)


    def multi_login(self):
        self.login()

