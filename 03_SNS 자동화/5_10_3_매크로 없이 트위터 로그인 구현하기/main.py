#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import twitter_bot_login as tb


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[1]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[2]

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = tb.LoginBot()

# �α����� �õ��մϴ�.
BOT.login(id, ps)

# �۾��� �������� ������� ��ũ�����̳� �� �� ����ݽô�.
time.sleep(5)
BOT.save_screenshot()

# ����� Ȯ���ϱ� ���� 10������ ����մϴ�.
time.sleep(10)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
