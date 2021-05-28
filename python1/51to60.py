# 초보자를 위한 파이썬 300제
#51~60

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

movie_rank.append("배트맨")

movie_rank.insert(1,'수펴맨')
print(movie_rank)

del movie_rank[3]
print(movie_rank)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums), min(nums))

print(sum(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

print(sum(nums)/len(nums))