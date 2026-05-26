import streamlit as st
import pandas as pd

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Tiket Konser",
    page_icon="🎫",
    layout="wide"
)

# =========================================================
# CLASS NODE LINKED LIST
# =========================================================
class TicketNode:
    def __init__(self, nama, konser, kategori, jumlah, total):
        self.nama = nama
        self.konser = konser
        self.kategori = kategori
        self.jumlah = jumlah
        self.total = total
        self.next = None


# =========================================================
# CLASS LINKED LIST
# =========================================================
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
                "Total Bayar": f"Rp {current.total:,}"
            })

            current = current.next

        return data


# =========================================================
# SESSION STATE
# =========================================================
if "tickets" not in st.session_state:
    st.session_state.tickets = TicketLinkedList()


# =========================================================
# DATA KONSER
# =========================================================
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

# =========================================================
# JUDUL YANG BISA DIGANTI LANGSUNG DI STREAMLIT
# =========================================================
judul_aplikasi = st.text_input(
    "✏️ Ubah Judul Aplikasi",
    "🎫 Aplikasi Pemesanan Tiket Konser"
)

subjudul = st.text_input(
    "✏️ Ubah Sub Judul",
    "Project Struktur Data Menggunakan Linked List"
)

st.title(judul_aplikasi)
st.write(subjudul)

st.divider()

# =========================================================
# SIDEBAR INPUT
# =========================================================
st.sidebar.header("📝 Form Pemesanan Tiket")

nama = st.sidebar.text_input("👤 Nama Pembeli")

konser = st.sidebar.selectbox(
    "🎵 Pilih Konser",
    list(konser_data.keys())
)

kategori = st.sidebar.radio(
    "🎫 Kategori Tiket",
    ["VIP", "Regular"]
)

jumlah = st.sidebar.number_input(
    "🔢 Jumlah Tiket",
    min_value=1,
    max_value=10,
    value=1
)

submit = st.sidebar.button("🎟️ Pesan Tiket")

st.sidebar.divider()

# =========================================================
# TAMPILAN KONSER
# =========================================================
st.header("🎤 Daftar Konser")

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Coldplay World Tour")

    st.write("📍 Jakarta International Stadium")
    st.write("📅 12 Juni 2026")
    st.write("💎 VIP : Rp 2,500,000")
    st.write("🎟️ Regular : Rp 1,200,000")

    st.success("Tiket tersedia")

with col2:

    st.subheader("NIKI Live Concert")

    st.write("📍 ICE BSD")
    st.write("📅 20 Juli 2026")
    st.write("💎 VIP : Rp 1,800,000")
    st.write("🎟️ Regular : Rp 850,000")

    st.success("Tiket tersedia")

with col3:

    st.subheader("Taylor Swift Eras Tour")

    st.write("📍 Gelora Bung Karno")
    st.write("📅 10 Agustus 2026")
    st.write("💎 VIP : Rp 3,500,000")
    st.write("🎟️ Regular : Rp 2,000,000")

    st.success("Tiket tersedia")

st.divider()

# =========================================================
# PROSES PEMESANAN
# =========================================================
if submit:

    if nama == "":

        st.error("Nama pembeli wajib diisi!")

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

        st.success("✅ Tiket berhasil dipesan!")

        # BALON SUDAH DIHAPUS

        st.subheader("🧾 Detail Pemesanan")

        col1, col2 = st.columns(2)

        with col1:

            st.write(f"👤 Nama : {nama}")
            st.write(f"🎵 Konser : {konser}")
            st.write(f"🎫 Kategori : {kategori}")

        with col2:

            st.write(f"🔢 Jumlah Tiket : {jumlah}")
            st.write(f"💰 Total Bayar : Rp {total:,}")

st.divider()

# =========================================================
# DATA PEMESANAN
# =========================================================
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

    st.divider()

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

    st.warning("Belum ada data pemesanan tiket.")

# =========================================================
# FOOTER
# =========================================================
st.divider()

footer_text = st.text_input(
    "✏️ Ubah Footer",
    "© 2026 | Project UAS Struktur Data - Tiket Konser"
)

st.caption(footer_text)