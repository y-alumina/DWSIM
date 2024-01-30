class ControlValve:
    def __init__(self):
        self.is_open = False

    def open_valve(self):
        if not self.is_open:
            print("Opening the valve")
            self.is_open = True
        else:
            print("Valve is already open")

    def close_valve(self):
        if self.is_open:
            print("Closing the valve")
            self.is_open = False
        else:
            print("Valve is already closed")

def main():
    valve_controler = ControlValve()

    try:
        while True:
            print("\nSelect an action:")
            print("1. Open Valve")
            print("2. Close Valve")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                valve_controler.open_valve()
            elif choice == '2':
                valve_controler.close_valve()
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again")

    except KeyboardInterrupt:
        print("Program stopped by the user.")

if __name__ == "__main__":
    main()
