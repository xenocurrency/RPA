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

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

#��� ������� ���� ������ ����
member_photo = sys.argv[1]

#��� ������ �ִ� ���ϸ� ����(CSV �����̾����)
personal_IDs = sys.argv[2]

#�ΰ� ���ϸ� ����
logo_filename = sys.argv[3]

#���ø� ���ϸ� ����
templete_filename = sys.argv[4]

#���ø� ������ �ִٸ� ���ø� ������ ����, ���ø� ������ ���ٸ� ���� ������
try:
    templete = Image.open(templete_filename)
except:
    templete = Image.new("RGBA", (800,1268), 'white')

#���ø� ������ �ҷ�����
Xdim, Ydim = templete.size

#url �Է�
url = "https://abcdefg.hij"

#������� ������ ���� ����
out_dir = "idcards"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

#�ΰ� �ҷ����� ������ ����
logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

#������� ��� �ҷ���. �̹��� Ȯ���� �� ������ �Ÿ��� ���� PHOTOS ����
photos = os.listdir(member_photo)
PHOTOS = []
for el in photos:
    if el.strip().split(".")[-1] not in "JPG jpg PNG png BMP bmp JPEG jpeg":
        continue
    PHOTOS.append(el)

#���� ���� ���� �����ϴ� ī����
COUNT = 0

#�ΰ��� ������ ũ�⸦ ����. ����� �ʺ��� 20%�� �ʺ� ����. ���̴� ������� �ʺ� ������ ��ŭ ����ؼ� ����
new_logo_x = int(Xdim * 0.2)
new_logo_y = int(logo_y * (new_logo_x / logo_x))

#�ΰ� ũ�� �����մϴ�
resized_logo = logo.resize((new_logo_x, new_logo_y))

#���� �ΰ� ����
logo.close()

#�������� �ҷ�����. csv������ �������� open()���
IDs = open(personal_IDs)

#����� �̾Ƴ�
header = IDs.readline()

#���ø�(�� �����)�� ������ �ΰ� ����
templete.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.95 - new_logo_y)))

#������ �ΰ� �ݽ��ϴ�
resized_logo.close()

#�̸���, ���� �۾���, �߰� �۾���, 3���� ��Ʈ�� ������. ��� ����ü
nameFont = ImageFont.truetype("font/gulim.ttc", 70)
smallFont = ImageFont.truetype("font/gulim.ttc", 40)
infoFont = ImageFont.truetype("font/gulim.ttc", 50)

#����� �ֻ�� url �Է�
x_offset = int(Xdim * 0.95 - smallFont.getsize(url)[0])
y_offset = int(Ydim * 0.02)
ImageDraw.Draw(templete).text(xy=(x_offset, y_offset), text=url, font=smallFont, fill="black")


#�������� ���� �ݺ��� ����.
#���������� ������ ������� ������ �ݵ�� �����ؾ� �մϴ�
for line in IDs:
    # CSV �ϱ� �޸� ������ �ɰ��� �ֽ��ϴ�
    splt = line.strip().split(", ")

    #������� �� ������ �����մϴ�. (�̸��� �μ���)
    name = splt[0]
    division = splt[3]

    #����� ���ø��� ����
    idcard = templete.copy()

    #������ ������ �ҷ���
    photo_for_id = Image.open(member_photo + "/" + PHOTOS[COUNT])

    #���� ������ ����. �ʺ�� ������� 50%, ���̴� �ʺ��� 4/3(������� ������)
    photo_for_id = photo_for_id.resize((int(Xdim/2), int((Xdim/2) * (4/3))))

    #������ ����� ���߾ӿ� ����
    idcard.paste(photo_for_id, (int(Xdim / 4), int(Ydim/2 - Xdim * 0.5 * (4/3) /2)))

    #�̸� ���̿� ���� �߰�
    temp_name = ""
    #for ���� in ������ str�� ������ str �� �ϳ��� el�� �Է��Ͽ� �ݺ��ϳ�����
    for el in name:
        temp_name += el + " "
    #������ ������ �����ϰ� �̸� ����
    name = temp_name[:-1]

    #���Կ� �̸��� ����. ����� ��� ����, ���Ͽ��� 20%
    x_offset = int(Xdim * 0.5 - nameFont.getsize(name)[0]/2)
    y_offset = int(Ydim * 0.8 - nameFont.getsize(name)[1])
    ImageDraw.Draw(idcard).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    #�̸� �Ʒ��� �μ����� ����. ����� ��� ����, ���Ͽ��� 15%
    x_offset = int(Xdim * 0.5 - infoFont.getsize(division)[0]/2)
    y_offset = int(Ydim * 0.85 - infoFont.getsize(division)[1])
    ImageDraw.Draw(idcard).text(xy=(x_offset, y_offset), text=division, font=infoFont, fill="black")

    #����� ���Ϸ� ����
    idcard.save(out_dir + "/" + PHOTOS[COUNT])

    #����� ������ ����
    idcard.close()

    #ī��Ʈ +1
    COUNT += 1

#���ø��� ���̻� �Ⱦ��� ����
templete.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")



