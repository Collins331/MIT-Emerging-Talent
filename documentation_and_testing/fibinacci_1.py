def fibonnaci_list(n: int) -> list[int]:
    # return a hard-coded value if n is too small
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    else:
        # make the right answer and return it
        list = fibonnaci_list(n - 1)
        list.append(list[-1] + list[-2])
        return list
    
    
if __name__ == "__main__":
    print(fibonnaci_list(5))