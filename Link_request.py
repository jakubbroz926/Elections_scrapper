import requests as rq
def requesting(link):
    link_local = rq.get(link)
    return link_local.text

if __name__ == "__main__":
    print("Module works")
