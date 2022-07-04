def main():
    scores = (70, 80, 55)
    print(scores)
    print(scores[0])
    print(len(scores), sum(scores))

    members = ("松田",)  # タプルで要素数1

    # セット

    nums = {10, 20, 30, 40}
    nums.add(50)
    nums.add(40)
    print(nums)


main()
