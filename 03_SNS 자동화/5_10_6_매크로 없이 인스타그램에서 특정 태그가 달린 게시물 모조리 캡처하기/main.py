#-*-coding:euc-kr


import sys
import time
import insta_bot_capture as ib
import os


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[1]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[2]

# �˻��� �±׸� �Է¹޽��ϴ�.
tag = sys.argv[3]

# ������� ������ ���� �̸��� �Է¹޽��ϴ�.
directory = sys.argv[4]

# ������� ������ ������ �����մϴ�.
if directory not in os.listdir():
    os.mkdir(directory)

# �ݺ� ȸ���� �Է¹޽��ϴ�.
NUMBER = int(sys.argv[5].strip())

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = ib.CaptureBot()

# �ν�Ÿ�׷� �α����� �մϴ�.
BOT.login(id, ps)

# �۾��� �����մϴ�.
BOT.insta_jungdok(tag, directory, NUMBER)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
