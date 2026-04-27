class StudentRecord:
    def __init__(self, student_name, student_gwa):
        self.student_name = student_name
        self.student_gwa = float(student_gwa)

    def __str__(self):
        return f"Student: {self.student_name} | GWA: {self.student_gwa}"

class GradeAnalyzer:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.all_students = []

    def create_sample_atudent_file(self):
        sample_data = [
            "April_Delos_Reyes 1.25", "Rexine_Dimaranan 1.00", "Valerie Landicho 1.50",
            "Jienella_Lumilan 1.10", "Kaycee_Mero 2.25", "Ghiro_Reyes 1.40",
            "Khent_Antenor 1.80", "Ray_Ver_Navarro 1.20", "Katherine Perido 2.50",
            "Janhe_Marielle 1.05", "John_Vincent 2.00", "Precious_Dahlia 1.35",
            "Erykka_Dimaranan 1.15", "Zion_Ramos 1.90", "Althea Ferma 2.10",
            "Kent_Andrei 1.45", "Rynezer Geronimo 1.65", "Cye Lawas 2.30",
            "Faith Aterrado 1.75", "Trizha Dimaranan 1.95"
        ]
        with open(self.data_file_path, 'w') as file:
            file.write("\n".join(sample_data))
        print(f"System: Created '{self.data_file_path}' with 20 student record.\n")

    def load_student_data(self):
        try:
            with open(self.data_file_path, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) == 2:
                        name, gwa = parts[0], parts[1]
                        new_student = StudentRecord(name, gwa)
                        self.all_students.append(new_student)
        except FileNotFoundError:
            self.create_sample_student_file()
            self.load_student_data()