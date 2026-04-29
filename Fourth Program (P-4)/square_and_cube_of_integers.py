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

    def process_math_operations(self):
        even_square_results = []
        odd_cube_results = []

        for num in self.numbers:
            if num % 2 == 0:
                result = num ** 2
                even_square_results.append(str(result))
            else:
                result = num ** 3
                odd_cube_results.append(str(result))

        self.save_results('double.txt', even_square_results)
        self.save_results('triple.txt', odd_cube_results)

        print("Calculated results saved to text files.")

    def save_results(self, filename, data_list):
        with open(filename, 'w') as output_file:
            output_file.write("\n".join(data_list))

math_bot = IntegerProcessor('integers.txt')
math_bot.load_data()
math_bot.process_math_operations()
