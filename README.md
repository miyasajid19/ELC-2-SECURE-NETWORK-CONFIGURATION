
# Secure Network Configuration

This repository contains the implementation of three cryptographic algorithms—Caesar Cipher, Playfair Cipher, and Hill Cipher—developed as part of the **CSED-Experiential Learning Activities-E110 2024** mini-project at Thapar Institute of Engineering and Technology.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Results and Analysis](#results-and-analysis)
- [Future Scope](#future-scope)
- [Acknowledgments](#acknowledgments)

## Overview

This project demonstrates the use of encryption and decryption to secure data using:
1. **Caesar Cipher**: Fast but less secure.
2. **Playfair Cipher**: Offers moderate security and speed.
3. **Hill Cipher**: Ensures robust security at the cost of higher computational overhead.

The program:
- Encrypts and decrypts text-based data.
- Measures and compares the performance of these algorithms.
- Visualizes execution times through comparative graphs.

## Features

- Implementation of encryption and decryption for three algorithms.
- Time benchmarking for each algorithm.
- File-based input and output for encrypted and decrypted text.
- Comparative analysis of algorithm performance.
- Graphical visualization of encryption and decryption times.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `numpy` for matrix operations in Hill Cipher.
  - `matplotlib` for visualizing performance metrics.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/secure-network-configuration.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd secure-network-configuration
   ```
3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place the text file to be encrypted as `testing.txt` in the root directory.
2. Run the main Python script:
   ```bash
   python main.py
   ```
3. Output:
   - Encrypted text files: `EncryptedText/`
   - Decrypted text files: `DecryptedText/`
   - Graph of encryption and decryption times is displayed.

## Results and Analysis

- **Caesar Cipher**: Fastest, but provides limited security.
- **Playfair Cipher**: Strikes a balance between speed and security.
- **Hill Cipher**: Most secure but computationally expensive.

A detailed analysis and comparison are presented in the project documentation.

## Future Scope

- Incorporation of modern cryptographic techniques.
- Extension to include asymmetric encryption algorithms.
- Development of a GUI for enhanced usability.

## Acknowledgments

Special thanks to the Department of Computer Science and Engineering, Thapar Institute of Engineering and Technology, for their guidance and support in completing this project.
