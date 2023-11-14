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


#���� �޼��� ���
print("Process Start")

#���� �ð� ���
start_time = time.time()

image_filename = sys.argv[1]

#�̹����� ������ ���� ����. ���ٸ� ����.
out_dir = "augmentation"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

#���� �̹��� �ҷ�����
image = Image.open(image_filename)
Xdim, Ydim = image.size

#ī��Ʈ ����
COUNT = 1

#���� �̹����� ���ϸ� ����. 00001.png
temp_new_file_name = "%05d.png" %COUNT
#���ϸ� ������ ������ ���� ������ ���� ī��Ʈ�� +1��
COUNT += 1

#�����̹����� ����. 2�� 0��
image.save(out_dir + "/" + temp_new_file_name)
image.close()

#���ϸ�� ����(1���� ����Ʈ)
FILELIST = [temp_new_file_name]

#���� �� �̹��� ��θ� �¿��Ī��. 2�� 1��
#for���� i ������ FILELIST�� ���ϸ��� ������ŭ int�������� ���� ��ȯ��
#for���� len�� ������ ����Ʈ �� ���� ������ int������ ���
#for ���� range�� ������ int 0���� range()�� int������ ���������� �ҷ��� i�� �־���. ��������? i�� 180�� �� ������
for i in range(len(FILELIST)):
    # ���ϸ�� �� �̹��� �ҷ�����. i�� int�̹Ƿ� ����Ʈ�� i��° str ���ϸ��� �ҷ���
    image = Image.open(out_dir + "/" + FILELIST[i])
    #��ȯ�̹����� ���ϸ� �����
    new_temp_name = "%05d.png" %COUNT
    #���� ������������� ī��Ʈ +1.���� ��ȯ�̹����� ���ϸ� ������ ���� ī��Ʈ +1��
    COUNT += 1
    #�̹��� �¿����
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    #�̹��� ����
    image.save(out_dir + "/" + new_temp_name)
    #�̹����ݱ�
    image.close()
    #��ȯ�� ���ϸ��� FILELIST�� �߰�
    FILELIST.append(new_temp_name)

#���� �� �̹��� ��θ� ���ϴ�Ī��. 2�� 2��
#for���� i ������ FILELIST�� ���ϸ��� ������ŭ int�������� ���� ��ȯ��
#for���� len�� ������ ����Ʈ �� ���� ������ int������ ���
#for ���� range�� ������ int 0���� range()�� int������ ���������� �ҷ��� i�� �־���. ��������? i�� 180�� �� ������
for i in range(len(FILELIST)):
    # ���ϸ�� �� �̹��� �ҷ�����. i�� int�̹Ƿ� ����Ʈ�� i��° str ���ϸ��� �ҷ���
    image = Image.open(out_dir + "/" + FILELIST[i])
    #��ȯ�̹����� ���ϸ� �����
    new_temp_name = "%05d.png" %COUNT
    #���� ������������� ī��Ʈ +1.���� ��ȯ�̹����� ���ϸ� ������ ���� ī��Ʈ +1��
    COUNT += 1
    #�̹��� �¿����
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    #�̹��� ����
    image.save(out_dir + "/" + new_temp_name)
    #�̹����ݱ�
    image.close()
    #��ȯ�� ���ϸ��� FILELIST�� �߰�
    FILELIST.append(new_temp_name)

#���� �� �̹��� ��θ� �����ȯ��. 2�� 3��
#for���� i ������ FILELIST��� ����Ʈ �� ���ϸ��� ������ŭ int�������� ���� ��ȯ��
#for���� len�� ������ ����Ʈ �� ���� ������ int������ ���
#for ���� range�� ������ int 0���� range()�� int������ ���������� �ҷ��� i�� �־���. ��������? i�� 180�� �� ������
for i in range(len(FILELIST)):
    #���ϸ�� �� �̹��� �ҷ�����. i�� int�̹Ƿ� ����Ʈ�� i��° str ���ϸ��� �ҷ���
    image = Image.open(out_dir + "/" + FILELIST[i])
    #��ȯ�̹����� ���ϸ� �����
    new_temp_name = "%05d.png" %COUNT
    #���� ������������� ī��Ʈ +1.���� ��ȯ�̹����� ���ϸ� ������ ���� ī��Ʈ +1��
    COUNT += 1
    #�̹��� �¿����
    image = image.convert('1')
    #�̹��� ����
    image.save(out_dir + "/" + new_temp_name)
    #�̹����ݱ�
    image.close()
    #��ȯ�� ���ϸ��� FILELIST�� �߰�
    FILELIST.append(new_temp_name)

#���� �� �̹����� 1000���� ��?����, ���� �� ��� �̹����� ������ 1���� ��ȯ
#1�� for���� el ������ FILELIST�� ���ϸ��� ������ŭ FILELIST �� ���ϸ����� str ���� ��ȯ��
for el in FILELIST:
    #for ���� range�� ������ int 0���� range()�� int������ ���������� �ҷ��� i�� �־���. ��������? i�� 180�� �� ������
    for i in range(180):
        #������� 1000�������� �ڵ� ����
        if COUNT > 1000:
            break
        #���ϸ�� �� �̹��� �ҷ�����. el�� str�̹Ƿ� ���� �Է� ����
        image = Image.open(out_dir + "/" + el)
        #��ȯ�̹����� ���ϸ� �����
        new_temp_name = "%05d.png" %COUNT
        #���� ������������� ī��Ʈ +1.���� ��ȯ�̹����� ���ϸ� ������ ���� ī��Ʈ +1��
        COUNT += 1
        #�̹��� �¿����
        image = image.rotate(i+1)
        #��Ȥ �̹��� ����� �ٲ�ٰ� �ϴ� ������ �缳���մϴ�
        image = image.resize((Xdim, Ydim))
        #�̹��� ����
        image.save(out_dir + "/" + new_temp_name)
        #�̹����ݱ�
        image.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
