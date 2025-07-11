"""
Python Word Frequency Counter
=============================

This script reads a large text file, counts the frequency of each word,
and writes the top 10 most common words to an output file.

It also profiles the execution using cProfile and saves a detailed report.

Author: Jose R. Mondragon
"""

import time
from collections import Counter
import cProfile
import pstats

def count_words_from_file(filepath: str, output_path: str) -> None:
    """
    Counts word frequencies in a text file and writes the top 10 to output_path.

    Args:
        filepath (str): Path to the input text file.
        output_path (str): Path to the output file to write the results.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        words = file.read().lower().split()

    counter = Counter(words)
    most_common = counter.most_common(10)

    with open(output_path, "w", encoding="utf-8") as out:
        out.write("Top 10 most common words:\n")
        for word, freq in most_common:
            out.write(f"{word}: {freq}\n")

def main():
    profiler = cProfile.Profile()
    profiler.enable()

    start = time.time()
    count_words_from_file("../big_file.txt", "result.txt")
    end = time.time()

    profiler.disable()
    print(f"✅ Execution time: {end - start:.3f} seconds")
    profiler.dump_stats("profile_python.prof")

    with open("profile_report.txt", "w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats(pstats.SortKey.CUMULATIVE)
        stats.print_stats()

if __name__ == "__main__":
    main()
