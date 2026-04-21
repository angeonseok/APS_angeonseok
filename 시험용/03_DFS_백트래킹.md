# 🌿 DFS / 백트래킹 유형

> **핵심 패턴**: 선택 → 탐색 → 되돌리기. 완전탐색이지만 가지치기로 최적화.

---

## 📌 2383 점심 식사시간

### 💡 핵심 아이디어
- 각 사람을 계단 1 or 계단 2로 보내는 모든 경우 DFS
- 배정 끝나면 `calc()` 로 각 계단 소요시간 계산 후 max
- `calc()`: 도착시간 정렬 → 4번째부터 `max(내도착, 3칸 앞 사람 완료시간)` 으로 대기 처리

```python
def calc(arr, length):
    if not arr: return 0
    arr.sort()
    end = []
    for i in range(len(arr)):
        start = arr[i] if i<3 else max(arr[i], end[i-3])
        end.append(start + length)
    return end[-1]

def dfs(idx):
    global ans
    if idx == len(people):
        t1 = calc(stair1_people[:], stair1_len)
        t2 = calc(stair2_people[:], stair2_len)
        ans = min(ans, max(t1, t2))
        return
    x,y = people[idx]
    dist1 = abs(x-stair1[0])+abs(y-stair1[1])+1
    stair1_people.append(dist1); dfs(idx+1); stair1_people.pop()
    dist2 = abs(x-stair2[0])+abs(y-stair2[1])+1
    stair2_people.append(dist2); dfs(idx+1); stair2_people.pop()
```

---

## 📌 4008 숫자 만들기

### 💡 핵심 아이디어
- 연산자 순서만 바꾸는 순열 완탐 (숫자 순서 고정)
- 재귀로 연산자 하나씩 소비하며 누적 계산
- 나눗셈: `int(total / nums[cnt])` → 음수 처리를 위해 `//` 대신 사용

```python
def cal_num(cnt, total, op1, op2, op3, op4):
    global max_num, min_num
    if cnt == n:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return
    if op1>0: cal_num(cnt+1, total+nums[cnt], op1-1, op2, op3, op4)
    if op2>0: cal_num(cnt+1, total-nums[cnt], op1, op2-1, op3, op4)
    if op3>0: cal_num(cnt+1, total*nums[cnt], op1, op2, op3-1, op4)
    if op4>0: cal_num(cnt+1, int(total/nums[cnt]), op1, op2, op3, op4-1)

cal_num(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(max_num - min_num)
```

---

## 📌 4128 요리사

### 💡 핵심 아이디어
- N개 재료를 N/2 : N/2 으로 나누는 모든 조합 완탐 (`combinations`)
- A그룹 고르면 B그룹은 자동 결정
- 시너지는 **쌍방향** 합산: `S[i][j] + S[j][i]`

```python
from itertools import combinations

for f1 in combinations(range(n), n//2):
    f2 = [i for i in range(n) if i not in f1]
    f1_syn = sum(synergy[f1[i]][f1[j]]+synergy[f1[j]][f1[i]]
                 for i in range(n//2) for j in range(i+1,n//2))
    f2_syn = sum(synergy[f2[i]][f2[j]]+synergy[f2[j]][f2[i]]
                 for i in range(n//2) for j in range(i+1,n//2))
    ans = min(ans, abs(f1_syn - f2_syn))
```

---

## 📌 5656 벽돌 깨기

### 💡 핵심 아이디어
- N번 구슬 던질 열 선택 → 모든 경우 DFS (W^N 완탐)
- `boom()`: BFS로 연쇄 폭발 처리 (벽돌값 = 폭발 반경)
- `fall()`: 각 열마다 0 제거 후 아래로 재배치
- 매 단계 배열 복사해서 상태 독립 유지

```python
def boom(a, arr):
    q = deque()
    for i in range(H):
        if arr[i][a]!=0: q.append((i,a,arr[i][a])); arr[i][a]=0; break
    while q:
        x,y,r = q.popleft()
        for k in range(1,r):
            for dir in dirs:
                nx,ny = x+dir[0]*k, y+dir[1]*k
                if 0<=nx<H and 0<=ny<W and arr[nx][ny]!=0:
                    q.append((nx,ny,arr[nx][ny])); arr[nx][ny]=0

def fall(arr):
    for i in range(W):
        temp = [arr[j][i] for j in range(H) if arr[j][i]!=0]
        for j in range(H): arr[j][i]=0
        for v in reversed(temp): arr[H-1-...][i]=v  # 아래부터 채움

def sol(depth, arr):
    global ans
    ans = min(ans, count(arr))
    if depth==N or count(arr)==0: return
    for i in range(W):
        clone = [row[:] for row in arr]
        boom(i, clone); fall(clone); sol(depth+1, clone)
```

---

## 📌 2112 보호 필름

### 💡 핵심 아이디어
- 각 행에 약품 A/B 투여 or 패스 → 3^D 완탐
- `check()`: 각 열마다 K개 연속 같은 값 있는지 확인
- 가지치기: 현재 투여 횟수 ≥ ans면 즉시 리턴

```python
def check():
    for i in range(w):
        cnt = 1
        for j in range(1,d):
            cnt = cnt+1 if arr[j][i]==arr[j-1][i] else 1
            if cnt>=k: break
        else: return False   # k개 연속 못 찾음
    return True

def inject(row, cnt):
    global ans
    if cnt >= ans: return        # 가지치기
    if check(): ans=min(ans,cnt)
    if row==d: return
    cur_row = arr[row][:]
    inject(row+1, cnt)           # 패스
    arr[row]=[0]*w; inject(row+1, cnt+1)  # A 투여
    arr[row]=[1]*w; inject(row+1, cnt+1)  # B 투여
    arr[row]=cur_row
```

---

## 📌 2115 벌꿀 채취

### 💡 핵심 아이디어
- **각 좌표별 최대 수익 미리 계산** → `arr_profit[i][j]`
- 구간 내 부분집합 완탐: 합이 C 이하인 경우 중 `꿀^2` 합 최대값
- 두 일꾼 좌표 쌍 브루트포스 (같은 행이면 구간 안 겹치는지 확인)

```python
def profit(idx, total, cur_sum, arr):
    global best
    if total > c: return
    if idx == m: best=max(best,cur_sum); return
    profit(idx+1, total, cur_sum, arr)                              # 안 채취
    profit(idx+1, total+arr[idx], cur_sum+arr[idx]**2, arr)        # 채취

# 좌표별 최대 수익 사전 계산
for i in range(n):
    for j in range(n-m+1):
        best=0; profit(0,0,0,arr[i][j:j+m]); arr_profit[i][j]=best

# 두 일꾼 완탐
for i1,j1 in ...:
    for i2,j2 in ...:
        if i1==i2 and abs(j1-j2)<m: continue  # 구간 겹침
        ans = max(ans, arr_profit[i1][j1]+arr_profit[i2][j2])
```

---

## 📌 2105 디저트 카페

### 💡 핵심 아이디어
- 대각선 4방향으로 사각형 그리기: 우하 → 좌하 → 좌상 → 우상
- 방향은 **현재 방향 or 다음 방향(+1)** 만 허용 (시계방향으로만 꺾기)
- `visited[디저트종류]`로 중복 디저트 체크
- 출발점 복귀 + 최소 4개 이상일 때 정답 갱신

```python
dirs = ((1,1),(1,-1),(-1,-1),(-1,1))  # 우하 좌하 좌상 우상

def dfs(si,sj,ci,cj,cnt,d):
    global ans
    for nd in (d, d+1):    # 현재 방향 or 다음 방향만
        if nd > 3: continue
        ni,nj = ci+dirs[nd][0], cj+dirs[nd][1]
        if 0<=ni<n and 0<=nj<n:
            if ni==si and nj==sj and cnt>=4:
                ans=max(ans,cnt); return
            elif not visited[arr[ni][nj]]:
                visited[arr[ni][nj]]=True
                dfs(si,sj,ni,nj,cnt+1,nd)
                visited[arr[ni][nj]]=False

# 출발 가능 범위: 우하/좌하/좌상 이동 여유 있는 위치
for i in range(n-2):
    for j in range(1, n-1):
        visited[arr[i][j]]=True
        dfs(i,j,i,j,1,0)
        visited[arr[i][j]]=False
```
