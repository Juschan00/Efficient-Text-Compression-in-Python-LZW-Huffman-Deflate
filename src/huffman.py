# Huffman Coding Compression Algorithm
import heapq
import time, os, fnmatch
from collections import defaultdict
from math import floor, ceil
from typing import AnyStr
from struct import *

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

# Function to build a frequency table from a given string
def build_frequency_table(s):
    # Create a default dictionary to store character frequencies
    frequency = defaultdict(int)
    # Iterate over each character in string
    for char in s:
        # Increment frequency of character
        frequency[char] += 1
    return frequency

# Function to build a Huffman tree from a frequency table
def build_huffman_tree(frequency):
    # Create a heap to store nodes of  Huffman tree
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    # Heapify list to maintain heap property
    heapq.heapify(heap)
    # While there are more than one nodes in heap
    while len(heap) > 1:
        # Extract two nodes with lowest frequencies
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        # Assign '0' to left child and '1' to right child
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        # Push merged node back into heap
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    # Return root node of Huffman tree
    return heap[0]

# Function to build Huffman codes from a Huffman tree
def build_huffman_codes(tree):
    # Create a dictionary to store Huffman codes
    huffman_codes = {}
    # Iterate over each node in Huffman tree
    for pair in tree[1:]:
        # Assign  Huffman code to corresponding symbol
        huffman_codes[pair[0]] = pair[1]
    return huffman_codes

def huffman_compress(data):
    # Get start time for calulating compression time
    start_time = time.time()    

    # Build the Huffman tree
    frequency_table = build_frequency_table(data)
    root = build_huffman_tree(frequency_table)

    # Generate Huffman codes
    huffman_codes = build_huffman_codes(root)

    bits = "".join(huffman_codes[char] for char in data)

    # Calculate compression time: end time - start time
    compression_time = time.time() - start_time  
    # Get compression output
    compression_output = int(bits, 2).to_bytes((len(bits) + 7) // 8, 'big')
    # Compressed binary string
    compressed_binary = bits
    # Compressed binary string length
    compression_length = ceil(len(compressed_binary) / 8)

    return compressed_binary, compression_time, compression_length, compression_output, huffman_codes

# Decompresses input data using Huffman Coding decompression algorithm.
def huffman_decompress(compressed_binary: str, huffman_codes: dict):
    # Get start time for calulating decompression time
    start_time = time.time()

    # Reverse the Huffman codes dictionary to map codes to characters
    reverse_huffman_codes = {code: char for char, code in huffman_codes.items()}

    # Initialize variables
    current_code = ""
    decompression_output = ""

    # Iterate over each bit in the compressed binary string
    for bit in compressed_binary:
        current_code += bit
        # Check if the current code corresponds to a character
        if current_code in reverse_huffman_codes:
            char = reverse_huffman_codes[current_code]
            decompression_output += char
            current_code = ""  # Reset the current code

    # Calculate decompression time: end time - start time
    decompression_time = time.time() - start_time
    # Deompressed binary string
    decompressed_binary = "".join(format(ord(c), '08b') for c in decompression_output)
    # Get decompressed binary string length
    decompression_length = len(decompression_output)

    return decompressed_binary, decompression_time, decompression_length, decompression_output

# Test Huffman compression and decompression
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folder_directory = os.path.join(BASE_DIR, "test_data", "huffman")
comp_folder_directory = os.path.join(folder_directory, "compressed")

# Count files in sample data folder
count = len(fnmatch.filter(os.listdir(folder_directory), '*.*')) - 1

# For loop iterating through every sample data file and compresses it, and outputs data for quantifying efficiency
for i in range(count):

    # Increment file number
    file_num = i + 1
    # Access orignial TXT file data for compression
    org_filepath = folder_directory + "test" + str(file_num) + ".txt"
    # Get original file name
    org_filename = os.path.splitext(os.path.basename(org_filepath))[0]
    file = open(org_filepath,"r")
    content = file.read()
    # Convert original txt file data to binary string
    org_binary = "".join(format(ord(c), '08b') for c in content)
    # Get original file size with binary string
    org_filesize = ceil(len(org_binary) / 8)

    # Get compressed binary string, compression time, compressed file size with binary string, compressed
    comp_binary, comp_time, comp_filesize, comp_output, huffman_codes = huffman_compress(content)
    decomp_binary, decomp_time, decomp_filesize, decomp_output = huffman_decompress(comp_binary, huffman_codes)

    # Set compressed file name in ".huffman" format
    comp_filename_huffman = org_filename + "_compressed.huf"
    # Write huffman file to store compressed data in ".huffman" format
    comp_filepath_huffman = os.path.join(comp_folder_directory, comp_filename_huffman) 
    comp_file_huffman = open(comp_filepath_huffman, "wb")
    for data in comp_output:
        comp_file_huffman.write(pack('>H',int(data)))
    comp_file_huffman.close()

    # Set compressed file name in ".bin" format
    comp_filename_bin = org_filename + "_compressed.bin"
    # Write bin file to store compressed data in ".bin" format
    comp_filepath_bin = os.path.join(comp_folder_directory, comp_filename_bin) 
    comp_file_bin = open(comp_filepath_bin, "wb")
    comp_file_bin.write(comp_binary.encode()) 
    comp_file_bin.close()

    # Calculate compression ratio: original file size / compressed file size
    comp_ratio = org_filesize / comp_filesize

    # Output data for quantifying efficiency
    print(f"---Huffman Compression Test {file_num}---")
    # print(f"Original Binary String: {org_binary}")
    # print(f"Compressed Binary String: {comp_binary}")
    # print(f"Decompressed Binary String: {decomp_binary}")
    # print("---")
    # print(f"Compression output: {comp_output}")  
    # print(f"Decompression output: {decomp_output}")  
    # print("---")
    
    print(f"Original File Size (Bytes): {org_filesize}")
    print(f"Compressed File Size (Bytes): {comp_filesize}")
    print(f"Decompressed File Size (Bytes): {decomp_filesize}")
    print("---")
    print(f"Compression Ratio: {comp_ratio:.2f}")
    print(f"Compression Time: {comp_time:.6f}")
    print(f"Decompression Time: {decomp_time:.6f}")
    print("---------------------------------")

    # print(f"{org_filesize},{comp_filesize},{comp_ratio:.2f},{comp_time:.6f},{decomp_time:.6f}")
    file.close()