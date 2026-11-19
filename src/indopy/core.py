"""Inti IndoPython: penerjemah keyword Indonesia -> Python, plus runner dan REPL."""
import builtins
import code
import io
import sys
import tokenize
import traceback

# --- Keyword Indonesia -> Python ------------------------------------------
KEYWORDS = {
    "kalau": "if",
    "atau_kalau": "elif",
    "lainnya": "else",
    "untuk": "for",
    "selama": "while",
    "dalam": "in",
    "fungsi": "def",
    "kembalikan": "return",
    "hasilkan": "yield",
    "kelas": "class",
    "anonim": "lambda",
    "Benar": "True",
    "Salah": "False",
    "Kosong": "None",
    "dan": "and",
    "atau": "or",
    "bukan": "not",
    "adalah": "is",
    "coba": "try",
    "kecuali": "except",
    "akhirnya": "finally",
    "lempar": "raise",
    "tegaskan": "assert",
    "impor": "import",
    "dari": "from",
    "sebagai": "as",
    "dengan": "with",
    "lewati": "pass",
    "berhenti": "break",
    "lanjut": "continue",
    "hapus": "del",
    "nonlokal": "nonlocal",
    "asinkron": "async",
    "tunggu": "await",
}

# --- Fungsi bawaan versi Indonesia (disuntik ke namespace) -----------------
BUILTINS_ID = {
    "cetak": print,
    "masukan": input,
    "rentang": range,
    "panjang": len,
    "tipe": type,
    "angka": int,
    "desimal": float,
    "teks": str,
    "boolean": bool,
    "daftar": list,
    "kamus": dict,
    "himpunan": set,
    "tupel": tuple,
    "urutkan": sorted,
    "balik": reversed,
    "jumlah": sum,
    "maks": max,
    "mini": min,
    "mutlak": abs,
    "bulatkan": round,
    "buka": open,
    "enumerasi": enumerate,
    "gabung": zip,
    "petakan": map,
    "saring": filter,
    "semua": all,
    "adaapa": any,
    "apakah_instansi": isinstance,
    "punya_atribut": hasattr,
    "ambil_atribut": getattr,
    "atur_atribut": setattr,
    "bantuan": help,
    "keluar": sys.exit,
}


def terjemahkan(sumber: str) -> str:
    """Ubah kode IndoPython jadi kode Python biasa (nomor baris tetap sama)."""
    ditambah = not sumber.endswith("\n")
    if ditambah:
        sumber += "\n"
    baris = sumber.splitlines(keepends=True)
    ganti = []  # (row, col_awal, col_akhir, teks_baru)
    sebelumnya = None
    for tok in tokenize.generate_tokens(io.StringIO(sumber).readline):
        if tok.type == tokenize.NAME and tok.string in KEYWORDS:
            # jangan ganti atribut, mis. obj.dalam
            if not (sebelumnya is not None and sebelumnya.string == "."):
                (r1, c1), (r2, c2) = tok.start, tok.end
                ganti.append((r1, c1, c2, KEYWORDS[tok.string]))
        if tok.type not in (tokenize.NL, tokenize.COMMENT):
            sebelumnya = tok
    for r, c1, c2, baru in reversed(ganti):
        b = baris[r - 1]
        baris[r - 1] = b[:c1] + baru + b[c2:]
    hasil = "".join(baris)
    return hasil[:-1] if ditambah else hasil


def buat_namespace() -> dict:
    ns = {"__name__": "__main__", "__builtins__": builtins}
    ns.update(BUILTINS_ID)
    return ns


def jalankan(sumber: str, nama_file: str = "<indopy>", ns: dict | None = None) -> int:
    ns = ns if ns is not None else buat_namespace()
    try:
        py = terjemahkan(sumber)
        objek = compile(py, nama_file, "exec")
        exec(objek, ns)
    except BrokenPipeError:
        return 0
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 0
    except (SyntaxError, tokenize.TokenError) as e:
        print(f"[IndoPython] Kesalahan sintaks: {e}", file=sys.stderr)
        return 1
    except Exception:
        print("[IndoPython] Terjadi kesalahan:", file=sys.stderr)
        traceback.print_exc()
        return 1
    return 0


class REPL(code.InteractiveConsole):
    def __init__(self):
        super().__init__(locals=buat_namespace(), filename="<indopy>")

    def runsource(self, source, filename="<indopy>", symbol="single"):
        try:
            py = terjemahkan(source)
        except tokenize.TokenError:
            return True  # blok belum selesai, minta baris lanjutan
        except IndentationError:
            return True
        return super().runsource(py, filename, symbol)
