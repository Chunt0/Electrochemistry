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
                data[0] = (1/2046)*float(data[0])
                data[1] = (5/(660.3*1023))*float(data[1])
                x_values.append(data[0])
                y_values.append(data[1])
        x_values = [sum(x_values[i:i+10])/10 for i in range(0, len(x_values), 10)]
        y_values = [sum(y_values[i:i+10])/10 for i in range(0, len(y_values), 10)]
    return x_values, y_values

# Add command-line argument parsing
parser = argparse.ArgumentParser(description='Plot data from a file.')
parser.add_argument('data_file', type=str, help='Path to the data file.')
args = parser.parse_args()

# Use the data file path provided as a command-line argument
data_file = args.data_file
x, y = parse_data(data_file)

plt.plot(x, y)
plt.xlabel('V_in')
plt.ylabel('I_out')
plt.title('Data Plot')
plt.grid(True)
plt.show()
