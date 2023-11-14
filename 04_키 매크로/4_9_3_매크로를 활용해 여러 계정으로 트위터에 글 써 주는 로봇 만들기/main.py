#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import twitter_bot_multi as tb


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
idfile = sys.argv[1]

# Ʈ���� ������� ���� ������ �Է¹޽��ϴ�.
filename = sys.argv[2]

# ���̵�� ��й�ȣ�� ��Ʈ�� ������ �� ����Ʈ�� ����ϴ�.
IDs = []

# ���̵� ����� ������ �ҷ��ɴϴ�.
idfile = open(idfile, encoding="utf-8")

# �̰� �� �پ� �о�ɴϴ�.
for line in idfile:
    # �� ���� �ĸ��� �ɰ� �ݴϴ�.
    splt = line.split(",")
    # ���빰�� �ΰ��� �ƴ� ������ ��� �����ݴϴ�.
    if len(splt) != 2:
        continue
    # IDs�� ���̵�� ��й�ȣ�� �����մϴ�.
    IDs.append((splt[0].strip(), splt[1].strip()))

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = tb.TwitterBot(filename)

# IDs�� ����� ������ �ϳ��� �ҷ��ɴϴ�.
for i in range(len(IDs)):
    # �α����� �õ��մϴ�.
    ID, PS = IDs[i]
    BOT.login(ID, PS)
    # �α��ο� ���������� ��ũ�����̳� �� �� ����ݽô�.
    BOT.save_screenshot(str(time.time) + ".png")
    # Ʈ���Ϳ� ��� ����� �ø��ϴ�.
    BOT.tweet_all()
    time.sleep(10)
    # ũ�ѷ��� �ݾ��ݴϴ�.
    BOT.kill()
    # ���� �۾��� �� ���� ������ �ִٸ�
    if i < len(IDs)-1:
        # ũ�ѷ��� �ٽ� �Ѽ� Ʈ���ͷ� �����մϴ�.
        BOT.go_to_twitter()
        time.sleep(3)


# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
