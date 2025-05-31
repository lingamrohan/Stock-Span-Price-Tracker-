from collections import deque

class StockSpanner:
    def __init__(self):
        self.stack = []  # Pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        # Compare with top of stack, and aggregate spans
        while self.stack and self.stack[-1][0] <= price:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price, span))
        return span


class MovingAverage:
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.window = deque()
        self.total = 0

    def next(self, price: float) -> float:
        self.window.append(price)
        self.total += price

        if len(self.window) > self.window_size:
            removed = self.window.popleft()
            self.total -= removed

        return self.total / len(self.window)


# Example usage:
if __name__ == "__main__":
    prices = [100, 80, 60, 70, 60, 75, 85]
    print("Prices:", prices)

    spanner = StockSpanner()
    ma = MovingAverage(window_size=3)

    print("\nDay | Price | Span | 3-Day Moving Avg")
    print("-" * 35)
    for day, price in enumerate(prices, start=1):
        span = spanner.next(price)
        avg = ma.next(price)
        print(f"{day:3} | {price:5} | {span:4} | {avg:16.2f}")
