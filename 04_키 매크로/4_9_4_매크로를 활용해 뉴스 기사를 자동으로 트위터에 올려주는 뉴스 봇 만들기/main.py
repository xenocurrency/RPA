#-*-coding:euc-kr

import sys
import time
import twitter_bot_news as tb

# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

#아이디를 시스템에서 입력받습니다
id = sys.argv[1]

#비밀번호를 시스템에서 입력받습니다
ps= sys.argv[2]

#검색어를 시스템에서 입력받습니다
keyword = sys.argv[3].strip()

#gb 클래스 파트 - 구글뉴스에서 키워드 기반으로 검색. 뉴스 텍스트 복사 및 스트링화
#크롤러를 부릅니다
BOT = tb.NewsBot()

#로그인을 시도합니다
BOT.login(id,ps)

#뉴스와 함께 삽입할 해시태그를 입력
hashtags = "#뉴스 #스크랩 하는 #자동화 #코드"

#구글에서 뉴스 검색하고
#트위터에 자동로그인하고 (x) <- 로그인은 미리해뒀음
#긁어온 모든 뉴스를 업로드함
BOT.tweet_all_news(keyword, hashtags)

#결과물 감상위해 10초 대기
time.sleep(10)

#크롤러 닫아줌
BOT.kill()


# 작업 종료 메세지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
