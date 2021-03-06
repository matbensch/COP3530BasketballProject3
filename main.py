import io
import time
import heapq

#Node class representing a player
class Node:
    def __init__(self,my_id,my_name):
        self.id = my_id
        self.name = my_name
        self.adj = set()

#breadth first search on graph with source node player1
#returns a tuple including the distance map and previous map
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

#dijkstras algorithm on graph with source node player1
#returns a tuple including the distance map and previous map
def dijkstra(player1):
    dist = {}
    prev = {}
    q = []
    for player in graph:
        dist[player] = float("inf")
        prev[player] = 'NULL'
    heapq.heappush(q,(0,player1))
    dist[player1] = 0

    while (len(q) > 0):
        cur = heapq.heappop(q)[1]
        for next in graph[cur].adj:
            alt = dist[cur] + 1
            if (alt < dist[next]):
                dist[next] = alt
                prev[next] = cur
                q.append((dist[next],next))
    return (dist,prev)

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

#checks that player1 name is valid
player1 = input('Player 1 Name: ').strip()
while(player1 not in name_to_id):
    player1 = input('Invalid Name, Try Again: ').strip()

#checks that player2 name is valid
player2 = input('Player 2 Name: ').strip()
while(player2 not in name_to_id):
    player2 = input('Invalid Name, Try Again: ').strip()

player1_id = name_to_id[player1]
player2_id = name_to_id[player2]

print()
#runs BFS
print('BFS:')
ti = time.perf_counter()
ret = bfs(player1_id)
dist = ret[0]
prev = ret[1]
print('Distance = '+str(dist[player2_id]))
ord = []
cur = player2_id
while(cur!='NULL'):
    ord.insert(0,graph[cur].name)
    cur = prev[cur]
for name in ord:
    print(name)
tf = time.perf_counter()-ti
print('Runtime: '+str(round(tf,3))+' s')
print()

#runs Dijkstra's
print('Dijkstra:')
ti = time.perf_counter()
ret = dijkstra(player1_id)
dist = ret[0]
prev = ret[1]
print('Distance = '+str(dist[player2_id]))
ord = []
cur = player2_id
while(cur!='NULL'):
    ord.insert(0,graph[cur].name)
    cur = prev[cur]
for name in ord:
    print(name)
tf = time.perf_counter()-ti
print('Runtime: '+str(round(tf,3))+' s')