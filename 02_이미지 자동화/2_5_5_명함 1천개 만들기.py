
import os
import sys
import time

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

#시작 메세지 출력
print("Process Start")

#시작 시간 기록
start_time = time.time()

#파일 읽어올 경로를 명령어에서 받음
personal_IDs = sys.argv[1]

#로고 파일명을 명령어에서 받음
logo_filename = sys.argv[2]

#주소와 홈페이지주소는 긴 텍스트이므로 직접 입력받음
location = "울릉도 동남쪽 뱃길따라 200리"
url = "https://latte_is_horse.abc"

#명함을 저장할 폴더 지정. 없다면 생성.
out_dir = "namecard"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

#로고 이미지를 불러옵니다
logo = Image.open(logo_filename)
#로고 사이즈를 불러옵니다
logo_x, logo_y = logo.size

#명함 사이즈를 지정
Xdim = 1039
Ydim = 697

#명함 사이즈에 맞게 로고 사이즈를 조정
new_logo_Y = int(Ydim * 0.4)
new_logo_X = int(logo_x * (new_logo_Y / Ydim))
#조정된 사이즈에 맞게 로고 이미지를 조정
resized_logo = logo.resize((new_logo_X, new_logo_Y))

#로고를 닫음(변형이 일어날수있으니 원본은 가급적 빨리 닫기)
logo.close()

#시스템에서 지정된 파일(.CSV)을 불러옵니다
IDs = open(personal_IDs)

#헤더만 불러옵니다. 아래에서 헤더 정보를 제외하고 처리하기 위함으로 추정됨
header = IDs.readline()

#명함 이미지를 생성
image = Image.new("RGBA", (Xdim, Ydim), "white")

#명함 이미지에 조정된 크기의 로고를 삽입
image.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.1)))

#조정된 로고를 닫음
resized_logo.close()

#이름용, 작은 글씨용, 중간 글씨용, 3가지 폰트를 정의함. 모두 굴림체
nameFont = ImageFont.truetype("font/gulim.ttc", 70)
smallFont = ImageFont.truetype("font/gulim.ttc", 40)
infoFont = ImageFont.truetype("font/gulim.ttc", 50)

#url 입력을 위해 위치정보 지정.
x_offset = int(Xdim * 0.95 - smallFont.getsize(url)[0])
y_offset = int(Ydim * 0.05)
#url을 명함이미지에 입력. 공통정보이므로 for문 밖에 위치
ImageDraw.Draw(image).text(xy=(x_offset, y_offset), text=url, font=smallFont, fill="black")

#주소 입력을 위해 위치정보 지정
x_offset = int(Xdim * 0.95 - smallFont.getsize(location)[0])
y_offset = int(Ydim * 0.95 - smallFont.getsize(location)[1])
#주소를 명함이미지에 입력. 공통정보이므로 for문 밖에 위치
ImageDraw.Draw(image).text(xy=(x_offset, y_offset), text=location, font=smallFont, fill="black")


#개인정보를 한 줄씩 불러옴
for line in IDs:
    #공백제거 후 ","별로 나눔
    splt = line.strip().split(", ")

    #이름/이메일/부서/전화번호를 추출 (str 타입)
    name = splt[0]
    e_mail =  splt[2]
    division = splt[3]
    telephone = splt[4]

    #명함 이미지를 복제.(원본에 글자들이 덮어쓰기 되면 안되므로)
    namecard = image.copy()

    #이름 사이에 공백 생성
    temp_name = ""
    for el in name:
        temp_name += el + " "
    name = temp_name[:-1]

    #이름 정보 위치 지정 후 복제된 명함 이미지에 붙여넣음
    x_offset = int(Xdim * 0.95 - nameFont.getsize(name)[0])
    y_offset = int(Ydim * 0.4 - nameFont.getsize(name)[1])
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    # 부서 정보 위치 지정 후 복제된 명함 이미지에 붙여넣음
    x_offset = int(Xdim * 0.95 - infoFont.getsize(division)[0])
    y_offset = int(Ydim * 0.5 - infoFont.getsize(division)[1])
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=division, font=infoFont, fill="black")

    # 전화번호 정보 위치 지정 후 복제된 명함 이미지에 붙여넣음
    x_offset = int(Xdim * 0.95 - infoFont.getsize(telephone)[0])
    y_offset = int(Ydim * 0.65 - infoFont.getsize(telephone)[1])
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=telephone, font=infoFont, fill="black")

    # 이메일 정보 위치 지정 후 복제된 명함 이미지에 붙여넣음
    x_offset = int(Xdim * 0.95 - infoFont.getsize(e_mail)[0])
    y_offset = int(Ydim * 0.75 - infoFont.getsize(e_mail)[1])
    ImageDraw.Draw(namecard).text(xy=(x_offset, y_offset), text=e_mail, font=infoFont, fill="black")

    # 복제된 명함 이미지를 저장함
    namecard.save(out_dir + "/" + division + "_" + name + "_" + telephone + ".png")

    # 복제된 명함 이미지를 닫음
    namecard.close()

#명함 이미지를 닫음. for 문 중간에서 복제해야 하므로 for 문 종료 후 닫음.
image.close()

# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")