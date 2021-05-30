# 초보자를 위한 파이썬 300제
#81~90

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,_,_= scores
print(valid_score)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

_,_,*valid_score = scores
print(valid_score)

_,*valid_score,_ = scores
print(valid_score)

temp={}

ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(ice)

ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)

print(ice["메로나"])

ice["메로나"] = 1300
print(ice)

del ice["메로나"]
print(ice)

