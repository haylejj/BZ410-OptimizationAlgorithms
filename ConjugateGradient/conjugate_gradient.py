from math import sqrt
class ConjugateGradient:
    def __init__(self, x1, x2, x3):
       self.x1 = x1
       self.x2 = x2
       self.x3 = x3
       self.objective_function_value = 0
       self.der_x1 = 0
       self.der_x2 = 0
       self.der_x3 = 0
       self.iteration = 0
       self.directions=list()
       self.euclidean_norms=list()
       self.update_function_and_derivatives()
    
    def update_function_and_derivatives(self):
       """Updates the objective function value and  derivatives"""
       self.objective_function_value = (self.x1 * self.x1 + 2 * self.x2 * self.x2 + 2 * self.x3 * self.x3 + 2 * self.x1 * self.x2 + 2 * self.x2 * self.x3)
       
       # Partial derivatives (kısmi türevleri güncelleme)
       self.der_x1 = 2 * self.x1 + 2 * self.x2
       self.der_x2 = 4 * self.x2 + 2 * self.x1 + 2 * self.x3
       self.der_x3 = 4 * self.x3 + 2 * self.x2
    
    def calculate_euclidean_norm(self):
       return sqrt(self.der_x1**2 + self.der_x2**2 + self.der_x3**2)
    
    def optimize(self, error_tolerance, step_size, max_iteration):
        """
        Parameters:
        error_tolerance (float): Tolerance value (ε)
        step_size (float): (α)
        max_iteration (int)
        """
        while self.iteration < max_iteration:
            print(f"Iteration: {self.iteration}, values: x1 = {self.x1:.6f}, x2 = {self.x2:.6f}, "
                  f"x3 = {self.x3:.6f}, func = {self.objective_function_value:.6f}")
            
            euclidean_norm = self.calculate_euclidean_norm()
            self.euclidean_norms.append(euclidean_norm)

            if euclidean_norm <= error_tolerance:
                print("======== Optimization Completed ========")
                print(f"Converged in {self.iteration} iterations.")
                print(f"x1={self.x1:.6f}, x2={self.x2:.6f}, x3={self.x3:.6f}, f={self.objective_function_value:.6f}")
                return
            
            if self.iteration == 0:
                # first iteration , should be negative direction
                direction_x1 = -self.der_x1
                direction_x2 = -self.der_x2
                direction_x3 = -self.der_x3
            else:
                # Fletcher-Reeves with β calculate
                previous_euclidean_norm = self.euclidean_norms[self.iteration - 1] # get last euclidean of iteration
                fletcher_reeves = (euclidean_norm * euclidean_norm) / (previous_euclidean_norm * previous_euclidean_norm)
                
                prev_dir = self.directions[self.iteration - 1]
                direction_x1 = -self.der_x1 + fletcher_reeves * prev_dir[0]
                direction_x2 = -self.der_x2 + fletcher_reeves * prev_dir[1]
                direction_x3 = -self.der_x3 + fletcher_reeves * prev_dir[2]
            
            self.directions.append((direction_x1,direction_x2,direction_x3))

            self.x1 = self.x1 + step_size * direction_x1
            self.x2 = self.x2 + step_size * direction_x2
            self.x3 = self.x3 + step_size * direction_x3
            
            self.iteration += 1
            
            self.update_function_and_derivatives()
            