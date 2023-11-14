#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import twitter_bot_news as tb


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[1]

# ��й�ȣ�� �Է¹޽��ϴ�.
ps = sys.argv[2]

# ��ũ���� ���� Ű���带 �Է¹޽��ϴ�.
keyword = sys.argv[3]

# Ʈ�� ���̿� �Է��� ������ �ۼ��մϴ�.
# �ʹ� ��� Ʈ���� �Է��� �� �˴ϴ�. ª�� �Է��սô�.
endswith = "#���� #���� #��"

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = tb.NewsBot(endswith)

# Ʈ���� �α����� �õ��մϴ�.
BOT.login(id, ps)

# �۾��� �����մϴ�.
BOT.news_go_go(keyword)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
