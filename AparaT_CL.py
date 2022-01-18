import random
import requests

class aparat:
    def __init__(self,link:str) -> None:
        main_url = "https://www.aparat.com/v/"
        post_hash = link[link.find(main_url)+len(main_url):]
        api = "https://www.aparat.com/api/fa/v1/video/video/show/videohash/"+post_hash+"?pr=1&mf=1&referer=direct"
        response = requests.get(url=api).json()
        post_data:dict = response["data"]
        self.data = response
        self.title = post_data["attributes"]["title"]
        self.description = post_data["attributes"]["description"]
        self.tags = post_data["attributes"]["tags"]
        self.seen = post_data["attributes"]["visit_cnt"]
        us_data = {}
        for j in response["included"]:
            if j["type"] == "Like":
                self.like = j["attributes"]["cnt"]
            elif j["type"] != "Follow":
                us_data["type"] = j["type"]
                us_data["user_name"] = j["attributes"]["username"]
                us_data["avatar"] = j["attributes"]["avatar"]
                us_data["follower"] = j["attributes"]["follower_cnt"].split(" ")[0]
        self.user_data = us_data
        file_link_all = post_data["attributes"]["file_link_all"]
        self.download_data = []
        for i in file_link_all:
            d = {}
            d["quality"] = i["profile"]
            d["url"] = i["urls"][0]
            self.download_data.append(d)
    def download(self,dic:str=None,num_link:int=None):
        file_name = "AparaT_CL"+str(random.randint(0,999))+".mp4"
        if num_link != None:
            l = self.download_data[num_link]["url"]
            bytes_down = requests.get(l,allow_redirects=True).content
            if dic == None:
                o = open(file_name,"wb")
                o.write(bytes_down)
                o.close()
            else:
                o = open(dic+file_name,"wb")
                o.write(bytes_down)
                o.close()
            return file_name
        else:
            l = self.download_data[0]["url"]
            bytes_down = requests.get(l,allow_redirects=True).content
            if dic == None:
                o = open(file_name,"wb")
                o.write(bytes_down)
                o.close()
            else:
                o = open(dic+file_name,"wb")
                o.write(bytes_down)
                o.close()
            return file_name