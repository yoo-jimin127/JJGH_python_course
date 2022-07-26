import numpy as np
import matplotlib.pyplot as plt

# 선 
dele = [7.35, 7.35, 7.09, 6.95, 6.89]
eriksen = [7.45, 7.53, 7.4, 7.08, 6.51]
son = [6.53, 7.14, 6.99, 7.1, 7.23]
kane = [7.53, 7.68, 7.6, 7.38, 7.2]
xs = [2015, 2016, 2017, 2018, 2019]

plt.plot(xs, dele, 'r-', label='Dele Alli')  # x, y, 선 색깔 및 타입 (r: 빨강, -: 실선)
plt.plot(xs, eriksen, 'g--', label='Christian Eriksen')  # (g: 초록, --: 파선)
plt.plot(xs, son, 'b-.', label='Heung-Min Son')  # (b: 파랑 -.: 1점 쇄선)
plt.plot(xs, kane, 'k:', label='Harry Kane')  # (k: 검정, -: 점선)
plt.xlim(2014.5, 2019.5)  # x 범위 설정 (start, end)
plt.ylim(6, 8)  # y 범위 설정 (start, end)
plt.legend(loc=8)  # loc=8로 하단 중앙에 범례 설정
plt.xlabel("Year")
plt.ylabel("Rating")
plt.title("DESK's Annual rating")
plt.show()
