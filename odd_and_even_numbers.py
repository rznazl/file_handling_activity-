class NumberSorter:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.number_list = []

    def create_sample_file(self):
        sample_numbers = [
            "9", "28", "4", "66", "12", "89", "34", "7", "19", "11",
            "92", "5", "18", "5", "77", "42", "29", "60", "81", "14"
        ]
        with open(self.input_file_path, 'w') as new_file:
            new_file.write("\n".join(sample_numbers))
        (print(f"File '{self.input_file_path}') created with 20 integers."))

    def load_numbers_from_file(self):
        try:
            with open(self.input_file_path, 'r') as source_file:
                raw_data = source_file.read().split()
                self.number_list = [int(item) for item in raw_data]
        except FileNotFoundError:
            print(f"Error: {self.input_file_path} not found. Now creating...")
            self.create_sample_file()
            self.load_numbers_from_file()

    def split_and_save_numbers(self):
       if not self.number_list:
           print("No numbers given to process.")
           return

       even_numbers = [str(n) for n in self.number_list if n % 2 == 0]
       odd_numbers = [str(n) for n in self.number_list if n % 2 != 0]