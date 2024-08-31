import sys
import os

def main():
    if not os.path.exists("main.py"):
        print("Error: `main.py` not found")
        sys.exit(1)
    if sys.argv[-1] in ["arm64-v8a", "armeabi-v7a", "x86", "x86_64"]:
        if os.path.exists("buildozer.spec"):
            os.remove("buildozer.spec")
        if not os.path.exists("buildozer_template.spec"):
            print("Error: `buildozer_template.spec` not found")
            sys.exit(1)
        with open("buildozer_template.spec", "r") as f, open("buildozer.spec", "w") as f1:
            content = f.read().replace("{{ arch }}", sys.argv[-1])
            f1.write(content)
    else:
        print("Error: invalid architecture")
        sys.exit(1)

if __name__ == "__main__":
    main()