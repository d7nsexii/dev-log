#키 판별 프로그램


height = int(input("당신의 키를 입력하세요 (cm): "))

if height > 170:
    print(" 당신은 키가 큰 편입니다.")
elif height > 165:
    print(" 당신은 키가 평균 입니다.")
else:
    print(" 당신은 키가 작은 편입니다.")
