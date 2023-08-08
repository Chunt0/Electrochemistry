import matplotlib.pyplot as plt
import argparse

def parse_data(file_path):
    """
    Parses data from a file and extracts x and y values for plotting.

    Parameters:
        file_path (str): The path to the data file.

    Returns:
        tuple: A tuple containing two lists. The first list contains the parsed x values,
               and the second list contains the parsed y values.
    """
    in_voltage_transfer_func = 5 / (10 * 1023)
    out_voltage_transfer_func = (5 * 1000) / (69.3 * 1023 * 100)
    x_values = []
    y_values = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            if len(data) == 2:
                data[0] = in_voltage_transfer_func * float(data[0])
                data[1] = out_voltage_transfer_func * float(data[1])
                x_values.append(data[0])
                y_values.append(data[1])
        x_values = [sum(x_values[i:i + 5]) / 5 for i in range(0, len(x_values), 5)]
        y_values = [sum(y_values[i:i + 5]) / 5 for i in range(0, len(y_values), 5)]
    return x_values, y_values

# Add command-line argument parsing
parser = argparse.ArgumentParser(description='Plot data from a file.')
parser.add_argument('data_file', type=str, help='Path to the data file.')
parser.add_argument('scan_rate', type=int, help='Scan Rate of CV')
args = parser.parse_args()

# Use the data file path provided as a command-line argument
data_file = args.data_file
scan_rate = args.scan_rate
x, y = parse_data(data_file)

# Save the new data to a file named "new_data.txt"
with open(f'FECN_{scan_rate}mVs_5cycles_data.txt', 'w') as file:
    for i in range(len(x)):
        file.write(f"{x[i]}\t{y[i]}\n")

# Plot the graph and save it to "graph.png"
plt.plot(x, y)
plt.xlabel('Electric Potential | v')
plt.ylabel('Current | mA')
plt.title(f'Current vs. Electric Potential | Scan Rate: {scan_rate} mV/s')
plt.grid(True)
plt.savefig(f'FECN_{scan_rate}mVs_5cycles.png')
