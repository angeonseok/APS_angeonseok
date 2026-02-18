from collections import deque

# 1. 원자 소멸 시뮬레이션

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    #0.5충돌 처리 위해 좌표 2배 스케일링
    atoms = []  #x,y,dir,energy
    for _ in range(n):
        x,y,d,k = map(int, input().split())
        atoms.append((2*x,2*y,d,k))

    ans = 0

    for _ in range(4000):
        if len(atoms) <= 1:
            break

    #이동 후 좌표별 총 에너지와 개수 기록
    pos = {}       #x,y > sum_energy, cnt
    moved = []     #이동 후 살아있는 원자 목록

    for x,y,d,k in atoms:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < -2000 or nx > 2000 or ny < -2000 or ny > 2000:
            continue

        moved.append((nx,ny,d,k))
        key = (nx,ny)

        if key in pos:
            pos[key][0] += k
            pos[key][1] += 1
        else:
            pos[key] = [k, 1]

    if not moved:
        break

    #충돌처리(충돌시 원자 소멸 + 에너지 합산)
    atoms = []
    for x,y,d,k in moved:
        if pos[(x,y)][1] >= 2:
            continue
        atoms.append((x,y,d,k))

    for (x,y), (s, c) in pos.items():
        if c >= 2:
            ans += s
    
    print(f'{tc} {ans}')

#-------------------------------------------------------------------------

#2 ***미생물 격리

T = int(input())
for tc in range(1, T+1):
    n,m,k = map(int,input().split())

    dx = [0,-1,1,0,0]
    dy = [0,0,0,-1,1]
    #경계에 닿으면 방향 반대로
    rev = [0,2,1,4,3]

    groups = [] #x,y,cnt,dir
    for _ in range(k):
        x,y,cnt,d = map(int, input().split())
        groups.append([x,y,cnt,d])

    for _ in range(m):
        #이동 후 같은 칸으로 모이는 그룹을 병합하기 위해 dict 사용
        cell = {} #key = (x,y) : [sum_cnt, max_cnt, dir_of_max]

        for x,y,cnt,d in groups:
            nx = x + dx[d]
            ny = y + dy[d]

            #경계 처리 : 미생물 컽 + 방향 반대
            if nx == 0 or ny == 0 or nx == n-1 or ny == n-1:
                cnt //= 2
                d = rev[d]

            if cnt == 0:
                continue

            key = (nx,ny)
            if key not in cell:
                cell[key] = [cnt, cnt, d]
            else:
                cell[key][0] += cnt

                #가장 큰 군집 방향 따라감
                if cnt > cell[key][1]:
                    cell[key][1] = cnt
                    cell[key][2] = d

        #dict > 다음 스텝 그룹 리스트로 구성
        groups = []
        for (x,y), (x,mx,dmx) in cell.items():
            groups.append([x,y,s,dmx])

    ans = sum(g[2] for g in groups)
    print(f'#{tc} {ans}')

#-------------------------------------------------------------------------

#3 무선 충전

T = int(input())
for tc in range(1,T+1):
    m,a = map(int, input().split())
    moveA = list(map(int, input().split()))
    moveB = list(map(int, input().split()))

    dx = [0,-1,0,1,0]
    dy = [0,0,1,0,-1]

    #BC정보 : x,y,coverage,power
    bc = []
    for i in range(a):
        x,y,c,p = map(int, input().split())
        bc.append((x,y,c,p,i))
    
    ax,ay = 1, 1
    bx,by = 10, 10

    #해당 좌표에서 접속 가능한 BC 후보(power,id) 리스트 반환
    def candidates(x,y):
        res = []
        for cx,cy,cov,p,idx in bc:
            if abs(cx-x) + abs(cy-y) <= cov :
                res.append((p,idx))
        return res
    
    ans = 0

    #0초 포함해서 m초까지 총 m+1번 충전 계산
    for t in range(m+1):
        ca = candidates(ax,ay)
        cb = candidates(bx,by)

        best = 0
        #둘 다 후보가 없으면 0
        if ca and not cb:
            best = max(p for p, _ in ca)
        elif cb and not ca:
            best = max(p for p, _ in cb)
        elif ca and cb:
            #a가 i, b가 j를 선택했을 때 최대 합
            for pa,ia in ca:
                for pb, ib in cb:
                    if ia == ib:
                        best = max(best,pa)
                    else:
                        best = max(best,pa+pb)
        ans += best

        #마지막 시점이면 이동 없음
        if t == m:
            break
        
        ax += dy[moveA[t]]
        ay += dx[moveA[t]]
        bx += dy[moveB[t]]
        by += dx[moveB[t]]
    
    print(f'#{tc} {ans}')

#-------------------------------------------------------------------------

#4 특이한 자석

T = int(input())
for tc in range(1,T+1):
    k = int(input())

    #각 자석은 8개 톱니, 0번이 12시 방향
    mags = [deque(map(int,input().split())) for _ in range(4)]

    for _ in range(k):
        idx,dir0 = map(int,input().split())
        idx -= 1 #0-index

        #각 자석 회전 방향 기록(0:회전x 1:시계 -1:반시계)
        rot = [0,0,0,0]
        rot[idx] = dir0

        #왼쪽으로 전파 : i와 i-1의 맞닿은 톱니 비교
        for i in range(idx, 0, -1):
            #i의 6번(왼쪽)과 i-1의 2번(오른쪽)이 다르면 전파
            if mags[i][6] != mags[i-1][2]:
                rot[i-1] = -rot[i]
            else:
                break
        
        #오른쪽으로 전파
        for i in range(idx,3):
            if mags[i][2] != mags[i+1][6]:
                rot[i+1] = -rot[i]
            else:
                break
        
        #실제 회전 적용
        for i in range(4):
            if rot[i] == 1:     #시계 : 오른쪽 1칸 > pop을 왼쪽에
                mags[i].appendleft(mags[i].pop())
            elif rot[i] == -1:  #반시계 : 왼쪽으로 한 칸 > popleft를 오른쪽
                mags[i].append(mags[i].popleft())

    score = 0
    for i in range(4):
        if mags[i][0] == 1:
            score += (1 << i)
    print(f'#{tc} {score}')

#-------------------------------------------------------------------------

#5 핀볼 게임
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    #블록별 반사 규칙 : block,dir > new_dir
    #블록 5는 벽처럼 반사(상 <> 하, 좌 <> 우)
    ref = {
        1 : [1,3,0,2],
        2 : [3,0,1,2],
        3 : [2,0,3,1],
        4 : [1,2,3,0],
        5 : [1,0,3,2]
    }

    #웜홀 좌표 저장 : 번호 6~10 각각 2개씩
    worm = {i : [] for i in range(6,11)}
    for i in range(n):
        for j in range(n):
            if 6 <= board[i][j] <= 10:
                worm[board[i][j].append((i,j))]

    #웜홀 번호로 들가면 반대편 웜홀 좌표 반환
    def other_worm(w,x,y):
        a, b = worm[w]
        return b if (a[0],a[1]) == (x,y) else a
    
    ans = 0

    #빈칸에서 4방향으로 발사
    for sx in range(n):
        for sy in range(n):
            if board[sx][sy] != 0:
                continue

            for d0 in range(4):
                x,y,d, = sx,sy,d0
                score = 0

                while 1:
                    nx = x + dx[d]
                    ny = y + dy[d]

                    #벽 밖으로 나가면 블록 5처럼 반사 + 1점
                    if nx < 0 or nx >=n or ny < 0 or ny >= n:
                        d = ref[5][d]
                        score += 1
                        #위치는 그대로, 다음 진행(반사 후 이동)
                        continue
                    
                    v = board[nx][ny]

                    #시작점으로 오거나 블랙홀이면 종료
                    if (nx,ny) == (sx,sy) or v == -1:
                        ans = max(ans,score)
                        break
                    
                    #블록(1~5) : 반사 + 점수 1
                    if 1 <= v <= 5:
                        d = ref[v][d]
                        score += 1
                        x,y = nx,ny
                         
                    #웜홀 : 반대편으로 텔포
                    elif 6 <= v <= 10:
                        ox,oy = other_worm(v,nx,ny)
                        x,y = ox,oy
                    
                    #빈 칸 : 그대로 이동
                    else:
                        x,y = nx,ny
    print(f'#{tc} {ans}')

#-------------------------------------------------------------------------

#6 활주로 건설

# 한 줄(line)에 대해 활주로 가능 여부 검사
def can_runway(line, X):
    N = len(line)
    used = [False] * N  # 경사로가 이미 놓인 칸 표시(중복 설치 방지)

    for i in range(N - 1):
        if line[i] == line[i + 1]:
            continue

        diff = line[i + 1] - line[i]

        # 1) 올라가는 경우: 뒤쪽으로 X칸이 모두 같은 높이여야 함
        if diff == 1:
            for j in range(i, i - X, -1):
                if j < 0 or used[j] or line[j] != line[i]:
                    return False
                used[j] = True

        # 2) 내려가는 경우: 앞쪽으로 X칸이 모두 다음 높이여야 함
        elif diff == -1:
            for j in range(i + 1, i + 1 + X):
                if j >= N or used[j] or line[j] != line[i + 1]:
                    return False
                used[j] = True

        # 3) 높이차가 2 이상이면 불가능
        else:
            return False

    return True


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    # 행 검사 + 열 검사
    for r in range(N):
        if can_runway(g[r], X):
            ans += 1
        col = [g[i][r] for i in range(N)]
        if can_runway(col, X):
            ans += 1

    print(f"#{tc} {ans}")

#-------------------------------------------------------------------------

#7 숫자 만들기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ops = list(map(int, input().split()))  # +, -, *, /
    nums = list(map(int, input().split()))

    # 최댓값/최솟값 갱신
    mx = -10**18
    mn = 10**18

    def dfs(i, cur, a, s, m, d):
        """
        i: 현재 nums 인덱스(다음에 사용할 숫자 위치)
        cur: 현재까지 계산값
        a,s,m,d: 남은 연산자 개수
        """
        nonlocal mx, mn
        if i == N:
            mx = max(mx, cur)
            mn = min(mn, cur)
            return

        x = nums[i]

        if a:
            dfs(i + 1, cur + x, a - 1, s, m, d)
        if s:
            dfs(i + 1, cur - x, a, s - 1, m, d)
        if m:
            dfs(i + 1, cur * x, a, s, m - 1, d)
        if d:
            # SWEA 4008은 "정수 나눗셈"인데, 파이썬 //는 음수에서 다름.
            # 일반적으로 문제 요구는 C/C++의 "0을 향해 버림" 방식이므로 int(cur/x)를 사용.
            dfs(i + 1, int(cur / x), a, s, m, d - 1)

    dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])

    print(f"#{tc} {mx - mn}")

#-------------------------------------------------------------------------

#8 요리사
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    # 시너지 합을 빠르게 계산하려면 pair 합을 쓰는 방식도 있지만,
    # N이 보통 16 이하라 조합+계산으로도 충분하다.
    best = 10**18

    # 조합을 비트마스크/재귀로 생성
    chosen = [False] * N

    def calc_diff():
        a = []
        b = []
        for i in range(N):
            (a if chosen[i] else b).append(i)

        sa = 0
        sb = 0
        # 팀 내부 시너지 합
        for i in range(N//2):
            for j in range(i+1, N//2):
                x, y = a[i], a[j]
                sa += S[x][y] + S[y][x]
                x, y = b[i], b[j]
                sb += S[x][y] + S[y][x]
        return abs(sa - sb)

    def dfs(idx, cnt):
        nonlocal best
        # cnt가 N/2 되면 나머지는 자동
        if cnt == N // 2:
            best = min(best, calc_diff())
            return
        # 끝까지 갔는데 못 채우면 종료
        if idx == N:
            return
        # 가지치기: 남은 원소로도 N/2 채울 수 없으면 컷
        if cnt + (N - idx) < N // 2:
            return

        # 선택
        chosen[idx] = True
        dfs(idx + 1, cnt + 1)
        chosen[idx] = False

        # 미선택
        dfs(idx + 1, cnt)

    # 대칭 제거: 0번은 무조건 A팀에 넣으면 절반만 탐색
    chosen[0] = True
    dfs(1, 1)

    print(f"#{tc} {best}")

#-------------------------------------------------------------------------

#9 디저트 카페
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]
    
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    ans = -1

    def inb(x, y):
        return 0 <= x < N and 0 <= y < N

    # 시작점 (sx,sy)에서 두 변 길이 a,b를 잡아 사각형을 만들면 구현이 쉬움.
    # 여기서는 DFS로 "방향은 증가만(0->1->2->3)" 하게 해서 중복을 줄임.
    def dfs(x, y, d, sx, sy, eaten):
        nonlocal ans

        # 4방향 다 돌고 시작점으로 돌아오면 종료
        # (실제로는 마지막 방향에서 시작점으로 돌아오는 순간 체크)
        for nd in (d, d + 1):  # 현재 방향 유지 or 다음 방향(최대 3까지)
            if nd >= 4:
                continue
            nx = x + dx[nd]
            ny = y + dy[nd]
            if not inb(nx, ny):
                continue

            # 시작점으로 돌아왔으면 성공
            if nx == sx and ny == sy and len(eaten) >= 4:
                ans = max(ans, len(eaten))
                continue

            dessert = g[nx][ny]
            if dessert in eaten:
                continue

            eaten.add(dessert)
            dfs(nx, ny, nd, sx, sy, eaten)
            eaten.remove(dessert)

    # 시작점은 테두리 너무 바깥이면 사각형이 안 나옴
    for i in range(N):
        for j in range(N):
            eaten = set([g[i][j]])
            dfs(i, j, 0, i, j, eaten)

    print(f"#{tc} {ans}")

#-------------------------------------------------------------------------

#10 ***탈주범 검거
T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]

    pipe_dirs = {
    0: [],
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
    }

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    opp = [1, 0, 3, 2]  # 반대 방향

    visited = [[False] * M for _ in range(N)]
    q = deque()

    visited[R][C] = True
    q.append((R, C, 1))  # (x,y,time=1부터)

    cnt = 1

    while q:
        x, y, t = q.popleft()
        if t == L:
            continue

        cur_type = g[x][y]
        for d in pipe_dirs[cur_type]:
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if visited[nx][ny]:
                continue
            nxt_type = g[nx][ny]
            if nxt_type == 0:
                continue

            # 다음 칸 파이프가 "반대 방향"으로 연결되어 있어야 이동 가능
            if opp[d] not in pipe_dirs[nxt_type]:
                continue

            visited[nx][ny] = True
            cnt += 1
            q.append((nx, ny, t + 1))

    print(f"#{tc} {cnt}")

#-------------------------------------------------------------------------

#11 등산로 조성

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    maxh = max(map(max, g))
    starts = [(i, j) for i in range(N) for j in range(N) if g[i][j] == maxh]

    visited = [[False] * N for _ in range(N)]
    ans = 0

    def dfs(x, y, cut_used, length):
        """
        cut_used: 이미 한 번 깎았는지 여부
        """
        nonlocal ans
        ans = max(ans, length)

        visited[x][y] = True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue

            if g[nx][ny] < g[x][y]:
                dfs(nx, ny, cut_used, length + 1)
            else:
                # 아직 안 깎았으면 K까지 깎아서 내려갈 수 있는지 체크
                if not cut_used:
                    needed = g[nx][ny] - (g[x][y] - 1)  # 최소 이만큼 깎아야 g[nx][ny] < g[x][y]
                    if 1 <= needed <= K:
                        original = g[nx][ny]
                        g[nx][ny] = g[x][y] - 1
                        dfs(nx, ny, True, length + 1)
                        g[nx][ny] = original
        visited[x][y] = False

    for sx, sy in starts:
        dfs(sx, sy, False, 1)

    print(f"#{tc} {ans}")

#-------------------------------------------------------------------------

#12 ***보호 필름
T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]

    # K=1이면 어떤 필름도 통과
    if K == 1:
        print(f"#{tc} 0")
        continue

    # 성능 검사: 모든 열이 연속 K개 이상 같은 값(0 또는 1) 존재해야 통과
    def check(arr):
        for c in range(W):
            run = 1
            ok = False
            for r in range(1, D):
                if arr[r][c] == arr[r - 1][c]:
                    run += 1
                else:
                    run = 1
                if run >= K:
                    ok = True
                    break
            if not ok:
                return False
        return True

    ans = K  # 이론상 K번까지 약품 주입하면 무조건 가능

    # 작업용 배열(수정)
    work = [row[:] for row in film]

    def dfs(r, used):
        """
        r: 현재 처리할 행
        used: 약품 주입한 행 수
        """
        nonlocal ans
        # 가지치기: 이미 ans 이상 사용하면 볼 필요 없음
        if used >= ans:
            return

        # 모든 행을 결정했으면 검사
        if r == D:
            if check(work):
                ans = used
            return

        # 1) 그대로 두기
        dfs(r + 1, used)

        # 2) A(0)로 주입
        saved = work[r][:]
        work[r] = [0] * W
        dfs(r + 1, used + 1)

        # 3) B(1)로 주입
        work[r] = [1] * W
        dfs(r + 1, used + 1)

        # 복원
        work[r] = saved

    # 이미 통과면 0
    if check(work):
        ans = 0
    else:
        dfs(0, 0)

    print(f"#{tc} {ans}")

#-------------------------------------------------------------------------

#13 프로세서 연결하기
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    g = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    cores = []
    # 가장자리에 있는 코어는 이미 연결된 것으로 취급(연결할 필요 없음)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if g[i][j] == 1:
                cores.append((i, j))

    best_core = -1   # 최대 연결 코어 수
    best_len = 10**18  # 그때의 최소 전선 길이

    def can_lay(x, y, d):
        """
        (x,y) 코어에서 방향 d로 뻗을 때
        설치 가능 여부 + 설치 길이 + 경로 좌표 반환
        """
        path = []
        nx, ny = x + dx[d], y + dy[d]
        while 0 <= nx < N and 0 <= ny < N:
            if g[nx][ny] != 0:
                return False, 0, []
            path.append((nx, ny))
            nx += dx[d]
            ny += dy[d]
        # 경계 밖으로 나갔다는 것은 가장자리까지 도달했다는 의미(연결 성공)
        return True, len(path), path

    def lay(path, val):
        for x, y in path:
            g[x][y] = val

    def dfs(idx, connected, length):
        nonlocal best_core, best_len

        # 가지치기 1: 남은 코어 모두 연결해도 best_core 못 넘으면 컷
        remain = len(cores) - idx
        if connected + remain < best_core:
            return

        # 끝까지 처리
        if idx == len(cores):
            if connected > best_core:
                best_core = connected
                best_len = length
            elif connected == best_core:
                best_len = min(best_len, length)
            return

        x, y = cores[idx]

        # 0) 이 코어를 연결하지 않는 경우(연결 수 최대가 우선이라서 경우 포함)
        dfs(idx + 1, connected, length)

        # 1) 4방향으로 연결 시도
        for d in range(4):
            ok, l, path = can_lay(x, y, d)
            if not ok:
                continue
            # 가지치기 2: 길이가 이미 best_len 이상인데 연결 수가 동일하게 갈 상황이면 컷(약하게 적용)
            # (연결 수가 더 커질 가능성은 남아 있으니 강하게 컷하면 위험)
            lay(path, 2)  # 전선 표시(2)
            dfs(idx + 1, connected + 1, length + l)
            lay(path, 0)  # 복원

    dfs(0, 0, 0)
    print(f"#{tc} {best_len}")

#-------------------------------------------------------------------------

#14 벽돌 깨기
T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(H)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    best = 10**18

    def count_bricks(board):
        return sum(1 for i in range(H) for j in range(W) if board[i][j] != 0)

    def drop(board, col):
        """
        col에 구슬 떨어뜨림:
        - 가장 위의 벽돌 찾기
        - BFS로 폭발(값-1 범위)
        - 중력 적용
        """
        # 1) 맞을 첫 벽돌 찾기
        r = 0
        while r < H and board[r][col] == 0:
            r += 1
        if r == H:
            return board  # 아무것도 없음

        q = deque()
        q.append((r, col, board[r][col]))
        board[r][col] = 0

        # 2) 폭발 BFS
        while q:
            x, y, p = q.popleft()
            # p=1이면 자기만 깨짐
            for d in range(4):
                nx, ny = x, y
                for _ in range(p - 1):
                    nx += dx[d]
                    ny += dy[d]
                    if not (0 <= nx < H and 0 <= ny < W):
                        break
                    if board[nx][ny] == 0:
                        continue
                    q.append((nx, ny, board[nx][ny]))
                    board[nx][ny] = 0

        # 3) 중력 적용: 각 열마다 아래로 당기기
        for c in range(W):
            stack = []
            for rr in range(H - 1, -1, -1):
                if board[rr][c] != 0:
                    stack.append(board[rr][c])
            rr = H - 1
            for v in stack:
                board[rr][c] = v
                rr -= 1
            for rr2 in range(rr, -1, -1):
                board[rr2][c] = 0

        return board

    def dfs(depth, board):
        """
        depth: 현재 던진 횟수
        board: 현재 보드 상태
        """
        nonlocal best

        # 남은 벽돌 수
        remain = count_bricks(board)
        best = min(best, remain)
        if remain == 0:
            return
        if depth == N:
            return

        # 가지치기: 이미 best가 0이면 더 볼 필요 없음
        if best == 0:
            return

        # 각 열에 대해 던져보기
        for c in range(W):
            # 보드 복사(깊은 복사)
            new_board = [row[:] for row in board]
            dfs(depth + 1, drop(new_board, c))

    dfs(0, [row[:] for row in origin])
    print(f"#{tc} {best}")