import time
import random

class HydrogenDispenser:
    def _init_(self, max_pressure_bar, cooling_temp_c):
        self.max_pressure_bar = max_pressure_bar  # Maximum dispensing pressure
        self.cooling_temp_c = cooling_temp_c  # Cooling temperature
        self.current_pressure_bar = 0
        self.flow_rate_kg_per_min = 1.0  # Flow rate in Kg/min
        self.dispensed_hydrogen_kg = 0

    def start_dispensing(self, target_hydrogen_kg):
        print("Starting hydrogen dispensing...")
        while self.dispensed_hydrogen_kg < target_hydrogen_kg:
            if self.current_pressure_bar < self.max_pressure_bar:
                self.current_pressure_bar += random.uniform(5, 10)  # Simulate pressure increase
                self.current_pressure_bar = min(self.current_pressure_bar, self.max_pressure_bar)
            self.dispensed_hydrogen_kg += self.flow_rate_kg_per_min
            self._cool_down()
            print(f"Dispensed: {self.dispensed_hydrogen_kg:.2f} Kg, Pressure: {self.current_pressure_bar:.2f} bar")
            time.sleep(1)  # Simulate real-time dispensing
        print("Dispensing complete.")

    def _cool_down(self):
        print(f"Cooling hydrogen to {self.cooling_temp_c} °C...")

# Example Usage
if __name__ == "__main__":

    dispenser = HydrogenDispenser(max_pressure_bar=700, cooling_temp_c=-40)  # 700 bar, -40°C cooling
    target_hydrogen_kg = 5  # Target amount of hydrogen to dispense
    dispenser.start_dispensing(target_hydrogen_kg)