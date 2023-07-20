import requests
from bs4 import BeautifulSoup



def search(url,text):
    try:
        resp=requests.get(url)
        resp.raise_for_status()

        soup=BeautifulSoup(resp.content,'html.parser')

        if text in soup.get_text():
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the:{e}")
        return False
    except Exception as e :
        print(f"An unexpected error occured:{e}")
        return False

if __name__=="__main__":

    input_url=input("Enter the url you want to search:")
    searchlist=[]
    for i in range(3):
        searchlist.append(input("Enter the text you want to search for :"))


    for i in range(len(searchlist)):
        if search(input_url, searchlist[i]):
            print(f"The URL '{input_url}' contains the text '{searchlist[i]}'. ")
        else:
            print(print(f"The URL '{input_url}' does not  contain the text '{searchlist[i]}'. "))
