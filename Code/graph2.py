# Christopher Hunt
# graph.py

import matplotlib.pyplot as plt
import argparse

def parse_data(file_path):
    x_values = []
    y_values = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            if len(data) == 2:
                data[0] = float(data[0])
                data[1] = float(data[1])
                x_values.append(data[0])
                y_values.append(data[1])
        x_values = [sum(x_values[i:i+5])/5 for i in range(0, len(x_values), 5)]
        y_values = [sum(y_values[i:i+5])/5 for i in range(0, len(y_values), 5)]
    return x_values, y_values

# Add command-line argument parsing
parser = argparse.ArgumentParser(description='Plot data from a file.')
parser.add_argument('data_file', type=str, help='Path to the data file.')
parser.add_argument('scan_rate', type = int, help='Scan Rate of CV')
args = parser.parse_args()

# Use the data file path provided as a command-line argument
data_file = args.data_file
scan_rate = args.scan_rate
x, y = parse_data(data_file)

plt.plot(x, y)
plt.xlabel('Electric Potential | v')
plt.ylabel('Current | mA')
plt.title(f'Current vs. Electric Potential | Scan Rate: {scan_rate} mV/s')
plt.grid(True)
plt.show()
