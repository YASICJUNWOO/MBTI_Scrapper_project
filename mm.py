from requests import get
from bs4 import BeautifulSoup

def extract_mbti_overview(mbti):
    url = "https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-"

    request = get(f"{url}{mbti}")

    mbti_data ={}

    if request.status_code != 200:
        return request.status_code
    else:
        soup = BeautifulSoup(request.text, "html.parser")
        article = soup.find("article", class_="main")

        #성격 유형
        type = article.find('h1')
        type_string = type.string.strip()[8:-1]
        mbti_data["type"] = type_string

        #특성들
        atts = article.find_all("h2")
        att_list = []
        for att in atts:
            att_list.append(att.string)
        mbti_data["att_list"] = att_list

    return mbti_data
