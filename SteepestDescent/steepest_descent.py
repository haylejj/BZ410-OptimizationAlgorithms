import math
class SteepestDescent:
   def __init__(self, x1, x2, x3):
       self.x1 = x1
       self.x2 = x2
       self.x3 = x3
       self.objective_function_value = 0
       self.der_x1 = 0
       self.der_x2 = 0
       self.der_x3 = 0
       self.iteration = 0
       self.update_function_and_derivatives()
   
   def update_function_and_derivatives(self):
       """Updates the objective function value and  derivatives"""
       self.objective_function_value = (self.x1 * self.x1 + 2 * self.x2 * self.x2 + 2 * self.x3 * self.x3 + 2 * self.x1 * self.x2 + 2 * self.x2 * self.x3)
       
       # Partial derivatives (kısmi türevleri güncelleme)
       self.der_x1 = 2 * self.x1 + 2 * self.x2
       self.der_x2 = 4 * self.x2 + 2 * self.x1 + 2 * self.x3
       self.der_x3 = 4 * self.x3 + 2 * self.x2
   
   def calculate_euclidean_norm(self):
       return math.sqrt(self.der_x1**2 + self.der_x2**2 + self.der_x3**2)
   
   def optimize(self, error_tolerance, step_size, max_iteration):
       """
       Applies the Steepest Descent optimization algorithm.
       
       Args:
           error_tolerance: Tolerance value for the gradient magnitude
           step_size: Step size for each iteration
           max_iteration: Maximum number of iterations
       """
       while self.iteration < max_iteration:
           print(f"Iteration: {self.iteration}, values: x1 = {self.x1:.6f}, x2 = {self.x2:.6f}, x3 = {self.x3:.6f}, func = {self.objective_function_value:.6f}")

           euclidean_norm = self.calculate_euclidean_norm()    
           if euclidean_norm <= error_tolerance:
               print("======== Optimization Completed ========")
               print(f"Converged in {self.iteration} iterations.")
               print(f"x1={self.x1:.6f}, x2={self.x2:.6f}, x3={self.x3:.6f}, f={self.objective_function_value:.6f}")
               return
           
           # direction must be negative because we want to minimize the function
           direction_x1 = -self.der_x1
           direction_x2 = -self.der_x2
           direction_x3 = -self.der_x3

           self.x1 = self.x1 + step_size * direction_x1
           self.x2 = self.x2 + step_size * direction_x2
           self.x3 = self.x3 + step_size * direction_x3
               
           self.iteration += 1
           self.update_function_and_derivatives()