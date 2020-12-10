def is_valid(x, previous):
    for p in previous:
        desired = x - p
        if desired in previous and desired != p:
            return True

    return False


def find_invalid(data, size):
    previous = []

    for x in data:
        if len(previous) < size:
            previous.append(x)
        else:
            if not is_valid(x, previous):
                return x

            previous.append(x)
            previous.pop(0)


def find_contiguous(data, desired_sum):
    for i in range(0, len(data)):
        j = i + 1
        sum = data[i]
        while j < len(data) and sum < desired_sum:
            sum += data[j]
            j += 1

        if sum == desired_sum and i < j-1:
            contiguous_range = data[i:j-1]
            return max(contiguous_range) + min(contiguous_range)


fp = open("input/9.txt")
data = [int(x) for x in fp.read().splitlines()]

invalid = find_invalid(data, 25)
print("Part 1: {}".format(invalid))
print("Part 2: {}".format(find_contiguous(data, invalid)))
