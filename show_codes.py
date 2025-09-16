import os

def read_codes():
    for root, dirs, files in os.walk("."):
        for file in sorted(files):
            if file.endswith((".java", ".xml", ".php", ".py", ".txt")):
                yield os.path.join(root, file)

if __name__ == "__main__":
    for filepath in read_codes():
        print("\n---", filepath, "---\n")
        with open(filepath, "r", encoding="utf-8") as f:
            print(f.read())
        input("\nPress Enter for next code...\n")
