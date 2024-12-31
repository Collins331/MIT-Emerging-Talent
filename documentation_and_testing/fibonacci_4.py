def fibonacci_list(how_many: int) -> list[int]:
    # two base cases
    if how_many == 0:
        return []
    if how_many == 1:
        return [0]

    all_of_them = [0, 1]
    # use iterator to count, ignore its value
    # the loop body will not execute if how_many is 2
    for _ in range(2, how_many):
        # add previous two values from the list
        next_one = all_of_them[-1] + all_of_them[-2]
        # append the new value to the list
        all_of_them.append(next_one)

    return all_of_them


if __name__ == "__main__":
    print(fibonacci_list(5))