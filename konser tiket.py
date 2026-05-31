import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Tiket Konser",
    page_icon="🎫",
    layout="wide"
)

# =====================================================
# CLASS NODE
# =====================================================
class TicketNode:
    def __init__(self, kode, nama, konser, seat,
                 kategori, jumlah, total):

        self.kode = kode
        self.nama = nama
        self.konser = konser
        self.seat = seat
        self.kategori = kategori
        self.jumlah = jumlah
        self.total = total
        self.next = None


# =====================================================
# LINKED LIST
# =====================================================
class TicketLinkedList:

    def __init__(self):
        self.head = None

    def tambah_tiket(
        self,
        kode,
        nama,
        konser,
        seat,
        kategori,
        jumlah,
        total
    ):

        node_baru = TicketNode(
            kode,
            nama,
            konser,
            seat,
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
                "Kode Tiket": current.kode,
                "Nama": current.nama,
                "Konser": current.konser,
                "Seat": current.seat,
                "Kategori": current.kategori,
                "Jumlah Tiket": current.jumlah,
                "Total Bayar": f"Rp {current.total:,}"
            })

            current = current.next

        return data


# =====================================================
# SESSION STATE
# =====================================================
if "tickets" not in st.session_state:
    st.session_state.tickets = TicketLinkedList()

if "seat_terpakai" not in st.session_state:
    st.session_state.seat_terpakai = {}

# =====================================================
# DATA KONSER
# =====================================================
konser_data = {

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

# =====================================================
# HEADER
# =====================================================
st.title("🎫 Aplikasi Pemesanan Tiket Konser")

st.write(
    "Project Struktur Data Menggunakan Linked List"
)

st.divider()

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.header("📝 Form Pemesanan")

nama = st.sidebar.text_input(
    "Nama Pembeli"
)

konser = st.sidebar.selectbox(
    "Pilih Konser",
    list(konser_data.keys())
)

semua_kursi = [
    "A1","A2","A3","A4","A5",
    "B1","B2","B3","B4","B5",
    "C1","C2","C3","C4","C5"
]

if konser not in st.session_state.seat_terpakai:
    st.session_state.seat_terpakai[konser] = []

kursi_tersedia = [
    kursi
    for kursi in semua_kursi
    if kursi not in st.session_state.seat_terpakai[konser]
]

seat = st.sidebar.selectbox(
    "💺 Pilih Kursi",
    kursi_tersedia
)

kategori = st.sidebar.radio(
    "Kategori Tiket",
    ["VIP", "Regular"]
)

jumlah = st.sidebar.number_input(
    "Jumlah Tiket",
    min_value=1,
    max_value=5,
    value=1
)

submit = st.sidebar.button(
    "🎟️ Pesan Tiket"
)

st.header("🎤 Daftar Konser")

for nama_konser, detail in konser_data.items():

    with st.container():

        st.subheader(nama_konser)

        st.write(
            f"📍 {detail['lokasi']}"
        )

        st.write(
            f"📅 {detail['tanggal']}"
        )

        st.write(
            f"💎 VIP : Rp {detail['vip']:,}"
        )

        st.write(
            f"🎫 Regular : Rp {detail['regular']:,}"
        )

        st.success("Tiket Tersedia")

st.divider()

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

        kode_tiket = (
            f"TRX-{len(st.session_state.tickets.tampilkan_data()) + 1}"
        )

        st.session_state.tickets.tambah_tiket(
            kode_tiket,
            nama,
            konser,
            seat,
            kategori,
            jumlah,
            total
        )

        st.session_state.seat_terpakai[konser].append(
            seat
        )

        st.success(
            "✅ Tiket berhasil dipesan!"
        )

        # =============================================
        # E-TICKET
        # =============================================
        st.subheader("🎫 E-Ticket")

        st.info(
            f"""
Kode Tiket : {kode_tiket}
Nama : {nama}
Konser : {konser}
Seat : {seat}
Kategori : {kategori}
Jumlah Tiket : {jumlah}
Total Bayar : Rp {total:,}
Status : Berhasil
"""
        )

st.divider()

# =====================================================
# DATA PEMESANAN
# =====================================================
st.header("📊 Data Pemesanan Tiket")

data = st.session_state.tickets.tampilkan_data()

if data:

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )

    total_pembeli = len(data)

    total_penghasilan = 0

    current = st.session_state.tickets.head

    while current:

        total_penghasilan += current.total

        current = current.next

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "👥 Total Pembeli",
            total_pembeli
        )

    with col2:

        st.metric(
            "💰 Total Penghasilan",
            f"Rp {total_penghasilan:,}"
        )

else:

    st.warning(
        "Belum ada data pemesanan tiket."
    )

# =====================================================
# FOOTER
# =====================================================
st.divider()

st.caption(
    "© 2026 | Project UAS Struktur Data - Tiket Konser"
)