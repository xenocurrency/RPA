#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import time


class TwitterBot:
    def __init__(self, contents, encoding="utf-8"):
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1600,900")
        # Ʈ���� Ȩ�������� �̵��մϴ�.
        self.go_to_twitter()

        # ������ ������ �о�ɴϴ�. ���ڵ��� utf-8�� �ƴ� ������ ������ ������ ���̴ϴ�.
        # �̶��� ���ڵ��� ����� �ֽø� �˴ϴ�. �⺻���� utf-8�Դϴ�.
        self.contents_file = open(contents, encoding=encoding)
        # �о�� ������ �ɰ� ����Ʈ�� ����ϴ�.
        self.contents = self.contents_file.read().split("\n")

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

    # Ʈ���� �������� �����ϴ� �޼����Դϴ�.
    def go_to_twitter(self):
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome()
        # Ʈ���� Ȩ�������� �̵��մϴ�.
        self.driver.get("https://twitter.com/i/flow/login")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �α����� �����ϴ� �޼����Դϴ�.
    def login(self, id, ps):
        # tab Ű�� ���� �����ݽô�. Ʈ���� �������� ���̵� â���� �̵��մϴ�.
        pw.key_press_once("tab")
        pw.key_press_once("tab")
        pw.key_press_once("tab")
        # ���̵� �Է��մϴ�.
        pw.typing(id)
        # enter Ű�� �����ݽô�. Ʈ���� �������� ��ȣâ���� �̵��մϴ�.
        pw.key_press_once("enter")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(3)
        # ��й�ȣ�� ���� �Է��մϴ�.
        pw.typing(ps)
        # ����Ű�� �����ݴϴ�. ��κ��� ����Ʈ���� �α����� ����˴ϴ�.
        pw.key_press_once("enter")
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(6)

    # ��ũ������ �����ϴ� �Լ��Դϴ�.
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    # Ʈ���Ϳ� ���� �ø��� �Լ��Դϴ�.
    def tweet(self, text, interval=15):
        # ���� ���� �ۼ��ϱ� ���� �ۼ� ���� �������� �̵��մϴ�.
        self.driver.get("https://twitter.com/intent/tweet")
        time.sleep(2)
        # Ŀ���� �⺻������ �Է�â�� �� �ֽ��ϴ�. Ʈ�� ������ �Է��մϴ�.
        pw.type_in(text)
        time.sleep(1)
        # ��Ʈ�� Ű�� ����Ű�� ������ Ʈ���� �Էµ˴ϴ�.
        pw.key_on("control")
        pw.key_on("enter")
        pw.key_off("control")
        pw.key_off("enter")
        # �ε� �ɶ����� �� �� ��ٸ��ϴ�.
        time.sleep(interval)

    # �о�� ��� ��ǵ��� ���ε��ϴ� �Լ��Դϴ�.
    # 3�� �������� ����� �ø��ϴ�. �ð� ������ �ٲٰ� ������ �Լ��� ȣ���� �� �ð��� �ʴ����� �Է��մϴ�.
    def tweet_all(self, interval=3):
        for el in self.contents:
            time.sleep(interval)
            self.tweet(el.strip(), interval)
