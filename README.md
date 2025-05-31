# 📈 Stock Span & Price Tracker

## 🧠 Concepts Used
- Stack
- Queue
- Sliding Window
- Data Structures and Algorithms (DSA)

---

## 🚀 Project Description

This is a beginner-friendly Python project to simulate a basic **stock market analysis tool**. It includes:

1. **Stock Span Calculator**: Determines how many consecutive days before the current day the stock price was less than or equal to today's price. Useful for short-term trend analysis.

2. **Moving Average Calculator**: Computes the moving average of stock prices over a configurable number of past days (sliding window), commonly used to smooth out short-term fluctuations.

These implementations are great for learning how to apply DSA concepts like **stacks** and **queues** in real-world-like problems.

---

## 🛠 Features

- ✅ Stack-based calculation of stock span (O(n) efficiency)
- ✅ Queue-based sliding window for real-time moving average
- ✅ Clean CLI output with easy-to-follow results
- ✅ Pure Python, no external libraries needed

---

## 📊 Sample Output
Day | Price | Span | 3-Day Moving Avg
----------------------------------------
  1 |   100 |    1 |            100.0
  2 |    80 |    1 |             90.0
  3 |    60 |    1 |             80.0
  4 |    70 |    2 |             70.0
  5 |    60 |    1 |             63.3
  6 |    75 |    4 |             68.3
  7 |    85 |    6 |             73.3
├── stock_tracker.py       # Main script with logic
├── README.md              # Project description



