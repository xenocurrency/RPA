#-*-coding:utf-8
"""
programmer : Juhyun Kim
GitHub : https://github.com/xenocurrency
Last Modification : 2023.12.02.
"""

import sys
import time
import websites_bot_login as wb


print("Process Start.")
start_time = time.time()

websites_info_filename = sys.argv[1]        # 웹사이트 로그인 정보가 있는 파일을 입력받음

BOT = wb.LoginBot(websites_info_filename)       # 크롤러를 불러옴
BOT.login()     # 로그인 메소드 실행

print("Process Done.")
end_time = time.time()

print("Processing time :  " + str(end_time - start_time) + "[sec]")

count = -1
while count != 0:       # 로그인한 웹사이트에서 작업 후 수기 종료
    count -= 1