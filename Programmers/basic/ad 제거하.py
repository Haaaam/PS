def solution(strArr):

    return [i for i in strArr if "ad" not in i]

strArr=["and","notad","abcd"]
print([i for i in strArr if "ad" not in i])
