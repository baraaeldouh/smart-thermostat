class SmartThermostat:
    def __init__(self, room_name, current_temp):
        self.room_name = room_name
        self.current_temp = current_temp
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"--- {self.room_name} thermostat is now ON ---")

    def turn_off(self):
        self.is_on = False
        print(f"--- {self.room_name} thermostat is now OFF ---")

    def set_temperature(self, target_temp):
        if self.is_on:
            self.current_temp = target_temp
            print(f"Temperature in {self.room_name} updated to {target_temp}°C.")
        else:
            print("Action Denied: Turn on the thermostat first.")

    def status(self):
        if self.is_on:
            state = "ON"
        else:
            state = "OFF"

        print(f"{self.room_name} | Status: {state} | Current Temp: {self.current_temp}°C")


        
thermostat = SmartThermostat("Living Room", 22.5)

thermostat.status()
thermostat.turn_on()
thermostat.set_temperature
        

        
    