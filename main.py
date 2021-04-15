import io

class Node:
    def __init__(self,my_id,my_name):
        self.id = my_id
        self.name = my_name
        self.adj = set()

fin = io.open('graph.txt','r',encoding='utf-8')
graph = {}

n = int(fin.readline())
for i in range(n):
    player1_id = fin.readline()
    player1_id = player1_id[0:len(player1_id)-1]
    player1_name = fin.readline()
    player1_name = player1_name[0:len(player1_name)-1]
    m = int(fin.readline())
    if not player1_id in graph:
        graph[player1_id] = Node(player1_id, player1_name)
    for j in range(m):
        player2_id = fin.readline()
        player2_id = player2_id[0:len(player2_id)-1]
        graph[player1_id].adj.add(player2_id)

name_to_id = {}
for id in graph:
    name_to_id[graph[id].name] = id

def bfs(player1):
    dist = {}
    prev = {}
    for player in graph:
        dist[player] = -1
        prev[player] = 'NULL'
    dist[player1] = 0
    q = []
    q.append(player1)

    while (len(q) > 0):
        cur = q.pop(0)
        for next in graph[cur].adj:
            if (dist[next] == -1):
                dist[next] = dist[cur] + 1
                prev[next] = cur
                q.append(next)
    return (dist,prev)

player1 = name_to_id[input().strip()]
player2 = name_to_id[input().strip()]
ret = bfs(player1)
dist = ret[0]
prev = ret[1]
print(dist[player2])
ord = []
cur = player2
while(cur!='NULL'):
    ord.insert(0,graph[cur].name)
    cur = prev[cur]
for name in ord:
    print(name)