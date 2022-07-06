from urllib import response
import requests


def main():
    response = requests.get("https://www.python.org/downloads/")
    text = response.text
    print(text)


if __name__ == "__main__":
    main()
