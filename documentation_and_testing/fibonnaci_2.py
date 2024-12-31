def fibonnaci_list(n: int, memo: dict = {}) -> list[int]:
    if n in memo:
        return memo[n]

    list = []

    # return a hard-coded value if n is too small
    if n == 0:
        pass
    elif n == 1:
        list = [0]
    elif n == 2:
        list = [0,1]
    else:
        # make the right answer
        list = fibonnaci_list(n - 1)
        list.append(list[-1] + list[-2])

    # save the answer for later and return it
    memo[n] = list
    return list


if __name__ == "__main__":
    print(fibonnaci_list(5))