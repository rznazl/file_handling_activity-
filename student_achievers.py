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