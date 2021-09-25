class Drone:
    def __init__(self, nickname, model, battery_percentage):
        self.nickname = nickname
        self.model = model
        self.battery_percentage = battery_percentage

    def show_stats(self):
        print(f"Hello Officer Randy, my battery is currently at {self.battery_percentage}")

    def hover_above_home(self):
        print("hovering above home base")

    def hover_above_mobile(self):
        print("hovering above mobile officer")

    def move_to_vehicle_in_question(self):
        print("moving to vehicle")

    def return_to_officer_vehicle(self):
        print("returning to officer: safe")


Drone_1 = Drone("taytay", "s1919", "100%")
print(f"Hello officer, my name is " + Drone_1.nickname + ", I am a model " + Drone_1.model + " and I have " + Drone_1.battery_percentage + " battery! LETS FUCKING GO!")

print(dir(Drone_1))

