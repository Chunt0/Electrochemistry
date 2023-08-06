# Christopher Hunt
# serial_2_txt.py
import serial
import sys

# Serial port configuration
serial_port = '/dev/ttyACM0'  # Replace with the appropriate serial port
baud_rate = 9600

# File path for saving data
file_path = 'data.txt'

# Open the serial port
ser = serial.Serial(serial_port, baud_rate)

# Open the file in append mode
with open(file_path, 'a') as file:
    try:
        # Read data from the serial port and write it to the file
        while True:
            if ser.in_waiting > 0:
                data = ser.readline().decode().strip()
                file.write(data + '\n')
                file.flush()  # Flush the buffer to ensure immediate writing

    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("Keyboard interrupt detected. Exiting...")
        ser.close()  # Close the serial port
        sys.exit(0)
