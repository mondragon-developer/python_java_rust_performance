/// Rust Word Frequency Counter
///
/// This program reads a large text file, counts the frequency of each word,
/// and writes the top 10 most common words to a file.
///
/// Author: Jose R. Mondragon

use std::collections::HashMap;
use std::fs;
use std::time::Instant;
use std::io::Write;

/// Counts words in a file and writes the top 10 to "result.txt"
fn main() {
    let start = Instant::now();

    let content = fs::read_to_string("../big_file.txt").expect("Failed to read file");
    let words = content.to_lowercase().split_whitespace();

    let mut counter = HashMap::new();
    for word in words {
        *counter.entry(word).or_insert(0) += 1;
    }

    let mut word_vec: Vec<_> = counter.iter().collect();
    word_vec.sort_by(|a, b| b.1.cmp(a.1));

    let mut file = fs::File::create("result.txt").expect("Cannot create file");
    writeln!(file, "Top 10 most common words:").unwrap();
    for (word, count) in word_vec.iter().take(10) {
        writeln!(file, "{}: {}", word, count).unwrap();
    }

    let duration = start.elapsed();
    println!("✅ Execution time: {:.3?} seconds", duration);
}
