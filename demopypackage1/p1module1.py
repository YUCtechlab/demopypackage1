#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:16:13 2019

@author: usergkdev
"""

from demopypackage1.subpackage1 import p1sp1module1

def p1m1function1(param1, param2):
    """ function in the main package that calls a function from a subpackage"""
    
    print("#### start p1m1function1 in package1/p1module1")
    
    # find param1 * 10
    res = p1sp1module1.p1sp1m1function1(param1)
      
    res = res + param2
    return res


