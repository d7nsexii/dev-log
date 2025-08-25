#가상 웹사이트 로그인 로직

db_id = "student01"
db_pw = "1234*"

user_id = input("아이디 입력: ")
user_pw = input("패스워드 입력: ")

if user_id == db_id and user_pw == db_pw:
    print(" 로그인이 성공적으로 완료되었습니다.")
elif user_id != db_id:
    print(" 존재하지 않는 아이디입니다.")
else:
    print(" 비밀번호가 틀렸습니다.")
