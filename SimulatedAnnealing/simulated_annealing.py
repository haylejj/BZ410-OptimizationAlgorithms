import math
import random

class SimulatedAnnealing:
    def __init__(self, x1, x2,lb,ub):
        self.lb = lb 
        self.ub = ub  
        self.x1 = max(lb, min(ub, x1))
        self.x2 = max(lb, min(ub, x2))
        self.best_x1 = x1
        self.best_x2 = x2
        self.current_value = 0
        self.best_value = 0
        self.iteration = 0
        self.temperature = 0
        self.update_function_value()
    
    def objective_function(self, x1, x2):
        """f(x1, x2) = x1^2 + x2^2"""
        return x1 ** 2 + x2 ** 2
            
    def update_function_value(self):
        """Mevcut çözümün fonksiyon değerini günceller"""
        self.current_value = self.objective_function(self.x1, self.x2)
        
        # En iyi değeri güncelle
        if self.iteration == 0 or self.current_value < self.best_value:
            self.best_value = self.current_value
            self.best_x1 = self.x1
            self.best_x2 = self.x2
    
    def generate_neighbor(self, step_size):
        """
        Hocanın formülüne göre komşu çözüm üretme:
        k = x + r(-1,1) * (ub-lb) * step_size
        
        Args:
            step_size: Adım boyutu (0-1 arası)
            
        Returns:
            Komşu çözüm ve fonksiyon değeri
        """
        r1=random.uniform(-1,1)
        r2=random.uniform(-1,1)

        neighbor_x1=self.x1 + r1 * (self.ub-self.lb) * step_size
        neighbor_x2=self.x2 + r2 * (self.ub-self.lb) * step_size

        # Sınırlar içinde kalmasını sağla
        neighbor_x1 = max(self.lb, min(self.ub, neighbor_x1))
        neighbor_x2 = max(self.lb, min(self.ub, neighbor_x2))
        # Komşu çözümün fonksiyon değerini hesapla
        neighbor_value = self.objective_function(neighbor_x1, neighbor_x2)
        
        return neighbor_x1, neighbor_x2, neighbor_value
    
    def calculate_acceptance_probability(self, current_value, neighbor_value, temperature):

        # Eğer komşu daha iyiyse, kesinlikle kabul et
        if neighbor_value <= current_value:
            return 1.0
        
        # Değilse, sıcaklığa bağlı olarak olasılık hesapla
        delta = neighbor_value - current_value
        return math.exp(-delta / temperature)
    
    def optimize(self, initial_temp, cooling_rate,max_iteration, step_size):
        """
        Args:
            initial_temp: Başlangıç sıcaklığı (Ts)
            cooling_rate: Soğutma katsayısı (α, 0-1 arası)
            max_iteration: Maksimum iterasyon sayısı (MaxIter)
            step_size: Adım boyutu (0-1 arası)
        """
  
        self.temperature=initial_temp
        self.iteration=0

        while self.iteration < max_iteration:

            neighbor_x1, neighbor_x2, neighbor_value= self.generate_neighbor(step_size)

            acceptance_probability = self.calculate_acceptance_probability(self.current_value, neighbor_value, self.temperature)
            
            random_value=random.random()

            if acceptance_probability > random_value:
                self.x1=neighbor_x1
                self.x2=neighbor_x2
                self.current_value=neighbor_value

                if self.current_value < self.best_value:
                    self.best_value = self.current_value
                    self.best_x1 = self.x1
                    self.best_x2 = self.x2

            self.temperature*=cooling_rate
            self.iteration+=1
        
        return (self.best_x1,self.best_x2),self.best_value
