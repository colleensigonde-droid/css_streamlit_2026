# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 05:21:25 2026

@author: colle
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Research Profile | Mechanical Engineering",
    layout="wide"
)
# Title of the app
st.title("Research Profile")
st.subheader("Vhahangwele Colleen Sigonde")

st.markdown(
    "### A research profile showcasing my work in mechanical engineering, "
    "nonlinear vibration analysis, and materials science."
)

st.caption("Mechanical Engineering • Nonlinear Vibration • Materials & FEA")

st.divider()

# Collect basic information
name="Ms. vhahangwele Colleen"
field="Mechanical Engineering-Dynamics and Materials"
institution = "Vaal University of Technology"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://blog.prosig.com/wp-content/uploads/2023/08/prosigdjb_a_featured_image_for_a_blog_article_on_the_basics_of__df65895c-d563-4211-995f-56107ce47fe2.png")

# add  ABOUT / RESEARCH IDENTITY  section
st.header("Research Identity")
st.markdown(
    """
I am a **Mechanical Engineering researcher and technologist** with a strong background in  
**nonlinear vibration analysis**, **fault diagnosis of rotating machinery**, and  
**materials-related engineering applications**.  

My research journey integrates **analytical modelling, numerical simulation, and experimental
investigation** to understand system behaviour and support engineering decision-making.
"""
)

# add  RESEARCH FOCUS  section

st.header("Research Focus")
st.markdown("""
- **Nonlinear vibration analysis**  
- **Fault diagnosis of rotating machinery**  
- **Vibration mechanics**  
- **Additive manufacturing and materials**  
- **Finite element analysis (FEA)**  
- **Materials science**
""")

# add SUMMARY OF COMPETENCE  section

st.header("Summary of Competence")
st.markdown("""
- **Laboratory testing & data acquisition:** setup and operation of complex experimental rigs;  
  data capture and handling using **Scout 2013** and **LabVIEW Analyzer**.  

- **Modelling & simulation:** development of engineering models and simulations using  
  **Mathcad**, **Simulink**, and **LabVIEW** for complex system behaviour.  

- **Engineering software proficiency:** **MATLAB**, **Origin**, **SolidWorks**, **Solid Edge**  
  for analysis, modelling, post-processing, and design support.  

- **Additive manufacturing support:** 3D printing design preparation and manufacturing
  simulation using **SolidWorks**.
""")

st.header("Publications")
st.markdown("""
1. **Sigonde, V. C.**, Koueiou, X. T., & Alugongo, A. A. (2022).  
   *Enhancing Fault Diagnosis of Gear Transmission Error Based on Experimental Analysis*.  
   **2022 IEEE 13th International Conference on Mechanical and Intelligent Manufacturing Technologies (ICMIMT)**, 135–140.  
   **DOI:** https://doi.org/10.1109/icmimt55556.2022.9845308

2. **Sigonde, V. C.**, Sozinando, D. F., Tchomeni, B. X., & Alugongo, A. A. (2025).  
   *Coupled Nonlinear Dynamic Modeling and Experimental Investigation of Gear Transmission Error for Enhanced Fault Diagnosis in Single-Stage Spur Gear Systems*.  
   **Dynamics**, 5, 37.  
   **DOI:** https://doi.org/10.3390/dynamics5030037
""")

# Add a contact section
st.header("Contact Information")
email = "vhahangweles@vut.ac.za"
st.write(f"You can reach {name} at {email}.")

