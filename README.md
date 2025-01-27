# Impact of Input Size on Algorithm Performance

This project investigates the relationship between input size and the execution time of a simple algorithm.
We chose to analyse the **Fibonacci Series** algorithm. The *goal* of this project is to understand how the performance
of this algorithm changes as the **_input size_** increases.

## METHODOLOGY

**Implementation**
> We implemented the Fibonacci Series algorithm in Python

**Testing**
> We ran the program with a range of input sizes, starting from a smaller value 
> _10_ and gradually increases by 5. For each input size we measured the execution
> time of the algorithm
 
**Data Collection**
> We recorded the input size and corresponding execution time for each run.

## Fibonacci Series : A Recursive Algorithm

### A python program - [check it here](/fib.py)
+ The first step in our project was creating some sample **inputs** with an empty list of **Execution time** 
```
# Importing Necessary Module

import time
import matplotlib.pyplot as plt

# Set of sample input
inputs = [10, 15, 20, 25, 30, 35, 40, 45]

execution_time = []
```

+ The next step was to implement a function that is recursive : **Calls itself** -
**_n_** represent the _n**TH**_ the program was to run again and again.

```
def Fibonacci_Series(n):
    if n <= 1:
        return 1
    else:
        return Fibonacci_Series(n-1) + Fibonacci_Series(n-2)
```
+ Iterating the program for each value of the Input List
```

for x in range(0, len(inputs)):
    # The time the programs starts
    start_time = time.time()

    # Default Time
    t = 0

    # Called for nTH number of time: a recursive function
    Fibonacci_Series(inputs[x])

    # The time the program ends for n Input
    end_time = time.time()

    # Time in Seconds
    t = (end_time - start_time)

    # Pushing each timer for different input into an Array
    execution_time.append(t)

    # Display each execute time to the user
    print(t)

```

+ In our final step, we took a step further and imply the use of matplotlib
to show us a graphical representation of 'Input Size' against 'Execution Time'
```

# Plots a Graph for 'Execution Time' Against ' Inputs'
plt.plot(inputs, execution_time, marker="o")

plt.xlabel("Input Sizes" )
plt.ylabel("Execution Time in seconds")
plt.title("fibonacci")

# Display Graph to Screen
plt.show()

```
### Result of our Program

![An image of an executed program result](/result.png)

We created a plot to visualize the relationship between input size and execution time. The plot shows that the execution time increases as the Input size increases. However, the increase seems to accelerate as the input size grow larger. This suggests that the factorial calculation algorithm has a time complexity that is more than linear

### More To See..

The result demonstrate the concept of scalability. As the Input size increases, the algorithm's performanance degrades. This is an Important considerations for real-world applications where algorithms may need to handle large inputs.

### Conclusion

Through this project , we gained aa deeper understanding of how input size affect algorithm perfoamance. The result highlight the importance of considering scalability when designing and implementing algorithms.

####
Written by [Daniel Amos](https://ohida.vercel.app)
