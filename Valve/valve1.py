'''The following code is a simulation of controlling a valve that opens and closes periodically with a certain time. 
The program runs in an infinite loop until the user stops it.'''

import time
start_time = time.time()

class ControlValve:
    def __init__(self):
        self.is_open = False

    def open_valve(self):
        if not self.is_open:
            curent_time = time.time() - start_time
            print("Open the valve -", curent_time)
            self.is_open = True
        else:
            print("Valve opened")

    def close_valve(self):
        if self.is_open:
            curent_time = time.time() - start_time
            print("Close the Valve -", curent_time)
            self.is_open = False
        else:
            print("Valve closed")

def main():
    valve_controler = ControlValve()

    try:
        while True:
            valve_controler.open_valve()
            time.sleep(5)  # Katup terbuka selama 5 detik
            valve_controler.close_valve()
            time.sleep(10)  # Katup tertutup selama 10 detik

    except KeyboardInterrupt:
        print("Program dihentikan oleh user.")

if __name__ == "__main__":
    main()
