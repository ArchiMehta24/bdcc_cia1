import time

# Function to compute the nth Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# To measure the executoon time of the fibonacci computation
def benchmark_fibonacci(n, implementation_name):
    start_time = time.time()
    result = fibonacci(n)
    elapsed_time = time.time() - start_time
    return implementation_name, result, elapsed_time

# Save results to a single file (append mode)
def save_results_to_file(result, filename="benchmark_results.txt"):
    with open(filename, "a") as f:
        implementation, output, elapsed_time = result

        # Include `n` in the saved results
        f.write(f"Name of the Interpreter: {implementation}, Fibonacci({n}): {output}, Time Taken: {elapsed_time:.4f} seconds\n")
        
        # Updated code for compatibility with Jython:
        # f.write("Name of the Interpreter: {}, Fibonacci({}): {}, Time Taken: {:.4f} seconds\n".format(implementation, n, output, elapsed_time))
    
    # print statement(incompatible with Jython):
    print(f"Result for {result[0]} saved to {filename}")
    
    # print statement for Jython compatibility:
    # print("Result for {} saved to {}".format(result[0], filename))

if __name__ == "__main__":
    # Adjust the Fibonacci input
    n = 35  # You can modify this for a different Fibonacci number

    # Define the interpreter name
    interpreter_name = "PyPy"  # Change this to "Jython" or "PyPy" when running in those environments

    # Run benchmark
    result = benchmark_fibonacci(n, interpreter_name)

    # Save result to a single .txt file
    save_results_to_file(result)

