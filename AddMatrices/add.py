def add(*argv):
    sum = list()
    for j in range(len(argv)):
        if len(argv[j]) != len(argv[j-1]):
                raise ValueError("Given matrices are not the same size.")
        for i in range(len(argv[j])):
            if len(argv[j][i]) != len(argv[j][i-1]):
                raise ValueError("Given matrices are not the same size.")
    
    for i, li in enumerate(argv[0]):
        sum.append(list())
        for j in li:
            sum[i].append(0)

    for arg in argv:
        for i, li in enumerate(arg):
            for j, num in enumerate(li):
                sum[i][j] += num

    return sum


def add_suggested_solution():
    def add(*matrices):
        """Add corresponding numbers in given 2-D matrices."""
        combined = []
        for rows in zip(*matrices):
            row = []
            for values in zip(*rows):
                total = 0
                for n in values:
                    total += n
                row.append(total)
            combined.append(row)
        return combined