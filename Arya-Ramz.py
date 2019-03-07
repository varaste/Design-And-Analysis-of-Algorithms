"""
https://quera.ir/problemset/contest/17902/%D8%B3%D8%A4%D8%A7%D9%84%D8%A7%D8%AA-%D9%85%D8%B3%D8%A7%D8%A8%D9%82%D9%87_%D8%B1%D9%85%D8%B2
"""
k, password, move = int(input()), input(), 0
for i in range(k):
    index = input().index(password[i])
    move += min(index, 9-index)
print(move)
