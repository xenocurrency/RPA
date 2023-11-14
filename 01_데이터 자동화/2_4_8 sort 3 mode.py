import os
import sys
try:
    import pyexcel as px
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'pyexcel'])
    pip.main(['install', 'pyexcel-xlsx'])
    try:
        import pyexcel as px
    except ModuleNotFoundError:
        time.sleep(2)
        import pyexcel as px

#Process Start 를 출력
print ("Process Start")

#시작시간 기록
start_time = time.time()

#데이터가 있는 폴더명을 시스템으로부터 입력받습니다
directory = sys.argv[1]

#템플릿을 시스템으로부터 입력받습니다
template = sys.argv[2]

#모드를 시스템으로부터 입력받습니다
MODE = sys.argv[3]

