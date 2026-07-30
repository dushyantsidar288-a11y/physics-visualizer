import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# --- APP SETUP ---
st.set_page_config(page_title="Advanced Physics Pro", layout="wide")

# --- SIDEBAR MENU (20 TOPICS) ---
st.sidebar.title("📚 M.Sc. Physics Menu")
topic = st.sidebar.radio(
    "Select Topic:",
    [
        "01. Home / Dashboard",
        "02. P-N Junction",
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
    st.title("Advanced Physics Educational Platform")
    st.write("Ye platform solid-state physics, crystallography, aur semiconductor electronics ke adhyayan ke liye banaya gaya hai.")
    st.info("👈 Bayen taraf diye gaye menu se koi bhi topic chun kar uski vistarit theory aur interactive graph dekhein.")

# --- 02. P-N JUNCTION ---
elif topic == "02. P-N Junction":
    st.title("Semiconductor P-N Junction")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("P-type aur N-type semiconductors ke milne se depletion region banta hai. Diffusion aur drift currents ke balance hone se built-in potential set hota hai.")
        v_app = st.slider("Applied Voltage (V)", -2.0, 0.5, 0.0, 0.1)
    with col2:
        v0 = 0.7 
        barrier = max(0.05, v0 - v_app)
        w = np.sqrt(barrier / v0) * 2 
        x = np.linspace(-5, 5, 500)
        potential = np.where(x < -w/2, 0, np.where(x > w/2, barrier, barrier * (0.5 - 0.5 * np.cos(np.pi * (x - (-w/2)) / w))))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, potential, color='purple', linewidth=3)
        ax.set_title("Potential Barrier & Depletion Width")
        st.pyplot(fig)

# --- 03. FERMI-DIRAC ---
elif topic == "03. Fermi-Dirac Distribution":
    st.title("Fermi-Dirac Distribution")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Fermions ke liye energy states me electrons ki probability occupation ko yeh function darshata hai: f(E) = 1 / (exp((E-EF)/kT) + 1)")
        T = st.slider("Temperature (K)", 0, 1000, 300, 50)
    with col2:
        E = np.linspace(0, 1, 500)
        E_f = 0.5
        k = 8.617e-5
        f_E = np.where(T == 0, np.where(E <= E_f, 1.0, 0.0), 1 / (np.exp((E - E_f) / (k * T)) + 1))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(E, f_E, color='blue', linewidth=2.5)
        ax.axvline(E_f, color='red', linestyle='--')
        ax.set_title(f"Fermi Distribution at T = {T} K")
        st.pyplot(fig)

# --- 04. NaCl CRYSTAL ---
elif topic == "04. NaCl Crystal 3D Lattice":
    st.title("NaCl Crystal Structure (3D)")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Sodium Chloride ka lattice face-centered cubic structure me hota hai jisme Na+ aur Cl- ions alternate positions par sthit hote hain.")
    with col2:
        x, y, z, color, size = [], [], [], [], []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    x.append(i); y.append(j); z.append(k)
                    if (i+j+k) % 2 == 0:
                        color.append('green'); size.append(15)
                    else:
                        color.append('blue'); size.append(10)
        fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=size, color=color, opacity=0.9))])
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

# --- 05. ABACAS ---
elif topic == "05. ABACAS Simulations":
    st.title("ABACAS Simulations")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Semiconductor material transport properties aur drift velocity analysis module.")
        mat = st.selectbox("Select Material", ["Silicon (Si)", "Gallium Arsenide (GaAs)"])
    with col2:
        mu_e, mu_h, Eg = (1400, 450, 1.12) if mat == "Silicon (Si)" else (8500, 400, 1.42)
        E_field = np.linspace(0, 10000, 100)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(E_field, mu_e * E_field / 10000, label="Electron Drift", color='blue')
        ax.plot(E_field, mu_h * E_field / 10000, label="Hole Drift", color='red', linestyle='--')
        ax.set_title(f"Drift Velocity ({mat})")
        ax.legend()
        st.pyplot(fig)

# --- 06. EXAM PREP ---
elif topic == "06. NET & CG Pre B.Ed Exam Prep":
    st.title("Exam Prep Module")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Physics Quiz")
        q1 = st.radio("At T=0K, probability above Fermi level?", ["1", "0.5", "0", "Infinity"])
        if st.button("Check Physics"):
            st.success("Correct!") if q1 == "0" else st.error("Incorrect.")
    with col2:
        st.subheader("B.Ed Quiz")
        q2 = st.radio("Learning me mehatvapurn:", ["Rattna", "Concept samajhna", "Shanti", "Exam"], key="b2")
        if st.button("Check B.Ed"):
            st.success("Sahi hai!") if q2 == "Concept samajhna" else st.error("Galat.")

# --- 07. BRAGG'S LAW ---
elif topic == "07. Bragg's Law & XRD":
    st.title("Bragg's Law & XRD")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("X-ray diffraction ke liye 2d sin(theta) = n*lambda formula use hota hai.")
        lam = st.slider("Wavelength", 0.5, 2.0, 1.5)
        d = st.slider("Spacing d", 1.0, 5.0, 2.0)
    with col2:
        theta = np.linspace(0, 90, 500)
        intensity = np.zeros_like(theta)
        for n in range(1, 4):
            val = (n * lam) / (2 * d)
            if val <= 1:
                intensity += np.exp(-((theta - np.degrees(np.arcsin(val)))**2) / 1.5)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(theta, intensity, color='crimson')
        ax.set_title("XRD Intensity Peaks")
        st.pyplot(fig)

# --- 08. BAND THEORY ---
elif topic == "08. Band Theory of Solids":
    st.title("Band Theory of Solids")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Valence band aur Conduction band ke beech energy gap solid ki conductivity tay karta hai.")
        mat_type = st.selectbox("Type", ["Insulator", "Semiconductor", "Conductor"])
    with col2:
        gap = 5.0 if mat_type == "Insulator" else (1.1 if mat_type == "Semiconductor" else 0.0)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Valence Band", "Conduction Band"], [1, 1], bottom=[-1, gap], color=['blue', 'orange'], width=0.5)
        ax.set_title(f"Bandgap: {mat_type}")
        st.pyplot(fig)

# --- 09. HALL EFFECT ---
elif topic == "09. Hall Effect":
    st.title("Hall Effect")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Magnetic field aur current ke perpendicular transverse voltage (VH = I*B / t*n*q) generate hota hai.")
        B = st.slider("Magnetic Field B", 0.1, 5.0, 1.0)
        I = st.slider("Current I", 1.0, 100.0, 10.0)
    with col2:
        B_arr = np.linspace(0, 5, 100)
        V_h = (I * 1e-3 * B_arr) / (1.0e-3 * 1e22 * 1.6e-19) * 1000
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(B_arr, V_h, color='navy')
        ax.set_title("Hall Voltage vs Field")
        st.pyplot(fig)

# --- 10. PHOTOVOLTAIC EFFECT ---
elif topic == "10. Photovoltaic Effect":
    st.title("Photovoltaic Effect")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Photons ke absorption se electron-hole pairs ban kar solar current generate karte hain.")
        light = st.slider("Light Intensity", 0.1, 2.0, 1.0)
    with col2:
        V = np.linspace(0, 0.6, 100)
        I_curr = light * 5 - 5 * (np.exp(V / 0.026) - 1)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(V, I_curr, color='darkorange')
        ax.set_title("Solar Cell I-V Curve")
        st.pyplot(fig)

# --- 11. QUANTUM HARMONIC OSCILLATOR ---
elif topic == "11. Quantum Harmonic Oscillator":
    st.title("Quantum Harmonic Oscillator")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Quantized energy levels En = (n + 1/2) hbar omega.")
        n_state = st.slider("State n", 0, 5, 0)
    with col2:
        x = np.linspace(-4, 4, 400)
        psi_sq = np.exp(-x**2) * (x**2)**n_state
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, psi_sq, color='teal')
        ax.set_title(f"Probability Density n={n_state}")
        st.pyplot(fig)

# --- 12. HEISENBERG UNCERTAINTY ---
elif topic == "12. Heisenberg Uncertainty":
    st.title("Heisenberg Uncertainty")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("dx * dp >= hbar / 2 relation.")
        dx = st.slider("dx", 0.01, 1.0, 0.1)
    with col2:
        dp = 0.5 / dx
        st.metric("Min dp", f"{dp:.3f}")
        p = np.linspace(-5, 5, 200)
        dist = np.exp(-(p)**2 / (2 * dp**2))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(p, dist, color='purple')
        ax.set_title("Momentum Spread")
        st.pyplot(fig)

# --- 13. MAXWELL-BOLTZMANN STATS ---
elif topic == "13. Maxwell-Boltzmann Stats":
    st.title("Maxwell-Boltzmann Stats")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Classical particles energy distribution.")
        temp = st.slider("Temp (K)", 100, 1000, 300)
    with col2:
        v = np.linspace(0, 2000, 200)
        f_v = v**2 * np.exp(-v**2 / (2 * temp))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(v, f_v, color='brown')
        ax.set_title("Speed Distribution")
        st.pyplot(fig)

# --- 14. BOSE-EINSTEIN CONDENSATE ---
elif topic == "14. Bose-Einstein Condensate":
    st.title("Bose-Einstein Condensate")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Bosons collapse into lowest quantum state at low temperatures.")
        T_bec = st.slider("T/Tc ratio", 0.0, 2.0, 0.5)
    with col2:
        frac = max(0.0, 1.0 - T_bec**1.5) if T_bec <= 1 else 0.0
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["BEC Fraction"], [frac], color='blue', width=0.4)
        ax.set_ylim(0, 1)
        st.pyplot(fig)

# --- 15. SUPERCONDUCTIVITY ---
elif topic == "15. Superconductivity":
    st.title("Superconductivity")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Zero resistance and Meissner effect below critical temperature.")
        T = st.slider("Temp (K)", 1, 20, 5)
    with col2:
        res = 0.0 if T < 9.2 else 1.0
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Resistance"], [res], color='green' if res==0 else 'red', width=0.4)
        ax.set_ylim(0, 1.2)
        st.pyplot(fig)

# --- 16. MAGNETIC HYSTERESIS ---
elif topic == "16. Magnetic Hysteresis":
    st.title("Magnetic Hysteresis")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Ferromagnetic B-H loop characteristics.")
        c_fac = st.slider("Coercivity", 0.5, 2.0, 1.0)
    with col2:
        H = np.linspace(-5, 5, 200)
        B = 1.5 * np.tanh(H / c_fac)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(H, B, color='black')
        ax.set_title("B-H Loop")
        st.pyplot(fig)

# --- 17. CRYSTAL DEFECTS ---
elif topic == "17. Crystal Defects":
    st.title("Crystal Defects")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Real crystals me ideal periodicity nahi hoti. Inme point defects, line defects aur surface defects hote hain jo mechanical strength ko prabhavit karte hain.")
        d_type = st.selectbox("Defect", ["Vacancy", "Interstitial", "Dislocation"])
    with col2:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(np.random.rand(10), np.random.rand(10), s=100, color='blue')
        ax.set_title(f"Defect View: {d_type}")
        st.pyplot(fig)

# --- 18. PHONONS & VIBRATIONS ---
elif topic == "18. Phonons & Vibrations":
    st.title("Phonons & Vibrations")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Collective lattice atomic vibrations.")
        q = np.linspace(0, np.pi, 100)
    with col2:
        omega = 2 * np.sin(q / 2)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(q, omega, color='magenta')
        ax.set_title("Dispersion Relation")
        st.pyplot(fig)

# --- 19. RAMAN EFFECT VISUALIZER ---
elif topic == "19. Raman Effect Visualizer":
    st.title("Raman Effect")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Inelastic scattering producing Stokes and Anti-Stokes lines.")
        shift = st.slider("Shift", 200, 1000, 500)
    with col2:
        x_s = np.linspace(-1500, 1500, 300)
        y = np.exp(-x_s**2 / 10000) + 0.6 * np.exp(-((x_s - shift)**2) / 4000)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x_s, y, color='darkcyan')
        ax.set_title("Raman Spectrum")
        st.pyplot(fig)

# --- 20. SILICON VS GaAs ANALYSIS ---
elif topic == "20. Silicon vs GaAs Analysis":
    st.title("Silicon vs GaAs")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Detailed Theory")
        st.write("Indirect vs Direct bandgap comparison.")
        prop = st.selectbox("Property", ["Bandgap", "Mobility"])
    with col2:
        val_si = 1.12 if prop == "Bandgap" else 1400
        val_gaas = 1.42 if prop == "Bandgap" else 8500
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Silicon", "GaAs"], [val_si, val_gaas], color=['blue', 'green'], width=0.5)
        ax.set_title(f"Comparison: {prop}")
        st.pyplot(fig)
    
