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


# Ʈ������������ ������. Ʈ���� �α��� �ּҸ� �̸� ������ �� ��ųʸ��Դϴ�.
LOGIN_URLS = {
    "twitter": "https://twitter.com/i/flow/login",
}


class LoginBot:
    def __init__(self, site):
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        self.options.add_argument("--window-size=1600,900")
        # �ɼ��� �Է��ؼ� ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome()
        # �α����Ϸ��� ����Ʈ�� �̵��� �α���â�� �մϴ�.
        try:
            self.driver.get(LOGIN_URLS[site.lower()])
            # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
            time.sleep(5)
        except KeyError:
            # �̸� ���õ��� ���� �ּ��Դϴ�. �ּ�â�� �ٷ� �Է��� �õ��մϴ�.
            self.driver.get(site)
            # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
            time.sleep(5)

    # ũ�ѷ��� �����ϴ� �޼����Դϴ�.
    # ���� ����¥�� �ڵ带 �Լ��� ���� ������ ���� ������ �ֽ��ϴٸ�,
    # ���� �������ڸ� Ŭ���� �ܺο��� Ŭ���� ���� �ڷῡ �ʹ� ��� �����ϴ� ��Ȳ�� ������ �ʱ� �����Դϴ�.
    def kill(self):
        self.driver.quit()

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

    def save_screenshot(self):
        self.driver.save_screenshot("test.png")