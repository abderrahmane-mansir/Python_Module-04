def crisis_management(filename: str) -> None:
    print(f"CRISIS ALERT: Attempting to access to '{filename}'...")
    try:
        with open(filename) as file:
            content = file.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, system maintained\n")
    else:
        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed\n")
    print(content + "\n")


def main() -> None:
    print("=== CRISIS RESPONSE PROTOCOLS ===\n")
    crisis_management("lost_archive.txt")
    crisis_management("classified_vault.txt")
    crisis_management("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
