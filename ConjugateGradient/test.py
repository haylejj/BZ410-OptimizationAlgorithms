from conjugate_gradient import ConjugateGradient

def test_conjugate_gradient():
    # Get initial values 
    x1_initial = float(input("x1: "))
    x2_initial = float(input("x2: "))
    x3_initial = float(input("x3: "))
        
    # Get algorithm parameters
    error_tolerance = float(input("Error tolerance: "))
    step_size = float(input("Step size: "))
    max_iteration = int(input("Maximum iterations: "))
    
    cg = ConjugateGradient(x1_initial, x2_initial, x3_initial)
    
    cg.optimize(error_tolerance, step_size, max_iteration)

    print("\nTest completed!")
    print(f"Initial values: x1={x1_initial}, x2={x2_initial}, x3={x3_initial}")
    print(f"Final values: x1={cg.x1:.6f}, x2={cg.x2:.6f}, x3={cg.x3:.6f}")
    print(f"Function value: {cg.objective_function_value:.6f}")
    print(f"Number of iterations: {cg.iteration}")

if __name__ == "__main__":
    test_conjugate_gradient()