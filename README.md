## Khayyam-pascal-triangle

This repository contains implementations of algorithms to generate and display Pascal's Triangle (also known as Khayyam's Triangle) in different ways. The repository includes both linear and formula-based solutions, implemented in Python and C++.

---

## Table of Contents
- [Introduction](#introduction)
- [Files](#files)
- [Usage](#usage)
- [Algorithms](#algorithms)
  - [Linear Solution (for Python)](#linear-solution-for-python)
  - [Nth Line Formula](#nth-line-formula)
- [Contributing](#contributing)

---

## Introduction

Pascal's Triangle is a triangular array of the binomial coefficients. Each number in the triangle is the sum of the two directly above it. This repository provides different approaches to generate and display Pascal's Triangle:

1. **Linear Solution**: The entire triangle is stored in a linear list, and the triangle is calculated iteratively before being printed.
2. **Nth Line Formula**: The nth line of Pascal's Triangle is calculated using the binomial coefficient formula.

## Files

- **Linear Solution for Khayyam Pascal Triangle.py**: Python implementation of the linear solution.
- **Linear Solution in C++ .cpp**: C++ implementation of the linear solution.
- **Nth line of Pascal Triangle.py**: Python implementation to calculate the nth line of Pascal's Triangle using the binomial coefficient formula.

## Usage

### Python

To run the Python scripts, ensure you have Python installed on your system. You can run the scripts using the following commands:

```bash

# Linear Solution
python "Linear Solution for Khayyam Pascal Triangle.py"

# Nth Line Formula
python "Nth line of Pascal Triangle.py"

```

### C++
To compile and run the C++ implementation, you need a C++ compiler (e.g., g++). Use the following commands:

```bash

# Compile
g++ "Linear Solution in C++.cpp" -o pascal_triangle

# Run
./pascal_triangle

```
---

## Algorithms

### Linear Solution (for Python)

The linear solution stores the entire Pascal's Triangle in a linear list. The algorithm works as follows:

1. Skip the first two lines (which are always `[1]` and `[1, 1]`) and print them directly.
2. For the rest of the lines, use a pointer to sum the two numbers above the current position to generate the next number in the sequence.
3. Print the triangle in a structured format after calculating all lines.

### Nth Line Formula

The nth line of Pascal's Triangle can be calculated using the binomial coefficient formula:

$$
C(n, k) = \frac{n!}{k! \cdot (n - k)!}
$$

Where:
- \( n \) is the row number.
- \( k \) is the position in the row (starting from 0).

This formula is implemented in the `Nth line of Pascal Triangle.py` file.

---

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.
