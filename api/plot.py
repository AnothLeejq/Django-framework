import numpy as np
from qutip.measurement import measure, measurement_statistics
from qutip.states import basis
from qutip.qip.operations import rx,rz

from math import sin,cos


def blochSphere(axis):
    results = {"0":0,"1":0}
    x,y,z = 0,0,0
    up = basis(2, 0)
    down = basis(2, 1)#kets
    for amount in axis:
        if amount["axis"] == "X":
            x += amount["amount"]
        if amount["axis"] == "Y":
            y += amount["amount"]
        if amount["axis"] == "Z":
            z += amount["amount"]
    x = rx(float(x%180))
    z = rz(float(z%360))
    measure(up, z) == (1.0, up)
    measure(down, z) == (-1.0, down)   
    post = -100
    for i in range(100):
        value, new_state = measure(up, x)
        if value > post:
            post = value
    for i in range(1000):
        value, new_state = measure(up, x)
        
        if value >= post : 
            results["1"] += 1
        else:
            results["0"] += 1

    return results
