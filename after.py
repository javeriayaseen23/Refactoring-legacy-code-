"""
This is a sample Python program.
It demonstrates the Refactored code.
"""

from typing import List


class ComputeStatistics:

    def __init__(self, file: str):
        """
        Constructor to take file path.
        :param file: holds address of file.
        """
        self.file = file

    def test_read_int(self):
        """
        This method tests read_int() method.
        """
        pass

    def read_int(self) -> List[int]:
        """
        This method reads integer values from file and creates a list of integers.
        :return: list of integers
        """
        data = []
        try:
            with open(self.file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        num = int(line)
                        data.append(num)
        except IOError as e:
            print(e)
        return data

    def count(self) -> int:
        """
        This method calculates the count of integers in the list.
        :return: count of integers in list.
        """
        data = self.read_int()
        return len(data)

    def summation(self) -> int:
        """
        This method calculates the summation of integers in the list.
        :return: sum of integers in list.
        """
        data = self.read_int()
        total = 0
        for x in data:
            total += x
        return total

    def average(self) -> float:
        """
        This method calculates the average of integers in the list.
        :return: average of integers in list.
        """
        data = self.read_int()
        total = self.summation()
        cnt = self.count()
        return total / cnt

    def minimum(self) -> int:
        """
        This method finds the minimum value in the list.
        :return: minimum integer in list.
        """
        data = self.read_int()
        return min(data)

    def maximum(self) -> int:
        """
        This method finds the maximum value in the list.
        :return: maximum integer in list.
        """
        data = self.read_int()
        return max(data)


if __name__ == "__main__":
    file = "random_nums.txt"
    cs = ComputeStatistics(file)
    print("The values are: " + str(cs.read_int()))
    print("Total values in file are: " + str(cs.count()))
    print("Summation of data is: " + str(cs.summation()))
    print("Average of data is: " + str(cs.average()))
    print("Minimum value from data is: " + str(cs.minimum()))
    print("Maximum value from data is: " + str(cs.maximum()))