def main():
    name = input("What's your name? ")
    if name.strip():
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

if __name__ == "__main__":
    main()