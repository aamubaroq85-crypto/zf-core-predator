import pandas as pd
import plotly.express as px
import sqlite3
import streamlit as st

st.set_page_config(page_title="Archival Log-Vault", page_icon="📜", layout="wide")

st.title("📜 Archival Log-Vault & Trend Analytics")
st.markdown(
    "Pusat penyimpanan arsip transaksi dan visualisasi metrik manifold"
    " berbasis `zf_manifold.db`."
)


# Ambil Data dari SQLite
@st.cache_data(ttl=5)
def load_data():
  conn = sqlite3.connect("zf_manifold.db")
  df = pd.read_sql_query("SELECT * FROM manifold_logs ORDER BY id DESC", conn)
  conn.close()
  return df


df_logs = load_data()

if df_logs.empty:
  st.warning(
      "⚠️ Belum ada data arsip terekam. Silakan lakukan pencatatan dari halaman"
      " Master Console (`app.py`)."
  )
else:
  # Tombol Ekspor CSV
  st.markdown("### 📥 Ekspor Data Arsip")
  csv_data = df_logs.to_csv(index=False).encode("utf-8")
  st.download_button(
      label="📥 Unduh Arsip (Format CSV)",
      data=csv_data,
      file_name="zf_manifold_archive.csv",
      mime="text/csv",
  )

  st.markdown("---")

  # Visualisasi Grafik Interaktif Plotly
  st.markdown("### 📈 Grafik Tren Metrik Manifold")
  fig = px.line(
      df_logs.sort_values("timestamp"),
      x="timestamp",
      y=["zf_score", "topological_drift"],
      markers=True,
      title="Fluktuasi ZF-Score & Topological Drift Berdasarkan Waktu",
      labels={"value": "Nilai Metrik", "timestamp": "Waktu Transmisi"},
  )
  st.plotly_chart(fig, use_container_width=True)

  st.markdown("---")
  st.markdown("### 📋 Tabel Riwayat Basis Data")
  st.dataframe(df_logs, use_container_width=True)
