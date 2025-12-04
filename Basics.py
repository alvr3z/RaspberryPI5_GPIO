import gpiod
import os
from time import sleep
from datetime import datetime

# Select chip type to manage GPIO Pins
chip = gpiod.Chip('gpiochip4')

class Device:
    global chip
    # Constructor
    def __init__(self, name, pin, state):
        self.name = name
        self.pin = pin
        self.state = state
        self.line = chip.get_line(pin) #
        self.line.request(consumer = name, type = gpiod.LINE_REQ_DIR_OUT)

    # Device ON
    def on(self):
        self.line.set_value(1) # send high voltage
        self.state = True

    # Device OFF
    def off(self):
        self.line.set_value(0)
        self.state = False
    
    def getStatus(self):
        print(f"Device: {self.name}")
        self.getStateDescription()
    
    # Show device state
    def getStateDescription(self):
        if self.state:
            print(f"{self.name} is now ON")
        else:
            print(f"{self.name} is now OFF")
            
    # Toggle Device State
    def toggle(self):
        self.state = not self.state
        self.line.set_value(self.state)
        self.getStateDescription()

class Button:
    global chip  
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.state = state
        self.line = chip.get_line(pin) #
        self.line.request(consumer = name, type = gpiod.LINE_REQ_DIR_IN)

    # Check if button is being pressed
    def isPressed(self):
        if self.line.get_value() == 1:
            return True
        else:
            return False

    # Getter & Setters
    def getPin(self):
        return self.pin
        
    def getName(self):
        return self.name

    def getState(self):
        return self.state

    # Show device state
    def getStateDescription(self):
        if self.state:
            print(f"{self.name} is now ON")
        else:
            print(f"{self.name} is now OFF")



def main():
    testDevice = Device("test", 21, False)
    
    while True:
        testDevice.on()
        testDevice.getStatus()
        sleep(1)
        testDevice.off()
        sleep(0.5)
        testDevice.getStatus()



main()
