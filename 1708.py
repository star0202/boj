import sys
input = sys.stdin.readline
from collections import deque
points = []
n = int(input())
for _ in range (n):
    points.append(list(map(int, input().split())))
points.sort(key=lambda x : (x[0], x[1]))
start = points[0]
def ccw(p0, p1, p2):
    dx1, dy1, dx2, dy2 = p1[0]-p0[0], p1[1]-p0[1], p2[0]-p1[0], p2[1]-p1[1]
    return dx1*dy2 - dy1*dx2
def distance(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
points.remove(start)
inf = []
for i in range (n-1):
    if start[0] == points[i][0]:
        inf.append(points[i])
    else:
        points[i].append((start[1]-points[i][1])/(start[0]-points[i][0]))
for i in inf:
    points.remove(i)
points.sort(key=lambda x : x[2])
for i in inf:    
    points.append(i)
scan = deque()
scan.append(start)
scan.append(points[0])
for i in range (1, len(points)):
    if ccw(scan[-2], scan[-1], points[i]) > 0:
        scan.append(points[i])
    elif ccw(scan[-2], scan[-1], points[i]) < 0:
        while True:
            scan.pop()
            if ccw(scan[-2], scan[-1], points[i]) >= 0:
                break
        scan.append(points[i])
    else:
        if distance(points[i], scan[-2]) > distance(scan[-1], scan[-2]):
            scan.pop()
            scan.append(points[i])
i = 0
while i+2 < len(scan):
    if ccw(scan[i], scan[i+1], scan[i+2]) == 0:
        scan.remove(scan[i+1])
        i += 1
print(len(scan))