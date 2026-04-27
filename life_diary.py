class Life_Happenings:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lines_to_save = []

    def collect_and_save(self):
        while True:
            line_input = input("Please enter anything about your life right now: ")
            self.lines_to_save.append(line_input)

            choice = input("Do you anything more to say? ").strip().lower()
            if choice == 'no':
                break

        with open(self.file_name, 'w') as diary_file:
            diary_file.write('\n'.join(self.lines_to_save))
        print("\n--- File Saved Successfully ---")

    def display_contents(self):
        print(f"\nContents of {self.file_name}:")
        try:
            with open(self.file_name, 'r') as diary_file:
                for line in diary_file:
                    print(line.strip())
        except FileNotFoundError:
            print("Error: The file could not be found.")