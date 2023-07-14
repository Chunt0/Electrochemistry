import matplotlib.pyplot as plt


def read_data(filename):
    x = []
    y = []
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            count += 1
            val = int(line.strip())
            x.append(count)
            y.append(val)

    return x, y

PATH = 'data.txt'

x, y = read_data(PATH)

plt.scatter(x,y)
plt.xlabel('Time [t] (s)')
plt.ylabel('Voltage [V] (v)')
plt.title('Voltage vs. Time')
plt.show()

