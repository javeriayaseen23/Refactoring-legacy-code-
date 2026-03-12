def compute_stats(file):
    total = 0
    sum_ = 0
    min_ = 0
    max_ = 0

    try:
        with open(file, 'r') as f:
            lines = f.readlines()

        first_line = int(lines[0].strip())
        min_ = first_line
        max_ = first_line

        for line in lines:
            line = line.strip()
            if line:
                num = int(line)
                total += 1
                sum_ += num

                if min_ > num:
                    min_ = num
                if max_ < num:
                    max_ = num

        print("total = " + str(total))
        print("summation = " + str(sum_))
        print("average = " + str(round(sum_ / total)))
        print("Minimum = " + str(min_))
        print("Maximum = " + str(max_))

    except IOError as e:
        print(e)


if __name__ == "__main__":
    compute_stats("random_nums.txt")