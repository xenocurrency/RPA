#-*-coding:euc-kr

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class CaptureBot:
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
        self.driver.maximize_window()

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
        time.sleep(5)
        # ID, PS �Է� ��Ҵ� <input> �±��Դϴ�. ��Ҹ� ã���ݽô�.
        input_field = self.driver.find_elements(By.TAG_NAME, "input")
        # ù ��° ��Ұ� ���̵��Դϴ�. ���̵� �Է��մϴ�.
        input_field[0].send_keys(id)
        # ��й�ȣ �Է� ��Ҵ� �� ��°�Դϴ�. ��й�ȣ�� �Է��մϴ�.
        input_field[1].send_keys(ps)
        # ����Ű�� �ļ� �α����� �������մϴ�.
        input_field[1].send_keys(Keys.RETURN)
        time.sleep(60)

    # �ν�Ÿ�׷����� �±׸� �˻��ϴ� �Լ��Դϴ�.
    def search_tag(self, tag):
        self.driver.get(self.querry + tag)
        # �ε��� ���� �ɸ� �� ������ ��� ����մϴ�.
        time.sleep(20)

    # �±� �˻� ȭ�鿡�� �α�Խñ� ù ��° ������ ��� Ŭ���մϴ�. (�ڵ��� �����̳� ���⿡�� �ν�Ÿ ũ�Ѹ� ������ �ɸ�)
    def select_picture(self):
        # ù��° �α�Խñ��� xpath�� �Ʒ��� �����ϴ�.
        recent_picture_xpath = '//*[@id="mount_0_0_gP"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[1]/div[1]/a/div[1]/div[2]'
        # �ֱ� ������ ��Ҹ� �����ɴϴ�.
        recent_picture = self.driver.find_element(By.XPATH, recent_picture_xpath)
        # �ֱ� ������ Ŭ���մϴ�.
        time.sleep(2)
        recent_picture.click()
        time.sleep(5)

    # �˻�������� ���ƴٴϸ� ������ ĸó�մϴ�.
    # num���� �� ���� �Խù��� ĸó�� �� �Է��մϴ�.
    # -1�� �Է��ϸ� ����ڰ� ���� �����ϱ� ������ ������ ����մϴ�.
    def capture_pictures(self, directory, num):
        # �ݺ� ȸ���� �����ϱ� ���� �����Դϴ�.
        count = num
        # count �� 0�� �ɶ����� �ݺ��մϴ�.
        while count != 0:
            # ī��Ʈ�� �� ���� ��Ƴ����ϴ�.
            # num�� -1�� ��� ��� 0���� �۾����⸸ �ϰ� 0�� ������ �����Ƿ� ������ ����˴ϴ�.
            count -= 1
            time.sleep(5)
            # ȭ���� ��°�� ĸó�ϴ°� �ǹ̰� ������ ������ �Խù� �κи� ĸ���սô�.
            # ��Ҹ� ã�� �ݴϴ�. article �±״� ������ �־� xpath�� ã���ϴ�.
            article_element = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div')
            # ��Һ��� ��ũ������ ���� �� �ֽ��ϴ�. ��� �ݽô�.
            article_element.screenshot(directory + "/" + str(time.time()) + ".png")
            # ��� ��ٷ� �ݽô�.
            time.sleep(5)
            # ���� �Խù��� �Ѿ�ô�. ���� ��ư���� link text�� "����"���� ����Ǿ� �ֽ��ϴ�. ��Ҹ� ã���ϴ�.
            # "����"�̶� �۾��� �����Ƿ� �ٸ����� �õ� ������ ����(link_text�� ������ ���� name�� ����) �ᱹ xpath�� ã���ϴ�.
            next_button = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button')
            # Ŭ���մϴ�.
            next_button.click()
            # �ε��� ���� 5������ ��ٷ� �ݴϴ�.
            time.sleep(5)

    # �ڵ� ����ȭ�� ���� �ڱⰡ �˾Ƽ� �ν�Ÿ �α����ϰ�, �˻��ϰ�, ĸó�� �� �ϴ� �޼��带 ����ô�.
    def insta_jungdok(self, tag, directory, num=100):
        # �±׵� �˻��ϰ�
        self.search_tag(tag)
        # ���� �� ���� ������ ����
        self.select_picture()
        # ĸó�� ���鼭 ������ �� �徿 �Ѱ��ݴϴ�.
        self.capture_pictures(directory, num)
