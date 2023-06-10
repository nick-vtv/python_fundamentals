def tribonacci(x):
    tribonacci_list = [0, 1, 1]

    if x <= 2:
        return tribonacci_list[:x+1]

    for i in range(3, x + 1):
        next_number = tribonacci_list[i-1] + tribonacci_list[i-2] + tribonacci_list[i-3]
        tribonacci_list.append(next_number)

    return tribonacci_list


length_of_sequence = int(input())
tribonacci_sequence = tribonacci(length_of_sequence)
tribonacci_sequence_from_one = list(map(str, tribonacci_sequence[1:]))
print(" ".join(tribonacci_sequence_from_one))
