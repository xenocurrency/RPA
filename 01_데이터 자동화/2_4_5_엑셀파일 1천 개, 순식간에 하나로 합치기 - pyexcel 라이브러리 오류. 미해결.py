#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6개월 치 업무를 하루 만에 끝내는 업무 자동화
Last Modification : 2020.02.12.
"""
import time
import os
import sys
import pyexcel as px

# 작업 시작 메시지를 출력합니다.
print("Process Start")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 하나로 합칠 파일들이 저장된 폴더 이름을 시스템으로부터 입력받습니다.
directory = sys.argv[1]

# 결과물 파일의 이름을 정의합니다.
outfile_name = "merged_ID_xlsx.xlsx"

# 폴더의 내용물을 열람해 목록을 생성합니다.
input_files = os.listdir(directory)

CONTENTS = []

# 폴더의 내용물을 하나하나 불러와 합치는 작업을 수행합니다.
# input_files에 저장된 파일 이름을 한 번에 하나씩 불러옵니다.
for filename in input_files:
    # 간혹 csv 파일이 아닌 파일이 섞여있을 수 있습니다. 이걸 걸러냅니다.
    if ".xlsx" not in filename:
        continue

    # xlsx 파일이 맞다면, 파일을 리스트형태로 읽어옵니다.
    data_array = px.get_array(file_name=directory + "/" + filename)

    # 헤더를 분리합니다.
    header = data_array[0]
    data_array = data_array[1:]

    # 헤더의 내용물을 최초1회만 입력합니다.
    if len(CONTENTS) == 0:
        CONTENTS.append(header)

    CONTENTS += data_array

px.save_as(array=CONTENTS, dest_file_name=outfile_name)


# 작업 종료 메시지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
