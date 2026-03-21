import sys

def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    
    try:
        print("Input Stream active. ", end="")
        id = input("Enter archivist ID: ")
        print("Input Stream active. ", end="")
        status = input("Enter status report: ")
    except KeyboardInterrupt as e:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    try:
        print(f"\n[STANDARD] Archive status from {id}:"
              f" {status}", file=sys.stdout)
        print("[ALERT] System diagnostic: "
              "Communication channels verified", file=sys.stderr)
        print("[STANDARD] Data transmission complete", file=sys.stdout)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    try:
        main()
    except BaseException as e:
        print(f"An unexpected error occurred: {e}")
