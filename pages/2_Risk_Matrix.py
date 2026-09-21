import streamlit as st

st.set_page_config(page_title="Risk Matrix Protocol", page_icon="🛡️", layout="wide")

st.title("🛡️ Risk Matrix & Dynamic Position Sizing")
st.markdown(
    "Modul kalkulasi manajemen risiko, alokasi modal, dan batas maksimum"
    " *drawdown* manifold."
)

st.sidebar.markdown("### ⚙️ Parameter Modal & Risiko")
total_capital = st.sidebar.number_input(
    "Total Modal (USD)", min_value=100.0, max_value=1000000.0, value=10000.0, step=500.0
)
risk_per_trade_pct = st.sidebar.slider(
    "Risiko per Transaksi (%)", 0.1, 5.0, 1.0, 0.1
)
leverage = st.sidebar.selectbox("Faktor Leverage", [1, 10, 50, 100, 200], index=3)

# Kalkulasi Risiko
risk_amount_usd = total_capital * (risk_per_trade_pct / 100.0)

col1, col2, col3 = st.columns(3)
with col1:
  st.metric("Total Modal Aktif", f"${total_capital:,.2f}")
with col2:
  st.metric(
      "Maksimum Risiko Kerugian",
      f"${risk_amount_usd:,.2f}",
      delta=f"-{risk_per_trade_pct}%",
      delta_color="inverse",
  )
with col3:
  st.metric("Rasio Leverage Aktif", f"1 : {leverage}")

st.markdown("---")
st.markdown("### 📊 Alokasi Tier Berdasarkan Protokol ZF-Core")

tier_data = {
    "Tier Alokasi": [
        "Tier 1 (Uji Ketahanan P_pure)",
        "Tier 2 (Konfirmasi Snap-back)",
        "Tier 3 (Penyempurnaan Klaster)",
    ],
    "Persentase Modal": ["30%", "50%", "20%"],
    "Alokasi USD": [
        f"${total_capital * 0.30:,.2f}",
        f"${total_capital * 0.50:,.2f}",
        f"${total_capital * 0.20:,.2f}",
    ],
    "Status Keamanan": ["Aktif / Waspada", "Standby", "Cadangan Optimal"],
}

import pandas as pd

df_risk = pd.DataFrame(tier_data)
st.table(df_risk)

st.success(
    "💡 **Saran Manajemen Risiko:** Pastikan *Topological Drift* berada di"
    " bawah ambang batas kritis sebelum mengeksekusi Tier 2 dan Tier 3."
)
