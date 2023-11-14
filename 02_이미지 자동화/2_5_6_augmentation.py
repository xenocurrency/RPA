#-*-coding:euc-kr

import time
import os
import sys

try:
    from PIL import Image
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'pillow'])
    try:
        from PIL import Image
    except ModuleNotFoundError:
        time.sleep(2)
        from PIL import Image


#시작 메세지 출력
print("Process Start")

#시작 시간 기록
start_time = time.time()

image_filename = sys.argv[1]

#이미지를 저장할 폴더 지정. 없다면 생성.
out_dir = "augmentation"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

#샘플 이미지 불러오기
image = Image.open(image_filename)
Xdim, Ydim = image.size

#카운트 생성
COUNT = 1

#원본 이미지용 파일명 생성. 00001.png
temp_new_file_name = "%05d.png" %COUNT
#파일명 생성을 했으니 다음 파일을 위해 카운트를 +1함
COUNT += 1

#원본이미지를 저장. 2의 0승
image.save(out_dir + "/" + temp_new_file_name)
image.close()

#파일목록 생성(1차원 리스트)
FILELIST = [temp_new_file_name]

#폴더 내 이미지 모두를 좌우대칭함. 2의 1승
#for문은 i 변수가 FILELIST내 파일명의 개수만큼 int형식으로 순차 변환함
#for문에 len을 넣으면 리스트 속 값의 개수를 int값으로 출력
#for 문에 range를 넣으면 int 0부터 range()속 int값까지 순차적으로 불러와 i에 넣어줌. 언제까지? i가 180이 될 때까지
for i in range(len(FILELIST)):
    # 파일목록 속 이미지 불러오기. i가 int이므로 리스트의 i번째 str 파일명을 불러옴
    image = Image.open(out_dir + "/" + FILELIST[i])
    #변환이미지용 파일명 만들기
    new_temp_name = "%05d.png" %COUNT
    #사진 만들어질때마다 카운트 +1.다음 변환이미지의 파일명 지정을 위해 카운트 +1함
    COUNT += 1
    #이미지 좌우반전
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    #이미지 저장
    image.save(out_dir + "/" + new_temp_name)
    #이미지닫기
    image.close()
    #변환한 파일명을 FILELIST에 추가
    FILELIST.append(new_temp_name)

#폴더 내 이미지 모두를 상하대칭함. 2의 2승
#for문은 i 변수가 FILELIST내 파일명의 개수만큼 int형식으로 순차 변환함
#for문에 len을 넣으면 리스트 속 값의 개수를 int값으로 출력
#for 문에 range를 넣으면 int 0부터 range()속 int값까지 순차적으로 불러와 i에 넣어줌. 언제까지? i가 180이 될 때까지
for i in range(len(FILELIST)):
    # 파일목록 속 이미지 불러오기. i가 int이므로 리스트의 i번째 str 파일명을 불러옴
    image = Image.open(out_dir + "/" + FILELIST[i])
    #변환이미지용 파일명 만들기
    new_temp_name = "%05d.png" %COUNT
    #사진 만들어질때마다 카운트 +1.다음 변환이미지의 파일명 지정을 위해 카운트 +1함
    COUNT += 1
    #이미지 좌우반전
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    #이미지 저장
    image.save(out_dir + "/" + new_temp_name)
    #이미지닫기
    image.close()
    #변환한 파일명을 FILELIST에 추가
    FILELIST.append(new_temp_name)

#폴더 내 이미지 모두를 흑백전환함. 2의 3승
#for문은 i 변수가 FILELIST라는 리스트 내 파일명의 개수만큼 int형식으로 순차 변환함
#for문에 len을 넣으면 리스트 속 값의 개수를 int값으로 출력
#for 문에 range를 넣으면 int 0부터 range()속 int값까지 순차적으로 불러와 i에 넣어줌. 언제까지? i가 180이 될 때까지
for i in range(len(FILELIST)):
    #파일목록 속 이미지 불러오기. i가 int이므로 리스트의 i번째 str 파일명을 불러옴
    image = Image.open(out_dir + "/" + FILELIST[i])
    #변환이미지용 파일명 만들기
    new_temp_name = "%05d.png" %COUNT
    #사진 만들어질때마다 카운트 +1.다음 변환이미지의 파일명 지정을 위해 카운트 +1함
    COUNT += 1
    #이미지 좌우반전
    image = image.convert('1')
    #이미지 저장
    image.save(out_dir + "/" + new_temp_name)
    #이미지닫기
    image.close()
    #변환한 파일명을 FILELIST에 추가
    FILELIST.append(new_temp_name)

#폴더 내 이미지가 1000장이 될?까지, 폴더 내 모든 이미지를 각도를 1도씩 변환
#1차 for문은 el 변수가 FILELIST내 파일명의 개수만큼 FILELIST 내 파일명으로 str 순차 변환함
for el in FILELIST:
    #for 문에 range를 넣으면 int 0부터 range()속 int값까지 순차적으로 불러와 i에 넣어줌. 언제까지? i가 180이 될 때까지
    for i in range(180):
        #결과물이 1000개넘으면 코드 종료
        if COUNT > 1000:
            break
        #파일목록 속 이미지 불러오기. el이 str이므로 직접 입력 가능
        image = Image.open(out_dir + "/" + el)
        #변환이미지용 파일명 만들기
        new_temp_name = "%05d.png" %COUNT
        #사진 만들어질때마다 카운트 +1.다음 변환이미지의 파일명 지정을 위해 카운트 +1함
        COUNT += 1
        #이미지 좌우반전
        image = image.rotate(i+1)
        #간혹 이미지 사이즈가 바뀐다고 하니 사이즈 재설정합니다
        image = image.resize((Xdim, Ydim))
        #이미지 저장
        image.save(out_dir + "/" + new_temp_name)
        #이미지닫기
        image.close()

# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
