#-*-coding:euc-kr
"""
update programmer : Juhyun Kim
GitHub : https://github.com/xenocurrency
update : 2023.11.23
===================================================================
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class NewsBot:
    def __init__(self, endswith):
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1024,768")
        # �ɼǿ� ��帮���� ����մϴ�. �ּ��� �����ϸ� ��帮���� �۾��� ����˴ϴ�.
        # self.options.add_argument("--headless=new")
        # �ɼ��� �Է��ؼ� ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome()
        # Ʈ���� �޽������� ������ ������ ����ϴ�.
        self.contents = []
        # ������ ����ϴ�.
        self.query = "https://www.google.com/search?tbm=nws&q="
        # �� ���̿� ���� ������ �Է��մϴ�.
        self.endswith = endswith

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # �α����� �����ϴ� �޼����Դϴ�.
    def login(self, id, ps):
        # Ʈ���� �α���â���� ���ϴ�.
        self.driver.get("https://twitter.com/i/flow/login")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)
        # ���̵� �Է��ϱ� ���� ���̵� �Է�â ��Ҹ� ã�ƿɴϴ�.
        # ���̵� �Է�â xapth ���� �� �Է�. selenium���������� �������� �ڵ尡 �ణ �ٸ�
        id_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        # id�� �Է��մϴ�.
        id_input.send_keys(id)
        #���� �Է�
        id_input.send_keys(Keys.RETURN)

        # ���â���� ��ȯ. �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)
        # ��й�ȣ�� �Է��մϴ�.
        # ��й�ȣ �Է�â xapth ���� �� �Է�. selenium���������� �������� �ڵ尡 �ణ �ٸ�
        ps_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        ps_input.send_keys(ps)
        ps_input.send_keys(Keys.RETURN)
        time.sleep(5)

    # ���ۿ��� ������ �ܾ�� Ʈ���ϱ� ���� �ٵ�� �Լ��Դϴ�.
    def prepare_contents(self, keyword):
        self.contents = []
        # �˻��� �����մϴ�.
        self.driver.get(self.query + keyword)
        # ���� ���� ���õ� ������Ʈ�� �ѹ��� �� ���ڽ��ϴ�.
        # ���� ���� �˻� ����� 'SoaBEf' ��� �̸��� Ŭ������ �����˴ϴ�.
        news_elements = self.driver.find_elements(By.CLASS_NAME, "SoaBEf")
        # ��� ������Ʈ�κ��� ������ �����ϰڽ��ϴ�.
        for el in news_elements:
            # ��� ������ �����մϴ�. <JheGif.nDgy9d> �±׷� �ۼ��Ǿ����ϴ�.
            headline = el.find_element(By.CLASS_NAME,"n0jPhd.ynAwRc.MBeuO.nDgy9d").text
            # ��� �����۸�ũ �±׸� �����մϴ�.
            hyperlink = el.find_element(By.TAG_NAME, "a")
            # ��� �����۸�ũ �±׿��� ��� �ּҸ� �����մϴ�.
            news_url = hyperlink.get_attribute("href")
            # �Ź��� ������ �����մϴ�. "MgUUmf NUnG9d"��� Ŭ���� �̸����� ����Ǿ� �ֽ��ϴ�.
            reference = el.find_element(By.CLASS_NAME, "MgUUmf.NUnG9d").text
            # ���� �� �κ��� ������ ���ϴ�. "GI74Re nDgy9d"��� Ŭ������ ��ϵǾ� �ֽ��ϴ�.
            head = el.find_element(By.CLASS_NAME, "GI74Re.nDgy9d").text
            # Ʈ���� �ø� ��� ����� ����ϴ�.
            news_summary = "\n".join((headline, reference, head, self.endswith, news_url))
            self.contents.append(news_summary)

    # �޽����� �Է¹޾� Ʈ���ϴ� �ż����Դϴ�.
    def tweet(self, string):
        # Ʈ�� ����� ���� �Է��� �� �ְ� ���� �������� �̵��մϴ�.
        self.driver.get("https://twitter.com/intent/tweet")
        time.sleep(5)
        # �޽��� �Է�â ��Ҹ� ã���ϴ�. xpath�� �����մϴ�.
        board = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        # �޽��� �Է�â�� �޽����� �����ϴ�.
        board.send_keys(string)
        # Ctrl + Enter�� ���� �޽����� �Խ��մϴ�.
        board.send_keys(Keys.CONTROL + Keys.RETURN)

    # self.contents�� ����� ��� �޽����� �ϳ��� Ʈ���ϴ� �ż����Դϴ�.
    def tweet_all(self, interval):
        # for���� ����� ��� �޽����� �ϳ��� �����մϴ�.
        for el in self.contents:
            # �޽����� �ϳ��� Ʈ���մϴ�.
            self.tweet(el)
            # �ε��� �� �ɸ� �� �����Ƿ� ��ٷ��ݴϴ�.
            time.sleep(interval)

    # Ű���带 �Է¹޾� ������ �˻��ϰ�, Ʈ���Ϳ��� ���ε��ϴ� ���� ����ϴ�.
    def news_go_go(self, keyword, interval=10):
        # ���� ��縦 �ܾ�ɴϴ�.
        self.prepare_contents(keyword)
        # �ܾ�� ��� �ڷḦ �ø��ϴ�.
        self.tweet_all(interval)

    def save_screenshot(self):
        self.driver.save_screenshot("test.png")
