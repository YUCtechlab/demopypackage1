#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:16:13 2019

@author: usergkdev

This is a test package.
sm1function adds 2 numbers
function 1 multiplies the sum by factor 10 as default
"""
import os
import sys
import fire

from configparser import ConfigParser
from importlib import resources

file_dir = os.path.dirname(os.path.realpath(__file__))
print("\nDirectory of main function executed:", file_dir)

repo_name = os.path.abspath(os.path.join(file_dir, os.pardir))
                                         
print("\nLocal repo name: ", repo_name )

#%%
if (not repo_name in sys.path):
    sys.path.insert(0, repo_name)
print("\nsys.path: ", sys.path )


#%%
from demopypackage1 import p1module1

def function1(param1=2, param2=3):
    """ Simple demo function"""
    print("\nThis program simply calculates: (param1*10 + param2 + bias) ")
    print("Default output: 2 * 10 + 3 + 100 = 123")
    print("Can also run e.g. as; python -m demopypackage1 --param1 0 --param2 0")
    
    print("### start function1 in module p1module1 called by __main__")
     
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("demopypackage1", "config.txt"))
    bias = cfg.get("bias", "bias1")
      
    # fine param1 * 10 + param2
    res = p1module1.p1m1function1(param1, param2)
    res = res + int(bias)

    print("Result is: ", res, " just as expected!")

if __name__ == "__main__":
    fire.Fire(function1)

# function1()
