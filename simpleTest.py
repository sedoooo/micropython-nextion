from machine import Pin, UART
import time
from nextion.nextion_hardware import NexHardware
from nextion.nextion_text import NexText
from nextion.nextion_slider import NexSlider
from nextion import ulogging as logging

# LED setup
led = Pin("E1", Pin.OUT)  # Confirm PE1 is valid for your Nucleo board

# Create a logger instance
logger = logging.getLogger("NextionLogger")
logger.setLevel(logging.DEBUG)

# Create an instance of NexHardware with a specific UART ID
# UART5_TX = B6 , UART5_RX = B12
nex = NexHardware(
    uart_id=5,  # Set the UART ID to 5 (or any other valid UART ID for your setup)
    baudrate=9600,
    logger=logger,
    timeout=100)

# Initialize the Nextion display
if nex.nexInit():
    print("Nextion display initialized successfully")
else:
    print("Failed to initialize Nextion display")
 
print("Init Finished")


# Create an instance of NexText
page_id = 0  # Page ID
text_component_id = 4  # Text component ID
text_component_name = "t0"  # Text component name
nex_text = NexText(nex, page_id, text_component_id, text_component_name)

# Set the text of the text field
nex_text.setText("Hello, Nextion!")

# Create an instance of NexSlider
slider_id = 5  # Slider ID
slider_name = "h1"  # Slider name
nex_slider = NexSlider(nex, page_id, slider_id, slider_name)

current_value = nex_slider.getValue()
print(f"Current slider value: {current_value}")

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
    current_value = nex_slider.getValue()
    print(f"Current slider value: {current_value}")

