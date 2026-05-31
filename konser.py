import streamlit as st
import pandas as pd

# =====================================================
# KONFIGURASI HALAMAN
# =====================================================
st.set_page_config(
    page_title="Tiket Konser",
    page_icon="🎫",
    layout="wide"
)

# =====================================================
# CLASS NODE
# =====================================================
class TicketNode:
    def __init__(self, nama, konser, kategori, jumlah, total):
        self.nama = nama
        self.konser = konser
        self.kategori = kategori
        self.jumlah = jumlah
        self.total = total
        self.next = None


# =====================================================
# CLASS LINKED LIST
# =====================================================
class TicketLinkedList:
    def __init__(self):
        self.head = None

    def tambah_tiket(self, nama, konser, kategori, jumlah, total):

        node_baru = TicketNode(
            nama,
            konser,
            kategori,
            jumlah,
            total
        )

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
                "Jumlah Tiket": current.jumlah,
                "Total Bayar": current.total
            })

            current = current.next

        return data


# =====================================================
# SESSION STATE
# =====================================================
if "tickets" not in st.session_state:
    st.session_state.tickets = TicketLinkedList()

if "konser_data" not in st.session_state:
    st.session_state.konser_data = {

        "Coldplay World Tour": {
            "lokasi": "Jakarta International Stadium",
            "tanggal": "12 Juni 2026",
            "vip": 2500000,
            "regular": 1200000
        },

        "NIKI Live Concert": {
            "lokasi": "ICE BSD",
            "tanggal": "20 Juli 2026",
            "vip": 1800000,
            "regular": 850000
        },

        "Taylor Swift Eras Tour": {
            "lokasi": "Gelora Bung Karno",
            "tanggal": "10 Agustus 2026",
            "vip": 3500000,
            "regular": 2000000
        }
    }

konser_data = st.session_state.konser_data

# =====================================================
# HEADER
# =====================================================
st.title("🎫 Aplikasi Pemesanan Tiket Konser")

st.write(
    "Project Struktur Data Menggunakan Linked List dan Streamlit"
)

st.divider()

# =====================================================
# SIDEBAR PEMESANAN
# =====================================================
st.sidebar.header("📝 Form Pemesanan")

nama = st.sidebar.text_input(
    "Nama Pembeli"
)

konser = st.sidebar.selectbox(
    "Pilih Konser",
    list(konser_data.keys())
)

kategori = st.sidebar.radio(
    "Kategori Tiket",
    ["VIP", "Regular"]
)

jumlah = st.sidebar.number_input(
    "Jumlah Tiket",
    min_value=1,
    max_value=10,
    value=1
)

submit = st.sidebar.button(
    "🎟️ Pesan Tiket"
)

# =====================================================
# UPDATE DATA KONSER
# =====================================================
st.sidebar.divider()

st.sidebar.header("✏️ Update Data Konser")

edit_konser = st.sidebar.selectbox(
    "Pilih Konser Yang Akan Diupdate",
    list(konser_data.keys())
)

lokasi_baru = st.sidebar.text_input(
    "Lokasi",
    konser_data[edit_konser]["lokasi"]
)

tanggal_baru = st.sidebar.text_input(
    "Tanggal",
    konser_data[edit_konser]["tanggal"]
)

vip_baru = st.sidebar.number_input(
    "Harga VIP",
    value=konser_data[edit_konser]["vip"]
)

regular_baru = st.sidebar.number_input(
    "Harga Regular",
    value=konser_data[edit_konser]["regular"]
)

if st.sidebar.button("💾 Update Konser"):

    konser_data[edit_konser]["lokasi"] = lokasi_baru
    konser_data[edit_konser]["tanggal"] = tanggal_baru
    konser_data[edit_konser]["vip"] = vip_baru
    konser_data[edit_konser]["regular"] = regular_baru

    st.sidebar.success(
        "Data konser berhasil diupdate"
    )

# =====================================================
# DAFTAR KONSER
# =====================================================
st.header("🎤 Daftar Konser")

col1, col2, col3 = st.columns(3)

konser_list = list(konser_data.items())

with col1:

    nama_konser, detail = konser_list[0]

    st.subheader(nama_konser)

    st.write("📍", detail["lokasi"])
    st.write("📅", detail["tanggal"])
    st.write(f"💎 VIP : Rp {detail['vip']:,}")
    st.write(f"🎟️ Regular : Rp {detail['regular']:,}")

with col2:

    nama_konser, detail = konser_list[1]

    st.subheader(nama_konser)

    st.write("📍", detail["lokasi"])
    st.write("📅", detail["tanggal"])
    st.write(f"💎 VIP : Rp {detail['vip']:,}")
    st.write(f"🎟️ Regular : Rp {detail['regular']:,}")

with col3:

    nama_konser, detail = konser_list[2]

    st.subheader(nama_konser)

    st.write("📍", detail["lokasi"])
    st.write("📅", detail["tanggal"])
    st.write(f"💎 VIP : Rp {detail['vip']:,}")
    st.write(f"🎟️ Regular : Rp {detail['regular']:,}")

st.divider()

# =====================================================
# PROSES PEMESANAN
# =====================================================
if submit:

    if nama == "":

        st.error(
            "Nama pembeli wajib diisi!"
        )

    else:

        if kategori == "VIP":
            harga = konser_data[konser]["vip"]

        else:
            harga = konser_data[konser]["regular"]

        total = harga * jumlah

        st.session_state.tickets.tambah_tiket(
            nama,
            konser,
            kategori,
            jumlah,
            total
        )

        st.success(
            "Tiket berhasil dipesan"
        )

# =====================================================
# DATA PEMESANAN
# =====================================================
st.header("📊 Data Pemesanan")

data = st.session_state.tickets.tampilkan_data()

if len(data) > 0:

    df = pd.DataFrame(data)

    df["Total Bayar"] = df["Total Bayar"].apply(
        lambda x: f"Rp {x:,}"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # =================================================
    # STATISTIK
    # =================================================
    total_pembeli = len(data)

    total_penghasilan = 0

    current = st.session_state.tickets.head

    while current:

        total_penghasilan += current.total
        current = current.next

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Pembeli",
            total_pembeli
        )

    with col2:

        st.metric(
            "Total Penghasilan",
            f"Rp {total_penghasilan:,}"
        )

    st.divider()

    csv = pd.DataFrame(data).to_csv(
        index=False
    )

    st.download_button(
        "📥 Download CSV",
        csv,
        file_name="data_tiket.csv",
        mime="text/csv"
    )

    if st.button("🗑️ Hapus Semua Pesanan"):

        st.session_state.tickets = TicketLinkedList()

        st.rerun()

else:

    st.warning(
        "Belum ada data pemesanan tiket"
    )

# =====================================================
# FOOTER
# =====================================================
st.divider()

st.caption(
    "© 2026 | Project UAS Struktur Data - Tiket Konser"
)