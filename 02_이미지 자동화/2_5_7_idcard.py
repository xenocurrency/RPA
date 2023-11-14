#-*-coding:euc-kr

import time
import os
import sys

try:
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'pillow'])
    try:
        from PIL import Image
        from PIL import ImageFont
        from PIL import ImageDraw
    except ModuleNotFoundError:
        time.sleep(2)
        from PIL import Image
        from PIL import ImageFont
        from PIL import ImageDraw

# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

#사원 증명사진 저장 폴더명 지정
member_photo = sys.argv[1]

#사원 정보가 있는 파일명 지정(CSV 파일이어야함)
personal_IDs = sys.argv[2]

#로고 파일명 지정
logo_filename = sys.argv[3]

#템플릿 파일명 지정
templete_filename = sys.argv[4]

#템플릿 파일이 있다면 템플릿 파일을 열고, 템플릿 파일이 없다면 새로 생성함
try:
    templete = Image.open(templete_filename)
except:
    templete = Image.new("RGBA", (800,1268), 'white')

#템플릿 사이즈 불러오기
Xdim, Ydim = templete.size

#url 입력
url = "https://abcdefg.hij"

#결과물을 저장할 폴더 생성
out_dir = "idcards"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

#로고 불러오고 사이즈 측정
logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

#증명사진 목록 불러옴. 이미지 확장자 외 파일을 거르기 위해 PHOTOS 생성
photos = os.listdir(member_photo)
PHOTOS = []
for el in photos:
    if el.strip().split(".")[-1] not in "JPG jpg PNG png BMP bmp JPEG jpeg":
        continue
    PHOTOS.append(el)

#제작 명함 개수 저장하는 카운터
COUNT = 0

#로고의 수정할 크기를 지정. 사원증 너비의 20%로 너비 조정. 높이는 기존대비 너비 조정된 만큼 비례해서 조정
new_logo_x = int(Xdim * 0.2)
new_logo_y = int(logo_y * (new_logo_x / logo_x))

#로고를 크기 수정합니다
resized_logo = logo.resize((new_logo_x, new_logo_y))

#원본 로고를 닫음
logo.close()

#인적사항 불러오기. csv파일을 열기위해 open()사용
IDs = open(personal_IDs)

#헤더를 뽑아냄
header = IDs.readline()

#템플릿(빈 사원증)에 수정된 로고를 삽입
templete.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.95 - new_logo_y)))

#수정된 로고를 닫습니다
resized_logo.close()

#이름용, 작은 글씨용, 중간 글씨용, 3가지 폰트를 정의함. 모두 굴림체
nameFont = ImageFont.truetype("font/gulim.ttc", 70)
smallFont = ImageFont.truetype("font/gulim.ttc", 40)
infoFont = ImageFont.truetype("font/gulim.ttc", 50)

#사원증 최상단 url 입력
x_offset = int(Xdim * 0.95 - smallFont.getsize(url)[0])
y_offset = int(Ydim * 0.02)
ImageDraw.Draw(templete).text(xy=(x_offset, y_offset), text=url, font=smallFont, fill="black")


#인적정보 별로 반복문 수행.
#인적정보의 순서와 증명사진 순서는 반드시 동일해야 합니다
for line in IDs:
    # CSV 니까 콤마 단위로 쪼갤수 있습니다
    splt = line.strip().split(", ")

    #사원증에 들어갈 정보만 추출합니다. (이름과 부서명)
    name = splt[0]
    division = splt[3]

    #사원증 템플릿을 복제
    idcard = templete.copy()

    #삽입할 사진을 불러옴
    photo_for_id = Image.open(member_photo + "/" + PHOTOS[COUNT])

    #사진 사이즈 조정. 너비는 사원증의 50%, 높이는 너비의 4/3(증명사진 비율임)
    photo_for_id = photo_for_id.resize((int(Xdim/2), int((Xdim/2) * (4/3))))

    #사진을 사원증 정중앙에 삽입
    idcard.paste(photo_for_id, (int(Xdim / 4), int(Ydim/2 - Xdim * 0.5 * (4/3) /2)))

    #이름 사이에 공백 추가
    temp_name = ""
    #for 문의 in 다음에 str을 넣으면 str 값 하나씩 el에 입력하여 반복하나보다
    for el in name:
        temp_name += el + " "
    #마지막 공백은 제외하고 이름 저장
    name = temp_name[:-1]

    #명함에 이름을 삽입. 사원증 가운데 정렬, 상하여백 20%
    x_offset = int(Xdim * 0.5 - nameFont.getsize(name)[0]/2)
    y_offset = int(Ydim * 0.8 - nameFont.getsize(name)[1])
    ImageDraw.Draw(idcard).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    #이름 아래에 부서명을 삽입. 사원증 가운데 정렬, 상하여백 15%
    x_offset = int(Xdim * 0.5 - infoFont.getsize(division)[0]/2)
    y_offset = int(Ydim * 0.85 - infoFont.getsize(division)[1])
    ImageDraw.Draw(idcard).text(xy=(x_offset, y_offset), text=division, font=infoFont, fill="black")

    #사원증 파일로 저장
    idcard.save(out_dir + "/" + PHOTOS[COUNT])

    #사원증 데이터 닫음
    idcard.close()

    #카운트 +1
    COUNT += 1

#템플릿도 더이상 안쓰니 닫음
templete.close()

# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")



