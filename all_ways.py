from typing import List, Dict
from copy import deepcopy
def all_ways_up(stairs: int, steps: List[int]) -> List[List[int]]:
    """_Find all the ways up a given number of stairs and given steps to take each time_

    Args:
        stairs (int): _Number of stairs_
        steps (List[int]): _steps you are allowed to take at a time_

    Returns:
        List[List[int]]: _A list of all the ways to get to the top_
    """
    all_ways: List[List[int]] = []
    if stairs < 0:
        return None
    if stairs == 0:
        return [[]]
    for step in steps:
        new_stairs: int = stairs - step

        result: List[int]= all_ways_up(stairs= new_stairs, steps= steps)
        if result != None:
            list(map(lambda value: value.append(step), result))
            all_ways.extend(result)
    return all_ways

def all_ways_up_memo(stairs: int, steps: List[int], memo: Dict[int, List[List[int]]] = {0:[[]], 1:[[1]], 2:[[2], [1, 1]]}):
    if stairs in memo:
        return memo[stairs]
    all_ways = []
    if stairs < 0:
        return None
    for step in steps:
        new_stairs: int = stairs - step
        result: List[List[int]] = all_ways_up_memo(stairs= new_stairs, steps= steps, memo=memo)
        if result != None:
            current = deepcopy(result)
            list(map(lambda ways: ways.append(step), current))
            all_ways.extend(current)
    memo[stairs] = all_ways
    return memo[stairs]

def main() -> None:
    steps: List[int] = [2, 1]
    stairs: int = 5
    all: List[List[int]] = all_ways_up_memo(stairs= stairs, steps= steps)

    print(f"All the possible ways to ascend to the top of {stairs} stairs given the steps {steps} are: {all}")

if __name__ == "__main__":
    main()