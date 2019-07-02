import queue
from typing import List
class Solution:
  def topoOrder(self, N: int, pre: List[List[int]] ) -> list:
    graph = []
    for i in range(N):
      graph.append([])
    inDeg = [0]* N

    for u, i in pre:
      graph[i].append(u)# i u 的位置要放对，index 是先修课，value是邻接点
      inDeg[u] +=1
    que = queue.Queue()
    for i in range (N):
      if inDeg[i] == 0:
        que.put(i)
    ls = []
    

    while len(que.queue)!= 0:
      a = que.get()
      ls.append(a)
      for w in graph[a]:
        print(w)
        inDeg[w] -=1
        if inDeg[w] == 0:
          que.put(w)
    
    #print (inDeg)
    for i in range(N):
      if inDeg[i] != 0: 
        print ("this is cycle")
        return None
    return ls


if __name__ == "__main__":
  pre = [[2,1],[1,0],[2,0]]
  num = 4
  sol = Solution()
  a = sol.topoOrder(num, pre)
  print (a)
  for i in range(len(a)):
    print(a[i], end = ' ')