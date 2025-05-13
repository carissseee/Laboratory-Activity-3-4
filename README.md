# OOPerate This:  A Computer Device Simulator

## Laboratory-Activity-3 & 4

# Group Members
| Name | GitHub Username |
|------|-----------------|
| Jared Aningalan | [JaredAningalan](https://github.com/dp) |
| Kishean Auditor | [carissseee](https://github.com/dp) |
| Dave Paunil | [dp30-sub](https://github.com/dp)|
| Jiselle Marasigan | [ellemrsgn27’s](https://github.com/dp) |

## Short Description of the System
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
### ```Mouse```

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

### ```Keyboard```
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



## How to Run The Program
This software is a computer device simulator that uses object-oriented programming (OOP) to illustrate different computer hardware components and how they work. The user can select from six different computer devices on the main menu that appears when the software has finished running: the mouse, keyboard, monitor, speaker, system unit, and camera. If the user wants to stop, they can also choose to terminate the program. The application will instantly show all of the device's details after you select one from the menu. The brand, material, color, price, and other technical characteristics particular to the item are all included in these specifications. The application will also show all of the functioning methods related to that specific device in accordance with the standards. These techniques reflect common tasks that the device can carry out, like clicking, scrolling, taking pictures, recording audio, typing, altering the brightness, or processing data. The output will provide users a sense of how each piece of hardware works by simulating these functionalities in a descriptive way.

Additionally, the user may access the device's features and functions without having to navigate through further menus after choosing one. For simplicity, all data and technique outputs are displayed at once. When finished, the application will return to the main menu, enabling the user to either exit the program or choose another device. This simulation's main goal is to assist users with comprehending Python's class inheritance, abstraction, and polymorphism while also offering a simple and engaging method of visualizing how various computer devices function. It acts as a hands-on practice for creating menu-driven apps and using object-oriented concepts with actual objects.

