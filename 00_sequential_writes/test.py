#!/usr/bin/env -S uv run --script

import os
import sys
import argparse

def run_sequential_write_test(file_path: str, num_runs: int, transfer_size: int, keep_file: bool):
    print(f"Starting test on '{file_path}'...")

    try:
        with open(file_path, 'wb') as file_handle:
            print(f"Writing to file {num_runs} times with a transfer size of {transfer_size} bytes...")
            for i in range(num_runs):
                random_data = os.urandom(transfer_size)
                file_handle.write(random_data)

            print("Writing complete.")

    except OSError as e:
        print(f"An OS error occurred: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
    finally:
        if not keep_file:
            try:
                os.remove(file_path)
                print(f"File '{file_path}' has been removed.")
            except OSError as e:
                print(f"Could not remove the file: {e}", file=sys.stderr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a sequential write test.")
    parser.add_argument("filename", help="The name of the file to generate.")
    parser.add_argument("--file-size", type=int, default=512 * 1024 * 1024, help="The total file size in bytes.")
    parser.add_argument("--transfer-size", type=int, default=512, help="The size of each write transfer in bytes.")
    parser.add_argument("--keep", action="store_true", help="Keep the generated file after the test.")
    args = parser.parse_args()

    iterations = args.file_size // args.transfer_size
    if args.file_size % args.transfer_size != 0:
        iterations += 1

    run_sequential_write_test(args.filename, iterations, args.transfer_size, args.keep)
