from typing import Any, Union

from bs4 import BeautifulSoup as BS
import Link_request as linkr
def souping(html_text, user_link):
    main_soup = BS(html_text,"html.parser")
    list_of_hrefs = main_soup.find_all("td", {"headers": ["t1sa1 t1sb1", "t2sa1 t2sb1", "t3sa1 t3sb1"]})
    new_list = []
    codes = [] # Now we can get codes of cities from main page
    for href in list_of_hrefs[:-1]:
        try:
            new_href = user_link.split("ps32")[0] + href.a.get("href")
        except AttributeError:
            pass
        new_list.append(new_href)
        codes.append(href.text)
    return new_list, codes
def souping_local(href):
    small_soup = BS(linkr.requesting(href), "html.parser")
    return small_soup

def gettting_city_name(small_soup):
    city = small_soup.find_all("h3")
    for small_city in city:
        if "Obec" in small_city.text:
            return small_city.text.split(": ")[1]


def local_labels(small_soup):
    headers = small_soup.find_all("th", {"id": ["sa2", "sa5", "sa6"]})
    heads = [head.text for head in headers]
    return heads


def local_parties(small_soup):
    headers = small_soup.find_all("td",{"headers": ["t1sa1 t1sb2","t2sa1 t2sb2"]})
    heads = [head.text for head in headers]
    return heads

def local_numbers(small_soup):
    voters = small_soup.find_all("td",{"headers":["sa2","sa5","sa6","t1sa2 t1sb3","t2sa2 t2sb3"]})
    numbers = [number.text for number in voters]

    return numbers


if __name__ == "__main__":
    print("Module works")