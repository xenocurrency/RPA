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


class LikeBot:
    def __init__(self):
        # ���� ���̽��� �����մϴ�.
        self.querry ="https://www.instagram.com/explore/tags/"
        # ������ ������̹��� �Է��� �ɼ��� �����մϴ�.
        self.options = Options()
        # �ɼǿ� �ػ󵵸� �Է��մϴ�.
        # self.options.add_argument("--window-size=1024,768")
        # �ɼǿ� ��帮���� ����մϴ�. �ּ��� �����ϸ� ��帮���� �۾��� ����˴ϴ�.
        # self.options.add_argument("headless")
        # ũ�� ������̹��� �ҷ��ɴϴ�.
        self.driver = webdriver.Chrome()

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
        # 10�� ���� ��ٷ� �ݴϴ�.
        time.sleep(30)

    # �ν�Ÿ�׷����� �±׸� �˻��ϴ� �Լ��Դϴ�.
    def search_tag(self, tag):
        self.driver.get(self.querry + tag)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(5)

    # �±� �˻� ȭ�鿡�� �α�Խñ� ù ��° ������ ��� Ŭ���մϴ�. (�ڵ��� �����̳� ���⿡�� �ν�Ÿ ũ�Ѹ� ������ �ɸ�)
    def select_picture(self):
        # ù��° �α�Խñ��� xpath�� �Ʒ��� �����ϴ�.
        recent_picture_xpath = '//*[@id="mount_0_0_Rx"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[2]/a/div[1]/div[2]'
        # �ֱ� ������ ��Ҹ� �����ɴϴ�.
        recent_picture = self.driver.find_element(By.XPATH, recent_picture_xpath)
        # �ֱ� ������ Ŭ���մϴ�.
        time.sleep(2)
        recent_picture.click()
        time.sleep(5)


    # �˻�������� ���ƴٴϸ� ������ ���ƿ� �����ϴ�.
    # num���� �� ���� �Խù��� ���ƿ� ���� �Է��մϴ�.
    # -1�� �Է��ϸ� ����ڰ� ���� �����ϱ� ������ ������ ����մϴ�.
    def press_like(self, num):
        # �ݺ� ȸ���� �����ϱ� ���� �����Դϴ�.
        count = num
        # count �� 1���� ���̸鼭, 0�� �ɶ����� �ݺ��մϴ�.
        # num�� -1�� ��� ��� 0���� �۾����⸸ �ϰ� 0�� ������ �����Ƿ� ������ ����˴ϴ�.
        while count != 0:
            # ���ƿ� ��ư�� �±׸� ���� ã��� ����ϴ�. ���ƿ� ��ư�� <svg> �±׷� ������� �ִµ�
            # ������Ʈ �߰���� : ���ƿ� ��ư�� svg �±״� ��Ʈ �׷��� div�±׿� ���������� �׷��� �� �κп��� �� �����ϼ���
            # �� ȭ�鿡 <svg> �±׸� ���� �ִ� ��ư�� �� �� ���� �ƴմϴ�.
            # �׷��Ƿ� �ϴ� <svg> �±׸� ���� ��Ҹ� ���� ����ɴϴ�.
            svg = self.driver.find_elements(By.TAG_NAME, "svg")
            # <svg> �±״� ���ο� aria-label �̶�� �̸��� ��Ʈ����Ʈ�� ���� �ֽ��ϴ�.
            # �� ��Ʈ����Ʈ�� '���ƿ�' �� svg��Ҹ� ã�Ƴ� Ŭ���սô�.
            # for ������ �ϴ� svg �±׵��� ������ �ҷ��ɴϴ�.
            for el in svg:
                # �±� ������ aria-label ��Ʈ����Ʈ�� ���ƿ� �� ��츸 ��Ƴ��ϴ�.
                # �̹� ���ƿ䰡 ������ �ִ� ��� ��Ʈ����Ʈ ���� "���ƿ� ���" �� ����˴ϴ�.
                # ���� �� ����� �̹� ���ƿ並 ���� �� �Խù��� �ǳʶ� �� �ִٴ� ������ �����ϴ�.
                # ���� �� �������� ����� ���ƿ䵵 ��� Ŭ���մϴ�.
                if el.get_attribute("aria-label") == "���ƿ�":
                    # ���ƿ� ��ư�ϰ�� Ŭ���մϴ�.
                    el.click()
                    time.sleep(1)
                    # ����� �޾����� for���� �����մϴ�.
                    # �Ʒ� break�� ����� ��ۿ��� ��� ���ƿ並 �����ϴ�.
                    # ī��Ʈ�� �� ���� ��Ƴ����ϴ�.
                    count -= 1
                    break
            # ���� �Խù��� �Ѿ�ô�. ���� ��ư���� link text�� "����"���� ����Ǿ� �ֽ��ϴ�. ��Ҹ� ã���ϴ�. (�ڵ��� �����̳� ���⿡�� �ν�Ÿ ũ�Ѹ� ������ �ɸ�)
            next_button = self.driver.find_element(By.LINK_TEXT, "����")
            # Ŭ���մϴ�.
            next_button.click()
            # �ε��� ���� 5������ ��ٷ� �ݴϴ�.
            time.sleep(5)

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� �ν�Ÿ �α����ϰ�, �˻��ϰ�, ĸó�� �� �ϴ� �޼��带 ����ô�.
    def insta_jungdok(self, tag, num=100):
        # �±׵� �˻��ϰ�
        self.search_tag(tag)
        # ���� �� ���� ������ ����
        self.select_picture()
        # ���ƿ並 �����鼭 ������ �� �徿 �Ѱ��ݴϴ�.
        self.press_like(num)
