# 전국 도서관 표준데이터 정보
# 1. 열람좌석수가 가장 많은 상위 TOP5 도서관은?
# 2. 자료수(도서+연속간행물+비도서)가 가장 많은 상위 TOP5 도서관은?

import csv
from collections import Counter

seat_counter = Counter()
data_counter = Counter()

with open('library.csv', encoding='utf-8') as f:
    f.readline()

    reader = csv.reader(f)

    # 도서관명,시도명,시군구명,도서관유형,운영시작시각,운영종료시각,열람좌석수,자료수(도서),자료수(연속간행물),자료수(비도서),대출가능
    for line in reader:
        # key : 시도명 시군구명 도서관명
        key = line[1].strip() + ' ' + line[2].strip() + ' ' + line[0].strip()

        # 열람좌석수
        seat_num = line[6].strip()

        # 자료수
        t1, t2, t3 = line[7].strip(), line[8].strip(), line[9].strip()
        if t1 == '':
            t1 = 0
        if t2 == '':
            t2 = 0
        if t3 == '':
            t3 = 0
        data_num = int(t1) + int(t2) + int(t3)

        seat_counter[key] = int(seat_num)
        data_counter[key] = data_num


print('< 열람좌석수 TOP 5 >')
for data in seat_counter.most_common(5):
    # print(data)
    print(data[0], data[1])

print()

print('< 자료수 TOP 5 >')
for data in data_counter.most_common(5):
    # print(data)
    print(data[0], data[1])