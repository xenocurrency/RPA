#-*-coding:euc-kr

import sys
import time
import twitter_bot_news as tb

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

#���̵� �ý��ۿ��� �Է¹޽��ϴ�
id = sys.argv[1]

#��й�ȣ�� �ý��ۿ��� �Է¹޽��ϴ�
ps= sys.argv[2]

#�˻�� �ý��ۿ��� �Է¹޽��ϴ�
keyword = sys.argv[3].strip()

#gb Ŭ���� ��Ʈ - ���۴������� Ű���� ������� �˻�. ���� �ؽ�Ʈ ���� �� ��Ʈ��ȭ
#ũ�ѷ��� �θ��ϴ�
BOT = tb.NewsBot()

#�α����� �õ��մϴ�
BOT.login(id,ps)

#������ �Բ� ������ �ؽ��±׸� �Է�
hashtags = "#���� #��ũ�� �ϴ� #�ڵ�ȭ #�ڵ�"

#���ۿ��� ���� �˻��ϰ�
#Ʈ���Ϳ� �ڵ��α����ϰ� (x) <- �α����� �̸��ص���
#�ܾ�� ��� ������ ���ε���
BOT.tweet_all_news(keyword, hashtags)

#����� �������� 10�� ���
time.sleep(10)

#ũ�ѷ� �ݾ���
BOT.kill()


# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
