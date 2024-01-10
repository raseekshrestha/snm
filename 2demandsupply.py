import matplotlib.pyplot as plt

def main():
    i_values = []
    P_values = []
    Q_values = []
    S_values = []

    Q, S, dp, sp, ds, ss, P = 0, 0, 0, 0, 0, 0, 0
    dp=195
    ds=1
    sp=165
    ss=-1
    P=10

    # print("Enter the value of demand price (dp):")
    # dp = float(input())
    # print("Enter the value of demand slope (ds):")
    # ds = float(input())
    # print("Enter the value of supply price (sp):")
    # sp = float(input())
    # print("Enter the value of supply slope (ss):")
    # ss = float(input())
    # print("Enter the value of initial price (P):")
    # P = float(input())

    for _ in range(1, 11):
        Q = dp - (ds * P)
        S = sp - (ss * P)
        P += 1

        i_values.append(_)
        P_values.append(P)
        Q_values.append(Q)
        S_values.append(S)

        if Q == S:
            print("Equilibrium Price is =", P)

    # Plotting
    # print(i_values,Q_values,S_values,P_values)
    plt.ylim(min(S_values)-10, max(S_values)+10)
    plt.plot(i_values, Q_values, label='Demand')
    plt.plot(i_values, S_values, label='Supply')
    plt.scatter(i_values, P_values, color='red', marker='x', label='Equilibrium Price')
    plt.xlabel('Iteration')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
