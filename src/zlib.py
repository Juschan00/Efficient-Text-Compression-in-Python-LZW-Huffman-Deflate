# ZLIB Compression and Decompression Algorithm

import time, os, fnmatch, zlib
from math import floor, ceil
from typing import AnyStr

# Compresses the input data using the ZLIB compression algorithm.
def zlib_compress(data: AnyStr) -> bytes:
    # Get start time for calculating compression time
    start_time = time.time()
    
    # "data" is the input data to be compressed
    if isinstance(data, str):
        data = data.encode()
    # Compress data using zlib.compress
    compressed = zlib.compress(data)

    # Calculate compression time: end time - start time
    compression_time = time.time() - start_time
    # Get compression output
    compression_output = compressed
    # Compressed binary string
    compressed_binary = bin(int.from_bytes(compressed, 'big'))[2:].zfill(len(compressed) * 8)
    # Compressed binary string length
    compression_length = len(compressed)

    return compressed_binary, compression_time, compression_length, compression_output

# Decompresses the input data using the ZLIB decompression algorithm.
def zlib_decompress(data: AnyStr) -> bytes:
    # Get start time for calculating the time taken for decompression
    start_time = time.time()
    if isinstance(data, str):
        data = data.encode()
    # Decompress data using zlib.decompress
    decompressed = zlib.decompress(data)

    # Calculate decompression time: end time - start time
    decompression_time = time.time() - start_time
    # Get decompression output, join bytes together from list, decode bytes (change type to string)
    decompression_output = decompressed.decode()
    # Decompressed binary string
    decompressed_binary = "".join(format(ord(c), '08b') for c in decompression_output)
    # Decompressed binary string length
    decompression_length = ceil(len(decompressed_binary) / 8)

    return decompressed_binary, decompression_time, decompression_length, decompression_output

# Test ZLIB compression and decompression
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

folder_directory = os.path.join(BASE_DIR, "test_data", "zlib")
comp_folder_directory = os.path.join(folder_directory, "compressed")

# Count files in sample data folder
count = len(fnmatch.filter(os.listdir(folder_directory), '*.*')) - 1

# For loop iterating through every sample data file and compresses it, then outputs the data for quantifying efficiency
for i in range(count):

    # Increment file number
    file_num = i + 1
    # Access original TXT file data for compression
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
    comp_binary, comp_time, comp_filesize, comp_output = zlib_compress(content)
    decomp_binary, decomp_time, decomp_filesize, decomp_output = zlib_decompress(comp_output)

    # Set compressed file name in ".zlib" format
    comp_filename_zlib = org_filename + "_compressed.zlib"
    # Write ZLIB file to store compressed data in ".zlib" format
    comp_filepath_zlib = os.path.join(comp_folder_directory, comp_filename_zlib) 
    comp_file_zlib = open(comp_filepath_zlib, "wb")
    comp_file_zlib.write(comp_output)
    comp_file_zlib.close()

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
    print(f"---ZLIB Compression Test {file_num}---")
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

    file.close()