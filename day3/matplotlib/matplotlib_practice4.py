import numpy as np
import matplotlib.pyplot as plt

# 산점도
goals = [13, 9, 8, 4, 3]
assists = [2, 9, 4, 2, 0]
players = ["Kane", "Son", "Alli", "Moura", "Bergwijn"]
plt.scatter(goals, assists)  # x 좌표, y 좌표 에 일치하는 점을 찍음

for goal, assist, player in zip(goals, assists, players):
    plt.annotate(player,  # 텍스트
                xy=(goal, assist),  # x 좌표, y 좌표
                xytext=(5, -5),  # x 좌표, y 좌표 이격
                textcoords="offset points")  # 좌표 point 기준으로 설정함)
plt.title("Tottenham Players Goal and Assists")
plt.xlim(0, 15)
plt.xlabel("Goals")
plt.ylabel("Assists")
plt.show()
