# Efficient Text Compression in Python

### Comparative Study of LZW, Huffman, and Deflate Algorithms

This repository provides **research-oriented Python implementations** of three fundamental lossless compression algorithms:

* **Huffman Coding**
* **Lempel–Ziv–Welch (LZW)**
* **Deflate (zlib)**

The project includes **reproducible experiments**, **benchmark datasets**, and **performance metrics** for analyzing compression efficiency and runtime behavior.

The goal is to provide a **clean experimental framework for evaluating classical and modern compression techniques**.

---

# 📌 Research Objectives

This project investigates the following questions:

1. How do **classical compression algorithms** (Huffman, LZW) compare with **modern hybrid methods** (Deflate)?
2. What are the trade-offs between:

   * compression ratio
   * compression time
   * decompression time
3. How do these algorithms behave across **different text datasets**?

The repository is designed to support **reproducible benchmarking and analysis**.

---

# 📂 Repository Structure

```
compression-algorithms/

├── test_data/
│   ├── huffman/          # Huffman experiment datasets
│   ├── lzw/              # LZW experiment datasets
│   └── zlib/             # Deflate (zlib) experiment datasets
│
├── src/
│   ├── huffman.py        # Huffman compression implementation
│   ├── lzw.py            # LZW compression implementation
│   └── zlib.py           # Deflate (zlib) compression implementation
│
├── benchmarks/
│   ├── huffman_results.csv
│   ├── lzw_results.csv
│   └── zlib_results.csv
│
└── README.md
```

The repository separates:

* **Algorithms** → `src/`
* **Experimental datasets** → `test_data/`
* **Benchmark results** → `benchmarks/`

This separation improves **reproducibility and experimental clarity**.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/compression-algorithms.git
cd compression-algorithms
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Recommended Python version:

```
Python 3.9+
```

---

# 📁 Dataset Configuration

Experimental input files should be placed in the `test_data` directory.

Example:

```
test_data/

huffman/
    sample1.txt
    sample2.txt
    compressed/

lzw/
    sample1.txt
    compressed/

zlib/
    sample1.txt
    compressed/
```

Compressed outputs will be stored inside the `compressed/` subdirectory.

---

# 🔧 Cross-Platform File Handling

To ensure portability across **macOS, Windows, and Linux**, file paths are generated dynamically instead of using hard-coded local paths.

Example implementation:

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folder_directory = os.path.join(BASE_DIR, "test_data", "huffman")
comp_folder_directory = os.path.join(folder_directory, "compressed")
```

This guarantees that the code works regardless of where the repository is cloned.

---

# 🧪 Running Experiments

Example usage:

```python
from src.lzw import LZWCompressor
from src.huffman import HuffmanCompressor
from src.zlib import DeflateCompressor

compressor = LZWCompressor()

compressed = compressor.compress("example text")
decompressed = compressor.decompress(compressed)
```

---

# 📊 Benchmark Results

Benchmark results are stored as structured CSV files in the `benchmarks/` directory.

| File                  | Description                     |
| --------------------- | ------------------------------- |
| `huffman_results.csv` | Huffman compression performance |
| `lzw_results.csv`     | LZW compression performance     |
| `zlib_results.csv`    | Deflate compression performance |

Each benchmark file typically records:

* input file name
* original file size
* compressed file size
* compression ratio
* compression time
* decompression time

---

# 📈 Example Visualization

Benchmark results can be visualized using **Pandas** and **Matplotlib**.

```python
import pandas as pd
import matplotlib.pyplot as plt

lzw = pd.read_csv("benchmarks/lzw_results.csv")
huffman = pd.read_csv("benchmarks/huffman_results.csv")
zlib = pd.read_csv("benchmarks/zlib_results.csv")

plt.plot(lzw["File"], lzw["CompressionRatio"], label="LZW")
plt.plot(huffman["File"], huffman["CompressionRatio"], label="Huffman")
plt.plot(zlib["File"], zlib["CompressionRatio"], label="Deflate")

plt.xlabel("Dataset")
plt.ylabel("Compression Ratio")
plt.title("Compression Performance Comparison")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

# 📚 Algorithms Implemented

### Huffman Coding

A **statistical compression algorithm** that assigns variable-length codes based on symbol frequency.

### LZW (Lempel–Ziv–Welch)

A **dictionary-based compression method** widely used in formats such as GIF.

### Deflate (zlib)

A hybrid algorithm combining:

* **LZ77 dictionary compression**
* **Huffman coding**

Deflate is used in many formats including **ZIP, PNG, and HTTP compression**.

---

# 🔬 Reproducibility

To reproduce results:

1. Place datasets inside `test_data/`
2. Run the compression scripts
3. Generate benchmark results in `benchmarks/`
4. Analyze results using visualization scripts

All experiments are designed to be **deterministic and reproducible**.

---

# 🤝 Contributing

Contributions are welcome.

Possible improvements include:

* additional compression algorithms
* new benchmark datasets
* performance optimizations
* visualization tools

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 📖 Citation

If you use this repository in research or coursework, please cite:

```
Justin Chan. Efficient Text Compression in Python:
Comparative Study of LZW, Huffman, and Deflate Algorithms.
GitHub Repository.
```

---
