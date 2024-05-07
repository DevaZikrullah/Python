import subprocess

def main():
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting program...")
            break

        try:
            result = subprocess.run(user_input, shell=True, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Error executing command: {e}")

if __name__ == "__main__":
    main()
