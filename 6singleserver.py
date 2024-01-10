def main():
    l = float(input("Enter Inter-arrival time of customers per hour: "))
    m = float(input("Enter the average time spent by customers per hour: "))

    p = 1 - l / m
    e = l / (m - l)
    et = 1 / (m - l)
    et = et * 60  # convert et to minutes

    print("\nThe probability that a customer won't have to wait at the counter:", p)
    print("\nExpected number of customers:", e)
    print("\nExpected time to be spent in the bank: {:.2f} minutes".format(et))

if __name__ == "__main__":
    main()
