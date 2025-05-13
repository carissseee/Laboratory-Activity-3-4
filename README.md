# OOPerate This:  A Computer Device Simulator

## Laboratory Activity 3 & 4

![COMPUTER DEVICE](https://github.com/user-attachments/assets/b0dc0920-c011-4e92-bdc5-477ed2291a9f)

# Group Members
| Name | GitHub Username |
|------|-----------------|
| Jared Aningalan | [JaredAningalan](https://github.com/dp) |
| Kishean Auditor | [carissseee](https://github.com/dp) |
| Dave Paunil | [dp30-sub](https://github.com/dp)|
| Jiselle Marasigan | [ellemrsgn27’s](https://github.com/dp) |

# Description
This  Python-based console-application simulates a Computer Device Management System by using the principles   of object-oriented programming. In this program the abstract base class is  ``` ComputerDevice``` and its subclasses includes `Mouse`, `Keyboard`, `Monitor`, `Speaker`, `SystemUnit`, and `WebCam` which contains their unique attributes and behaviors. To allow users to interact with the devices, it will display a text-based menu to show its functionalities such as, viewing its specifications, performing operations like turning on/off, typing, adjusting settings and other particular methods. This project demonstrates class inheritance, abstraction, and polymorphism in a structured and practical way.

## Code Snippet
### ```ComputerDevice```
```python
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


```
🖱️ ### ```Mouse```

```python
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


mouse = Mouse(
    "Logitech",
    "Plastic",
    "Black",
    1200,
    "Wireless",
    16000,
    "Optical")
```
The `Mouse` class, a subclass of `ComputerDevice`, models the characteristics and behaviors of a computer mouse while demonstrating object-oriented principles such as inheritance, encapsulation, and method overriding. It inherits general attributes like `brand`, `material`, `color`, and `price` from the parent class, and introduces mouse-specific attributes including `connectivity` (wired or wireless), `dpi` (sensitivity), and `sensor` type (optical or laser). The class includes a __str__() method for generating a user-friendly summary of all attributes. Functional methods simulate mouse interactions: `click()` for clicking, `scroll()` for scrolling, and `move_cursor(direction)` for directional cursor movement. Additionally, the `on()` and `off()` methods simulate powering the device on and off, respectively.

⌨️ ### ```Keyboard```
```python
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


keyboard = Keyboard(
    "Logitech",
    "Plastic",
    "Black",
    3000,
    "QWERTY",
    104,
    "Mechanical")
```
The `Keyboard` class is a subclass of the abstract base class `ComputerDevice`. It includes inherited attributes from the base class like `brand`, `material`, `color`, and `price` by using `super()` method. It also has specific properties for a keyboard such as `layout`, `number_of_keys`, and `key_type`. The class methods are `type()`, `press_key()`, and `release_key()` that shows keyboard functionality, as well as power control methods `on()` and `off()` that came from base class by using @abstractmethod. This class is used to simulate a keyboard in a simple computer system.

🖥️ ### ```Monitor```
``` python

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


monitor = Monitor(
    "Dell",
    "Plastic",
    "Black",
    5000,
    27,
    "1920x1080",
    144)

```
The `Monitor` class is a subclass of the abstract base class `ComputerDevice`. It includes inherited attributes from the base class like `brand`, `material`, `color`, and `price` using `super()` method. It also introduces specific properties for a monitor such as `size`, `resolution`, and `refresh_rate`. Its methods show monitor functionalities such as `display()` for displaying content, `adjust_brightness()`, and `set_resolution()`, along with the power control methods `on()` and `off()` that came from the base class by using `@abstractmethod`. This class is used to simulate a monitor in a simple computer system.

🔊 ### ```Speaker```
```python

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


speaker = Speaker(
    "Sony",
    "Plastic",
    "Purple",
    "₱8,999.00",
    "Yes",
    "20 Hz - 20,000 Hz",
    "24 Watts")

```
Another subclass from `ComputerDevice`  is `Speaker` which inherits attributes from the parent `CompuerDevice` such as `brand`, `material`, `color`, and `price` by using `super()`mehod. Its own attributes includes `dual`, `frequency`, and `power_output`. All of its attributes are set by using the `def __init__` method while displayed as a string using def `__str__(self)`. The def `on()` and `def off()` method came from the parent class ComputerDevice by using `@abstractmethod`  which will have a different implementation for this device. The remaining methods such as `play_sound`, `adjust_volume`, and `mute()`  will return strings and statements about the device.

⚙️ ### ```SystemUnit```
```python


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


system_unit = SystemUnit(
    "AMD Ryzen 9",
    "Aluminum",
    "Black",
    "₱13,287.53",
    "3.7 GHz",
    12,
    "Zen 3")

```


```SystemUnit``` is one of the subclass of ```ComputerDevice``` that inherits attributes such as material, color, and price by using ```super() method```. Its unique attributes include clock speed, number of cores, and architecture. This are all set by using the ```def __init__``` method
while ```def __str__``` method for its display. The ```def on()``` and ```def off()``` method came from the parent class ```ComputerDevice``` by using ```@abstractmethod``` which will have a different implementation for this device. The remaining methods such as ```process_data```, ```execute_instruction```, ```manage_memory``` will return strings and statement about the device.


📸 ###  ```WebCam```

```python


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


    webcam = WebCam(
        "Logitech BRIO 300",
        "Plastic and Graphite",
        "White",
        "₱3,290.00",
        1080,
        30,
        60)

```

WebCam is another subclass which inherits its attributes by containing ComputerDevice  in its parameters. It uses the ```super()```  method to inherit the attributes from the parent class ComputerDevice within the ```def __init__``` method. Besides this, the WebCam subclass has its own attributes such as resolution, framerate, and field of view which is also included in its parameters.

To display its attributes, it will use ```def __str__(self)``` while for its other methods such as ```capture_image```, ```start_recording```, ```stop_recording```, it will use an f string and reference to its attribute such ```self.brand``` to specify the object of ```WebCam```.







# How to Run The Program
This software is a computer device simulator that uses object-oriented programming (OOP) to illustrate different computer hardware components and how they work. The user can select from six different computer devices on the main menu that appears when the software has finished running: the mouse, keyboard, monitor, speaker, system unit, and camera. If the user wants to stop, they can also choose to terminate the program. The application will instantly show all of the device's details after you select one from the menu. The brand, material, color, price, and other technical characteristics particular to the item are all included in these specifications. The application will also show all of the functioning methods related to that specific device in accordance with the standards. These techniques reflect common tasks that the device can carry out, like clicking, scrolling, taking pictures, recording audio, typing, altering the brightness, or processing data. The output will provide users a sense of how each piece of hardware works by simulating these functionalities in a descriptive way.

![image](https://github.com/user-attachments/assets/ea08d674-92e8-405c-bfa4-2090fc76745c)

Additionally, the user may access the device's features and functions without having to navigate through further menus after choosing one. For simplicity, all data and technique outputs are displayed at once. When finished, the application will return to the main menu, enabling the user to either exit the program or choose another device. This simulation's main goal is to assist users with comprehending Python's class inheritance, abstraction, and polymorphism while also offering a simple and engaging method of visualizing how various computer devices function. It acts as a hands-on practice for creating menu-driven apps and using object-oriented concepts with actual objects.

![image](https://github.com/user-attachments/assets/d59d1916-8399-4054-8408-678560046831)

# 🙏 Acknowledgment

<p align="justify">
  &nbsp; We would like to express our heartfelt gratitude for our teacher <b>Ms. Fatima Marie Agdon</b> sincere
  support and encouragement for this project. Your dedication to teach us and your thoughtful guidance helped
  us to think critically and improve at every stage. We are truly grateful for the time and effort you devoted
  to helping us grow. We are incredibly grateful for all the time and effort you've given us. This project
  would not have been possible without your unwavering support.
</p>

<br />

*Sincerely,* <br />
**Team 7**

