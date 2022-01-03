# 총수입 > 총비용(고정비용+가변비용) 일 때 판매량 / 없으면 -1
# A 고정비용 B 가변비용 C 노트북 가격

A, B, C = map(int, input().split())

# (C-B)n > A 일때 n을 구하면 됨
if C > B: # 0으로 나눌 수 없음
    print((A//(C-B))+1)
else:
    print(-1)