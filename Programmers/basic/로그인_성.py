def solution(id_pw, db):

    if id_pw in db:
        return 'login'
    else:
        for i in db:
            id,pw=i[0],i[1]

            if id==id_pw[0]:
                if pw!=id_pw[1]:
                    return 'wrong pw'
        return 'fail'



ip_pw=["rabbit04", "98761"]
db=[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]
print(solution(ip_pw,db))