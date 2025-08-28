# Sequential Write Performance Benchmarks

This directory contains scripts to benchmark the sequential write performance
of Fusion against a standard `ext4` filesystem.

## Requirements

- The directories `/fusion` and `/ext4` must exist and be writable.
- [`hyperfine`](https.github.com/sharkdp/hyperfine) version 1.19 or higher must
  be installed.
- [`uv`](https://github.com/astral-sh/uv) must be installed to run the Python
  test script.

## `test.py`

The `test.py` script is a helper utility for performing sequential write tests.
It generates a file of a specified size by writing random data in chunks.

### Arguments

- `filename`: The path to the output file.
- `--file-size`: The total size of the file to generate in bytes (default:
  512MiB).
- `--transfer-size`: The size of each individual write operation in bytes
  (default: 512 bytes).
- `--keep`: If specified, the generated file will not be deleted after the test
  completes.

## Usage

To run the benchmarks, first clone the repository, then prepare the
environment by creating the test directories. Ensure the `fusion` binary is in
your `PATH`.

```bash
git clone https://github.com/alberto-miranda/fusion-performance-benchmarks.git
cd fusion-performance-benchmarks/00_sequential_writes
mkdir -p /fusion /ext4
./run.sh
```

The benchmark results are stored in the `results` directory in Markdown format.
Each file is named with a timestamp, for example `bench-1756367027.md`. The 
results include the command run, the mean, standard deviation, median, min,
and max execution times.

