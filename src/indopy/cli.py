"""Command line: `idpy tes.indo`"""
import argparse
import sys

from . import __version__
from .core import REPL, jalankan, terjemahkan


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        prog="idpy",
        description="IndoPython - Python versi Indonesia",
    )
    p.add_argument("file", nargs="?", help="file .indo yang mau dijalankan")
    p.add_argument("-c", dest="perintah", help="jalankan kode langsung dari argumen")
    p.add_argument("--lihat", action="store_true",
                   help="tampilkan hasil terjemahan ke Python, tanpa dijalankan")
    p.add_argument("--versi", action="version", version=f"IndoPython {__version__}")
    a = p.parse_args(argv)

    if a.perintah is not None:
        sumber, nama = a.perintah, "<-c>"
    elif a.file:
        try:
            with open(a.file, encoding="utf-8") as f:
                sumber, nama = f.read(), a.file
        except FileNotFoundError:
            print(f"[IndoPython] File nggak ketemu: {a.file}", file=sys.stderr)
            return 1
    else:
        banner = (f"IndoPython {__version__} (Python {sys.version.split()[0]})\n"
                  "Ketik keluar() atau Ctrl+D untuk keluar.")
        REPL().interact(banner=banner, exitmsg="Sampai jumpa!")
        return 0

    if a.lihat:
        print(terjemahkan(sumber), end="")
        return 0
    return jalankan(sumber, nama)


if __name__ == "__main__":
    sys.exit(main())
