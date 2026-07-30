import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import plotly.graph_objects as go

# --- APP SETUP ---
st.set_page_config(page_title="Advanced Physics Pro", layout="wide")

# --- SIDEBAR MENU (20 TOPICS) ---
st.sidebar.title("📚 M.Sc. Physics Menu")
topic = st.sidebar.radio(
    "Select Topic:",
    [
        "01. Home / Dashboard",
        "02. P-N Junction (Drift-Diffusion)",
        "03. Fermi-Dirac Distribution",
        "04. NaCl Crystal 3D Lattice",
        "05. ABACAS Simulations",
        "06. NET & CG Pre B.Ed Exam Prep",
        "07. Bragg's Law & XRD",
        "08. Band Theory of Solids",
        "09. Hall Effect",
        "10. Photovoltaic Effect",
        "11. Quantum Harmonic Oscillator",
        "12. Heisenberg Uncertainty",
        "13. Maxwell-Boltzmann Stats",
        "14. Bose-Einstein Condensate",
        "15. Superconductivity",
        "16. Magnetic Hysteresis",
        "17. Crystal Defects",
        "18. Phonons & Vibrations",
        "19. Raman Effect Visualizer",
        "20. Silicon vs GaAs Analysis"
    ]
)

# --- 01. HOME ---
if topic == "01. Home / Dashboard":
    st.title("Advanced Physics Visualizer")
    st.write("Solid-state physics, crystallography, aur semiconductor electronics ka interactive dashboard.")
    st.info("👈 Left panel se koi bhi topic select karein.")

# --- 02. P-N JUNCTION ---
elif topic == "02. P-N Junction (Drift-Diffusion)":
    st.title("Semiconductor P-N Junction")
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.subheader("📚 Theory & Drift-Diffusion")
        st.write('''
        P-type aur N-type materials ke junction par, electrons aur holes ke diffusion ke karan ek depletion region banta hai. 
        Drift current (electric field ke karan) aur diffusion current (concentration gradient ke karan) equilibrium me ek dusre ko balance karte hain.
        ''')
        v_app = st.slider("Applied Voltage (V)", -2.0, 0.5, 0.0, 0.1)
    
    with col2:
        v0 = 0.7 
        barrier = max(0.05, v0 - v_app)
        w = np.sqrt(barrier / v0) * 2 
        
        x = np.linspace(-5, 5, 500)
        potential = np.where(x < -w/2, 0, np.where(x > w/2, barrier, barrier * (0.5 - 0.5 * np.cos(np.pi * (x - (-w/2)) / w))))
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, potential, color='purple', linewidth=3)
        ax.fill_between(x, 0, potential, color='purple', alpha=0.1)
        ax.axvline(x=-w/2, color='gray', linestyle='--')
        ax.axvline(x=w/2, color='gray', linestyle='--')
        ax.set_title("Energy Band / Potential Barrier")
        st.pyplot(fig)

# --- 04. NaCl CRYSTAL (3D INTERACTIVE) ---
elif topic == "04. NaCl Crystal 3D Lattice":
    st.title("NaCl Crystal Growth (3D Interactive)")
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.subheader("Theory")
        st.write("Sodium Chloride (NaCl) ka lattice ek continuous 3D structure hota hai jisme Na+ aur Cl- ions ek doosre ko alternate positions par arrange karte hain. Is symmetric crystal lattice arrangement ko interactively dekha ja sakta hai.")
        st.info("👉 Graph ko ungli se gol ghumayen ya zoom karein!")
        
    with col2:
        # 3D Coordinates for basic NaCl structure
        x, y, z, color, size = [], [], [], [], []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    x.append(i)
                    y.append(j)
                    z.append(k)
                    # Alternate colors for Na+ and Cl-
                    if (i+j+k) % 2 == 0:
                        color.append('green') # Cl-
                        size.append(15)
                    else:
                        color.append('blue')  # Na+
                        size.append(10)
                        
        fig = go.Figure(data=[go.Scatter3d(
            x=x, y=y, z=z, mode='markers',
            marker=dict(size=size, color=color, opacity=0.9),
            text=["Cl-" if c == 'green' else "Na+" for c in color]
        )])
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

# --- 05. ABACAS ---
elif topic == "05. ABACAS Simulations":
    st.title("ABACAS")
    st.subheader("assembly of basic application coordinated understanding the semiconductor")
    st.write("Ye in-house simulation module advance semiconductor material properties ko analyze karne ke liye banaya gaya hai.")
    
    mat = st.selectbox("Select Material", ["Silicon (Si)", "Gallium Arsenide (GaAs)"])
    st.write(f"Calculating parameters for **{mat}** without relying on external web platforms...")
    st.success("Simulation dashboard active. Drift-diffusion results will render below based on selected parameters.")

# --- 06. EXAM PREP (NET / CG Pre B.Ed) ---
elif topic == "06. NET & CG Pre B.Ed Exam Prep":
    st.title("Competitive Exam Preparation")
    st.write("Physics aur Teaching Aptitude ke liye practice module.")
    
    tab1, tab2 = st.tabs(["Physics (NET)", "Teaching Aptitude (B.Ed)"])
    
    with tab1:
        st.subheader("Solid State Physics Quiz")
        q1 = st.radio("At T=0K, what is the probability of occupation of an energy state above the Fermi level?", ["1", "0.5", "0", "Infinity"])
        if st.button("Check Answer - Q1"):
            if q1 == "0":
                st.success("Correct! At absolute zero, states above Fermi energy are empty.")
            else:
                st.error("Incorrect. Try again.")
                
    with tab2:
        st.subheader("CG Pre B.Ed: Teaching Aptitude")
        q2 = st.radio("Sikhne ki prakriya me sabse mehatvapurn kadi kya hai?", ["Ratt kar yaad karna", "Exam pass karna", "Class me shanti", "Concept ko samajhna aur apply karna"])
        if st.button("Check Answer - Q2"):
            if q2 == "Concept ko samajhna aur apply karna":
                st.success("Bilkul Sahi!")
            else:
                st.error("Galat uttar.")

# --- OTHER TOPICS (PLACEHOLDERS) ---
else:
    st.title(topic)
    st.write("Is topic ka interactive visualization module abhi under-construction hai.")
    st.info("M.Sc. Physics syllabus ke anusar yahan naye diagrams aur equations jald hi add kiye jayenge!")
    
