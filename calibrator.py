import numpy as np
import math

PI = math.pi


def d2a(deg):
    return deg*1.0/180*PI


def rotate(a, b, w, r, v):
    a = d2a(a)
    b = d2a(b)
    w = d2a(w)
    r = d2a(r)
    x0 = np.sin(b) * np.sin(a)
    y0 = np.sin(b) * np.cos(a)
    z0 = np.cos(b)
    if v:
        p_ori = [-x0, -y0, -z0]
    else:
        p_ori = [x0, y0, z0]
    t = w - PI*0.5
    R0 = [[np.cos(t), np.sin(t), 0], [np.sin(t)*(-1), np.cos(t), 0], [0, 0, 1]]
    if v:
        k = r*(-1) - PI
    else:
        k = r * (-1)
    R1 = [[np.cos(k), 0, np.sin(k)*(-1)], [0, 1, 0], [np.sin(k), 0, np.cos(k)]]
    o = t*(-1)
    R2 = [[np.cos(o), np.sin(o), 0], [np.sin(o)*(-1), np.cos(o), 0], [0, 0, 1]]
    result = np.dot(R0, R1)
    result = np.dot(result, R2)
    result = np.dot(p_ori, result)
    x = result[0]
    y = result[1]
    z = result[2]
    if z < 0:
       x = -x
       y = -y
       z = -z
    if round(z, 6) == 0:
        return "FM"
    elif round(z, 6) == 1:
        return "FM"
    else:
        dip = round(abs(math.atan((math.sqrt(x*x+y*y))/z))/PI*180, 1)
        if (round(x, 6) == 0 and round(y, 6) == 0):
            return "FM"
        if (round(x, 6) == 0 and round(y, 6) != 0):
            results = (0.0, dip)
            return results
        elif (round(y, 6) == 0 and round(x, 6) != 0):
            results = (90.0, dip)
            return results
        elif (x > 0 and y > 0):
            results = (round(abs(math.atan(x/y)/PI*180), 1), dip)
            return results
        elif (x < 0 and y > 0):
            results = (round(360-abs(math.atan(x/y)/PI*180), 1), dip)
            return results
        elif (x > 0 and y < 0):
            results = (round(180-abs(math.atan(x/y)/PI*180), 1), dip)
            return results
        else:
            results = (round(180+abs(math.atan(x/y)/PI*180), 1), dip)
            return results
