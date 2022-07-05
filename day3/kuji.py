import random
import time


def main():
    lotts = ["{:04d}".format(i) for i in range(10000)]

    #print(lotts)
    n=int(input("宝くじを何枚買いますか>"))
    my_lotts=sorted(random.sample(lotts,n))
    print(my_lotts)
    lucky="{:04d}".format(random.randrange(10000))
    for l in lucky:
        time.sleep(1)
        print(l)
    result=[[]for i in range(4)]
    for lott in my_lotts:
        if lucky==lott:
            result[0].append(lott)
        elif lucky[-3:]==lott[-3:]:
            result[1].append(lott)
        elif lucky[-2:]==lott[-2:]:
            result[2].append(lott)
        elif lucky[-1]==lott[-1]:
            result[3].append(lott)
    for i in range(len(result)):
        print("{}等賞{:*>4s}".format(i+1,lucky[i:]),result[i])
main()
