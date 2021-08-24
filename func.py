import numpy as np
import math

def slope(pos, big_axis, small_axis):
    return np.array([-big_axis*((pos[1] - small_axis)/small_axis), small_axis*((pos[0] - big_axis)/big_axis)])

def meet(v, pos, big_axis, small_axis):
    a = (v[0]/big_axis)**2 + (v[1]/small_axis)**2
    b = 2*v[0]*(pos[0] - big_axis)/((big_axis)**2) + 2*v[1]*(pos[1] - small_axis)/((small_axis)**2)
    c = ((pos[0] - big_axis)/big_axis)**2 + ((pos[1] - small_axis)/small_axis)**2 - 1
    D = b**2 - 4*a*c
    Sol = (-b + math.sqrt(D))/(2*a)
    if (Sol < 0): Sol = (-b - math.sqrt(D))/(2*a)
    
    meet_x = pos[0] + v[0]*Sol
    meet_y = pos[1] + v[1]*Sol

    return np.array([meet_x, meet_y])

def reflect(v, meet_point, big_axis, small_axis):
    slope_vector = slope(meet_point, big_axis, small_axis)

    p = (slope_vector[0]*v[1] - slope_vector[1]*v[0])/(slope_vector[0]**2 + slope_vector[1]**2)  #These two variables p and q are useless but they
    q = (slope_vector[0]*v[0] + slope_vector[1]*v[1])/(slope_vector[0]**2 + slope_vector[1]**2)  #allow to read the code easier, remove to boost for some tiny bit

    return np.array([slope_vector[1]*p + slope_vector[0]*q, slope_vector[1]*q - slope_vector[0]*p])