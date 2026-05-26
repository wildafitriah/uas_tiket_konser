import streamlit as st
import pandas as pd

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="Tiket Konser",
    page_icon="🎫",
    layout="wide"
)

# ==========================================
# LINKED LIST
# ==========================================
class TicketNode:
    def __init__(self, nama, konser, kategori, jumlah, total):
        self.nama = nama
        self.konser = konser
        self.kategori = kategori
        self.jumlah = jumlah
        self.total = total
        self.next = None


class TicketLinkedList:
    def __init__(self):
        self.head = None

    def tambah_tiket(self, nama, konser, kategori, jumlah, total):
        node_baru = TicketNode(nama, konser, kategori, jumlah, total)

        if self.head is None:
            self.head = node_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node_baru

    def tampilkan_data(self):
        data = []

        current = self.head

        while current:
            data.append({
                "Nama": current.nama,
                "Konser": current.konser,
                "Kategori": current.kategori,
                "Jumlah": current.jumlah,
                "Total Bayar": f"Rp {current.total:,}"
            })

            current = current.next

        return data


# ==========================================
# SESSION STATE
# ==========================================
if "tickets" not in st.session_state:
    st.session_state.tickets = TicketLinkedList()

# ==========================================
# DATA KONSER
# ==========================================
konser_data = {
    "Coldplay World Tour": {
        "Lokasi": "Jakarta International Stadium",
        "Tanggal": "12 Juni 2026",
        "VIP": 2500000,
        "Regular": 1200000
    },

    "NIKI Live Concert": {
        "Lokasi": "ICE BSD",
        "Tanggal": "20 Juli 2026",
        "VIP": 1800000,
        "Regular": 850000
    },

    "Taylor Swift Eras Tour": {
        "Lokasi": "Gelora Bung Karno",
        "Tanggal": "10 Agustus 2026",
        "VIP": 3500000,
        "Regular": 2000000
    }
}

# ==========================================
# JUDUL
# ==========================================
st.title("🎫 Aplikasi Pemesanan Tiket Konser")
st.write("Project Struktur Data Menggunakan Linked List")

st.divider()

# ==========================================
# DAFTAR KONSER
# ==========================================
st.subheader("🎵 Daftar Konser")

for nama_konser, detail in konser_data.items():

    st.write(f"### {nama_konser}")
    st.write(f"📍 Lokasi : {detail['Lokasi']}")
    st.write(f"📅 Tanggal : {detail['Tanggal']}")
    st.write(f"💎 VIP : Rp {detail['VIP']:,}")
    st.write(f"🎟️ Regular : Rp {detail['Regular']:,}")

    st.divider()

# ==========================================
# FORM PEMESANAN
# ==========================================
st.subheader("📝 Form Pemesanan")

with st.form("form_pemesanan"):

    nama = st.text_input("Nama Pembeli")

    konser = st.selectbox(
        "Pilih Konser",
        list(konser_data.keys())
    )

    kategori = st.radio(
        "Kategori Tiket",
        ["VIP", "Regular"]
    )

    jumlah = st.number_input(
        "Jumlah Tiket",
        min_value=1,
        max_value=10,
        value=1
    )

    submit = st.form_submit_button("Pesan Tiket")

# ==========================================
# PROSES PEMESANAN
# ==========================================
if submit:

    if nama == "":
        st.error("Nama pembeli wajib diisi!")
    else:

        if kategori == "VIP":
            harga = konser_data[konser]["VIP"]
        else:
            harga = konser_data[konser]["Regular"]

        total = harga * jumlah

        st.session_state.tickets.tambah_tiket(
            nama,
            konser,
            kategori,
            jumlah,
            total
        )

        st.success("Tiket berhasil dipesan!")

        st.write("### Detail Pemesanan")
        st.write(f"👤 Nama : {nama}")
        st.write(f"🎵 Konser : {konser}")
        st.write(f"🎫 Kategori : {kategori}")
        st.write(f"🔢 Jumlah Tiket : {jumlah}")
        st.write(f"💰 Total Bayar : Rp {total:,}")

st.divider()

# ==========================================
# DATA PEMESANAN
# ==========================================
st.subheader("📊 Data Pemesanan Tiket")

data = st.session_state.tickets.tampilkan_data()

if data:
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    total_pembeli = len(data)

    total_penghasilan = 0

    current = st.session_state.tickets.head

    while current:
        total_penghasilan += current.total
        current = current.next

    st.write(f"### 👥 Total Pembeli : {total_pembeli}")
    st.write(f"### 💰 Total Penghasilan : Rp {total_penghasilan:,}")

else:
    st.info("Belum ada data pemesanan tiket.")