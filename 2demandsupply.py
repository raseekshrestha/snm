import matplotlib.pyplot as plt

def main():
    i_values = []
    P_values = []

    Q, S, dp, sp, ds, ss, P = 0, 0, 0, 0, 0, 0, 0

    print("Enter the value of demand price (dp):")
    dp = float(input())
    print("Enter the value of demand slope (ds):")
    ds = float(input())
    print("Enter the value of supply price (sp):")
    sp = float(input())
    print("Enter the value of supply slope (ss):")
    ss = float(input())
    print("Enter the value of initial price (P):")
    P = float(input())

    for _ in range(1, 11):
        Q = dp - (ds * P)
        S = sp - (ss * P)
        P += 1

        i_values.append(_)
        P_values.append(P)

        if Q == S:
            print("Equilibrium Price is =", P)

    # Plotting
    plt.plot(i_values, P_values, label='Equilibrium Price')
    plt.xlabel('Iteration')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
