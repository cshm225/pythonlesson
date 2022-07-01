import random


def main():
    num = random.randint(1, 100)
    max_count = 5
    print('1~100の数字の中から一つ選んだよ。')
    print('その数字を', max_count, '回以内に当ててね。')
    for i in range(1, max_count+1):
        print(i,"回目")
        ans = int(input())
        if ans == num:
            print("seikai")
            break
        if i != max_count:
            if ans <= num:
                print("mottodekai")
            if ans >= num:
                print("mottotisai")
    else:
        print("seikai",num)


main()
