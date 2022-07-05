import pprint as p


def main():
    # q1
    data = [[100-i-j for j in range(10)]for i in range(10)]
    p.pprint(data)

    # q2
    data = [[1 if i == j or i+j ==
             4 else 0 for j in range(5)]for i in range(5)]
    p.pprint(data)

    # q3
    data = [[i*10-(j*10) for j in range(10)]for i in range(10)]
    p.pprint(data)

    # q4
    data = [[1 if i == j else 2 if j <
             i else 0 for j in range(5)] for i in range(5)]
    p.pprint(data)

    # q5
    data = [[i+1 if i == j else 0 for j in range(4)]for i in range(4)]
    p.pprint(data)

    # q6
    data = [[60+i+j for j in range(9)]for i in range(0, 40, 10)]
    p.pprint(data)

    # q7
    data = [[(i+1)*(j+1) for j in range(9)]for i in range(9)]
    p.pprint(data)

    # q8
    data = [[3 if i == 1 and j == 1 else 7 for j in range(3)]for i in range(3)]
    p.pprint(data)

    # q9
    data = [[(i+1)*(j+1) for j in range(9)]for i in range(2, 9, 2)]
    p.pprint(data)

    # q10
    data = [[i*(j+1) if i == 2 else i*(j+1)+j for j in range(5)]
            for i in range(2, 0, -1)]
    p.pprint(data)

    # q11
    data = [["*" if i % 2 == 0 and j %
             2 != 0 else "_" for j in range(9)]for i in range(9)]
    p.pprint(data)

    # q12
    data = [[i**2+j for j in range(10)]for i in range(10)]
    p.pprint(data)

    # q13
    data = [[i-j for j in range(i)]for i in range(10, 0, -1)]
    p.pprint(data)


main()
