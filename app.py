import streamlit as st
import random
import sqlite3
from datetime import datetime

st.set_page_config(
    page_title="ZF-Core V16.7-PREDATOR | Aa Baroq Applied Technologies",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inisialisasi Basis Data SQLite Dinamis
def init_db():
    conn = sqlite3.connect('zf_manifold.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS zf_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            asset TEXT,
            zf_score REAL,
            system_state TEXT,
            authorization TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_to_db(asset, score, state, auth):
    conn = sqlite3.connect('zf_manifold.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO zf_logs (timestamp, asset, zf_score, system_state, authorization) VALUES (?, ?, ?, ?, ?)",
              (timestamp, asset, score, state, auth))
    conn.commit()
    conn.close()

init_db()

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

exec_auth = "REVOKED" if (zf_score > 0.85 or sacred_pause_active or zf_score > 0.99) else "GRANTED"

# Rekam otomatis ke database SQLite
log_to_db(selected_pair, zf_score, system_state, exec_auth)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Selected Asset", value=selected_pair)
    st.metric(label="Topological Drift (D_matrix)", value=f"{random.uniform(0.001, 0.045):.4f}")

with col2:
    st.metric(label="V-Pure Volume Index", value=f"{random.randint(1200, 4800)} Lots")
    st.metric(label="Elasticity Lambda (lambda_dyn)", value=f"{random.uniform(1.12, 1.85):.3f}")

with col3:
    st.metric(label="Second Derivative (d2P/dt2)", value=f"{random.uniform(-0.02, 0.02):.4f}")
    st.metric(label="Execution Authorization", value=exec_auth)

st.markdown("---")
st.subheader("📊 Tiered Execution & Resonance Re-entry Protocol")

if "TOPOLOGICAL FRACTURE" in system_state or "SACRED PAUSE" in system_state or "COLD LOGIC" in system_state:
    st.error(f"⚠️ EKSEKUSI DITAHAN OLEH SISTEM: Konsol berada dalam status **{system_state}**.")
else:
    t1, t2, t3 = st.columns(3)
    with t1:
        st.info("**Tier 1 (30% Alokasi)**\nStatus: *Uji Ketahanan P_pure*")
    with t2:
        st.warning("**Tier 2 (50% Alokasi)**\nStatus: *Konfirmasi Snap-back*")
    with t3:
        st.success("**Tier 3 (20% Alokasi)**\nStatus: *Penyempurnaan Klaster*")

st.success("✅ Transmisi manifold saat ini telah otomatis diarsipkan ke dalam basis data SQLite (`zf_manifold.db`). Pilih menu **Log_Vault** di bilah navigasi samping kiri untuk melihat tabel arsip.")
