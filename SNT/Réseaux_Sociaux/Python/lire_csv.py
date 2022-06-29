#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 20:57:28 2022

@author: pierre
"""

import csv

with open("../graphonline/exemple1.csv") as file_name : array = list(csv.reader(file_name))
tableau=[l[1:] for l in array[1:]]
print(array)
print(tableau)
