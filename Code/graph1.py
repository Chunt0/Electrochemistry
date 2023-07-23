import matplotlib.pyplot as plt

def read_data(file_path):
    x_values = []
    y_values = []
    line_counter = 0  # Initialize the line counter

    with open(file_path, 'r') as file:
        for line in file:
            line_counter += 1  # Increment the line counter with each line read
            if line_counter % 4 == 0:  # Use the modulus operator to check if it's the 4th line
                data = line.strip().split('\t')
                if len(data) == 2:
                    data[0] = (.5/1023)*float(data[0])
                    data[1] = ((4/1023)*float(data[1]) - 2)/12500*10**6
                    x_values.append(data[0])
                    y_values.append(data[1])

    return x_values, y_values

data_file = 'data1.txt'  # Update with your file path
x, y = read_data(data_file)

plt.scatter(x, y)
plt.xlabel('V_in')
plt.ylabel('I_out')
plt.title('Data Plot')
plt.grid(True)
plt.show()
