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
    st.title("Advanced Physics Educational Platform")
    st.write("Ye platform solid-state physics, crystallography, aur semiconductor electronics ke adhyayan ke liye banaya gaya hai.")
    st.info("👈 Bayen (left) taraf diye gaye menu se koi bhi topic chun kar uski vistarit theory aur interactive graph dekhein.")

# --- 02. P-N JUNCTION ---
elif topic == "02. P-N Junction (Drift-Diffusion)":
    st.title("Semiconductor P-N Junction: Comprehensive Study")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Jab ek P-type semiconductor (jisme holes majority carriers hote hain) aur ek N-type semiconductor (jisme electrons majority carriers hote hain) ko aapas me joda jata hai, tab ek P-N junction banta hai.
        
        **1. Concentration Gradient aur Diffusion:** Junction ke dono taraf charge carriers ki sankhya me antar hone ke karan electrons N-side se P-side aur holes P-side se N-side ki taraf diffuse hote hain.
        
        **2. Depletion Region:** Diffusion ki wajah se junction par ions chhoot jate hain, jisse ek electric field establish hota hai. Ye field ek aisa region banata hai jahan free mobile carriers nahi hote, ise **Depletion Region** kehte hain.
        
        **3. Drift Current:** Built-in potential ki wajah se minority carriers ka opposite movement **Drift Current** kehlata hai. Equilibrium par:
        $$J_{diff} + J_{drift} = 0$$
        """)
        v_app = st.slider("Applied Voltage (V) [Biasing]", -2.0, 0.5, 0.0, 0.1)
    with col2:
        v0 = 0.7 
        barrier = max(0.05, v0 - v_app)
        w = np.sqrt(barrier / v0) * 2 
        x = np.linspace(-5, 5, 500)
        potential = np.where(x < -w/2, 0, np.where(x > w/2, barrier, barrier * (0.5 - 0.5 * np.cos(np.pi * (x - (-w/2)) / w))))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, potential, color='purple', linewidth=3)
        ax.fill_between(x, 0, potential, color='purple', alpha=0.1)
        ax.set_title("Potential Barrier & Depletion Width Visualization")
        ax.set_xlabel("Position across Junction")
        ax.set_ylabel("Potential Barrier (eV)")
        st.pyplot(fig)

# --- 03. FERMI-DIRAC ---
elif topic == "03. Fermi-Dirac Distribution":
    st.title("Fermi-Dirac Statistics & Distribution Function")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Fermi-Dirac statistics un particles (jaise electrons) par lagu hoti hai jo Pauli exclusion principle ka palan karte hain (Fermions).
        
        **Probability Function:**
        $$f(E) = \\frac{1}{e^{(E - E_F) / kT} + 1}$$
        
        - **At $T = 0\\text{ K}$:** Fermi level ($E_F$) ke niche ke sabhi states ki probability 1 hoti hai, aur upar ke states ki probability 0 hoti hai (step function).
        - **At $T > 0\\text{ K}$:** Thermal energy ke karan $E_F$ ke aas-pass electrons thermal excitation dikhate hain, aur probability curve dhalwan (sloped) ho jata hai.
        """)
        T = st.slider("Temperature (Kelvin)", 0, 1000, 300, 50)
    with col2:
        E = np.linspace(0, 1, 500)
        E_f = 0.5
        k = 8.617e-5
        f_E = np.where(T == 0, np.where(E <= E_f, 1.0, 0.0), 1 / (np.exp((E - E_f) / (k * T)) + 1))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(E, f_E, color='blue', linewidth=2.5)
        ax.axvline(E_f, color='red', linestyle='--', label="Fermi Energy (E_F)")
        ax.set_title(f"Fermi-Dirac Distribution at T = {T} K")
        ax.set_xlabel("Energy (eV)")
        ax.set_ylabel("Occupation Probability f(E)")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

# --- 04. NaCl CRYSTAL (3D) ---
elif topic == "04. NaCl Crystal 3D Lattice":
    st.title("Sodium Chloride (NaCl) Crystal Structure")
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Sodium Chloride (NaCl) ka crystal structure face-centered cubic (FCC) lattice par adharit hota hai jisme do interpenetrating FCC sublattices hote hain—ek Na+ ions ka aur dusra Cl- ions ka.
        
        - **Coordination Number:** Is structure me har Na+ ion ko 6 Cl- ions ghere rehte hain, aur har Cl- ion ko 6 Na+ ions ghere rehte hain (6:6 coordination).
        - **Ionic Bonding:** Ye strong electrostatic attraction par nirbhar karta hai jo crystal ko ek sthir geometric aakar deta hai.
        """)
        st.info("👉 3D model ko mouse ya ungli se rotate karke alag-alag angles se dekhein!")
    with col2:
        x, y, z, color, size = [], [], [], [], []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    x.append(i); y.append(j); z.append(k)
                    if (i+j+k) % 2 == 0:
                        color.append('green'); size.append(15) # Cl-
                    else:
                        color.append('blue'); size.append(10)  # Na+
        fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=size, color=color, opacity=0.9))])
        fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        st.plotly_chart(fig, use_container_width=True)

# --- 05. ABACAS ---
elif topic == "05. ABACAS Simulations":
    st.title("ABACAS Semiconductor Analysis")
    st.subheader("assembly of basic application coordinated understanding the semiconductor")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Ye module semiconductor materials ke transport properties aur drift velocity ka vishleshan karta hai. High electric field ke tahat carriers ki mobility par kya asar padta hai, iska adhyayan kiya jata hai.
        """)
        mat = st.selectbox("Select Semiconductor Material", ["Silicon (Si)", "Gallium Arsenide (GaAs)"])
    with col2:
        mu_e, mu_h, Eg = (1400, 450, 1.12) if mat == "Silicon (Si)" else (8500, 400, 1.42)
        color = 'blue' if mat == "Silicon (Si)" else 'green'
        E_field = np.linspace(0, 10000, 100)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(E_field, mu_e * E_field / 10000, label="Electron Drift", color=color, linewidth=2)
        ax.plot(E_field, mu_h * E_field / 10000, label="Hole Drift", color='red', linestyle='--', linewidth=2)
        ax.set_title(f"Drift Velocity vs Electric Field ({mat})")
        ax.set_xlabel("Electric Field (V/cm)")
        ax.set_ylabel("Drift Velocity")
        ax.grid(True)
        ax.legend()
        st.pyplot(fig)

# --- 06. EXAM PREP ---
elif topic == "06. NET & CG Pre B.Ed Exam Prep":
    st.title("Competitive Examination Preparation Module")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Physics (NET / SET Level)")
        q1 = st.radio("At T=0K, what is the probability of occupation of an energy state above the Fermi level?", ["1", "0.5", "0", "Infinity"], key="net_q")
        if st.button("Check Physics Answer"):
            if q1 == "0":
                st.success("Sahi jawab! Absolute zero par Fermi level ke upar sabhi states khaali hote hain.")
            else:
                st.error("Galat. Sahi uttar '0' hai.")
    with col2:
        st.subheader("Teaching Aptitude (CG Pre B.Ed)")
        q2 = st.radio("Sikhne ki prakriya (Learning Process) me sabse prabhavi tatva kya hai?", ["Ratt kar yaad karna", "Concept ki spashtata aur vyavaharik samajh", "Kewal pariksha paas karna", "Shikshak ka darr"], key="bed_q")
        if st.button("Check B.Ed Answer"):
            if q2 == "Concept ki spashtata aur vyavaharik samajh":
                st.success("Ekdam Sahi!")
            else:
                st.error("Galat uttar.")

# --- 07. BRAGG'S LAW ---
elif topic == "07. Bragg's Law & XRD":
    st.title("Bragg's Law & X-ray Diffraction (XRD)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Jab X-rays crystal par aati hain, toh alag-alag planes se paravartan (reflection) ke baad constructive interference ke liye Bragg's law satisfy hona zaruri hai:
        $$2d \\sin\\theta = n\\lambda$$
        Iske adhar par hum crystal ki interplanar spacing ($d$) aur structure ko samajhte hain.
        """)
        wavelength = st.slider("X-ray Wavelength (nm)", 0.5, 2.0, 1.5, 0.1)
        d_spacing = st.slider("Plane Spacing d (nm)", 1.0, 5.0, 2.0, 0.1)
    with col2:
        theta = np.linspace(0, 90, 500)
        intensity = np.zeros_like(theta)
        for n in range(1, 4):
            val = (n * wavelength) / (2 * d_spacing)
            if val <= 1:
                intensity += np.exp(-((theta - np.degrees(np.arcsin(val)))**2) / 1.5) * (4 - n)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(theta, intensity, color='crimson', linewidth=2)
        ax.set_title("XRD Diffraction Intensity Peaks")
        ax.set_xlabel("Bragg Angle Theta (degrees)")
        ax.set_ylabel("Intensity")
        ax.grid(True)
        st.pyplot(fig)

# --- 08. BAND THEORY ---
elif topic == "08. Band Theory of Solids":
    st.title("Band Theory of Solids & Energy Gaps")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Kronig-Penney model aur Bloch theorem ke adhar par, periodic crystal potential me ghoomne wale electrons ki energy continuous na hokar discrete bands me banti hai.
        
        - **Valence Band:** Electrons se bhara hua lower energy band.
        - **Conduction Band:** Free conduction ke liye upri band.
        - **Bandgap ($E_g$):** Insulators me bada, semiconductors me chhota, aur conductors me overlap hota hai.
        """)
        mat_type = st.selectbox("Select Solid Classification", ["Insulator", "Semiconductor", "Conductor"])
    with col2:
        gap = 5.0 if mat_type == "Insulator" else (1.1 if mat_type == "Semiconductor" else 0.0)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Valence Band", "Conduction Band"], [1, 1], bottom=[-1, gap], color=['blue', 'orange'], width=0.5)
        ax.set_title(f"Energy Band Structure: {mat_type} (Gap = {gap} eV)")
        ax.set_ylabel("Energy Levels")
        st.pyplot(fig)

# --- 09. HALL EFFECT ---
elif topic == "09. Hall Effect":
    st.title("Hall Effect & Charge Carrier Determination")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Jab kisi conductor ya semiconductor me current bahta hai aur uspar perpendicular magnetic field lagaya jata hai, toh Lorentz force ke karan charge carriers ek taraf ikatthe ho jate hain. Isse ek transverse voltage (**Hall Voltage**) banta hai:
        $$V_H = \\frac{I B}{t n q}$$
        Is formula ki madad se hum carrier concentration ($n$) aur material ka type (P-type ya N-type) nikalte hain.
        """)
        B = st.slider("Magnetic Field B (Tesla)", 0.1, 5.0, 1.0, 0.1)
        I = st.slider("Current I (mA)", 1.0, 100.0, 10.0, 5.0)
    with col2:
        B_arr = np.linspace(0, 5, 100)
        V_h = (I * 1e-3 * B_arr) / (1.0e-3 * 1e22 * 1.6e-19) * 1000
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(B_arr, V_h, color='navy', linewidth=2.5)
        ax.set_title("Hall Voltage vs Magnetic Field")
        ax.set_xlabel("Magnetic Field (T)")
        ax.set_ylabel("Hall Voltage (mV)")
        ax.grid(True)
        st.pyplot(fig)

# --- 10. PHOTOVOLTAIC EFFECT ---
elif topic == "10. Photovoltaic Effect":
    st.title("Photovoltaic Effect & Solar Cells")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Jab threshold energy se zyada photons semiconductor par padte hain, toh valence band se electrons conduction band me chale jate hain, jisse Electron-Hole pairs bante hain. Junction ka built-in electric field inhe alag karke external circuit me current flow karata hai.
        """)
        light_intensity = st.slider("Light Intensity (Suns)", 0.1, 2.0, 1.0, 0.1)
    with col2:
        V = np.linspace(0, 0.6, 100)
        I = light_intensity * 5 - 5 * (np.exp(V / 0.026) - 1)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(V, I, color='darkorange', linewidth=2.5)
        ax.set_title("Solar Cell I-V Characteristic Curve")
        ax.set_xlabel("Voltage (V)")
        ax.set_ylabel("Current (A)")
        ax.grid(True)
        st.pyplot(fig)

# --- 11. QUANTUM HARMONIC OSCILLATOR ---
elif topic == "11. Quantum Harmonic Oscillator":
    st.title("Quantum Harmonic Oscillator")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Quantum mechanics me harmonic oscillator molecular vibrations, crystal lattice phonons, aur electromagnetic fields ko samajhne ka mukhya adhar hai. Iske energy eigenvalues quantized hote hain:
        $$E_n = \\left(n + \\frac{1}{2}\\right) \\hbar \\omega$$
        """)
        n_state = st.slider("Quantum State n", 0, 5, 0)
    with col2:
        x = np.linspace(-4, 4, 400)
        psi_sq = np.exp(-x**2) * (x**2)**n_state # Conceptual representation for viz
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(x, psi_sq, color='teal', linewidth=2.5)
        ax.set_title(f"Probability Density Function for n = {n_state}")
        ax.set_xlabel("Position x")
        ax.set_ylabel("|psi|^2")
        ax.grid(True)
        st.pyplot(fig)

# --- 12. HEISENBERG UNCERTAINTY ---
elif topic == "12. Heisenberg Uncertainty":
    st.title("Heisenberg's Uncertainty Principle")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Heisenberg ke anishchitata siddhant ke anusar kisi kan ki sthiti ($x$) aur samveg ($p$) ko ek sath atyant sateekta se nahi maapa ja sakta:
        $$\\Delta x \\cdot \\Delta p \\ge \\frac{\\hbar}{2}$$
        Jitna sateek hum position nikalenge, momentum ki anishchitata utni hi badh jayegi.
        """)
        dx = st.slider("Position Uncertainty (dx)", 0.01, 1.0, 0.1, 0.05)
    with col2:
        dp = 0.5 / dx
        st.metric(label="Minimum Momentum Uncertainty (dp)", value=f"{dp:.3f}")
        p = np.linspace(-5, 5, 200)
        dist = np.exp(-(p)**2 / (2 * dp**2))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(p, dist, color='purple', linewidth=2.5)
        ax.set_title("Momentum Spread Distribution")
        ax.set_xlabel("Momentum p")
        ax.grid(True)
        st.pyplot(fig)

# --- 13. MAXWELL-BOLTZMANN STATS ---
elif topic == "13. Maxwell-Boltzmann Stats":
    st.title("Maxwell-Boltzmann Classical Statistics")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Ye classical particles (jaise gas molecules ya distinguishable particles) ke liye thermal equilibrium par energy aur speed ka distribution darshati hai. Isme quantum effects ko naganya mana jata hai.
        """)
        temp = st.slider("Temperature (K)", 100, 1000, 300, 50)
    with col2:
        v = np.linspace(0, 2000, 200)
        m = 4.65e-26
        k_b = 1.38e-23
        f_v = (m / (2 * np.pi * k_b * temp))**1.5 * 4 * np.pi * v**2 * np.exp(-m * v**2 / (2 * k_b * temp))
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(v, f_v * 1e10, color='brown', linewidth=2.5)
        ax.set_title("Molecular Speed Distribution Curve")
        ax.set_xlabel("Speed (m/s)")
        ax.grid(True)
        st.pyplot(fig)

# --- 14. BOSE-EINSTEIN CONDENSATE ---
elif topic == "14. Bose-Einstein Condensate":
    st.title("Bose-Einstein Condensation (BEC)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Jab bosons (integer spin wale particles) ko absolute zero ke atyant nikat temperature par thanda kiya jata hai, toh sabhi atoms ek hi lowest quantum state me collapse ho jate hain, jise **Bose-Einstein Condensate** kehte hain.
        """)
        T_bec = st.slider("Temperature Ratio (T/Tc)", 0.0, 2.0, 0.5, 0.1)
    with col2:
        frac = max(0.0, 1.0 - T_bec**1.5) if T_bec <= 1 else 0.0
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Condensate Fraction"], [frac], color='blue', width=0.4)
        ax.set_ylim(0, 1)
        ax.set_title("BEC Population Fraction at Given T/Tc")
        st.pyplot(fig)

# --- 15. SUPERCONDUCTIVITY ---
elif topic == "15. Superconductivity":
    st.title("Superconductivity & Meissner Effect")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Kuch materials critical temperature ($T_c$) ke niche apni electrical resistance ko poori tarah zero kar lete hain aur magnetic field ko apne andar se bahar dhakel dete hain (Meissner Effect). Ye Cooper pairs ke formation ke karan hota hai.
        """)
        T = st.slider("Operating Temperature (K)", 1, 20, 5, 1)
        Tc = 9.2
    with col2:
        state = "Superconducting State" if T < Tc else "Normal Conductor State"
        st.success(f"Current Status: **{state}**")
        res = 0.0 if T < Tc else 1.0
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(["Electrical Resistance"], [res], color='green' if res==0 else 'red', width=0.4)
        ax.set_ylim(0, 1.2)
        ax.set_title("Resistance vs Temperature Phase")
        st.pyplot(fig)

# --- 16. MAGNETIC HYSTERESIS ---
elif topic == "16. Magnetic Hysteresis":
    st.title("Magnetic Hysteresis (B-H Loop)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write("""
        Ferromagnetic materials me magnetizing field ($H$) ko badhane aur ghatane par magnetic induction ($B$) piche chhut jata hai. Is closed loop ko **Hysteresis Loop** kehte hain, jo coercivity aur retentivity ko darshata hai.
        """)
        coercivity = st.slider("Material Coercivity Factor", 0.5, 2.0, 1.0, 0.1)
    with col2:
        H = np.linspace(-5, 5, 200)
        B = 1.5 * np.tanh(H / coercivity)
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(H, B, color='black', linewidth=2.5)
        ax.set_title("B-H Hysteresis Curve")
        ax.set_xlabel("Magnetic Field H")
        ax.set_ylabel("Magnetic Induction B")
        ax.grid(True)
        st.pyplot(fig)

# --- 17. CRYSTAL DEFECTS ---
elif topic == "17. Crystal Defects":
    st.title("Crystallographic Defects & Imperfections")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.subheader("📚 Detailed Theory")
        st.write
        Real crystals me ideal periodicity nahi hoti. Inme point defects (vacancy, interstitial), line defects (dislocations), aur surface defects hote hain jo materials ki mechanical strength aur conductivity ko prabhavit karte hain.
        
