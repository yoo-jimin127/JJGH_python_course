import numpy as np
import matplotlib.pyplot as plt

# 막대 그래프
scorers = ['Kane', 'Son', 'Moura', 'Llorente', 'Alli', 'Eriksen']
number_of_goals = [20, 20, 9, 7, 7, 7]

xs = [i for i, _ in enumerate(scorers)]
plt.bar(xs, number_of_goals)  # 해당 인덱스에 일치하는 값을 가진, 바 형태 그래프 생성
plt.xlabel("Scorers")
plt.ylabel("Goals")
plt.xticks([i for i, _ in enumerate(scorers)], scorers)  # x 눈금 및 레이블 설정 
plt.title("Tottenham Hotspur's Top Scorers in 2018-2019")
plt.ylim(0, 25)  # y 범위 설정 (start, end)

for index, value in enumerate(number_of_goals):
    plt.text(index - 0.1, value + 0.5, str(value))  # x 좌표, y 좌표, text
plt.show()
