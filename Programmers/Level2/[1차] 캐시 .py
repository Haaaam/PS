def solution(cacheSize, cities):

    cache = []
    answer = 0
    # 캐시사이즈가 0알때
    if cacheSize == 0:
        answer += len(cities) * 5

    # 캐시사이즈가 1보다 크거나 같을때
    else:

        for i in cities:

            # 대문자로 변경
            i = i.upper()

            # cache의 길이가 cacheSize보다 작은 경우
            if len(cache) < cacheSize:
                if i in cache:
                    cache.remove(i)
                    cache.append(i)
                    answer+=1
                else:
                    cache.append(i)
                    answer += 5

            else:
                if i in cache:
                    cache.remove(i)
                    cache.append(i)
                    answer += 1

                # i가 cache에 없을 경우
                elif i not in cache:

                    if len(cache) >= cacheSize:
                        cache.append(i)
                        cache.remove(cache[0])
                        answer += 5
                    else:
                        cache.append(i)
                        answer+=5
    return answer
# 캐시
# 제이지가 작성한 부분중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 발견
# 어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만
# 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황
# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램 작성하기
# input: cacheSize, cities
# return "총 실행시간"
# 조건: 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용
# cache hit일 경우 실행시간 1, cache miss일 경우 실행시간 5
cacheSize=3
cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize,cities))



