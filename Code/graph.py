import matplotlib.pyplot as plt

def read_data(file_path):
    x_values = []
    y_values = []

    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            if len(data) == 2:
                data[0] = (2/1023)*float(data[0]) - 1
                data[1] = ((4/1023)*float(data[1]) - 2)/12500*10**6
                x_values.append(data[0])
                y_values.append(data[1])

    return x_values, y_values

data_file = 'data.txt'  # Update with your file path
x, y = read_data(data_file)

plt.plot(x, y, 'o')
plt.xlabel('V_in')
plt.ylabel('I_out')
plt.title('Data Plot')
plt.grid(True)
plt.show()