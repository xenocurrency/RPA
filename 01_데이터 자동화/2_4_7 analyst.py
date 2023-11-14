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

#filename 을 input_files만큼 반복
for filename in input_files:
    if ".xlsx" not in filename:
        continue

    #엑셀파일을 리스트형태로 저장한다
    file = px.get_array(file_name=directory + "/" + filename)

    #리스트 형태의 데이터의 1번째 열. 즉, 헤더정보를 문자열로 저장한다
    header = str(file[0])

    #딕셔너리에 헤더정보가 있는지 확인
    if header in HEADERS:
        #있다면 값을 1증가
        HEADERS[header] += 1
    #없다면 값은 1로 지정
    else:
        HEADERS[header]  = 1

#결과물 리포트 작성 위한 스트링을 생성
REPORT = ""

#리포트에 내용물을 자동으로 작성??
for key in HEADERS:
    REPORT += "Header : " + key + "\n"
    REPORT += "Count : " + str(HEADERS[key]) + "\n\n"

#리포트 출력
print(REPORT)

#리포트를 파일 내 저장
report_file = open(report_filename, 'w')
report_file.write(REPORT)
report_file.close()

print("Process Done")

end_time = time.time()
print("Processing Time : " + str(end_time - start_time) + "seconds.")