"""The following code is a simulation of controlling a valve that opens and closes periodically with a certain time. 
The program runs in an infinite loop until the user stops it."""

import time
start_time = time.time()

class ControlValve:
    def __init__(self):
        self.is_open = False

    def open_valve(self):
        if not self.is_open:
            current_time = time.time() - start_time
            print("Opening the valve -", current_time)
            self.is_open = True
        else:
            print("Valve si already opened.")

    def close_valve(self):
        if self.is_open:
            curent_time = time.time() - start_time
            print("Closing the Valve -", current_time)
            self.is_open = False
        else:
            print("Valve is already closed.")

def main():
    valve_controller = ControlValve()

    try:
        while True:
            valve_controller.open_valve()
            time.sleep(10)  # open valve for 10 seconds
            valve_controller.close_valve()
            time.sleep(5)  # close valve for 5 seconds

    except KeyboardInterrupt:
        print("The program is stopped by the user.")

if __name__ == "__main__":
    main()
