# IndoPython 🇮🇩

Python versi Indonesia. Tulis kode pakai keyword bahasa Indonesia, semua fitur dan library Python tetap jalan.

```
fungsi sapa(nama):
    kalau nama == "Dunia":
        cetak("Halo, Dunia!")
    lainnya:
        cetak("Halo,", nama)

untuk i dalam rentang(3):
    sapa("Dunia")
```

## Instalasi

Butuh Python 3.10+. Nggak ada dependensi lain.

```bash
git clone https://github.com/AdityaDevID/indopython
cd indopython
pip install .
```

Atau langsung dari GitHub:

```bash
pip install git+https://github.com/AdityaDevID/indopython
```

Setelah itu command `idpy` bisa dipakai dari mana aja (di Termux juga bisa).

## Cara pakai

```bash
idpy tes.indo                 # jalanin file
idpy                          # REPL interaktif
idpy -c 'cetak("hai")'        # jalanin 1 baris
idpy --lihat tes.indo         # lihat hasil terjemahan ke Python
idpy --versi
```

Tanpa install juga bisa: `python -m indopy tes.indo` (dari folder `src`).

Contoh lengkap ada di folder `examples/`.

## Tes

```bash
pip install pytest
pytest
```

## Cara kerja

Transpiler ringan. Kode dibaca pakai modul `tokenize` bawaan Python, token keyword Indonesia diganti ke keyword Python (string, komentar, dan atribut seperti `obj.dalam` nggak ikut diganti), lalu dijalankan dengan `exec`. Nomor baris tetap sama, jadi pesan error menunjuk baris yang benar.

## Keyword

| Indo | Python | Indo | Python |
|---|---|---|---|
| `kalau` | `if` | `coba` | `try` |
| `atau_kalau` | `elif` | `kecuali` | `except` |
| `lainnya` | `else` | `akhirnya` | `finally` |
| `untuk` | `for` | `lempar` | `raise` |
| `selama` | `while` | `tegaskan` | `assert` |
| `dalam` | `in` | `impor` | `import` |
| `fungsi` | `def` | `dari` | `from` |
| `kembalikan` | `return` | `sebagai` | `as` |
| `hasilkan` | `yield` | `dengan` | `with` |
| `kelas` | `class` | `lewati` | `pass` |
| `anonim` | `lambda` | `berhenti` | `break` |
| `Benar` | `True` | `lanjut` | `continue` |
| `Salah` | `False` | `hapus` | `del` |
| `Kosong` | `None` | `nonlokal` | `nonlocal` |
| `dan` | `and` | `asinkron` | `async` |
| `atau` | `or` | `tunggu` | `await` |
| `bukan` | `not` | | |
| `adalah` | `is` | | |

## Fungsi bawaan

`cetak` `masukan` `rentang` `panjang` `tipe` `angka` `desimal` `teks` `boolean` `daftar` `kamus` `himpunan` `tupel` `urutkan` `balik` `jumlah` `maks` `mini` `mutlak` `bulatkan` `buka` `enumerasi` `gabung` `petakan` `saring` `semua` `adaapa` `apakah_instansi` `punya_atribut` `ambil_atribut` `atur_atribut` `bantuan` `keluar`

Keyword dan fungsi Python aslinya tetap bisa dipakai (`print`, `if`, dst), jadi boleh dicampur.

## Catatan

- Keyword `global` tetap pakai `global` (sama dengan Python).
- Pesan error dari Python masih berbahasa Inggris.
- Mau nambah keyword atau fungsi? Edit dict `KEYWORDS` dan `BUILTINS_ID` di `src/indopy/core.py`. PR welcome!

## Lisensi

MIT
