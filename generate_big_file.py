def generate_file(filename="big_file.txt", size_in_mb=100):
    line = "This is a sample sentence that will be repeated many times.\n"
    line_size = len(line.encode('utf-8'))
    repetitions = (size_in_mb * 1024 * 1024) // line_size

    with open(filename, "w", encoding="utf-8") as f:
        for _ in range(repetitions):
            f.write(line)

    print(f"✅ Archivo '{filename}' generado con ~{size_in_mb}MB.")

if __name__ == "__main__":
    generate_file()
