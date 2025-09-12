# Efficient Text Compression in Python – LZW, Huffman & Deflate

Optimized Python implementations of **Lempel-Ziv-Welch (LZW)**, **Huffman Coding**, and **Deflate (zlib)** algorithms. Includes reproducible experiments with benchmarks on compression ratio and runtime, stored as CSV files for easy analysis.

---

## 🚀 Features
- Modular Python implementations: `LZW.py`, `Huffman.py`, `Deflate_Zlib.py`  
- Organized datasets per algorithm (`data_Huffman`, `data_LZW`, `data_Deflate_ZLIB`)  
- Benchmark results stored as CSV files (`LZW.csv`, `Huffman.csv`, `ZLIB.csv`)  
- Ready-to-run with reproducible workflows for research  

---

## 📂 Repository Structure
```

├── data/
│   ├── data\_Huffman/       # Huffman experiment input/output
│   ├── data\_LZW/           # LZW experiment input/output
│   ├── data\_Deflate\_ZLIB/  # Deflate (zlib) experiment input/output
│
├── src/
│   ├── Huffman.py          # Huffman implementation
│   ├── LZW\.py              # LZW implementation
│   ├── Deflate\_Zlib.py     # Deflate implementation
│
├── benchmarks/
│   ├── Huffman.csv         # Huffman benchmark results
│   ├── LZW\.csv             # LZW benchmark results
│   ├── ZLIB.csv            # Deflate benchmark results
│
└── README.md               # Documentation

````

---

## ⚡ Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/your-username/compression-algorithms.git
cd compression-algorithms
pip install -r requirements.txt
````

---

## 🛠 Usage

Run benchmarks across all algorithms:

```bash
python benchmarks/run_all.py
```

Or test individual algorithms directly:

```python
from src.LZW import LZWCompressor
from src.Huffman import HuffmanCompressor
from src.Deflate_Zlib import DeflateCompressor

# Example: LZW
compressor = LZWCompressor()
compressed = compressor.compress("your text here")
decompressed = compressor.decompress(compressed)
```

---

## 📊 Results

Benchmark results are stored as CSV files in `benchmarks/` for reproducibility:

* **Huffman.csv** – compression ratio, compression/decompression time
* **LZW\.csv** – compression ratio, compression/decompression time
* **ZLIB.csv** – compression ratio, compression/decompression time

---

## 📈 Sample Results Visualization

You can easily plot benchmark results using **Matplotlib** or **Pandas**.
Example: comparing compression ratios across algorithms.

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load benchmark CSVs
lzw = pd.read_csv("benchmarks/LZW.csv")
huffman = pd.read_csv("benchmarks/Huffman.csv")
zlib = pd.read_csv("benchmarks/ZLIB.csv")

# Example assumes each CSV has 'File' and 'CompressionRatio' columns
plt.plot(lzw["File"], lzw["CompressionRatio"], label="LZW")
plt.plot(huffman["File"], huffman["CompressionRatio"], label="Huffman")
plt.plot(zlib["File"], zlib["CompressionRatio"], label="Deflate (zlib)")

plt.xlabel("Dataset")
plt.ylabel("Compression Ratio")
plt.title("Compression Ratio Comparison")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

This produces a clear visualization comparing how each algorithm performs across datasets.

---

## 🎯 Research Goals

* Compare classical (Huffman, LZW) vs modern (Deflate) compression methods
* Quantify trade-offs between compression efficiency and speed
* Provide reproducible, research-ready benchmarks

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
