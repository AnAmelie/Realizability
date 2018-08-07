#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 02:04:33 2018

@author: katelyn
"""
import itertools as it
import copy
#recursion
"""
def toString(List):
    return ''.join(List)

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        print (toString(a))
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

# Driver program to test the above function
string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n-1)

# This code is contributed by Bhavya Jain






for string in itertools.imap(''.join, itertools.product('ABC', repeat=3)):
    print string

"""
#modding in the land of knots
def kmod(num, length):
    if num%(2*length) == 0:
        return int(2*length)
    else:
        return int(num%(2*length))
       


#find all the different permutations 
def getPathPermutations(evens):
    length = len(evens)
    indices = [i for i in range(length)]
    perms = []
    perms2 = []
    for i in range(2, length+1):
        array = list(it.permutations(indices, i))
        perms = perms + array 
    
    for j in perms:
        perms2.append(list(j))
    
    return perms2


#returns the diff array shifted over by however many specified as num.     
def getShift(array, num):
    
    shift = []
    for i in range(len(array)):
        shift.append(array[(i+num)%len(array)])
    return shift


#Returns the same array in reverse order
def getMirror(array):
    mirror = []
    for i in range(0, len(array)):
        mirror.append(array[len(array)-1-i])
        
    return mirror



#get the odd and diff array
def getOdds(ListOrLength): 
    odds = []
    if type(ListOrLength) == list:
        length = len(ListOrLength)
    else:
        length = ListOrLength
    for i in range(length):
        odds.append(2*i+1)

    return odds

#generate the list of equivalent paths
def getEquivalentPaths(path1):
    pathList = []
    mirror = getMirror(path1)
    
    for i in range(0, len(evens)):
        newpath = getShift(path1, i)
        newpath2 = getShift(mirror, i)
        
        if newpath not in pathList:
            pathList.append(newpath)
        if newpath2 not in pathList:
            pathList.append(newpath2)
            
            
    return pathList
    
    
    
#Check to see if two paths are equivalent
def isEquivalentPath(path1, path2):
    pathList = getEquivalentPaths(path1)
    if path2 in pathList:
        return True
    else:
        return False

#check to see if two numbers are connected
def isConnected(num1, num2, evens):
    length = len(evens)
    if num1 == kmod(num2+1, length) or num1 == kmod(num2-1, length):
        return True
    else:
        return False

#counts the number of subsets and returns True if the path has too many subsets to be a face
def hasTooManySubsets(path, pathlist, evens):
    #pathlist = getRealUniquePaths(evens)
    if path in pathlist:
        pathlist.remove(path)
    count = 0
    for i in pathlist:
        if set(i).issubset(set(path)):
            count = count + 1
            
    if count > len(path) - 2:
        return True
    else:
        return False
    


#Check to see if it's a real path
def isPath(path, evens):
    odds = getOdds(evens)
    #length = len(evens)
    pathlength = len(path)
    
    #first check to see if the path starting from the odd is connected
    oddfirst = True
    
    for i in range(pathlength+2):
        if isConnected( evens[(path[(i)%pathlength])], odds[(path[(i+1)%pathlength])], evens) == False:
            oddfirst = False
            break

    
    evenfirst = True
    for i in range(pathlength+2):
        if isConnected(odds[path[(i)%pathlength]], evens[path[(i+1)%pathlength]], evens) == False:
            evenfirst = False
            break
            #print ('evens', evens[path[(i+1)%pathlength]])
            #print('odds', odds[path[(i)%pathlength]])
            #print("")
            
    if oddfirst == True or evenfirst == True:
        
        return True
    else:
        return False
    

#get rid of all the paths which are equivalent to those already in the list. ex. (1,2,3) = (2, 3, 1) so only keep the first
def getUniquePaths(evens):
    allperms = getPathPermutations(evens)
    uniquepaths = []
    
    for i in allperms:
        addIt = True
        for j in uniquepaths:
            if isEquivalentPath(i, j) == True:
                addIt = False
        
        if addIt == True:
            uniquepaths.append(i)
            
    return uniquepaths


#Just get the length n paths
def getNLengthPaths(evens, n):
    perms = getUniquePaths(evens)
    perms2 = []
    
    for i in perms:
        if len(i) == n:
            if isPath(i, evens):
                perms2.append(i)
            
    return perms2



#This takes forevverrrrrrrr. Don't call it unless absolutely necessary
    
#Check to see if all the paths are actually real. Return only unique paths
def getRealUniquePaths(evens):
    uniquepaths = getUniquePaths(evens)
    realpaths = []
    finalpaths = []
    
    #Determine if they're actually paths. Only add them if they are. 
    for i in uniquepaths:
        if isPath(i, evens) == True:
            realpaths.append(i)
    """     
    
    #determining if they have too many subsets. Get rid of the path if it does
    for k in realpaths:
        count = 0
     
        for i in realpaths:
            if set(i).issubset(set(k)):
                count = count + 1
        
        
        if count < len(k) - 1:
            finalpaths.append(k)

    #88888888888888888888888888888888888888
    """
    
    
    return finalpaths
 
    

#def getFaces(evens):
    



    
evens = [6,8,2,4]
#odds = [1, 3, 5]
#print(getMirror(odds))

#print (getPathPermutations(evens))
#print ("")

#pathlist11 = getUniquePaths(evens)
#pathlist11 = getNLengthPaths(evens, 3)

pathlist111 = getRealUniquePaths(evens)
"""
for i in pathlist11:
    if isPath(i, evens) == True:
        pathlist111.append(i)
        print("True")
"""


for i in pathlist111:
    print (i)
    print (isPath(i, evens))
    print ("")
    
    
#print(hasTooManySubsets([1,2,4,3], pathlist evens))
#print(isEquivalent([1,2,3], [2,3,4]))
#print(getEquivalentpaths([1,2,3, 4]))

#print (isPath([0,1], evens))

#print (isConnected(10, 1, evens))

#print (isPath([0,2,1,3], evens))
