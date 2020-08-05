def robot_traverse(maze,a,b,k1):
    maze = [[0 for i in range(b)] for i in range(a)]
    q = [[0,0,0]]
    visited = [[False for j in range(b)] for i in range(a)]
    visited[0][0] = True
    path_dict = {}
    while q:
        x,y,k,px,py = q.pop(0)

        if k==k1 and x==a-1 and y == b-1:
            return True
        if x-1>=0 and visited[x-1][y] == False:
            visited[x-1][y] = (x,y)
            q.append([x-1,y,k+1])
        if x+1<a and visited[x+1][y] == False:
            visited[x+1][y] = (x,y)
            q.append([x+1,y,k+1])
        if y-1>=0 and visited[x][y-1] == False:
            visited[x][y-1] = (x,y)
            q.append([x,y-1,k+1])
        if y+1<b and visited[x][y+1] == False:
            visited[x][y+1] = (x,y)
            q.append([x,y+1,k+1])
test_cases = input()
for i in range(int(test_cases)):
    print("Enter Input")
    a,b,k = input().split(" ")
    if robot_traverse(int(a),int(b),int(k)-1):
        print(1)
    else:
        print(0)