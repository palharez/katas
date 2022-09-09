class Solution:
    def countStudents(self, students, sandwiches):

        while sandwiches:
            attempt = 0

            sandwich = sandwiches.pop(0)

            while students:
                attempt += 1

                if attempt > len(students):
                    return len(students)

                student = students.pop(0)

                if student == sandwich:
                    break

                else:
                    students.append(student)

        return 0
