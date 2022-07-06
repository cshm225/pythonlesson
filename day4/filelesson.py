from cgitb import text


text = input("kiroku>")
file = open("ted.txt", "a")
file.write(text+"\n")
file.close()

text = input("tuiki")
with open("ted.txt","a") as file:
    file.write(text+"\n")
