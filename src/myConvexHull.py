import numpy as np
from pandas import array

# sort the 2d array by x then by y
def sort(A: array) -> (array):
    array = np.array(A)
    indexSorted = np.lexsort((array[:,1],array[:,0]))

    sortedArray = []
    for i in indexSorted:
        sortedArray.append(A[i])

    return sortedArray

# find determinant, a helper function to find pointPosition
def determinant(P1: array, P2: array, P3: array) -> (float):
    x1, y1 = P1[0], P1[1]
    x2, y2 = P2[0], P2[1]
    x3, y3 = P3[0], P3[1]

    return x1 * y2 + x3 * y1 + x2 * y3 -  x3 * y2 - x2 * y1 - x1 * y3

# find whether a point P3 is above/below line P1P2
def pointPosition(P1: array, P2: array, P3: array) -> (int):
    if (determinant(P1, P2, P3) > 0): # above line P1P2
        return 1
    elif (determinant(P1, P2, P3) < 0): # below line P1P2
        return -1
    else: # in line P1P2
        return 0

# finding the farthest Point from line P1P2
def farthestPoint(P1: array, P2: array, arrayofPoints: array):
    
    # assume arrayofPoints is not empty
    x1, y1 = P1[0], P1[1]
    x2, y2 = P2[0], P2[1]
    tempFarthest = -999
    farthest = [-999,-999]
    for point in arrayofPoints:
        x, y = point[0], point[1]
        distance = (1/2) * abs((x1 - x) * (y2 - y1) - (x1 - x2) * (y - y1))
        if (distance > tempFarthest):
            tempFarthest = distance
            farthest = point

    return farthest

# find the solution Points
def findPoints(P1, P2, arrayofPoints, solutionPoints):
    
    if (len(arrayofPoints) == 0):
        pass
    else:

        # get the farthest point
        P3 = farthestPoint(P1, P2, arrayofPoints)

        # add the farthest point to the solution
        solutionPoints.append(P3)
        # remove it from the collection of points to be checked
        arrayofPoints.remove(P3)
        # remove P2, will add it again to the end
        if (P2 in solutionPoints):
            solutionPoints.remove(P2) 

        # check for points below the line P1P3 and P3P2
        belowP1P3 = []
        belowP3P2 = []
        for point in arrayofPoints:
            if (pointPosition(P1, P3, point) < 0):
                belowP1P3.append(point)       
            if (pointPosition(P3, P2, point) < 0):
                belowP3P2.append(point)

        # recursive
        findPoints(P1, P3, belowP1P3, solutionPoints)
        findPoints(P3, P2, belowP3P2, solutionPoints)

        # append to the end of solution points 
        solutionPoints.append(P2) 

def myConvexHull(A: array) -> (array):
    
    # sort the points ascending by x, then by y
    sortedArray = sort(A)

    # take the left-end point
    P1 = sortedArray[0]
    # take the right-end point
    P2 = sortedArray[len(sortedArray)-1]

    # add the left-end and right-end points to solution
    solutionPoints = []
    solutionPoints.append(P1)
    solutionPoints.append(P2)

    # remove the left-end point and the right-end point from the collection of points
    sortedArray.remove(P1)
    sortedArray.remove(P2)

    # divide the collection of points into above and below side
    above = []
    below = []
    for point in sortedArray:
        if (pointPosition(P1, P2, point) > 0): # if point is above line P1P2
            above.append(point)
        elif (pointPosition(P1, P2, point) < 0): # if point is below line P1P2
            below.append(point)
    
    # divide and conquer
    findPoints(P1, P2, below, solutionPoints) # find the convex hull points above
    findPoints(P2, P1, above, solutionPoints) # find the convex hull points below

    return solutionPoints