import json
import os

class PerformanceTracking:
    next_id = 8655

    def __init__(self, name):
        self.name = name
        self.score = {}
        self.student_id = self.generate_student_id()

    def generate_student_id(self):
        student_id = PerformanceTracking.next_id
        PerformanceTracking.next_id += 1
        return student_id

    def add_score(self, score, subject):
        self.score[subject] = score

    def calculate_average(self):
        total_score = sum(self.score.values())
        total_subjects = len(self.score)
        if total_subjects == 0:
            return 0
        return total_score / total_subjects

    def to_dict(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'score': self.score
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data['name'])
        student.student_id = data['student_id']
        student.score = data['score']
        return student


# Path to the file that stores student data
DATA_FILE = 'students_data.json'


# Function to save all student data to the file
def save_data(students):
    with open(DATA_FILE, 'w') as file:
        json.dump(students, file, indent=4)


# Function to load student data from the file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            # Ensure that the data is always a list
            if isinstance(data, list):
                return data
            else:
                return []
    return []


# Function to find a student by ID
def find_student_by_id(student_id, students_data):
    for student_data in students_data:
        if student_data['student_id'] == student_id:
            return PerformanceTracking.from_dict(student_data)
    return None


# Main Program
def main():
    while True:  # Keep looping until user decides to exit
        # Load existing student data from the file
        students_data = load_data()

        # Ask the user if they want to add a new student or find an existing one
        action = input("Enter 'new' to add a new student, 'find' to find an existing student, or 'exit' to quit: ").lower()

        if action == 'new':
            # Get the user's name and create a new student object
            name = input("Enter name: ")
            student = PerformanceTracking(name)

            # Enter the subjects and scores
            while True:
                subject = input("Enter subject (or type 'quit' to finish): ")
                if subject.lower() == 'quit':
                    break

                while True:
                    try:
                        score = float(input(f"Enter score for {subject}: "))
                        if score < 0 or score > 100:
                            print("Invalid score. Please enter a score between 0 and 100.")
                        else:
                            student.add_score(score, subject)
                            break  # Valid score entered, break out of the score input loop
                    except ValueError:
                        print("Invalid input. Please enter a valid number for the score.")

            # Save the new student data
            students_data.append(student.to_dict())
            save_data(students_data)

            # Display the student's unique ID
            print(f"\nStudent ID: {student.student_id}\n")

            # Display the student's performance
            print(f"\nPerformance for {student.name} (ID: {student.student_id}):")
            for subject, score in student.score.items():
                print(f"{subject}: {score}")
                if score <= 40:
                    print("Improve your marks.")
                elif score <= 60:
                    print("You can do better.")
                elif score <= 80:
                    print("Good performance.")
                else:
                    print("Excellent performance.")

            # Calculate the average score
            average = student.calculate_average()
            print(f"\nTotal average score: {average:.2f}")

            # Pass/Fail based on average score
            if average < 40:
                print("Status: Fail. Needs improvement.")
            else:
                print("Status: Pass.")

            # Additional performance feedback based on average score
            if average <= 40:
                print("Overall performance: Needs significant improvement.")
            elif 40 < average <= 60:
                print("Overall performance: You can do better.")
            elif 60 < average <= 80:
                print("Overall performance: Good performance.")
            else:
                print("Overall performance: Excellent.")

        elif action == 'find':
            # Ask for the student ID to search for an existing student
            student_id = int(input("Enter student ID to find: "))

            # Find the student by ID
            student = find_student_by_id(student_id, students_data)
            if student:
                # Display the student's performance
                print(f"\nPerformance for {student.name} (ID: {student.student_id}):")
                for subject, score in student.score.items():
                    print(f"{subject}: {score}")
                    if score <= 40:
                        print("Improve your marks.")
                    elif score <= 60:
                        print("You can do better.")
                    elif score <= 80:
                        print("Good performance.")
                    else:
                        print("Excellent performance.")

                # Calculate the average score
                average = student.calculate_average()
                print(f"\nTotal average score: {average:.2f}")

                # Pass fail Show fun
                if average < 40:
                    print("Status: Fail. Needs improvement.")
                else:
                    print("Status: Pass.")

                # Additional performance feedback based on average score
                if average <= 40:
                    print("Overall performance: Needs significant improvement.")
                elif 40 < average <= 60:
                    print("Overall performance: You can do better.")
                elif 60 < average <= 80:
                    print("Overall performance: Good performance.")
                else:
                    print("Overall performance: Excellent.")
            else:
                print(f"Student with ID {student_id} not found.")

        elif action == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please enter 'new'u, 'find', or 'exit'.")


if __name__ == "__main__":
    main()

