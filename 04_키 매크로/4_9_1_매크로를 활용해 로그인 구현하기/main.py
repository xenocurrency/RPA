#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import login_macro as lm


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# �α����� ����Ʈ�� �Է¹޽��ϴ�.
site = sys.argv[1]

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[2]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[3]

# ũ�ѷ��� �ҷ��ɴϴ�.
crawler = lm.LoginBot(site)

# �α����� �õ��մϴ�.
crawler.login(id, ps)

# �α��ο� ���������� ��ũ�����̳� �� �� ����ݽô�.
crawler.save_screenshot()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
