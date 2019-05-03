# -*-coding:utf-8-*-

from math import atan2
from random import randint

# Returns the polar angle (radians) from p0 to p1.
# If p1 is None, defaults to replacing it with the
# global variable 'anchor', normally set in the 
# 'graham_scan' function.
def polar_angle(p0,p1=None):
    if p1==None: p1=anchor
    y_span=p0[1]-p1[1]
    x_span=p0[0]-p1[0]
    return atan2(y_span,x_span)


# Returns the euclidean distance from p0 to p1,
# square root is not applied for sake of speed.
# If p1 is None, defaults to replacing it with the
# global variable 'anchor', normally set in the 
# 'graham_scan' function.
def distance(p0,p1=None):
    if p1==None: p1=anchor
    y_span=p0[1]-p1[1]
    x_span=p0[0]-p1[0]
    return y_span**2 + x_span**2


# Returns the determinant of the 3x3 matrix...
#   [p1(x) p1(y) 1]
#   [p2(x) p2(y) 1]
#   [p3(x) p3(y) 1]
# If >0 then counter-clockwise
# If <0 then clockwise
# If =0 then collinear
def det(p1,p2,p3):
    return   (p2[0]-p1[0])*(p3[1]-p1[1]) \
            -(p2[1]-p1[1])*(p3[0]-p1[0])


# Sorts in order of increasing polar angle from 'anchor' point.
# 'anchor' variable is assumed to be global, set from within 'graham_scan'.
# For any values with equal polar angles, a second sort is applied to
# ensure increasing distance from the 'anchor' point.
def quicksort(a):
    if len(a)<=1: return a
    smaller,equal,larger=[],[],[]
    piv_ang=polar_angle(a[randint(0,len(a)-1)]) # select random pivot
    for pt in a:
        pt_ang=polar_angle(pt) # calculate current point angle
        if   pt_ang<piv_ang:  smaller.append(pt)
        elif pt_ang==piv_ang: equal.append(pt)
        else:                 larger.append(pt)
    return   quicksort(smaller) \
            +sorted(equal,key=distance) \
            +quicksort(larger)


# Returns the vertices comprising the boundaries of
# convex hull containing all points in the input set. 
# The input 'points' is a list of (x,y) coordinates.
# If 'show_progress' is set to True, the progress in 
# constructing the hull will be plotted on each iteration.
def graham_scan(points,show_progress=False):
    global anchor # to be set, (x,y) with smallest y value

    # Find the (x,y) point with the lowest y value,
    # along with its index in the 'points' list. If
    # there are multiple points with the same y value,
    # choose the one with smallest x.
    min_idx=None
    for i,(x,y) in enumerate(points):
        if min_idx==None or y<points[min_idx][1]:
            min_idx=i
        if y==points[min_idx][1] and x<points[min_idx][0]:
            min_idx=i

    # set the global variable 'anchor', used by the
    # 'polar_angle' and 'distance' functions
    anchor=points[min_idx]

    # sort the points by polar angle then delete 
    # the anchor from the sorted list
    sorted_pts=quicksort(points)
    del sorted_pts[sorted_pts.index(anchor)]

    # anchor and point with smallest polar angle will always be on hull
    hull=[anchor,sorted_pts[0]]  
    for s in sorted_pts[1:]:
        while det(hull[-2],hull[-1],s)<=0:
            del hull[-1] # backtrack
            if len(hull)<2: break
        hull.append(s)
        if show_progress: scatter_plot(points,hull)
    return hull

