import pprint


def main():

    data = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(data)

    W = 10
    H = 10
    data = list()
    for i in range(H):
        temp = list()
        for j in range(W):
            temp.append(0)
        data.append(temp)
    pprint.pprint(data)

    data = [1, 2, 3]+[4, 5]
    print(data)
    # [1,2,3,4,5]

    data = [1, 2, 3]*3
    print(data)
    # [1,2,3,1,2,3,1,2,3]

    # 内包表記
    data = [[0]*W for i in range(H)]
    pprint.pprint(data)

    data=[i for i in range(1,11)]
    pprint.pprint(data)

    data = [[i*W+j for j in range(H)] for i in range(H)]
    pprint.pprint(data)

    data=[[i*j for j in range(1,10)] for i in range(1,10)]
    pprint.pprint(data)


main()
