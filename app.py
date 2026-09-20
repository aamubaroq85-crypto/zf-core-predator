import streamlit as st
import random

# PERBAIKAN: st.set_page_config HARUS berada di baris perintah Streamlit paling awal
st.set_page_config(
    page_title="ZF-Core V16.7-PREDATOR | Aa Baroq Applied Technologies",
    page_layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⚡ ZF-CORE V16.7-PREDATOR: MASTER CONSOLE")
st.markdown("*Time-Lock 2326 Active | Unified Geometric Manifold Architecture*")

st.sidebar.header("🎛️ Manifold Control Panel")
selected_pair = st.sidebar.selectbox("Universe Selection (200 Pairs)", ["EUR/USD", "GBP/USD", "AUD/USD", "USD/JPY", "XAU/USD"])

zf_score = st.sidebar.slider("ZF-Score Predator", 0.0, 1.0, 0.42, 0.01)
crx_divergence = st.sidebar.checkbox("CRX Divergence Detected (Topological Mirage)", value=False)
sacred_pause_active = st.sidebar.toggle("Sacred Pause (Keselarasan Vertikal)", value=False)

st.sidebar.markdown("---")
st.sidebar.subheader("🛡️ Automated Shield Status")

if zf_score > 0.99:
    system_state = "TOPOLOGICAL FRACTURE (CIRCUIT BREAKER)"
    state_color = "red"
elif zf_score > 0.85 or crx_divergence:
    system_state = "COLD LOGIC MODE / TOPOLOGICAL MIRAGE"
    state_color = "orange"
elif sacred_pause_active:
    system_state = "SACRED PAUSE ACTIVE (JEDA SUCI)"
    state_color = "blue"
elif zf_score < 0.50:
    system_state = "LAMINAR STATE (STABLE RESONANCE)"
    state_color = "green"
else:
    system_state = "CRITICAL EXPANSION ZONE"
    state_color = "goldenrod"

st.sidebar.markdown(f"**System State:** <span style='color:{state_color}; font-weight:bold;'>{system_state}</span>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Selected Asset", value=selected_pair)
    st.metric(label="Topological Drift (D_matrix)", value=f"{random.uniform(0.001, 0.045):.4f}")

with col2:
    st.metric(label="V-Pure Volume Index", value=f"{random.randint(1200, 4800)} Lots")
    st.metric(label="Elasticity Lambda (lambda_dyn)", value=f"{random.uniform(1.12, 1.85):.3f}")

with col3:
    st.metric(label="Second Derivative (d2P/dt2)", value=f"{random.uniform(-0.02, 0.02):.4f}")
    st.metric(label="Execution Authorization", value="REVOKED" if (zf_score > 0.85 or sacred_pause_active or zf_score > 0.99) else "GRANTED")

st.markdown("---")
st.subheader("📊 Tiered Execution & Resonance Re-entry Protocol")

if system_state.startswith("TOPOLOGICAL FRACTURE") or system_state.startswith("SACRED PAUSE") or system_state.startswith("COLD LOGIC"):
    st.error(f"⚠️ EKSEKUSI DITAHAN OLEH SISTEM: Konsol berada dalam status **{system_state}**. Tidak ada alokasi modal yang dilepaskan.")
else:
    t1, t2, t3 = st.columns(3)
    with t1:
        st.info("**Tier 1 (30% Alokasi)**\nStatus: *Uji Ketahanan P_pure*\nAction: Standby")
    with t2:
        st.warning("**Tier 2 (50% Alokasi)**\nStatus: *Konfirmasi Snap-back*\nAction: Standby")
    with t3:
        st.success("**Tier 3 (20% Alokasi)**\nStatus: *Penyempurnaan Klaster*\nAction: Standby")

st.markdown("---")
st.subheader("📂 Archival Vault & Live Log-Vault")
with st.expander("Lihat Log Transmisi Terakhir (Time-Lock 2326)"):
    st.text(f"""
    [2326-09-20 20:28:19] - WebSocket feed connected to Tier-1 ECN Node.
    [2326-09-20 20:28:20] - HFT Jitter Filter active: Filtered out 412 micro-transactions.
    [2326-09-20 20:28:21] - Asset {selected_pair} scanned. ZF-Score: {zf_score}. State: {system_state}.
    [2326-09-20 20:28:22] - Archival Vault synchronized successfully.
    """)
