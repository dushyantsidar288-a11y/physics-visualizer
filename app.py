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
        st.write("P-type aur N-type materials ke junction par depletion region banta hai. Drift aur diffusion currents equilibrium me balance hoti hain.")
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
        ax.set_title("Energy Band / Potential Barrier")
        st.pyplot(fig)

# --- 03. FERMI-DIRAC ---
elif topic == "03. Fermi-Dirac Distribution":
    st.title("Fermi-Dirac Distribution")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Theory")
        st.write("Fermions ke liye energy states me electrons ki probability distribution ko darshata hai: $f(E) = \\frac{1}{e^{(E-E_F)/kT} + 1}$")
        T = st.slider("Temperature (K)", 0, 1000, 300, 50)
    with col2:
        E = np.linspace(0, 1, 500)
        E_f = 0.5
        k = 8.617e-5
        f_E = np.where(T == 0, np.where(E <= E_f, 1.0, 0.0), 1 / (np.exp((E - E_f) / (k * T)) + 1))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(E, f_E, color='blue', linewidth=2)
        ax.axvline(E_f, color='red', linestyle='--', label="Fermi Energy")
        ax.set_title(f"Fermi Function at T={T}K")
        ax.grid(True)
        st.pyplot(fig)

# --- 04. NaCl CRYSTAL (3D) ---
elif topic == "04. NaCl Crystal 3D Lattice":
    st.title("NaCl Crystal Growth (3D Interactive)")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.subheader("Theory")
        st.write("Sodium Chloride ka lattice ek continuous 3D repeating structure banata hai jisme Na+ aur Cl- ions alternate positions par hote hain.")
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
    st.title("ABACAS")
    st.subheader("assembly of basic application coordinated understanding the semiconductor")
    mat = st.selectbox("Select Material", ["Silicon (Si)", "Gallium Arsenide (GaAs)"])
    mu_e, mu_h, Eg = (1400, 450, 1.12) if mat == "Silicon (Si)" else (8500, 400, 1.42)
    color = 'blue' if mat == "Silicon (Si)" else 'green'
    E_field = np.linspace(0, 10000, 100)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(E_field, mu_e * E_field / 10000, label="Electron Drift", color=color)
    ax.plot(E_field, mu_h * E_field / 10000, label="Hole Drift", color='red', linestyle='--')
    ax.set_title(f"Drift Velocity ({mat}, Eg={Eg}eV)")
    ax.legend()
    st.pyplot(fig)

# --- 06. EXAM PREP ---
elif topic == "06. NET & CG Pre B.Ed Exam Prep":
    st.title("Competitive Exam Preparation")
    tab1, tab2 = st.tabs(["Physics (NET)", "Teaching Aptitude (B.Ed)"])
    with tab1:
        st.subheader("Solid State Physics Quiz")
        q1 = st.radio("At T=0K, probability of occupation above Fermi level?", ["1", "0.5", "0", "Infinity"])
        if st.button("Check Q1"):
            st.success("Correct!") if q1 == "0" else st.error("Incorrect.")
    with tab2:
        st.subheader("CG Pre B.Ed")
        q2 = st.radio("Sikhne me sabse mehatvapurn:", ["Rattna", "Concept samajhna", "Shanti", "Exam"])
        if st.button("Check Q2"):
            st.success("Bilkul Sahi!") if q2 == "Concept samajhna" else st.error("Galat.")

# --- 07. BRAGG'S LAW ---
elif topic == "07. Bragg's Law & XRD":
    st.title("Bragg's Law & XRD")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory: $2d \\sin\\theta = n\\lambda$")
        wavelength = st.slider("Wavelength", 0.5, 2.0, 1.5)
        d_spacing = st.slider("Spacing d", 1.0, 5.0, 2.0)
    with col2:
        theta = np.linspace(0, 90, 500)
        intensity = np.zeros_like(theta)
        for n in range(1, 4):
            val = (n * wavelength) / (2 * d_spacing)
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
        st.subheader("Theory")
        st.write("Bloch theorem ke anusar periodic potential me electrons ki energy bands (Valence band aur Conduction band) banti hain.")
        mat_type = st.selectbox("Material Type", ["Insulator", "Semiconductor", "Conductor"])
    with col2:
        fig, ax = plt.subplots(figsize=(6, 4))
        gap = 5.0 if mat_type == "Insulator" else (1.1 if mat_type == "Semiconductor" else 0.0)
        ax.bar(["Valence Band", "Conduction Band"], [1, 1], bottom=[-1, gap], color=['blue', 'orange'])
        ax.set_title(f"Energy Band Gap: {mat_type}")
        st.pyplot(fig)

# --- 09. HALL EFFECT ---
elif topic == "09. Hall Effect":
    st.title("Hall Effect & Carrier Concentration")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory: $V_H = \\frac{IB}{tnq}$")
        B = st.slider("Magnetic Field B (T)", 0.1, 5.0, 1.0)
        I = st.slider("Current I (mA)", 1.0, 100.0, 10.0)
    with col2:
        B_arr = np.linspace(0, 5, 100)
        V_h = (I * 1e-3 * B_arr) / (1.0e-3 * 1e22 * 1.6e-19) * 1000
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(B_arr, V_h, color='navy')
        ax.set_title("Hall Voltage vs Magnetic Field")
        st.pyplot(fig)

# --- 10. PHOTOVOLTAIC EFFECT ---
elif topic == "10. Photovoltaic Effect":
    st.title("Photovoltaic Effect (Solar Cell)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Light photons ke absorption se electron-hole pairs generate hote hain jo junction field ke karan separate hokar current banate hain.")
        light_intensity = st.slider("Light Intensity (Suns)", 0.1, 2.0, 1.0)
    with col2:
        V = np.linspace(0, 0.6, 100)
        I = light_intensity * 5 - 5 * (np.exp(V / 0.026) - 1)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(V, I, color='darkorange', linewidth=2)
        ax.set_title("I-V Characteristic Curve")
        st.pyplot(fig)

# --- 11. QUANTUM HARMONIC OSCILLATOR ---
elif topic == "11. Quantum Harmonic Oscillator":
    st.title("Quantum Harmonic Oscillator")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Energy levels: $E_n = (n + \\frac{1}{2})\\hbar\\omega$. Ye molecular vibrations aur lattice phonons ko samajhne me kaam aata hai.")
        n_state = st.slider("Quantum Number n", 0, 5, 0)
    with col2:
        x = np.linspace(-4, 4, 400)
        psi = np.exp(-x**2 / 2) * eval(f"np.polynomial.hermite.hermite_val(x, [0]*{n_state} + [1])") if n_state > 0 else np.exp(-x**2 / 2)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, psi**2, color='teal')
        ax.set_title(f"Probability Density (|psi|^2) for n={n_state}")
        st.pyplot(fig)

# --- 12. HEISENBERG UNCERTAINTY ---
elif topic == "12. Heisenberg Uncertainty":
    st.title("Heisenberg Uncertainty Principle")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("$\\Delta x \\cdot \\Delta p \\ge \\frac{\\hbar}{2}$. Position aur momentum ko ek sath ekdam sateek tarike se nahi maapa ja sakta.")
        dx = st.slider("Position Uncertainty (dx)", 0.01, 1.0, 0.1)
    with col2:
        dp = 0.5 / dx  # Minimum uncertainty product limit
        st.metric(label="Min Momentum Uncertainty (dp)", value=f"{dp:.3f}")
        p = np.linspace(-5, 5, 200)
        dist = np.exp(-(p)**2 / (2 * dp**2))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(p, dist, color='purple')
        ax.set_title("Momentum Distribution Spread")
        st.pyplot(fig)

# --- 13. MAXWELL-BOLTZMANN STATS ---
elif topic == "13. Maxwell-Boltzmann Stats":
    st.title("Maxwell-Boltzmann Statistics")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Classical particles ke liye energy distribution state.")
        temp = st.slider("Temperature (K) MB", 100, 1000, 300)
    with col2:
        v = np.linspace(0, 2000, 200)
        m = 4.65e-26 # Mass of N2 approx
        k_b = 1.38e-23
        f_v = (m / (2 * np.pi * k_b * temp))**1.5 * 4 * np.pi * v**2 * np.exp(-m * v**2 / (2 * k_b * temp))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(v, f_v * 1e10, color='brown')
        ax.set_title("Speed Distribution")
        st.pyplot(fig)

# --- 14. BOSE-EINSTEIN CONDENSATE ---
elif topic == "14. Bose-Einstein Condensate":
    st.title("Bose-Einstein Condensate (BEC)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Ultra-low temperatures par bosons ek hi quantum state me collapse ho jate hain.")
        T_bec = st.slider("Temperature Ratio (T/Tc)", 0.0, 2.0, 1.0)
    with col2:
        frac = max(0.0, 1.0 - T_bec**1.5) if T_bec <= 1 else 0.0
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Condensate Fraction"], [frac], color='blue', width=0.4)
        ax.set_ylim(0, 1)
        ax.set_title("BEC Population Fraction")
        st.pyplot(fig)

# --- 15. SUPERCONDUCTIVITY ---
elif topic == "15. Superconductivity":
    st.title("Superconductivity & Meissner Effect")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Zero electrical resistance aur magnetic field ka expulsion (Meissner effect) critical temperature ($T_c$) ke niche.")
        T = st.slider("Operating Temp (K)", 1, 20, 5)
        Tc = 9.2 # e.g. Niobium
    with col2:
        state = "Superconducting" if T < Tc else "Normal State"
        st.success(f"Material State: **{state}**")
        res = 0.0 if T < Tc else 1.0
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Electrical Resistance"], [res], color='green' if res==0 else 'red')
        ax.set_ylim(0, 1.2)
        st.pyplot(fig)

# --- 16. MAGNETIC HYSTERESIS ---
elif topic == "16. Magnetic Hysteresis":
    st.title("Magnetic Hysteresis (B-H Loop)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Ferromagnetic materials me magnetic field ($H$) ke sath flux density ($B$) ka loop.")
        coercivity = st.slider("Coercivity Factor", 0.5, 2.0, 1.0)
    with col2:
        H = np.linspace(-5, 5, 200)
        B = 1.5 * np.tanh(H / coercivity)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(H, B, color='black', linewidth=2)
        ax.set_title("Hysteresis Loop")
        st.pyplot(fig)

# --- 17. CRYSTAL DEFECTS ---
elif topic == "17. Crystal Defects":
    st.title("Crystal Defects (Point & Line)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Vacancies, interstitials, aur dislocations crystal ki mechanical aur electrical properties ko badalte hain.")
        defect_type = st.selectbox("Defect Type", ["Vacancy", "Interstitial", "Dislocation"])
    with col2:
        st.info(f"Selected view: Visualizing structural distortion due to {defect_type}")
        xx = np.random.rand(10)
        yy = np.random.rand(10)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(xx, yy, s=100, color='blue')
        ax.set_title(f"Lattice Distortion: {defect_type}")
        st.pyplot(fig)

# --- 18. PHONONS & VIBRATIONS ---
elif topic == "18. Phonons & Vibrations":
    st.title("Phonons & Lattice Vibrations")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Crystal lattice me atoms ke collective vibrations ko phonons kehte hain (acoustic aur optical branches).")
        q_val = np.linspace(0, np.pi, 100)
    with col2:
        omega = 2 * np.sin(q_val / 2)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(q_val, omega, color='magenta', linewidth=2)
        ax.set_title("Dispersion Relation (Acoustic Branch)")
        st.pyplot(fig)

# --- 19. RAMAN EFFECT VISUALIZER ---
elif topic == "19. Raman Effect Visualizer":
    st.title("Raman Effect (Stokes & Anti-Stokes)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Inelastic scattering of photons. Rayleigh line ke sath Stokes (lower energy) aur Anti-Stokes (higher energy) lines milti hain.")
        shift = st.slider("Raman Shift (cm^-1)", 200, 1000, 500)
    with col2:
        x_shift = np.linspace(-1500, 1500, 300)
        y = np.exp(-x_shift**2 / 10000) + 0.6 * np.exp(-((x_shift - shift)**2) / 4000) + 0.3 * np.exp(-((x_shift + shift)**2) / 4000)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x_shift, y, color='darkcyan', linewidth=2)
        ax.set_title("Raman Spectrum")
        st.pyplot(fig)

# --- 20. SILICON VS GaAs ANALYSIS ---
elif topic == "20. Silicon vs GaAs Analysis":
    st.title("Silicon vs Gallium Arsenide Comparison")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("Theory")
        st.write("Silicon indirect bandgap material hai, jabki GaAs direct bandgap material hai jo optoelectronics me use hota hai.")
        prop = st.selectbox("Compare Property", ["Bandgap (eV)", "Electron Mobility"])
    with col2:
        val_si = 1.12 if prop == "Bandgap (eV)" else 1400
        val_gaas = 1.42 if prop == "Bandgap (eV)" else 8500
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Silicon", "GaAs"], [val_si, val_gaas], color=['blue', 'green'])
        ax.set_title(f"Comparison: {prop}")
        st.pyplot(fig)
