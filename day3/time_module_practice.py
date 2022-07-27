import time

# time 모듈로 현재 시간 구하기
print("변환 전 시간 : ", time.time())

# 날짜와 시간 형태로 변환하기
print(time.localtime(time.time()))

# 날짜/시간 포맷에 맞춰 출력하기
print(time.strftime("%Y-%m-%d", time.localtime(time.time())))
