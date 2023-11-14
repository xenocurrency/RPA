#-*-coding:euc-kr

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import time
import pyperclip


class NewsBot:
    def __init__(self):
        #���� ���̽��� ����
        self.querry = "https://www.google.com/search?tbm=nws&q="
        #������ ������̹��� �Է��� �ɼ��� ����
        self.options = Options()
        #�ɼǿ� �ػ󵵸� �Է�
        self.options.add_argument("--window-size=1600,900")
        #ũ�� ������̹��� �ҷ���
        self.driver = webdriver.Chrome()
        #������ ������ ������ ������ ����
        self.news_list = []
        self.news_text = ""
        #�ϴ� Ʈ���� �α��� ȭ������ ���ϴ�

    #ũ�ѷ� ���� �޼ҵ�
    def kill(self):
        self.driver.quit()

    #�˻��� �ǽ��ϴ� �޼ҵ�
    def search(self, keyword):
        self.driver.get(self.querry + keyword)
        #�ε� �ð�
        time.sleep(3)

    #���ΰ�ħ �޼ҵ�
    def refresh(self):
        pw.key_press_once("f5")

    #�������� ��� ������ �����ϰ� Ŭ�����忡 �����ϴ� �޼ҵ�
    def copy_all(self):
        pw.ctrl_a()
        time.sleep(1)
        #Ȥ�ø𸣴� ctrl_c�� �����Ͽ� Ȯ���ϰ� ����
        pw.ctrl_c()
        time.sleep(1)
        pw.ctrl_c()
        time.sleep(1)
        pw.ctrl_c()

    #������ ��� ������ �����Ͽ� ���� �� �� �� ������縸 �̾Ƴ��� 2���� �޼ҵ�(=�Լ�)
    def scrap_news(self):
        #��� ���� �����Ͽ� ����
        self.copy_all()
        #���� ����Ʈ�� �ʱ�ȭ. ���� �پ��ϰ� Ȱ���ϱ� ���� �ʱ�ȭ
        #���� - ���� ������Ʈ ���� Ʈ���Ѵٸ�, ���������� �� �ø� �ʿ�� ����
        self.news_list = []
        #�ؽ�Ʈ�� Ŭ�����忡�� ������ ��Ʈ������ ���ɴϴ�
        self.news_text = pyperclip.paste()
        #��Ʈ���� �� �پ� �ɰ��� splt ����Ʈ�� ����
        splt = self.news_text.split("\n")

        #���۴����� �̹��� ����, ������, �Խýð�, ������� ������ ������ ������
        #���빰�� ���پ� ������ ��������

        #����Ʈ �� ���ҵ��� �ϳ���(=���ڵ��� �� �پ�) �ҷ���
        for i, line in enumerate(splt):
            #���ڰ� 3�� �̸��� ���ʿ��� ������ �����Ͽ� �ǳʶ�
            if len(line.strip()) < 3:
                continue
            #���� �ۼ� ������ �˷��ִ� ���� �����ϸ� ���� 3�� ���� �̾ƿ� �ϳ��� ��Ʈ������ ������
            elif line.strip()[-3:] in "�� ��  �� ��  �� ��  �ð� ��  �� ��  �� ��  .197  .198  .199  .200  .201  .202":
                new_news = "\n".join(splt[i - 3:i])
                #��ģ ��Ʈ���� ���� ����Ʈ �� ����
                self.news_list.append(new_news)

    #���� ��縦 ���ۿ��� �˻� ��, ����Ʈ�� �ٵ�� 3���� �޼ҵ�
    def news_crawler(self, keyword):
        self.search(keyword)
        self.scrap_news()

    #��ũ������ �����ϴ� �޼ҵ�
    def save_screenshot(self, filename):
        self.driver.save_screenshot(filename)

    #Ʈ���� �α��� �������� �����ϴ� �޼ҵ�
    def go_to_twitter(self):
        #Ʈ���� Ȩ�������� �̵�
        self.driver.get("http://twitter.com/i/flow/login")
        #�ε� ���
        time.sleep(2)

    #Ʈ���� Ȩ���� �̵��ϴ� �޼ҵ�
    def twitter_home(self):
        self.driver.get("http://twitter.com/home")
        #�ε� ���
        time.sleep(2)

    #Ʈ���� �α��� �����ϴ� 2���� �޼ҵ�
    def login(self, id, ps):
        #Ʈ���� �α��� �������� �̵�
        self.go_to_twitter()
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

    #Ʈ���� �ۼ� �������� �̵��ؼ� ���� �ø��� �޼ҵ�
    def tweet(self, text, interval):
        #Ʈ���� �ۼ� �������� �̵�
        self.driver.get("http://twitter.com/intent/tweet")
        time.sleep(2)
        #Ŀ���� �⺻������ �Է�â�� �� �ֽ��ϴ�. �ٷ� �����Է���
        pw.type_in(text)
        time.sleep(1)
        #ctrl+���� ġ�� Ʈ�� �Էµ�
        pw.key_on("control")
        pw.key_on("enter")
        pw.key_off("control")
        pw.key_off("enter")
        #�ε����� ���� ��ٸ�
        time.sleep(interval)

    #��ũ���� ��� ������ Ʈ���Ϳ� �ø��� 2���� �޼ҵ�
    #15�ʰ������� ������ �ø�. �ð������� �ٲٷ��� �޼ҵ� ȣ�� ��, �ð��� �� ������ �Է��մϴ�
    #�ؽ��±׸� �Է��� ���, �Բ� �����մϴ�
    def tweet_all(self, hashtags="", interval=15):
        for el in self.news_list:
            self.tweet(el.strip() + " " + hashtags, interval)

    #���ۿ��� ������ �˻��ϰ�,
    #Ʈ���Ϳ� �α��� �ϰ� (x) <- �α����� �̸��ص���
    #�ܾ�� ��� ������ ���ε� ���� �ϴ� 4���� �޼ҵ��Դϴ�
    # 15�ʰ������� ������ �ø�. �ð������� �ٲٷ��� �޼ҵ� ȣ�� ��, �ð��� �� ������ �Է��մϴ�
    # �ؽ��±׸� �Է��� ���, �Բ� �����մϴ�
    def tweet_all_news(self, keyword, hashtags="", interval=15):
        self.news_crawler(keyword)
        self.twitter_home()
        self.tweet_all(hashtags, interval)
        time.sleep(interval)



