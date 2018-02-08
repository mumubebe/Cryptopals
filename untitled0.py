#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:14:11 2018

@author: danielmurberg
"""

def len_recurring(n, d, history):
    if n == 0:
        return -1
    if (n, d) in history:
        dist = len(history) - history.index((n, d))
        return dist
    if(n // d):
        history.append((10 * (n % d), d))
        return len_recurring(10 * (n % d), d, history)
    else:
        history.append((10 * n, d))
        return len_recurring(10 * n, d, history)


print(len_recurring(2, 6, []))