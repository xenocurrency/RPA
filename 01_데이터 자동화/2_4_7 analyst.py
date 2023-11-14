#-*-coding:euc-kr
import time
import os
import sys
try:
    import pyexcel as px
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'pyexcel'])
    pip.main(['install', 'pyexcel-xlsx'])
    try:
        import pyexcel as px
    except ModuleNotFoundError:
        time.sleep(2)
        import pyexcel as px

print("Process Start")

start_time = time.time()

directory = sys.argv[1]

report_filename = sys.argv[2]

input_files = os.listdir(directory)

#Create dictionary
HEADERS = {}

#filename �� input_files��ŭ �ݺ�
for filename in input_files:
    if ".xlsx" not in filename:
        continue

    #���������� ����Ʈ���·� �����Ѵ�
    file = px.get_array(file_name=directory + "/" + filename)

    #����Ʈ ������ �������� 1��° ��. ��, ��������� ���ڿ��� �����Ѵ�
    header = str(file[0])

    #��ųʸ��� ��������� �ִ��� Ȯ��
    if header in HEADERS:
        #�ִٸ� ���� 1����
        HEADERS[header] += 1
    #���ٸ� ���� 1�� ����
    else:
        HEADERS[header]  = 1

#����� ����Ʈ �ۼ� ���� ��Ʈ���� ����
REPORT = ""

#����Ʈ�� ���빰�� �ڵ����� �ۼ�??
for key in HEADERS:
    REPORT += "Header : " + key + "\n"
    REPORT += "Count : " + str(HEADERS[key]) + "\n\n"

#����Ʈ ���
print(REPORT)

#����Ʈ�� ���� �� ����
report_file = open(report_filename, 'w')
report_file.write(REPORT)
report_file.close()

print("Process Done")

end_time = time.time()
print("Processing Time : " + str(end_time - start_time) + "seconds.")