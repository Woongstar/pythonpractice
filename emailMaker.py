names = ["웅스타","아이언맨","헐크","스트레인지"]
for name in names:
    with open("{}.txt".format(name),"w",encoding="utf8") as email_file:

        email_file.write(f"""
안녕하세요 {name}님.
개발자 양지웅입니다.
현재 저는 AI와 빅데이터 분석에 관심이 많습니다. 공부해야 하게 많지만 많이 응원해주시고
{name}님의 많은 지원부탁드립니다. 감사합니다.
좋은하루 보내세요.
        """)