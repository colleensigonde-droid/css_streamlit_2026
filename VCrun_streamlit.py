# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 07:07:15 2026

@author: colle
"""

import subprocess

file = "VCApp_profiler.py"


subprocess.Popen(
    ["streamlit", "run", file], shell=True
)