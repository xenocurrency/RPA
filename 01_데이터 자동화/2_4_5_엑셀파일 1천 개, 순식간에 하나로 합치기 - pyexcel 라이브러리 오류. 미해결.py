#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.12.
"""
import time
import os
import sys
import pyexcel as px

# �۾� ���� �޽����� ����մϴ�.
print("Process Start")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# �ϳ��� ��ĥ ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[1]

# ����� ������ �̸��� �����մϴ�.
outfile_name = "merged_ID_xlsx.xlsx"

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

CONTENTS = []

# ������ ���빰�� �ϳ��ϳ� �ҷ��� ��ġ�� �۾��� �����մϴ�.
# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ csv ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".xlsx" not in filename:
        continue

    # xlsx ������ �´ٸ�, ������ ����Ʈ���·� �о�ɴϴ�.
    data_array = px.get_array(file_name=directory + "/" + filename)

    # ����� �и��մϴ�.
    header = data_array[0]
    data_array = data_array[1:]

    # ����� ���빰�� ����1ȸ�� �Է��մϴ�.
    if len(CONTENTS) == 0:
        CONTENTS.append(header)

    CONTENTS += data_array

px.save_as(array=CONTENTS, dest_file_name=outfile_name)


# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
