#-*-coding:euc-kr
"""
update programmer : Juhyun Kim
GitHub : https://github.com/xenocurrency
update : 2023.11.15
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
import random


class ReplyBot:
    def __init__(self, replyfile):
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.instagram.com/explore/tags/"
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� ��帮���� ����մϴ�. �ּ��� �����ϸ� ��帮���� �۾��� ����˴ϴ�.
        # self.options.add_argument("headless")
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1024,768")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome()
        # ��� ������ ���� ������ �ҷ��ɴϴ�. ���ڵ��� utf8�� �ƴϸ� �ٲ��ּ���.
        self.replyfile = open(replyfile, encoding="utf8")
        # ��� ���� ����Ʈ�� ����ϴ�.
        self.replylist = self.replyfile.read().split("\n")

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # �ν�Ÿ�׷� �α��� �Լ��Դϴ�.
    def login(self, id, ps):
        # �α��� �������� �̵��մϴ�.
        self.driver.get("https://www.instagram.com/accounts/login/")
        # �ε��� ���� 10�� ���� ��ٷ� �ݴϴ�.
        time.sleep(10)
        # ID, PS �Է� ��Ҵ� <input> �±��Դϴ�. ��Ҹ� ã���ݽô�.
        input_field = self.driver.find_elements(By.TAG_NAME, "input")
        # ù ��° ��Ұ� ���̵��Դϴ�. ���̵� �Է��մϴ�.
        input_field[0].send_keys(id)
        # ��й�ȣ �Է� ��Ҵ� �� ��°�Դϴ�. ��й�ȣ�� �Է��մϴ�.
        input_field[1].send_keys(ps)
        # ����Ű�� �ļ� �α����� �������մϴ�.
        input_field[1].send_keys(Keys.RETURN)
        # 60�� ���� ��ٷ� �ݴϴ�.
        time.sleep(60)

    # �ν�Ÿ�׷����� �±׸� �˻��ϴ� �Լ��Դϴ�.
    def search_tag(self, tag):
        self.driver.get(self.querry + tag)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �±� �˻� ȭ�鿡�� �α�Խñ� ù ��° ������ ��� Ŭ���մϴ�.
    def select_picture(self):
        #�� �Խñ��� ��Ÿ���� Ŭ���� �̸��� "_aagw"�Դϴ�
        pictures = self.driver.find_elements(By.CLASS_NAME, "_aagw")
        # ù��° ������ Ŭ���մϴ�
        time.sleep(2)
        pictures[0].click()
        time.sleep(5)

    # �˻�������� ���ƴٴϸ� ������ ���ƿ並 ������ ��۵� ��ϴ�.
    # num���� �� ���� �Խù��� ���ƿ� ���� �Է��մϴ�.
    # -1�� �Է��ϸ� ����ڰ� ���� �����ϱ� ������ ������ ����մϴ�.
    def press_like_and_reply(self, num):
        # �ݺ� ȸ���� �����ϱ� ���� �����Դϴ�.
        count = num
        # count �� 1���� ���̸鼭, 0�� �ɶ����� �ݺ��մϴ�.
        # num�� -1�� ��� ��� 0���� �۾����⸸ �ϰ� 0�� ������ �����Ƿ� ������ ����˴ϴ�.
        while count != 0:
            # ���ƿ� ��ư�� �±׸� ���� ã��� ����ϴ�. ���ƿ� ��ư�� <svg> �±׷� ������� �ִµ�
            # �� ȭ�鿡 <svg> �±׸� ���� �ִ� ��ư�� �� �� ���� �ƴմϴ�.
            # �׷��Ƿ� �ϴ� <svg> �±׸� ���� ��Ҹ� ���� ����ɴϴ�.
            svg = self.driver.find_elements(By.TAG_NAME,"svg")
            # <svg> �±״� ���ο� aria-label �̶�� �̸��� ��Ʈ����Ʈ�� ���� �ֽ��ϴ�.
            # �� ��Ʈ����Ʈ�� '���ƿ�' �� svg��Ҹ� ã�Ƴ� Ŭ���սô�.
            # for ������ �ϴ� svg �±׵��� ������ �ҷ��ɴϴ�.
            for el in svg:
                # �±� ������ aria-label ��Ʈ����Ʈ�� ���ƿ� �� ��츸 ��Ƴ��ϴ�.
                # �̹� ���ƿ䰡 ������ �ִ� ��� ��Ʈ����Ʈ ���� "���ƿ� ���" �� ����˴ϴ�.
                # ���� �� ����� �̹� ���ƿ並 ���� �� �Խù��� �ǳʶ� �� �ִٴ� ������ �����ϴ�.
                # �̹� ���ƿ並 ���� �Խù��� �ǳʶݴϴ�.
                if el.get_attribute("aria-label") == "���ƿ� ���":
                    break
                # ���ƿ� ��ư�� ã���ϴ�.
                if el.get_attribute("aria-label") == "���ƿ�":
                    # ���ƿ� ��ư�� Ŭ���մϴ�.
                    el.click()
                    # ������ ���� ��ٷ� �ݴϴ�.
                    time.sleep(5)
                    # ��� ���� �� �������� �ϳ��� �̾Ƽ� ����� �޾��ݽô�.
                    # ������ ���� �� �� �� �õ��մϴ�.
                    # �������ؼ� 3���̸� �˴ϴ�.
                    # �̷��� try except���� ���� ���°� ������ ���� ���� ���ƾ� �� �ڵ� ����Դϴ�.
                    try:
                        self.send_reply(random.choice(self.replylist))
                    except:
                        time.sleep(5)
                        try:
                            self.send_reply(random.choice(self.replylist))
                        except:
                            time.sleep(5)
                            self.send_reply(random.choice(self.replylist))
                    # ī��Ʈ�� �� ���� ��Ƴ����ϴ�.
                    count -= 1
                    break
            # ���� �Խù��� �Ѿ�ô�. ���� ��ư���� CLASS NAME �� "_abl-"�� ����Ǿ� �ֽ��ϴ�. ��Ҹ� ã���ϴ�.
            next_button = self.driver.find_element(By.CLASS_NAME,"_abl-")
            # Ŭ���մϴ�.
            next_button.click()
            # ����� �� �� ���� �ΰ� �޾ƾ� �մϴ�. �� �׷��� �ν�Ÿ ������� ��� ���� �ߴ� ������ �ݴϴ�.
            time.sleep(30)

    # ����� ����� �Լ��Դϴ�.
    def send_reply(self, text):
        # ��� �Է�â�� <textarea> ��� �±׿� �ֽ��ϴ�.
        textarea = self.driver.find_element(By.TAG_NAME,"textarea")
        textarea.send_keys(text + Keys.RETURN)

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� �ν�Ÿ �α����ϰ�, �˻��ϰ�, ��۵� �� �޾��ִ� �޼��带 ����ô�.
    def insta_jungdok(self, tag, num=100):
        # �±׵� �˻��ϰ�
        self.search_tag(tag)
        # ���� �� ���� ������ ����
        self.select_picture()
        # ���ƿ並 ������, ����� �޸鼭 ������ �� �徿 �Ѱ��ݴϴ�.
        self.press_like_and_reply(num)
