def create_archive(filename: str) -> None:
    try:
        print(f"Initializing new storage unit: {filename}")
        file = open(filename, "w")
        print("Storage unit created successfully...\n")
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee")
    except FileNotFoundError as e:
        print(f"Error FileNotFoundError: {e}")
    finally:
        file.close()
    try:
        file = open(filename, "r")
        print("Inscribing preservation data...")
        content = file.read()
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    filename = "ancient_fragment.txt"
    create_archive(filename)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
