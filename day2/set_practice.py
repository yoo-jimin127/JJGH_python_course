set_A = {1, 2, 3, 4, 5, 6}
set_B = {5, 6, 7, 8, 9, 10}

# 교집합 : 공통으로 있는 것
set_교 = set_A & set_B
# print(set_교)
set_교2 = set_A.intersection(set_B)
# print(set_교2)

# 합집합 : 집합의 모든 것들을 합치는 것
set_합 = set_A | set_B
# print(set_합)
set_합2 = set_A.union(set_B)
# print(set_합2)

# 차집합 : A-B B-A
set_차 = set_B - set_A
print(set_차)
set_차2 = set_B.difference(set_A)
print(set_차2)
