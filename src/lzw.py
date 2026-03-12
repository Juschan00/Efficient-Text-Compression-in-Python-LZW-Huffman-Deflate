#LZW Compression and Decompression Algorithm

import time, os, fnmatch
from math import floor, ceil
from typing import AnyStr
from struct import *

ASCII_TO_INT: dict = {i.to_bytes(1, 'big'): i for i in range(256)}
INT_TO_ASCII: dict = {i: b for b, i in ASCII_TO_INT.items()}

# Compresses the input data using the LZW compression algorithm.
def lzw_compress(data: AnyStr) -> bytes:
    # Get start time for calulating compression time
    start_time = time.time()
    
    # "data" is the input data to be compressed
    if isinstance(data, str):
        data = data.encode()
    keys: dict = ASCII_TO_INT.copy()
    n_keys: int = 256
    compressed: list = []
    start: int = 0
    n_data: int = len(data)+1
    while True:
        if n_keys >= 512:
            keys = ASCII_TO_INT.copy()
            n_keys = 256
        for i in range(1, n_data-start):
            w: bytes = data[start:start+i]
            if w not in keys:
                compressed.append(keys[w[:-1]])
                keys[w] = n_keys
                start += i-1
                n_keys += 1
                break
        else:
            compressed.append(keys[w])
            break
    bits: str = ''.join([bin(i)[2:].zfill(9) for i in compressed])

    # Calculate compression time: end time - start time
    compression_time = time.time() - start_time
    # Get compression output
    compression_output = int(bits, 2).to_bytes(ceil(len(bits) / 8), 'big')
    # Compressed binary string
    compressed_binary = bits
    # Compressed binary string length
    compression_length = ceil(len(bits) / 8)

    return compressed_binary, compression_time, compression_length, compression_output

# Decompresses the input data using the LZW decompression algorithm.
def lzw_decompress(data: AnyStr) -> bytes:
    # Get start time for calulating the time taken for decompression
    start_time = time.time()
    if isinstance(data, str):
        data = data.encode()
    keys: dict = INT_TO_ASCII.copy()
    bits: str = bin(int.from_bytes(data, 'big'))[2:].zfill(len(data) * 8)
    n_extended_bytes: int = floor(len(bits) / 9)
    bits: str = bits[-n_extended_bytes * 9:]
    data_list: list = [int(bits[i*9:(i+1)*9], 2)
                       for i in range(n_extended_bytes)]
    previous: bytes = keys[data_list[0]]
    decompressed: list = [previous]
    n_keys: int = 256
    for i in data_list[1:]:
        if n_keys >= 512:
            keys = INT_TO_ASCII.copy()
            n_keys = 256
        try:
            current: bytes = keys[i]
        except KeyError:
            current = previous + previous[:1]
        decompressed.append(current)
        keys[n_keys] = previous + current[:1]
        previous = current
        n_keys += 1

    # Calculate decompression time: end time - start time
    decompression_time = time.time() - start_time
    # Get decompression output, join bytes together from list, decode bytes (change type to string)
    decompression_output = b''.join(decompressed).decode()
    # Deompressed binary string
    decompressed_binary = "".join(format(ord(c), '08b') for c in decompression_output)
    # Decompressed binary string length
    decompression_length = ceil(len(decompressed_binary) / 8)

    return  decompressed_binary, decompression_time, decompression_length, decompression_output

# Test LZW compression and decompression
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folder_directory = os.path.join(BASE_DIR, "test_data", "lzw")
comp_folder_directory = os.path.join(folder_directory, "compressed")

# Count files in sample data folder
count = len(fnmatch.filter(os.listdir(folder_directory), '*.*')) - 1

# For loop iterating through every sample data file and compresses it, then outputs the data for quantifying efficiency
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
    # Get the original file size with the binary string
    org_filesize = ceil(len(org_binary) / 8)

    # Get compressed binary string, compression time, compressed file size with binary string, compressed
    comp_binary, comp_time, comp_filesize, comp_output = lzw_compress(content)
    decomp_binary, decomp_time, decomp_filesize, decomp_output = lzw_decompress(comp_output)

    # Set compressed file name in ".lzw" format
    comp_filename_lzw = org_filename + "_compressed.lzw"
    # Write LZW file to store compressed data in ".lzw" format
    comp_filepath_lzw = os.path.join(comp_folder_directory, comp_filename_lzw) 
    comp_file_lzw = open(comp_filepath_lzw, "wb")
    for data in comp_output:
        comp_file_lzw.write(pack('>H',int(data)))
    comp_file_lzw.close()

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
    print(f"---LZW Compression Test {file_num}---")
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