def create_archive(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("Accessing Storage Vault: ", file.name)
    except FileNotFoundError as e:
        print(f"Error FileNotFoundError: {e}")
    try:
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    filename = "ancient_fragment.txt"
    vault_access(filename)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
