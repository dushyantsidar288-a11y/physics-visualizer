import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# App ka layout wide set karna taaki theory aur graph side-by-side acche dikhein
st.set_page_config(page_title="P-N Junction App", layout="wide")

st.title("Semiconductor P-N Junction: Theory, Diagram & Visualization")
st.markdown("---")

# Screen ko do hisson me baantna (Left me theory, Right me visuals)
col1, col2 = st.columns([1, 1.2]) 

with col1:
    st.subheader("📚 Theory (Siddhant)")
    st.write('''
    **1. P-Type aur N-Type Semiconductor:**
    Jab ek P-type (jisme positive 'Holes' zyada hote hain) aur N-type (jisme negative 'Electrons' zyada hote hain) material ko ek sath joda jata hai, toh P-N junction banta hai.

    **2. Depletion Region (Kshaya Kshetra):**
    Junction ke bilkul paas, electrons aur holes ek dusre se mil kar neutralize ho jate hain. Is wajah se beech me ek aisi jagah banti hai jahan koi free charge carrier nahi hota. Ise *Depletion Region* kehte hain.

    **3. Biasing (Voltage) ka Asar:**
    - **Forward Bias (+V):** Jab positive voltage lagate hain, toh Depletion region patla (narrow) ho jata hai aur Potential barrier chota ho jata hai, jisse current asani se behta hai.
    - **Reverse Bias (-V):** Jab negative voltage lagate hain, toh Depletion region aur chauda (wide) ho jata hai aur barrier badh jata hai, jo current ko rokta hai.
    ''')
    
    st.info("👇 Niche diye gaye slider se Voltage badal kar dekhein ki Diagram (Depletion width) aur Graph (Barrier height) me live kya badlav aata hai!")
    
    # Interactive Slider
    V_app = st.slider("Applied Voltage (V) [Biasing]", min_value=-2.0, max_value=0.5, value=0.0, step=0.1)

with col2:
    # Calculations based on applied voltage
    V0 = 0.7 # Silicon ke liye Built-in potential lagbhag 0.7V hota hai
    barrier = max(0.05, V0 - V_app)
    # Depletion width (W) voltage ke hisaab se badalti hai
    W = np.sqrt(barrier / V0) * 2 

    st.subheader("📊 Diagram & Graph Visualization")
    
    # Ek hi figure me 2 hisse banana (Upar Diagram, Niche Graph)
    fig, (ax_diag, ax_graph) = plt.subplots(2, 1, figsize=(8, 6), gridspec_kw={'height_ratios': [1, 2]})

    # --- 1. SCHEMATIC BLOCK DIAGRAM ---
    ax_diag.axis('off') # Diagram ke borders chhupane ke liye
    ax_diag.set_xlim(-5, 5)
    ax_diag.set_ylim(0, 2)

    # P-Region (Blue)
    ax_diag.add_patch(patches.Rectangle((-5, 0), 5-W/2, 2, facecolor='#add8e6', edgecolor='black'))
    ax_diag.text(-2.5 - W/4, 1, 'P-Type\n(Holes +)', ha='center', va='center', fontsize=12, fontweight='bold')

    # N-Region (Red)
    ax_diag.add_patch(patches.Rectangle((W/2, 0), 5-W/2, 2, facecolor='#ffcccb', edgecolor='black'))
    ax_diag.text(2.5 + W/4, 1, 'N-Type\n(Electrons -)', ha='center', va='center', fontsize=12, fontweight='bold')

    # Depletion Region (Grey with pattern)
    ax_diag.add_patch(patches.Rectangle((-W/2, 0), W, 2, facecolor='#d3d3d3', edgecolor='black', hatch='//'))
    ax_diag.text(0, 1, 'Depletion\nRegion', ha='center', va='center', fontsize=10)
    ax_diag.set_title("P-N Junction Physical Diagram", fontweight="bold")

    # --- 2. POTENTIAL BARRIER GRAPH ---
    x = np.linspace(-5, 5, 500)
    potential = np.zeros_like(x)
    
    # Graph ka curve banane ke liye calculation
    for i, pos in enumerate(x):
        if pos < -W/2:
            potential[i] = 0
        elif pos > W/2:
            potential[i] = barrier
        else:
            normalized_pos = (pos - (-W/2)) / W
            potential[i] = barrier * (0.5 - 0.5 * np.cos(np.pi * normalized_pos))

    # Graph Plot karna
    ax_graph.plot(x, potential, color='purple', linewidth=3)
    ax_graph.fill_between(x, 0, potential, color='purple', alpha=0.1)
    ax_graph.set_title("Potential Barrier (Energy) Graph", fontweight="bold")
    ax_graph.set_xlabel("Position (x)")
    ax_graph.set_ylabel("Potential / Energy Barrier")
    ax_graph.set_xlim(-5, 5)
    ax_graph.set_ylim(-0.2, 3.0)
    
    # Depletion region ki boundaries ko dotted line se dikhana
    ax_graph.axvline(x=-W/2, color='gray', linestyle='--')
    ax_graph.axvline(x=W/2, color='gray', linestyle='--')
    ax_graph.grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    
    # Streamlit me figure ko dikhana
    st.pyplot(fig)
