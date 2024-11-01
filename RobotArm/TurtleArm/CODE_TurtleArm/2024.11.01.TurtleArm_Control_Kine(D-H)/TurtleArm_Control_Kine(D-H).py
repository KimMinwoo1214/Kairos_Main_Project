import pandas as pd
import numpy as np
import math
pi = math.pi
sin = math.sin
cos = math.cos

# Denavit-Hatenberg-Parameter
# th : z축에 대한 회전
# al : x축에 대한 회전
# a : x축에 대한 이동
# d : z축에 대한 이동

# 총 6축
th = np.array([0,0,0,0,0,0])*pi/180 # rad
a = np.array([0,-425,-392,0,0,0,0]) # mm
d = np.array([89,0,0,109,95,82]) # mm
al = np.array([90,0,0,90,-90,0])*pi/180 # rad

T = [0 for i in range(6)]

for i in range(6):
    T[i] = np.array([
        [cos(th[i]), -sin(th[i]) * cos(al[i]), sin(th[i]) * sin(al[i]), a[i] * cos(th[i])],
        [sin(th[i]), cos(th[i]) * cos(al[i]), -cos(th[i]) * sin(al[i]), a[i] * sin(th[i])],
        [0, sin(al[i]), cos(al[i]), d[i]],
        [0, 0, 0, 1]])


# T05 : T[0]*T[1]....*T[5]
T05 = pd.DataFrame(T[0].dot(T[1]).dot(T[2]).dot(T[3]).dot(T[4]).dot(T[5]))
print(T05)

