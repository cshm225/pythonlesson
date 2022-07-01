def main():
    dist = 384400000000
    thickness = 1
    count = 0
    while True:
        thickness = thickness*2
        count += 1
        print(count, "回折り曲げた")
        if thickness >= dist:
            break
    print(count)


main()
