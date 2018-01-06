# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 18:12:14 2018

@author: aborsay
"""

def oddTuples(aTup):
    newTup =()
    for i,a in enumerate(aTup):
        if(i%2==0):
            newTup += (aTup[i],)
    return newTup


def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1


def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def how_many(aDict):
    numberOfValues = 0
    for k in aDict:
        numberOfValues += len(aDict[k])
    return numberOfValues

def biggest(aDict):
    largest = []
    for k in aDict:
        