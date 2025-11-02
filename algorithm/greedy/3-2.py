# 입력조건
# - 첫째 줄에 N(2 ≤ N ≤ 1,000), M(1 ≤ N ≤ 10,000), K(1 ≤ N ≤ 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# - 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각가의 자연수는 1이상 10,000 이하의 수로 주어진다.
# - 입력으로 주어지는 K는 항상 M보다 작거나 같다.
#
# N: 배열의 크기, M: 숫자가 더해지는 횟수, K: 연속해서 더해질 수 있는 횟수
# 입력예시: 
# 5 8 3
# 2 4 5 4 6
# 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5

# -------------------------------------------------------------------
# 개인 풀이
# -------------------------------------------------------------------
n, m, k = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_n_sorted_reverse = sorted(arr_n, reverse=True)

i_cnt = 0

result = 0

for i in range(m):
    i = 0

    if i_cnt < k:
        i = 0
        i_cnt += 1
    else:
        i = 1
        i_cnt = 0

    result += arr_n_sorted_reverse[i]

print(result)

# -------------------------------------------------------------------
# 책 답변
# -------------------------------------------------------------------
# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력

