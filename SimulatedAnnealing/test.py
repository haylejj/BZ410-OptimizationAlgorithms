from simulated_annealing import  SimulatedAnnealing

def test_simulated_annealing():

    # Get initial values 
    x1_initial = float(input("x1: "))
    x2_initial = float(input("x2: "))
    lb_initial = float(input("lb: "))
    ub_initial = float(input("ub: "))
    # Get algorithm parameters
    initial_temp = float(input("Initial Temporary: "))
    step_size = float(input("Step size: "))
    max_iteration = int(input("Maximum iterations: "))
    cooling_rate=float(input("Cooling Rate: "))
    

    optimizer = SimulatedAnnealing(x1_initial, x2_initial,lb_initial,ub_initial)
    

    optimizer.optimize(initial_temp,cooling_rate,max_iteration,step_size)
    
    print("\nTest completed!")
    print(f"Initial values: x1={x1_initial}, x2={x2_initial}, lb={lb_initial}, ub={ub_initial}")
    print(f"Final values: x1={optimizer.best_x1:.6f}, x2={optimizer.best_x2:.6f}, best value={optimizer.best_value:.6f}")
    print(f"Temperature: {optimizer.temperature:.6f}")
    print(f"Number of iterations: {optimizer.iteration}")

if __name__ == "__main__":
    test_simulated_annealing()