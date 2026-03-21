def vault_access(filename: str) -> None:
    print("Initiating secure vault access...")
    with open(filename) as file:
        content = file.read()
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")
    print("SECURE EXTRACTION:")
    print(content + "\n")


def secure_preservation(filename: str) -> None:
    print("SECURE PRESERVATION:", end="")
    content = "\n[CLASSIFIED] New security protocols archived"
    with open(filename, "a") as file:
        file.write(content)
    print(content)
    print("Vault automatically sealed upon completion")


def main() -> None:
    filename = "classified_data.txt"
    vault_access(filename)
    secure_preservation(filename)
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
