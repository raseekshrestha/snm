import matplotlib.pyplot as plt

def main():
    r1, r2, r3 = map(float, input("Input three resistances values: ").split())
    v = float(input("Input voltage: "))

    i_values = []
    i1_values = []
    i2_values = []
    i3_values = []
    eqi_values = []

    print("i\ti1\ti2\ti3")
    for _ in range(1, 11):
        i1 = v / r1
        i2 = v / r2
        i3 = v / r3
        i = i1 + i2 + i3
        r = (r1 * r2 * r3) / ((r2 * r3) + (r1 * r3) + (r1 * r2))
        eqi = v / r

        i_values.append(i)
        i1_values.append(i1)
        i2_values.append(i2)
        i3_values.append(i3)
        eqi_values.append(eqi)

        print(f"{i}\t{i1}\t{i2}\t{i3}")
        v += 1

    # Plotting
    plt.plot(range(1, 11), i_values, label='i')
    plt.plot(range(1, 11), i1_values, label='i1')
    plt.plot(range(1, 11), i2_values, label='i2')
    plt.plot(range(1, 11), i3_values, label='i3')
    plt.plot(range(1, 11), eqi_values, label='eqi')

    plt.xlabel('Iteration')
    plt.ylabel('Current Values')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
