# 🔍 BFS 탐색 유형

> **핵심 패턴**: 최단거리 or 도달 가능 범위 탐색. 큐에 상태 넣고 레벨(거리) 단위로 퍼져나감.

---

## 📌 1953 탈주범 검거

### 💡 핵심 아이디어
- 터널 구조물마다 연결 방향이 다름 → `pipeline` 딕셔너리로 관리
- **양방향 연결 확인** 필수: 내가 그쪽으로 뻗어도, 상대도 나를 향해야 함
- `visited` 값에 거리 저장, L 이하인 곳만 카운트

```python
dirs = ((-1,0),(0,1),(1,0),(0,-1))  # 상 우 하 좌
pipeline = {
    1:(0,1,2,3), 2:(0,2), 3:(1,3),
    4:(0,1), 5:(1,2), 6:(2,3), 7:(0,3)
}

def link(i,j,ni,nj):
    # 상대방 터널이 나를 향하는지 확인
    for d in pipeline[arr[ni][nj]]:
        a,b = ni+dirs[d][0], nj+dirs[d][1]
        if a==i and b==j: return True
    return False

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        if visited[x][y] == l: continue   # L초 이후는 탐색 불필요
        for d in pipeline[arr[x][y]]:
            nx,ny = x+dirs[d][0], y+dirs[d][1]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]!=0 and visited[nx][ny]==0:
                if link(x,y,nx,ny):
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx,ny)); cnt+=1
    return cnt
```

---

## 📌 5650 핀볼 게임

### 💡 핵심 아이디어
- 외곽 벽을 **5번 블록(상하좌우 반사)** 으로 패딩 → 벽 충돌을 블록 충돌과 동일하게 처리
- `reflect` 딕셔너리: 블록 종류 × 진행방향 → 반사 후 방향
- 웜홀은 쌍으로 저장, 통과 시 반대편으로 순간이동 (방향 유지, 점수 없음)
- 출발점으로 돌아오면 종료, 블랙홀 만나면 종료

```python
dirs = ((-1,0),(1,0),(0,-1),(0,1))  # 상 하 좌 우
reflect = {
    1:{0:1,1:3,2:0,3:2},   # ◤ 우상단
    2:{0:3,1:0,2:1,3:2},   # ◥ 우상단(반대)
    3:{0:2,1:0,2:3,3:1},
    4:{0:1,1:2,2:3,3:0},
    5:{0:1,1:0,2:3,3:2},   # 수평/수직 반사
}

# 외곽 패딩
arr = [[5]*(n+2)]
for row in arr_input: arr.append([5]+row+[5])
arr.append([[5]*(n+2)])

def game(arr, si, sj, d):
    i,j = si,sj; score = 0
    while True:
        ni,nj = i+dirs[d][0], j+dirs[d][1]
        obj = arr[ni][nj]
        if obj == -1: return score
        if 1<=obj<=5: d=reflect[obj][d]; score+=1
        elif 6<=obj<=10:
            a,b = wormhole[obj]
            ni,nj = b if (ni,nj)==a else a
        i,j = ni,nj
        if ni==si and nj==sj: return score
```

---

## 📌 2117 홈 방범 서비스

### 💡 핵심 아이디어
- 마름모(다이아몬드) 영역을 k=1부터 **한 겹씩 확장**하며 집 수 누적
- 새로운 테두리만 추가로 탐색 → 매번 전체 재계산 불필요
- 테두리 조건: `|dx| + |dy| == k-1`
- 손익분기: `집수 * M >= 운영비용(k²+(k-1)²)` 이면 정답 갱신

```python
for i in range(n):
    for j in range(n):
        cnt = 0
        for k in range(1, 2*n):
            # 마름모 테두리(k겹) 좌표만 순회
            for dx in range(-k+1, k):
                dy_val = k-1-abs(dx)
                for dy in [dy_val, -dy_val]:
                    ni,nj = i+dx, j+dy
                    if 0<=ni<n and 0<=nj<n:
                        cnt += arr[ni][nj]
                    if dy_val == 0: break  # 중심점 중복 방지

            cost = k*k + (k-1)*(k-1)
            if cnt*m - cost >= 0:
                ans = max(ans, cnt)
```
