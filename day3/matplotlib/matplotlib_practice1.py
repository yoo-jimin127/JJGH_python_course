import numpy as np
import matplotlib.pyplot as plt

# 꺾은선 그래프
years = [2015, 2016, 2017, 2018, 2019]
rank = [5, 3, 2, 3, 4]
plt.plot(
    years,  # x축 데이터
    rank,  # y축 데이터
    color='blue',  # 선 색깔
    marker='o',  # 꼭짓점 설정
    linestyle='solid'  # 선 스타일 설정
)
plt.xlim(2014.5, 2019.5)  # x 범위 설정 (start, end)
plt.ylim(6, 1)  # y 범위 설정 (start, end)
plt.title("Tottenham Hotspur's EPL Rankings 2015-2019")  # title 설정
plt.xlabel('year')  # x축 레이블 설정
plt.ylabel('rank')  # y축 레이블 설정
plt.show()
