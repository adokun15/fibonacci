"""
==AUTHOR: Daniel Amos
==PROJECT: Impact of Input Size on Algorithms Performance
==GOAL: To help students understand the concept of scalability

==TASKS
i) Implement a program ( fibonacci sequence )
ii) Run the program for increasing input sizes and measure execution time
iii) Present findings with performance graphs
iv) Analyze and discuss how performance changes with input size
"""
import time
import matplotlib.pyplot as plt

inputs = [10, 15, 20, 25, 30, 35, 40, 45]
execution_time = []


def Fibonacci_Series(n):
    if n <= 1:
        return 1
    else:
        return Fibonacci_Series(n-1) + Fibonacci_Series(n-2)


for x in range(0, len(inputs)):
    # The time the programs starts
    start_time = time.time()

    # Default Time
    t = 0

    # Called for nTH number of time
    Fibonacci_Series(inputs[x])

    # The time the program ends for n Input
    end_time = time.time()

    # Time in Seconds
    t = (end_time - start_time)

    # Pushing each timer for different input into an Array
    execution_time.append(t)

    print(t)

# Plot a Graph for 'Execution Time' Against ' Inputs'
plt.plot(inputs, execution_time, marker="o")

plt.xlabel("Input Sizes")
plt.ylabel("Execution Time in milliseconds")
plt.title("fibonacci")

# Display Graph to Screen
plt.show()
