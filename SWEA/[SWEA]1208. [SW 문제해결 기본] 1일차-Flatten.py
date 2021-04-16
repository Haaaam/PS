for i in range(10):
    dump=int(input())
    box_height=list(map(int,input().split()))
    for _ in range(dump):
        target=min(box_height)
        max_box=max(box_height)
        if max(box_height)-min(box_height)==0:
            break
        else:
            box_height[box_height.index(target)]+=1
            box_height[box_height.index(max_box)]-=1
    print(f"#{i+1} {max(box_height)-min(box_height)}")

