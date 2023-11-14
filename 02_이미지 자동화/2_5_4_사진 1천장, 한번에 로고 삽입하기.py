#필요 라이브러리 읽어오기, 이미지 작업용 pillow의 Image를 import함
import os
import sys
import time

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

#파일 읽어올 경로를 명령어에서 받음
directory = sys.argv[1]

#로고 파일명을 명령어에서 받음
logo_filename = sys.argv[2]

#로고가 포함된 이미지를 저장할 폴더 지정. 없다면 생성.
out_dir = "images_with_logo"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

#이미지 파일을 불러옴
input_files = os.listdir(directory)
print(input_files)
print(type(input_files))

#로고 이미지 사이즈 측정
logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

#파일명을 순차적으로 불러옴
for filename in input_files:
    #이미지 확장자가 아닌 파일은 제외함
    exp = filename.strip().split('.')[-1]
    if exp not in ("JPG jpg JPEG jpeg PNG png BMP bmp"):
        continue

    #이미지를 불러옴
    image = Image.open(directory + "/" + filename)
    #이미지의 크기를 알아냅니다
    X_dim, Y_dim = image.size

    #로고 파일을 이미지 사이즈에 맞게 조정합니다.
    # 먼저 x,y축 중 긴 축에 해당하는 축을 1/5 사이즈로 조정하여 로고 사이즈로 정합니다
    # 짧은 축은 긴축의 줄어든 비율만큼 줄입니다
    # x축이 길다면 아래처럼 조정합니다
    if logo_x / X_dim > logo_y / Y_dim:
        new_logo_x = int(X_dim / 5)
        new_logo_y = int(logo_y * (new_logo_x / logo_x))
    #만약 y축이 길다면 아래처럼 조정합니다
    else:
        new_logo_y = int(Y_dim / 5)
        new_logo_x = int(logo_x * (new_logo_y / logo_y))

    #로고 이미지 크기를 조정합니다
    resized_logo = logo.resize((new_logo_x,new_logo_y))

    #로고를 입력받은 사진에 붙여넣습니다. 투명도 지정하여 붙여넣습니다
    image.paste(resized_logo, (int(X_dim/50), int(Y_dim/50)), resized_logo)

    #변경된 이미지를 저장합니다
    image.save(out_dir + "/" + filename)

    #이미지를 닫습니다
    image.close()

print("Process Done")

end_time = time.time()
print("Processing Time : " + str(end_time - start_time) + "seconds")










