import os

def menu():
    print("\nSMART CROWD DENSITY & RISK ZONE ANALYZER")
    print("-------------------------------------")
    print("1. Train YOLO Model")
    print("2. Detect Crowd in Image")
    print("3. Detect Crowd in Live Video")
    print("4. Show Density Graph")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        os.system("python scripts/train.py")

    elif choice == "2":
        os.system("python scripts/detect_image.py")

    elif choice == "3":
        os.system("python scripts/detect_video.py")

    elif choice == "4":
        os.system("python scripts/density_visual.py")

    elif choice == "5":
        print("Exiting... Thank you!")
        break

    else:
        print("Invalid choice! Try again.")
