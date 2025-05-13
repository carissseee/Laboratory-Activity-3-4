from abc import ABC, abstractmethod

class ComputerDevice(ABC):
    def __init__(self, brand, material, color, price):
        self.brand = brand
        self.material = material
        self.color = color
        self.price = price

    @abstractmethod
    def on(self): pass

    @abstractmethod
    def off(self): pass


class WebCam(ComputerDevice):
    def __init__(self, brand, material, color, price, resolution, framerate, field_of_view):
        super().__init__(brand, material, color, price)
        self.resolution = resolution
        self.framerate = framerate
        self.field_of_view = field_of_view

    def __str__(self):
        return (
            f"Brand: {self.brand}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Price: PHP {self.price}\n"
            f"Resolution: {self.resolution}\n"
            f"Framerate: {self.framerate}fps\n"
            f"Field of View: {self.field_of_view} degrees"
        )

    def capture_image(self):
        return "Image is being captured..."      
    def start_recording(self):
        return f"{self.brand} is currently recording..."
    def stop_recording(self):
        return f"{self.brand} has stopped recording..."
    def on(self):
        return f"Turning on {self.brand}"
    def off(self):
        return f"Turning off {self.brand}"


webcam = WebCam("Logitech BRIO 300", "Plastic and Graphite", "White", "₱3,290.00", 1080, 30, 60)

class Mouse(ComputerDevice):
    def __init__(self, brand, material, color, price, connectivity, dpi, sensor):
        super().__init__(brand, material, color, price)
        self.connectivity = connectivity
        self.dpi = dpi
        self.sensor = sensor

    def __str__(self):
        return (
            f"Brand: {self.brand}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Price: PHP {self.price}\n"
            f"Connectivity: {self.connectivity}\n"
            f"DPI: {self.dpi}\n"
            f"Sensor: {self.sensor}"
        )

    def click(self):
        return f"{self.brand} mouse clicked."
    def scroll(self):
        return f"{self.brand} mouse scrolling."
    def move_cursor(self, direction):
        return f"{self.brand} mouse moving cursor {direction}."
    def on(self):
        return f"Turning on {self.brand} mouse"
    def off(self):
        return f"Turning off {self.brand} mouse"


mouse = Mouse("Logitech", "Plastic", "Black", 1200, "Wireless", 16000, "Optical")


class Keyboard(ComputerDevice):
    def __init__(self, brand, material, color, price, layout, number_of_keys, key_type):
        super().__init__(brand, material, color, price)
        self.layout = layout
        self.number_of_keys = number_of_keys
        self.key_type = key_type

    def __str__(self):
        return (
            f"Brand: {self.brand}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Price: PHP {self.price}\n"
            f"Layout: {self.layout}\n"
            f"Number of Keys: {self.number_of_keys}\n"
            f"Key Type: {self.key_type}"
        )

    def type(self):
        return "Typing on the keyboard..."      
    def press_key(self):
        return "Key pressed."      
    def release_key(self):
        return "Key released."      
    def on(self):
        return f"{self.brand} keyboard is ready to use."      
    def off(self):
        return f"{self.brand} keyboard is shutting down."


keyboard = Keyboard("Logitech", "Plastic", "Black", 3000, "QWERTY", 104, "Mechanical")

class Monitor(ComputerDevice):
    def __init__(self, brand, material, color, price, size, resolution, refresh_rate):
        super().__init__(brand, material, color, price)
        self.size = size
        self.resolution = resolution
        self.refresh_rate = refresh_rate

    def __str__(self):
        return (
            f"Brand: {self.brand}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Price: PHP {self.price}\n"
            f"Size: {self.size}\n"
            f"Resolution: {self.resolution}\n"
            f"Refresh Rate: {self.refresh_rate} Hz"
        )


    def display(self):
        return f"Displaying content on {self.brand} monitor."      
    def adjust_brightness(self, level):
        return f"Adjusting brightness to {level}%."      
    def set_resolution(self, resolution):
        return f"Changing resolution to {resolution}."
    def on(self):
        return f"{self.brand} monitor is powering on."
    def off(self):
        return f"{self.brand} monitor is shutting down."


monitor = Monitor("Dell", "Plastic", "Black", 5000, 27, "1920x1080", 144)

class SystemUnit(ComputerDevice):
    def __init__(self, brand, material, color, price, clock_speed, number_of_cores, architecture):
        super().__init__(brand, material, color, price)
        self.clock_speed = clock_speed
        self.number_of_cores = number_of_cores
        self.architecture = architecture

    def __str__(self):
        return (
            f"Brand: {self.brand}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Price: PHP {self.price}\n"
            f"Clock Speed: {self.clock_speed}\n"
            f"Cores: {self.number_of_cores}\n"
            f"Architecture: {self.architecture}"
        )

    def process_data(self):
        return "Processing data..."
    def execute_instruction(self):
        return "Executing instruction..."
    def manage_memory(self):
        return "Managing memory..."
    def on(self):
        return f"Turning on {self.brand} system unit"
    def off(self):
        return f"Turning off {self.brand} system unit"


system_unit = SystemUnit("AMD Ryzen 9", "Aluminum", "Black", "₱13,287.53", "3.7 GHz", 12, "Zen 3")


class Speaker(ComputerDevice):
    def __init__(self, brand, material, color, price, dual, frequency, power_output):
        super().__init__(brand, material, color, price)
        self.dual = dual
        self.frequency = frequency
        self.power_output = power_output

    def __str__(self):
        return (
            f"Brand: {self.brand}\n"
            f"Material: {self.material}\n"
            f"Color: {self.color}\n"
            f"Price: PHP {self.price}\n"
            f"Dual: {self.dual}\n"
            f"Frequency: {self.frequency}\n"
            f"Power Output: {self.power_output}"
        )

    def play_sound(self):
        return "Playing sound..."
    def adjust_volume(self):
        return "Adjusting volume..."
    def mute(self):
        return "Muted."
    def on(self):
        return f"{self.brand} speaker is on."
    def off(self):
        return f"{self.brand} speaker is off."


speaker = Speaker("Sony", "Plastic", "Purple", "₱8,999.00", "Yes", "20 Hz - 20,000 Hz", "24 Watts")

def main_menu():
    while True:
        print("\nSelect a Computer Device:")
        print("1. Mouse")
        print("2. Keyboard")
        print("3. Monitor")
        print("4. Speaker")
        print("5. System Unit")
        print("6. WebCam")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            mouse_menu(mouse)
        elif choice == "2":
            keyboard_menu(keyboard)
        elif choice == "3":
            monitor_menu(monitor)
        elif choice == "4":
            speaker_menu(speaker)
        elif choice == "5":
            system_unit_menu(system_unit)
        elif choice == "6":
            webcam_menu(webcam)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


def mouse_menu(sample_mouse):
    while True:
        print(f"\n--- {mouse.brand} Menu ---:")
        print(" 1. View Specifications")
        print(" 2. Turn On")
        print(" 3. Click")
        print(" 4. Scroll")
        print(" 5. Move Cursor")
        print(" 6. Turn Off")
        print(" 0. Back to Main Menu")
        choice = input("Enter your choice:")

        if choice == "1":
            print(mouse)
        elif choice == "2":
            print(mouse.on())
        elif choice == "3":
            print(mouse.click())
        elif choice == "4":
            print(mouse.scroll())
        elif choice == "5":
            print(mouse.move_cursor())
        elif choice == "6":
            print(mouse.off())
        elif choice == "0":
            break
        else:
            print("Invalid Input. Please try again. ")


def keyboard_menu(sample_keyboard):
    while True:
        print(f"\n--- {keyboard.brand} Menu ---:")
        print("1. View Specifications")
        print("2. Turn On")
        print("3. Type")
        print("4. Press Key")
        print("5. Release Key")
        print("6. Turn Off")
        print("0. Back to Main Menu")
        choice = input("Enter your choice:")

        if choice == "1":
            print(keyboard)
        elif choice == "2":
            print(keyboard.on())
        elif choice == "3":
            print(keyboard.type())
        elif choice == "4":
            print(keyboard.press_key())
        elif choice == "5":
            print(keyboard.release_key())
        elif choice == "6":
            print(keyboard.off())
        elif choice == "0":
            break
        else:
            print("Invalid Input. Please try again. ")


def monitor_menu(sample_monitor):
    while True:
        print(f"\n--- {monitor.brand} Menu ---:")
        print("1. View Specifications")
        print("2. Turn On")
        print("3. Display")
        print("4. Adjust Brightness")
        print("5. Set Resolution")
        print("6. Turn Off")
        print("0. Back to Main Menu")
        choice = input("Enter your choice:")

        if choice == "1":
            print(monitor)
        elif choice == "2":
            print(monitor.on())
        elif choice == "3":
            print(monitor.display())
        elif choice == "4":
            print(monitor.adjust_brightness(85))
        elif choice == "5":
            print(monitor.set_resolution( "1920x1080"))
        elif choice == "6":
            print(monitor.off())
        elif choice == "0":
            break
        else:
            print("Invalid Input. Please try again. ")


def speaker_menu(sample_speaker):
    while True:
        print(f"\n--- {speaker.brand} Menu ---:")
        print("1. View Specifications")
        print("2. Turn On")
        print("3. Play Sound")
        print("4. Adjust Volume")
        print("5. Mute")
        print("6. Turn Off")
        print("0. Back to Main Menu")
        choice = input("Enter your choice:")

        if choice == "1":
            print(speaker)
        elif choice == "2":
            print(speaker.on())
        elif choice == "3":
            print(speaker.play_sound())
        elif choice == "4":
            print(speaker.adjust_volume())
        elif choice == "5":
            print(speaker.mute())
        elif choice == "6":
            print(speaker.off())
        elif choice == "0":
            break
        else:
            print("Invalid Input. Please try again. ")


def system_unit_menu(system):
    while True:
        print(f"\n--- {system_unit.brand} Menu ---:")
        print("1. View Specifications")
        print("2. Turn On")
        print("3. Process Data")
        print("4. Execute Instruction")
        print("5. Manage Memory")
        print("6. Turn Off")
        print("0. Back to Main Menu")
        choice = input("Enter your choice:")

        if choice == "1":
            print(system_unit)
        elif choice == "2":
            print(system_unit.on())
        elif choice == "3":
            print(system_unit.process_data())
        elif choice == "4":
            print(system_unit.execute_instruction())
        elif choice == "5":
            print(system_unit.manage_memory())
        elif choice == "6":
            print(system_unit.off())
        elif choice == "0":
            break
        else:
            print("Invalid Input. Please try again. ")


def webcam_menu(sample_webcam):
    while True:
        print(f"\n--- {webcam.brand} Menu ---:")
        print("1. View Specifications")
        print("2. Turn On")
        print("3. Capture Image")
        print("4. Start Recording")
        print("5. Stop Recording")
        print("6. Turn Off")
        print("0. Back to Main Menu")
        choice = input("Enter your choice:")

        if choice == "1":
            print(webcam)
        elif choice == "2":
            print(webcam.on())
        elif choice == "3":
            print(webcam.capture_image())
        elif choice == "4":
            print(webcam.start_recording())
        elif choice == "5":
            print(webcam.stop_recording())
        elif choice == "6":
            print(webcam.off())
        elif choice == "0":
            break
        else:
            print("Invalid Input. Please try again. ")

main_menu ()
