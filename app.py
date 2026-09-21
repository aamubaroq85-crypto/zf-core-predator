import sqlite3
from datetime import datetime
import streamlit as st

# Konfigurasi Halaman
st.set_page_config(
    page_title="ZF-Core V16.7-PREDATOR [PREMIUM]", page_icon="🔐", layout="wide"
)

# Inisialisasi Database SQLite (Tabel Log & Tabel Lisensi)


def init_db():
  conn = sqlite3.connect("zf_manifold.db")
  cursor = conn.cursor()

  # Tabel Log Manifold
  cursor.execute("PRAGMA table_info(manifold_logs);")
  columns = [info[1] for info in cursor.fetchall()]
  if columns and "auto_signal" not in columns:
    cursor.execute("DROP TABLE IF EXISTS manifold_logs;")

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS manifold_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            asset TEXT,
            zf_score REAL,
            topological_drift REAL,
            v_pure_lots INTEGER,
            second_derivative REAL,
            crx_divergence INTEGER,
            sacred_pause INTEGER,
            auto_signal TEXT,
            status TEXT
        )
    """)

  # Tabel Lisensi Pengguna Premium
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS licenses (
            key TEXT PRIMARY KEY,
            owner TEXT,
            tier TEXT,
            expires_date TEXT
        )
    """)

  # Masukkan Master Key Default untuk Administrator / Pengujian (Contoh: "BAROQ-PREDATOR-2026")
  cursor.execute(
      "INSERT OR IGNORE INTO licenses (key, owner, tier, expires_date) VALUES"
      " (?, ?, ?, ?)",
      ("BAROQ-PREDATOR-2026", "Master Admin", "Institutional", "2027-12-31"),
  )

  conn.commit()
  conn.close()


init_db()


# Fungsi Verifikasi Lisensi
def verify_license(key):
  if not key:
    return False, None
  conn = sqlite3.connect("zf_manifold.db")
  cursor = conn.cursor()
  cursor.execute(
      "SELECT owner, tier, expires_date FROM licenses WHERE key = ?", (key,)
  )
  row = cursor.fetchone()
  conn.close()
  if row:
    return True, {"owner": row[0], "tier": row[1], "expires_date": row[2]}
  return False, None


# --- SISTEM AUTENTIKASI PAYWALL (PREMIUM GATE) ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False
  st.session_state.license_info = None

if not st.session_state.authenticated:
  st.title("🔐 ZF-CORE V16.7-PREDATOR: SECURE PREMIUM GATE")
  st.markdown(
      "*Professional Quantitative Manifold Ecosystem | Aa Baroq Applied"
      " Technologies*"
  )
  st.info(
      "Aplikasi ini dilindungi oleh protokol lisensi komersial berbayar. Harap"
      " masukkan *License Key* valid Anda untuk mengakses konsol."
  )

  with st.form("license_form"):
    entered_key = st.text_input(
        "Masukkan License Key Premium Anda:", type="password"
    )
    submit_button = st.form_submit_button("🔓 Verifikasi & Masuk Konsol")

    if submit_button:
      is_valid, info = verify_license(entered_key)
      if is_valid:
        st.session_state.authenticated = True
        st.session_state.license_info = info
        st.success(
            f"✅ Lisensi Terverifikasi! Selamat datang, {info['owner']} ("
            f"Tier: {info['tier']})."
        )
        st.rerun()
      else:
        st.error(
            "❌ License Key tidak valid atau kedaluwarsa. Hubungi administrator"
            " Aa Baroq Applied Technologies untuk mendapatkan akses."
        )

  # Informasi Pembelian Lisensi / Call to Action
  st.markdown("---")
  st.markdown("### 💳 Dapatkan Akses Lisensi Premium")
  st.write(
      "Ingin mengintegrasikan mesin manifold dan *Auto Buy/Sell* otonom ke"
      " dalam operasi trading Anda?"
  )
  if st.button("🌐 Hubungi Tim Penjualan / Request Key"):
    st.markdown(
        "Silakan kirimkan permohonan lisensi komersial Anda langsung melalui"
        " portal resmi **Aa Baroq Applied Technologies**."
    )

  st.stop()  # Menghentikan eksekusi kode di bawah jika belum terautentikasi

# --- KONSOL UTAMA (Hanya Tampil Jika Sudah Berbayar / Terautentikasi) ---
st.title("⚡ ZF-CORE V16.7-PREDATOR: MASTER CONSOLE")
info = st.session_state.license_info
st.markdown(
    f"*Time-Lock 2326 Active | License Tier: **{info['tier']}** (Owner:"
    f" {info['owner']})*"
)

# Sidebar Kontrol Manifold Lengkap
st.sidebar.markdown("### 🎛️ Manifold Control Panel")
asset = st.sidebar.selectbox(
    "Universe Selection (200 Pairs)",
    ["EUR/USD", "GBP/USD", "USD/JPY", "BTC/USD", "XAU/USD"],
)
zf_score = st.sidebar.slider("ZF-Score Predator", 0.0, 1.0, 0.42)

# Kotak Centang & Tombol Sakelar
crx_divergence = st.sidebar.checkbox(
    "CRX Divergence Detected (Topological Mirage)"
)
sacred_pause = st.sidebar.toggle("Sacred Pause (Keselarasan Vertikal)")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🛡️ Automated Shield Status")
if sacred_pause:
  system_state = "PAUSED (VERTICAL ALIGNMENT)"
  st.sidebar.warning(f"System State: {system_state}")
elif crx_divergence:
  system_state = "TURBULENT (TOPOLOGICAL MIRAGE)"
  st.sidebar.error(f"System State: {system_state}")
else:
  system_state = "LAMINAR STATE (STABLE RESONANCE)"
  st.sidebar.success(f"System State: {system_state}")

# Logika Penentuan Sinyal Auto Buy / Sell
if sacred_pause:
  auto_signal = "HOLD / STANDBY (Sacred Pause Active)"
  signal_color = "orange"
elif crx_divergence:
  auto_signal = "AUTO SELL / CLOSE (Topological Mirage Warning)"
  signal_color = "red"
elif zf_score >= 0.70:
  auto_signal = "AUTO BUY (Strong Laminar Resonance)"
  signal_color = "green"
elif zf_score <= 0.30:
  auto_signal = "AUTO SELL (Resonance Breakdown)"
  signal_color = "red"
else:
  auto_signal = "NEUTRAL / ACCUMULATION"
  signal_color = "blue"

# Parameter metrik otomatis
topological_drift = 0.0312 if not crx_divergence else 0.0895
v_pure_lots = 2435 if not sacred_pause else 0
second_derivative = 0.0010

col1, col2 = st.columns(2)
with col1:
  st.metric("Selected Asset", asset)
  st.metric("Topological Drift (D_matrix)", f"{topological_drift:.4f}")
with col2:
  st.metric("V-Pure Volume Index", f"{v_pure_lots} Lots")
  st.metric("Second Derivative (d2P/dt2)", f"{second_derivative:.4f}")

st.markdown("---")
st.markdown("### ⚡ Automated Execution Engine (Auto Buy / Sell)")
st.markdown(
    f"Rekomendasi Sinyal Algoritmik Saat Ini: **:{signal_color}[{auto_signal}]**"
)

st.markdown("---")
st.markdown("### 📊 Tiered Execution & Resonance Re-entry Protocol")
st.info(
    "**Tier 1 (30% Alokasi)** Status: *Uji Ketahanan P_pure* \n\n"
    "**Tier 2 (50% Alokasi)** Status: *Konfirmasi Snap-back* \n\n"
    "**Tier 3 (20% Alokasi)** Status: *Penyempurnaan Klaster*"
)

# Tombol Rekam Transmisi ke SQLite
if st.button("🚀 Catat & Arsipkan Transmisi Manifold"):
  conn = sqlite3.connect("zf_manifold.db")
  cursor = conn.cursor()
  cursor.execute(
      """
        INSERT INTO manifold_logs (timestamp, asset, zf_score, topological_drift, v_pure_lots, second_derivative, crx_divergence, sacred_pause, auto_signal, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
      (
          datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          asset,
          zf_score,
          topological_drift,
          v_pure_lots,
          second_derivative,
          int(crx_divergence),
          int(sacred_pause),
          auto_signal,
          system_state,
      ),
  )
  conn.commit()
  conn.close()
  st.success(
      "✅ Transmisi manifold beserta sinyal Auto Buy/Sell berhasil diarsipkan ke"
      " basis data SQLite!"
  )

# Tombol Keluar / Ganti Akun
if st.sidebar.button("🔒 Keluar (Logout Lisensi)"):
  st.session_state.authenticated = False
  st.session_state.license_info = None
  st.rerun()

# --- FITUR FOOTER PROFESIONAL ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #6c757d; font-size: 0.85em;'>
        <p><b>ZF-Core V16.7-PREDATOR [PREMIUM EDITION]</b> | Developed under <b>Aa Baroq Applied Technologies</b></p>
        <p>Secure Commercial Manifold Geodesic Distribution &bull; All Rights Reserved &copy; 2026</p>
    </div>
    """,
    unsafe_allow_html=True,
)
