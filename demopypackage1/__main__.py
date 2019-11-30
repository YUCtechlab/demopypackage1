#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:16:13 2019

@author: usergkdev

This is a test package.
sm1function adds 2 numbers
function 1 multiplies the sum by factor 10 as default
"""

'''
Date:
=====
2019 11 30

Project status:
===============
Finished.

Issues why project unfinished:
==============================
none

Purpose:
========
To demo how to create a Python package, host it on GitHub
and publish it to PyPI, so other people can install the package.

Description:
============
Main script is __main__.py.
This calls p1module1.py
The overall functionality is super simple, just some math.

Inspired by/some code reuse from:
=================================
tbd

Python environment: conda activate <...>
========================================
base

How to edit:
============
Spyder in above environment

Input files consumed:
=====================
config.txt

Output files written:
=====================
none

Visual output:
==============
See stdout

Configuration file:
===================
config.txt

Configuration to do:
====================
none

How to run:
===========
Experiment 1
============
From folder: 
------------
demopypackage1

Command:
--------
python -m demopypackage1 --param1 0 --param2 0

Run from Spyder console:
------------------------
Just run the script __main__.py when open

Assumptions this module makes:
==============================
Uses:
    fire
    importlib
    configparser
'''


import os
import socket
import sys
import fire

from configparser import ConfigParser
from importlib import resources

print("\n*******************************************************")
print("Welcome to this test script for a Python package")
print("*******************************************************")
hostname=socket.gethostname()
print("Hostname =             ", hostname)
print("Current working dir =  ", os.getcwd() )

file_dir = os.path.dirname(os.path.realpath(__file__))
print("\nDirectory of main function executed:", file_dir)

repo_name = os.path.abspath(os.path.join(file_dir, os.pardir))
                                         
print("\nLocal repo name: ", repo_name )
print("\nPython version: ", sys.version)

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
    print("\nbias read from config.txt: ", bias)
      
    # fine param1 * 10 + param2
    res = p1module1.p1m1function1(param1, param2)
    res = res + int(bias)

    print("Result is: ", res, " just as expected!")

if __name__ == "__main__":
    fire.Fire(function1)

# function1()
