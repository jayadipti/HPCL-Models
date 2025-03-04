import time
import random

class HydrogenDispenser:
    def _init_(self, max_pressure_bar, cooling_temp_c):
        self.max_pressure_bar = max_pressure_bar  
        self.cooling_temp_c = cooling_temp_c  
        self.current_pressure_bar = 0
        self.flow_rate_kg_per_min = 1.0  
        self.dispensed_hydrogen_kg = 0

    def start_dispensing(self, target_hydrogen_kg):
        print("Starting hydrogen dispensing...")
        while self.dispensed_hydrogen_kg < target_hydrogen_kg:
            if self.current_pressure_bar < self.max_pressure_bar:
                self.current_pressure_bar += random.uniform(5, 10)  
                self.current_pressure_bar = min(self.current_pressure_bar, self.max_pressure_bar)
            self.dispensed_hydrogen_kg += self.flow_rate_kg_per_min
            self._cool_down()
            print(f"Dispensed: {self.dispensed_hydrogen_kg:.2f} Kg, Pressure: {self.current_pressure_bar:.2f} bar")
            time.sleep(1)  
        print("Dispensing complete.")

    def _cool_down(self):
        print(f"Cooling hydrogen to {self.cooling_temp_c} °C...")


if __name__ == "__main__":

    dispenser = HydrogenDispenser(max_pressure_bar=700, cooling_temp_c=-40)  
    target_hydrogen_kg = 5  
    dispenser.start_dispensing(target_hydrogen_kg)
