#!/usr/bin/env python3
import time
from turtle import forward, left, right, speed


def generate_dragon_curve_sequence(n: int) -> str:
    if n == 0:
        # Base case with a single "R" fold
        return "R"
    else:
        prev_sequence = generate_dragon_curve_sequence(n - 1)
        # Step 1 & 2: Make a reversed copy of the sequence, replacing 'R' with 'L' and vice versa
        reverse_sequence = prev_sequence[::-1]
        reverse_sequence = reverse_sequence.replace("L", "temp")
        reverse_sequence = reverse_sequence.replace("R", "L")
        reverse_sequence = reverse_sequence.replace("temp", "R")

        # Step 3: Join original and modified copy with an 'R' in between
        return prev_sequence + "R" + reverse_sequence


def draw_dragon_curve(sequence):
    for move in sequence:
        forward(10)  # Move forward for each letter
        if move == "R":
            right(60)
        elif move == "L":
            left(120)


# Example usage for a specific depth
depth = 12  # Adjust the depth as needed
sequence = generate_dragon_curve_sequence(depth)
print(sequence)

speed(0)
draw_dragon_curve(sequence)
time.sleep(10)
