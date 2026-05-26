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

        # jika linked list kosong
        if self.head is None:
            self.head = node_baru

        # jika linked list ada isi
        else:

            current = self.head

            while current.next:
                current = current.next

            current.next = node_baru

    # menampilkan data
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
# HEADER
# =========================================================
st.title("🎫 Aplikasi Pemesanan Tiket Konser")

st.write(
    "Project Struktur Data Menggunakan Linked List dan Streamlit"
)

st.divider()


# =========================================================
# SIDEBAR EDIT DATA KONSER
# =========================================================
st.sidebar.header("⚙️ Edit Data Konser")

# =========================================================
# KONSER 1
# =========================================================
nama_konser1 = st.sidebar.text_input(
    "Nama Konser 1",
    "Coldplay World Tour"
)

lokasi1 = st.sidebar.text_input(
    "Lokasi Konser 1",
    "Jakarta International Stadium"
)

tanggal1 = st.sidebar.text_input(
    "Tanggal Konser 1",
    "12 Juni 2026"
)

vip1 = st.sidebar.number_input(
    "Harga VIP 1",
    value=2500000
)

regular1 = st.sidebar.number_input(
    "Harga Regular 1",
    value=1200000
)

st.sidebar.divider()

# =========================================================
# KONSER 2
# =========================================================
nama_konser2 = st.sidebar.text_input(
    "Nama Konser 2",
    "NIKI Live Concert"
)

lokasi2 = st.sidebar.text_input(
    "Lokasi Konser 2",
    "ICE BSD"
)

tanggal2 = st.sidebar.text_input(
    "Tanggal Konser 2",
    "20 Juli 2026"
)

vip2 = st.sidebar.number_input(
    "Harga VIP 2",
    value=1800000
)

regular2 = st.sidebar.number_input(
    "Harga Regular 2",
    value=850000
)

st.sidebar.divider()

# =========================================================
# KONSER 3
# =========================================================
nama_konser3 = st.sidebar.text_input(
    "Nama Konser 3",
    "Taylor Swift Eras Tour"
)

lokasi3 = st.sidebar.text_input(
    "Lokasi Konser 3",
    "Gelora Bung Karno"
)

tanggal3 = st.sidebar.text_input(
    "Tanggal Konser 3",
    "10 Agustus 2026"
)

vip3 = st.sidebar.number_input(
    "Harga VIP 3",
    value=3500000
)

regular3 = st.sidebar.number_input(
    "Harga Regular 3",
    value=2000000
)

# =========================================================
# DATA KONSER
# =========================================================
konser_data = {

    nama_konser1: {
        "lokasi": lokasi1,
        "tanggal": tanggal1,
        "vip": vip1,
        "regular": regular1
    },

    nama_konser2: {
        "lokasi": lokasi2,
        "tanggal": tanggal2,
        "vip": vip2,
        "regular": regular2
    },

    nama_konser3: {
        "lokasi": lokasi3,
        "tanggal": tanggal3,
        "vip": vip3,
        "regular": regular3
    }

}

# =========================================================
# FORM PEMESANAN
# =========================================================
st.sidebar.header("📝 Form Pemesanan Tiket")

nama = st.sidebar.text_input(
    "👤 Nama Pembeli"
)

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

submit = st.sidebar.button(
    "🎟️ Pesan Tiket"
)

# =========================================================
# TAMPILAN DAFTAR KONSER
# =========================================================
st.header("🎤 Daftar Konser")

konser_list = list(konser_data.items())

col1, col2, col3 = st.columns(3)

# =========================================================
# KOLOM 1
# =========================================================
with col1:

    nama_konser, detail = konser_list[0]

    st.subheader(nama_konser)

    st.write(f"📍 {detail['lokasi']}")
    st.write(f"📅 {detail['tanggal']}")
    st.write(f"💎 VIP : Rp {detail['vip']:,}")
    st.write(f"🎟️ Regular : Rp {detail['regular']:,}")

    st.success("Tiket tersedia")

# =========================================================
# KOLOM 2
# =========================================================
with col2:

    nama_konser, detail = konser_list[1]

    st.subheader(nama_konser)

    st.write(f"📍 {detail['lokasi']}")
    st.write(f"📅 {detail['tanggal']}")
    st.write(f"💎 VIP : Rp {detail['vip']:,}")
    st.write(f"🎟️ Regular : Rp {detail['regular']:,}")

    st.success("Tiket tersedia")

# =========================================================
# KOLOM 3
# =========================================================
with col3:

    nama_konser, detail = konser_list[2]

    st.subheader(nama_konser)

    st.write(f"📍 {detail['lokasi']}")
    st.write(f"📅 {detail['tanggal']}")
    st.write(f"💎 VIP : Rp {detail['vip']:,}")
    st.write(f"🎟️ Regular : Rp {detail['regular']:,}")

    st.success("Tiket tersedia")

st.divider()

# =========================================================
# PROSES PEMESANAN
# =========================================================
if submit:

    if nama == "":

        st.error("Nama pembeli wajib diisi!")

    else:

        # menentukan harga
        if kategori == "VIP":
            harga = konser_data[konser]["vip"]

        else:
            harga = konser_data[konser]["regular"]

        # menghitung total
        total = harga * jumlah

        # simpan ke linked list
        st.session_state.tickets.tambah_tiket(
            nama,
            konser,
            kategori,
            jumlah,
            total
        )

        st.success("✅ Tiket berhasil dipesan!")

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

    # =====================================================
    # STATISTIK
    # =====================================================
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

    st.warning(
        "Belum ada data pemesanan tiket."
    )

# =========================================================
# FOOTER
# =========================================================
st.divider()

st.caption(
    "© 2026 | Project UAS Struktur Data - Tiket Konser"
)