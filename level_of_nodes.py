# This programme tells the level of all the nodes present in a given tree using bfs.
# Here n is the number of vetex starting from 0 and n-1 edges are given.

# input format
# 7
# 0 1
# 0 2
# 1 3
# 1 4
# 1 5
# 2 6

def ii(): return int(input())
def ai(): return list(map(int, input().split()))
def mi(): return map(int, input().split())

n = ii()
ad_lst = [[] for i in range(n)]  # This is tree
for _ in range(n-1):
	a,b = mi()
	ad_lst[b].append(a)
	ad_lst[a].append(b)
print(ad_lst)  # printing tree
visited = [False for i in range(n)]  # initially all vertex are unvisited
ver_lev = [0 for i in range(n)]  # this will keep track of level 
queue = [0]
fr, re = 0, 0
while fr <= re:  # while queue is not empty
	cu_ver = queue[fr]
	fr += 1                      # dequeueing the current vertex
	visited[cu_ver] = True       # marking it visited
	for neg in ad_lst[cu_ver]:   # traversing it's neighbour
		if visited[neg] == False:  # if not visited then visit
			visited[neg] = True      # marking it visited
			queue.append(neg)        # enqueueing it 
			re += 1
			ver_lev[neg] += ver_lev[cu_ver] + 1  # neighbour level is one more than it's parent level
print(ver_lev)
