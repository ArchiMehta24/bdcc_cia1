import matplotlib.pyplot as plt

# Function to parse the data from the text file
def parse_data(filename):
    data = {}
    fibonacci_values = set()

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            interpreter = parts[0].split(": ")[1]
            n_value = int(parts[1].split("(")[1].split(")")[0])
            time_taken = float(parts[2].split(": ")[1].split(" ")[0])

            # Add to dictionary
            if interpreter not in data:
                data[interpreter] = []
            data[interpreter].append((n_value, time_taken))

            # Collect Fibonacci input values
            fibonacci_values.add(n_value)

    # Ensure the data is sorted by Fibonacci values for each interpreter
    for interpreter in data:
        data[interpreter] = sorted(data[interpreter])

    return data, sorted(fibonacci_values)

# Parse the data from the file
filename = "benchmark_results.txt"
data, fibonacci_values = parse_data(filename)

# Visualize the data 
for interpreter, values in data.items():
    n_values, times = zip(*values)
    plt.plot(n_values, times, marker="o", label=interpreter)

# Add titles and labels
plt.title("Performance Comparison of Python Implementations")
plt.xlabel("Fibonacci Input (n)")
plt.ylabel("Execution Time (seconds)")
plt.legend()
plt.grid()

# Set specific x-axis ticks
plt.xticks([25, 30, 35])

# Save and show the chart
plt.savefig("performance_comparison_chart.png")
plt.show()
