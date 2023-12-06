# 지정된 사이트들의 멀티 로그인

지정된 사이트들에 각각의 ID,PW를 이용하여 로그인하는 프로그램입니다.

>python multi_login.py <Excel File\>

## 한계
로그인 화면의 비번입력란에서 엔터를 쳐서 로그인이 실행 안되는 사이트라면 로그인 불가합니다.

## Excel File 양식
<Excel File\> 에는 사이트 별 로그인 정보를 적어줍니다. 
- 한 사이트의 로그인 정보는 하나의 행에 입력합니다.
- LOGIN URL
- ID
- PW
- TAB FOR ID
- TAB FOR PW

[사이트목록]
1. 도매토피아 : https://dometopia.com/member/login
2. 도매콜 : https://www.domecall.net/member/login.php
3. 펀타스틱 : https://funtasticb2b.co.kr/member/login


## 배치파일
multi_login.bat 실행해도 동일한 기능을 수행합니다.

