# -*- coding: utf-8 -*-
"""
(Update 11/dec: The exercise was updated and simplified. Sorry for the disturbance.)

Given a list of points, for example P=[(5, 0), (2, 3), (6, 2), (1, 0)], in order to find the two closest points, we would need to compute that distance of every pair of points. That would be O(n²).

There is a faster algorithm which is O(n log(n)), as described here (planar case). Write a function closest_pair(points) that implements that algorithm and returns the minimum distance rounded to the units place.

    First of all: Pre-process step: order the points by the X-coordinate

    Now, call another function that:

    Splits the points into a left (L) and a right (R) list of same size.

Call your function recursively to compute the minimum distance of that left (dL) and right list (dR). Now, dLR = min(dL, dR). Do not forget to add the base case to the function.

In addition, we must also compare the points from the left list to the right list because there are points (like these two green points below) which are very close together. This step is slower than the previous one because computing the Euclidean distance between all points from the left list to all points of the right list is slow. We can improve that a little bit by first computing the X-distance between those points and filtering those points whose X-distance is smaller than dLR. (Computing the X-distance is much faster than the Euclidean-distance because the X-distance uses abs instead of sqrt.) The result of this will be dM.

Return the minimum between dLR and dM.

"""

def distance(a, b):
        x1, y1 = a
        x2, y2 = b
        return ((x2-x1)**2+(y2-y1)**2)**0.5

def calculate(alist, min_dist=9999999999):
    for x1, y1 in alist:
        for x2, y2 in alist:
            if abs(x2 - x1) < min_dist:
                dist = distance((x1,y1),(x2,y2))
                min_dist = dist if (dist != 0 and dist < min_dist) else min_dist
    return round(min_dist)

def closest_pair(points):
    points.sort()
    return calculate(points)