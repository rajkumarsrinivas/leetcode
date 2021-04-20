from typing import List

# better solution O(n) with almost no extra space.
def isSubsequence(a: str, b: str) -> bool:
    index = 0
    for s in a:
        if(s == b[index]):
            index += 1
        if index >= len(b):
            return True
    return False

if __name__ == "__main__":
    print(isSubsequence("allepaaappeelll", "apple"))