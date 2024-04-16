from Pyro4 import expose
import math

class Solver:
    def __init__(self, workers=None, input_file_name=None, output_file_name=None):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.workers = workers

    def solve(self):
        print("Job Started")
        print("Workers %d" % len(self.workers))
        numbers = self.read_input()

        # Calculate factorial sum
        total_sum = self.calculate_factorial(numbers)

        # Output
        self.write_output(total_sum)

        print("Job Finished")

    @staticmethod
    def calculate_factorial(numbers):
        total_sum = sum(math.factorial(num) for num in numbers)
        return total_sum

    def read_input(self):
        with open(self.input_file_name, 'r') as f:
            numbers = [int(line) for line in f]
        return numbers

    def write_output(self, output):
        with open(self.output_file_name, 'w') as f:
            f.write(str(output))
            f.write('\n')
