from steepest_descent import SteepestDescent

def test_steepest_descent():

    # Get initial values 
    x1_initial = float(input("x1: "))
    x2_initial = float(input("x2: "))
    x3_initial = float(input("x3: "))
    
    # Get algorithm parameters
    error_tolerance = float(input("Error tolerance: "))
    step_size = float(input("Step size: "))
    max_iteration = int(input("Maximum iterations: "))
    

    optimizer = SteepestDescent(x1_initial, x2_initial, x3_initial)
    

    optimizer.optimize(error_tolerance, step_size, max_iteration)
    
    print("\nTest completed!")
    print(f"Initial values: x1={x1_initial}, x2={x2_initial}, x3={x3_initial}")
    print(f"Final values: x1={optimizer.x1:.6f}, x2={optimizer.x2:.6f}, x3={optimizer.x3:.6f}")
    print(f"Function value: {optimizer.objective_function_value:.6f}")
    print(f"Number of iterations: {optimizer.iteration}")

if __name__ == "__main__":
    test_steepest_descent()