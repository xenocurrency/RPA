# 업무자동화 예제 연습 목적
# 목표
# 1) 한 폴더 속 모든(1천개) txt 데이터 파일들을 하나의 xlsx로 저장하고 싶다.

# 작업 쪼개기
# 1) 폴더 속 1천개의 txt 데이터 파일들을 불러온다
# 2) <:> 기호를 기준으로 데이터와 헤더를 구분한다. 
# 3) 헤더는 최초 1회 저장하고, 데이터는 1천개를 순차적으로 저장한다
# 4) 헤더, 데이터 리스트에 < ,> 를 집어넣는다
# 5) csv 파일 완성. xlsx로 변환한다

# 해결방법 생각
# 1) 작업쪼개기 1)~4)는 기본명령어, 작업쪼개기 5)는 구글링 -> pyexcel로 처리


import time
import os
import pyexcel as px
import sys

#작업 시작 메세지 출력
print("Process Start")

#시작 시간을 기록
start_time = time.time()

#하나로 합칠 파일들이 저장되는 폴더 이름을 시스템으로부터 입력 받음(매번 바뀔 변수는 시스템으로부터 입력받아서 범용성을 키움)
directory = sys.argv[1]

#임시생성 결과물 파일의 이름을 정의 (종종 수정하는 경우 코드 상단에 배치함)
temp_file_name = "temp.csv"

#최종 결과물 파일 이름을 정의 (종종 수정하는 경우 코드 상단에 배치함)
outfile_name = "merged_ID.xlsx"

#임시생성 결과물 파일을 utf-8 인코팅타입으로 생성합니다.
temp_file = open(temp_file_name, 'w', encoding="utf-8")

# .txt원본 파일들이 있는 폴더에서 파일명 목록을 불러옵니다
# 불러온 파일 목록을 리스트로 생성합니다
input_files = os.listdir(directory)

#엑셀용 헤더를 리스트로 정의함
headers = []
outfile_has_header = False

# 폴더의 내용물을 하나하나 합치는 작업 수행
# input_files에 저장된 파일이름을 한번에 하나씩 불러옴
for filename in input_files:
    #텍스트 파일이 아닌 경우 걸러냄
    if ".txt" not in filename:
        continue

    #텍스트 파일이 맞다면, 파일을 읽어옴
    file = open(directory + "/" + filename)

    #파일을 저장할 리스트를 정의함
    contents = []

    #한 줄씩 읽으며 아래 작업 수행
    for line in file:
        # <:> 으로 데이터와 헤더를 구분하여 데이터만 contents에 입력합니다. 공백은 제거합니다.
        if ":" in line:
            splits = line.split(":")
            contents.append(splits[-1].strip())

        #헤더가 입력되지 않았다면 헤더를 입력합니다. 공백은 제거합니다.
        if len(contents) > len(headers):
            headers.append(splits[0].strip())

    #header 리스트 변수 사이에 <,>를 추가한 뒤, temp_file에 기록합니다
    #최초 1회만 임시생성 결과물 파일에 기록합니다
    if not outfile_has_header:
        header = ", ".join(headers)
        temp_file.write(header)
        outfile_has_header = True

    #contents 리스트의 변수 사이에 <,>를 추가한 뒤, 임시생성 결과물 파일에 입력합니다
    new_line = ", ".join(contents)
    temp_file.write("\n" + new_line)

    #파일을 닫음
    file.close()

#임시 생성 결과물 파일을 닫음
temp_file.close()

#임시 생성 결과물(csv파일)을 결과물(xlsx파일)로 변환. pyexcel 라이브러리의 기능 차용
px.merge_all_to_a_book([temp_file_name], outfile_name)

#불필요해진 임시 생성 결과물 파일을 삭제
os.remove(temp_file_name)

#작업완료 메세지 출력
print("Process Done.")

#종료시간 기록하고, 작업수행시간 출력
end_time = time.time()
print("Computing Time : " + str(end_time - start_time) + "seconds")

