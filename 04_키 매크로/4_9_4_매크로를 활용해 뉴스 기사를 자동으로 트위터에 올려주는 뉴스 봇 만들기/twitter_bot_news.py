#-*-coding:euc-kr

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import time
import pyperclip


class NewsBot:
    def __init__(self):
        #쿼리 베이스를 제작
        self.querry = "https://www.google.com/search?tbm=nws&q="
        #셀레늄 웹드라이버에 입력할 옵션을 지정
        self.options = Options()
        #옵션에 해상도를 입력
        self.options.add_argument("--window-size=1600,900")
        #크롬 웹드라이버를 불러옴
        self.driver = webdriver.Chrome()
        #정리된 뉴스를 저장할 변수를 만듦
        self.news_list = []
        self.news_text = ""
        #일단 트위터 로그인 화면으로 갑니다

    #크롤러 종료 메소드
    def kill(self):
        self.driver.quit()

    #검색을 실시하는 메소드
    def search(self, keyword):
        self.driver.get(self.querry + keyword)
        #로딩 시간
        time.sleep(3)

    #새로고침 메소드
    def refresh(self):
        pw.key_press_once("f5")

    #페이지의 모든 내용을 선택하고 클립보드에 복사하는 메소드
    def copy_all(self):
        pw.ctrl_a()
        time.sleep(1)
        #혹시모르니 ctrl_c를 세번하여 확실하게 복사
        pw.ctrl_c()
        time.sleep(1)
        pw.ctrl_c()
        time.sleep(1)
        pw.ctrl_c()

    #페이지 모든 내용을 선택하여 복사 후 그 중 뉴스기사만 뽑아내는 2차원 메소드(=함수)
    def scrap_news(self):
        #모든 내용 선택하여 복사
        self.copy_all()
        #뉴스 리스트를 초기화. 추후 다양하게 활용하기 위해 초기화
        #예시 - 매일 업데이트 뉴스 트윗한다면, 지난뉴스를 또 올릴 필요는 없음
        self.news_list = []
        #텍스트를 클립보드에서 추출해 스트링으로 따옵니다
        self.news_text = pyperclip.paste()
        #스트링을 한 줄씩 쪼개어 splt 리스트로 저장
        splt = self.news_text.split("\n")

        #구글뉴스는 이미지 정보, 헤드라인, 게시시간, 본문요약 순으로 정보가 제공됨
        #내용물을 한줄씩 읽으며 정보취합

        #리스트 내 원소들을 하나씩(=글자들을 한 줄씩) 불러옴
        for i, line in enumerate(splt):
            #문자가 3개 미만은 불필요한 정보로 간주하여 건너뜀
            if len(line.strip()) < 3:
                continue
            #뉴스 작성 시점을 알려주는 문자 등장하면 앞의 3개 줄을 뽑아와 하나의 스트링으로 합쳐줌
            elif line.strip()[-3:] in "달 전  주 전  일 전  시간 전  분 전  초 전  .197  .198  .199  .200  .201  .202":
                new_news = "\n".join(splt[i - 3:i])
                #합친 스트링을 뉴스 리스트 내 삽입
                self.news_list.append(new_news)

    #뉴스 기사를 구글에서 검색 후, 리스트로 다듬는 3차원 메소드
    def news_crawler(self, keyword):
        self.search(keyword)
        self.scrap_news()

    #스크린샷을 저장하는 메소드
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    #트위터 로그인 페이지에 접속하는 메소드
    def go_to_twitter(self):
        #트위터 홈페이지로 이동
        self.driver.get("http://twitter.com/i/flow/login")
        #로딩 대기
        time.sleep(2)

    #트위터 홈으로 이동하는 메소드
    def twitter_home(self):
        self.driver.get("http://twitter.com/home")
        #로딩 대기
        time.sleep(2)

    #트위터 로그인 수행하는 2차원 메소드
    def login(self, id, ps):
        #트위터 로그인 페이지로 이동
        self.go_to_twitter()
        # tab 키를 세번 눌러줍시다. 트위터 전용으로 아이디 창으로 이동합니다.
        pw.key_press_once("tab")
        pw.key_press_once("tab")
        pw.key_press_once("tab")
        # 아이디를 입력합니다.
        pw.typing(id)
        # enter 키를 눌러줍시다. 트위터 전용으로 암호창으로 이동합니다.
        pw.key_press_once("enter")
        # 로딩이 오래 걸릴 수 있으니 잠시 대기합니다.
        time.sleep(3)
        # 비밀번호를 마저 입력합니다.
        pw.typing(ps)
        # 엔터키를 눌러줍니다. 대부분의 사이트에서 로그인이 실행됩니다.
        pw.key_press_once("enter")
        # 로딩이 오래 걸릴 수 있으니 잠시 대기합니다.
        time.sleep(6)

    #트위터 작성 페이지로 이동해서 글을 올리는 메소드
    def tweet(self, text, interval):
        #트위터 작성 페이지로 이동
        self.driver.get("http://twitter.com/intent/tweet")
        time.sleep(2)
        #커서가 기본적으로 입력창에 가 있습니다. 바로 내용입력함
        pw.type_in(text)
        time.sleep(1)
        #ctrl+엔터 치면 트윗 입력됨
        pw.key_on("control")
        pw.key_on("enter")
        pw.key_off("control")
        pw.key_off("enter")
        #로딩까지 몇초 기다림
        time.sleep(interval)

    #스크랩한 모든 뉴스를 트위터에 올리는 2차원 메소드
    #15초간격으로 뉴스를 올림. 시간간격을 바꾸려면 메소드 호출 시, 시간을 초 단위로 입력합니다
    #해시태그를 입력할 경우, 함께 삽입합니다
    def tweet_all(self, hashtags="", interval=15):
        for el in self.news_list:
            self.tweet(el.strip() + " " + hashtags, interval)

    #구글에서 뉴스를 검색하고,
    #트위터에 로그인 하고 (x) <- 로그인은 미리해뒀음
    #긁어온 모든 뉴스를 업로드 까지 하는 4차원 메소드입니다
    # 15초간격으로 뉴스를 올림. 시간간격을 바꾸려면 메소드 호출 시, 시간을 초 단위로 입력합니다
    # 해시태그를 입력할 경우, 함께 삽입합니다
    def tweet_all_news(self, keyword, hashtags="", interval=15):
        self.news_crawler(keyword)
        self.twitter_home()
        self.tweet_all(hashtags, interval)
        time.sleep(interval)



