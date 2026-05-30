# TransactionAnalyzer

**TransactionAnalyzer** is a high-performance analytical tool written in modern **C++20**, designed for monitoring and analyzing large-scale networks of bank transactions. The primary goal of the project is to provide an efficient infrastructure for detecting financial fraud and uncovering money laundering chains (AML - Anti-Money Laundering).

---

## About the Project

By law, banking systems are required to analyze money flows and identify anomalies. From a graph theory perspective, bank accounts represent vertices, and individual payments act as directed edges within a network.

This project loads extensive datasets (in CSV and JSON formats) and builds a memory-optimized directed graph. An isolated evaluation module then runs on top of this architecture, utilizing advanced graph algorithms to fulfill two key analytical objectives:

* **Money Laundering Detection (DFS):** Criminals often launder money through a chain of shell companies until it returns to the original source. The application uses the Depth-First Search (DFS) algorithm to trace payments and detect these illegal cyclic dependencies.
* **Client Risk Analysis (BFS):** The system can evaluate the connection of regular accounts to known criminal entities on a blacklist. Using the Breadth-First Search (BFS) algorithm, it determines the shortest possible transaction path, helping investigators reconstruct the exact flow of funds.

The application emphasizes strict object-oriented design, data encapsulation, and maximum execution speed using modern features of the C++ Standard Template Library (STL).