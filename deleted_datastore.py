
import requests

# ─── KONFIGURASI ──────────────────────────────────────────
API_KEY        = ""
UNIVERSE_ID    = ""
DATASTORE_NAME = ""           # Ganti sesuai nama DataStore
DRY_RUN        = False         # True = simulasi, False = hapus sungguhan
# ──────────────────────────────────────────────────────────

HEADERS = {
    "x-api-key": API_KEY
}

def delete_datastore():
    print("=" * 60)
    print("  Roblox DataStore Deleter [FIXED]")
    print("=" * 60)
    print(f"  Universe ID    : {UNIVERSE_ID}")
    print(f"  DataStore Name : {DATASTORE_NAME}")
    print(f"  Mode           : {'DRY RUN (simulasi)' if DRY_RUN else '⚠  EKSEKUSI SUNGGUHAN'}")
    print("=" * 60)

    if DRY_RUN:
        print(f"\n  [DRY RUN] Akan menghapus DataStore: '{DATASTORE_NAME}'")
        print("  Ubah DRY_RUN = False untuk eksekusi sungguhan.")
        return

    confirm = input(f"\n  Ketik nama DataStore '{DATASTORE_NAME}' untuk konfirmasi: ")
    if confirm.strip() != DATASTORE_NAME:
        print("\n[INFO] Nama tidak cocok. Dibatalkan.")
        return

    print("\n[INFO] Menghapus DataStore...")

    # ✅ URL yang BENAR — tanpa :archive
    url = (
        f"https://apis.roblox.com/cloud/v2/universes/{UNIVERSE_ID}"
        f"/data-stores/{requests.utils.quote(DATASTORE_NAME, safe='')}"
    )

    response = requests.delete(url, headers=HEADERS)

    print("\n" + "=" * 60)
    if response.status_code in (200, 204):
        print(f"  ✓ DataStore '{DATASTORE_NAME}' berhasil dihapus!")
    else:
        print(f"  ✗ Gagal menghapus DataStore!")
        print(f"  Status : {response.status_code}")
        print(f"  Pesan  : {response.text}")
    print("=" * 60)


if __name__ == "__main__":
    delete_datastore()