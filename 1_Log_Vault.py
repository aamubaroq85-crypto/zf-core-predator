import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Archival Log-Vault | ZF-Core V16.7",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📂 Archival Vault & SQLite Log-Explorer")
st.markdown("*Manifold Historical Persistence Engine | Aa Baroq Applied Technologies*")

def load_logs():
    conn = sqlite3.connect('zf_manifold.db')
    df = pd.read_sql_query("SELECT * FROM zf_logs ORDER BY id DESC", conn)
    conn.close()
    return df

try:
    df_logs = load_logs()
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.metric(label="Total Log Records Stored", value=len(df_logs))
    with col2:
        if st.button("🗑️ Kosongkan Arsip Basis Data"):
            conn = sqlite3.connect('zf_manifold.db')
            conn.execute("DELETE FROM zf_logs")
            conn.commit()
            conn.close()
            st.rerun()

    st.markdown("---")
    st.subheader("📋 Tabel Riwayat Pemindaian Dinamis")
    
    # Menampilkan data dalam bentuk interaktif
    st.dataframe(df_logs, use_container_width=True)

except Exception as e:
    st.warning("⚠️ Basis data belum terdeteksi. Silakan buka halaman Utama (`app.py`) terlebih dahulu untuk menginisialisasi sistem.")
