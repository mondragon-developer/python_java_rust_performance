# Language Performance Benchmark: Python vs Java vs Rust

## Objective

To compare the execution performance of Python, Java, and Rust when processing a large 100MB text file. Each implementation reads the file, counts the frequency of each word, and prints the 10 most common words.

---

## Project Structure

```
language-comparison-speed/
├── generate_big_file.py            # Script to generate a ~100MB file
├── big_file.txt                    # (Ignored by git)
├── python_word_counter/            # Python implementation with profiler
├── java_word_counter/              # Java implementation
├── rust_word_counter/              # Rust implementation
├── .gitignore                      # Excludes large/generated files
└── README.md                       # This file
```

---

## Method

Each program:
- Reads `big_file.txt`
- Counts word frequencies
- Outputs top 10 most common words to `resultado.txt`
- Measures total execution time
- In Python, a detailed profiling report is also generated

---

## ⏱ Results (on Intel i7, 16GB RAM)

| Language | Time (s) | Notes                        |
|----------|----------|------------------------------|
| Python   | ~9.3     | Easy to write, slower        |
| Java     | ~2.4     | Balanced and scalable        |
| Rust     | ~0.6     | Fastest and most efficient   |

---

## How to Use

1. Run the generator:
```bash
python generate_big_file.py
```

2. Run each implementation:

**Python**
```bash
cd python_word_counter
python main.py
```

**Java**
```bash
cd java_word_counter
javac Main.java
java Main
```

**Rust**
```bash
cd rust_word_counter
cargo run
```

---

## Takeaways (My humble opinion so far)

- **Rust** is ideal for performance-critical systems, CLI tools, and embedded devices.
- **Java** remains strong in enterprise systems with good performance and ecosystem support.
- **Python** is excellent for rapid prototyping, data analysis, and teaching, despite being slower.

**Recommendation:** Use Rust for modules where performance matters. Use Python or Java when development speed and team familiarity are more critical.

---

## Author

**Jose R. Mondragon**  
Senior Software Engineer | Educator | AI & Simulation Enthusiast  
LinkedIn: [https://www.linkedin.com/in/mondradev/] 
GitHub: []

---
