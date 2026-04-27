class IntegerProcessor:
    def __init__(self, source_file):
        self.source_file = source_file
        self.numbers = []

    def create_initial_file(self):
        sample_integers = [
            "2", "3", "4", "5", "10", "7", "8", "9", "12", "11",
            "6", "13", "14", "15", "20", "17", "18" "19", "28", "21"
        ]
        with open(self.source_file, 'w') as file:
            file.write("\n".join(sample_integers))
        print(f"System: Created '{self.source_file}' with 20 integers.\n")

    def load_data(self):
        try:
            with open(self.source_file, 'r') as file:
                self.numbers = [int(line.strip()) for line in file if line.strip()]
        except FileNotFoundError:
            self.create_initial_file()
            self.load_data()