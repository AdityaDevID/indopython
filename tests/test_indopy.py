import subprocess
import sys
from pathlib import Path

from indopy import buat_namespace, jalankan, terjemahkan

ROOT = Path(__file__).resolve().parent.parent


def test_keyword_dasar():
    assert terjemahkan("kalau Benar:\n    lewati\n") == "if True:\n    pass\n"


def test_string_dan_komentar_aman():
    src = 'cetak("untuk kalau")  # untuk apa\n'
    assert terjemahkan(src) == src


def test_atribut_tidak_diganti():
    assert terjemahkan("obj.dalam\n") == "obj.dalam\n"


def test_fstring_ekspresi_diterjemahkan():
    assert "None" in terjemahkan('x = f"{Kosong}"\n')


def test_nomor_baris_tetap():
    src = "fungsi f():\n    kembalikan 1\n\nf()\n"
    assert terjemahkan(src).count("\n") == src.count("\n")


def test_jalankan(capsys):
    assert jalankan('cetak("hai", panjang("abc"))', ns=buat_namespace()) == 0
    assert capsys.readouterr().out == "hai 3\n"


def test_sintaks_salah():
    assert jalankan("kalau Benar cetak(1)") == 1


def test_cli_file():
    out = subprocess.run(
        [sys.executable, "-m", "indopy", str(ROOT / "examples" / "fizzbuzz.indo")],
        capture_output=True, text=True,
    )
    assert out.returncode == 0
    assert out.stdout.splitlines()[14] == "FizzBuzz"
