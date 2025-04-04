from SteepestDescent.steepest_descent import SteepestDescent
from ConjugateGradient.conjugate_gradient import ConjugateGradient

def comparasion_conjugateGradient_steepestDescent():
     # Get initial values 
    x1_initial = float(input("x1: "))
    x2_initial = float(input("x2: "))
    x3_initial = float(input("x3: "))
    
    # Get algorithm parameters
    error_tolerance = float(input("Error tolerance: "))
    step_size = float(input("Step size: "))
    max_iteration = int(input("Maximum iterations: "))

    steepest_descent=SteepestDescent(x1_initial,x2_initial,x3_initial)
    conjugate_gradient=ConjugateGradient(x1_initial,x2_initial,x3_initial)

    steepest_descent.optimize(error_tolerance,step_size,max_iteration)
    conjugate_gradient.optimize(error_tolerance,step_size,max_iteration)

    print("\nSteepest Descent:")
    print("Iterations needed: {}".format(steepest_descent.iteration))
    
    print("\nConjugate Gradient:")
    print("Iterations needed: {}".format(conjugate_gradient.iteration))



if __name__ == "__main__":
    comparasion_conjugateGradient_steepestDescent()