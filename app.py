import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App Setup
st.set_page_config(page_title="Physics Visualizer", layout="wide")

# Sidebar Navigation
st.sidebar.title("Physics Menu")
st.sidebar.write("Select a topic below:")
topic = st.sidebar.radio(
    "Topics",
    [
        "Home", 
        "1. Fermi-Dirac Distribution", 
        "2. P-N Junction", 
        "3. NaCl Crystal Growth",
        "4. ABACAS Simulations"
    ]
)

# Home Page
if topic == "Home":
    st.title("Welcome to Physics Visualizer")
    st.write("Interactive visualizations for solid-state and semiconductor physics.")
    st.info("👈 Left side menu se koi bhi topic select karein.")

# Topic 1: Fermi-Dirac
elif topic == "1. Fermi-Dirac Distribution":
    st.title("Fermi-Dirac Distribution")
    st.write("Energy state probabilities at different temperatures.")
    
    T = st.slider("Temperature (Kelvin)", min_value=0, max_value=1000, value=300, step=50)
    
    k = 8.617e-5  
    E_f = 0.5     
    E = np.linspace(0, 1, 500)
    
    if T == 0:
        f_E = np.where(E <= E_f, 1.0, 0.0)
    else:
        f_E = 1 / (np.exp((E - E_f) / (k * T)) + 1)
        
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(E, f_E, color='blue', linewidth=2)
    ax.set_title(f"Fermi-Dirac Function at T = {T} K")
    ax.set_xlabel("Energy (eV)")
    ax.set_ylabel("Probability f(E)")
    ax.axvline(x=E_f, color='red', linestyle='--', label="Fermi Energy")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# Topic 2: P-N Junction
elif topic == "2. P-N Junction":
    st.title("Semiconductor P-N Junction")
    st.write("Drift-diffusion characteristics and built-in potential.")
    
    x = np.linspace(-5, 5, 400)
    potential = 0.5 * (np.tanh(x) + 1)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, potential, color='purple', linewidth=2)
    ax.set_title("Built-in Potential")
    ax.set_xlabel("Position")
    ax.set_ylabel("Potential (V)")
    ax.grid(True)
    st.pyplot(fig)

# Topic 3: NaCl Crystal Growth
elif topic == "3. NaCl Crystal Growth":
    st.title("NaCl Crystal Growth")
    st.write("Visualization of the sodium chloride crystal lattice arrangement.")
    st.info("The atomic arrangement forms a continuous and repeating crystal structure.")

# Topic 4: ABACAS
elif topic == "4. ABACAS Simulations":
    st.title("ABACAS")
    st.subheader("assembly of basic application coordinated understanding the semiconductor")
    st.write("Advanced semiconductor material simulations and parameter configuration.")
