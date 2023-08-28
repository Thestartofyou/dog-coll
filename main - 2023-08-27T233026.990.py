class DogAdventure:
    def __init__(self, name):
        self.name = name
        self.adventure_diary = []

    def record_entry(self, date, location, photo_url, notes):
        entry = {
            "date": date,
            "location": location,
            "photo_url": photo_url,
            "notes": notes
        }
        self.adventure_diary.append(entry)

    def view_diary(self):
        print("\nAdventure Diary for", self.name)
        for entry in self.adventure_diary:
            print("Date:", entry["date"])
            print("Location:", entry["location"])
            print("Notes:", entry["notes"])
            print("Photo:", entry["photo_url"])
            print("-" * 30)

def main():
    dog_name = input("Enter your dog's name: ")
    dog = DogAdventure(dog_name)

    while True:
        print("\nAdventure Diary Menu")
        print("1. Record a new adventure entry")
        print("2. View adventure diary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            location = input("Enter location: ")
            photo_url = input("Enter photo URL: ")
            notes = input("Enter notes: ")

            dog.record_entry(date, location, photo_url, notes)
            print("Adventure entry recorded!")

        elif choice == "2":
            dog.view_diary()

        elif choice == "3":
            print("Exiting the Adventure Diary.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

