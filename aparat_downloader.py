import requests
class aparat:
    def __init__(self,link:str) -> None:
        main_url = "https://www.aparat.com/v/"
        post_hash = link[link.find(main_url)+len(main_url):]
        api = "https://www.aparat.com/api/fa/v1/video/video/show/videohash/"+post_hash+"?pr=1&mf=1&referer=direct"
        response = requests.get(url=api).json()
        post_data:dict = response["data"]
        self.data = post_data
        self.title = post_data["data"]["attributes"]["title"]
        self.description = post_data["data"]["attributes"]["description"]
        self.tags = post_data["data"]["attributes"]["tags"]
        self.seen = post_data["data"]["attributes"]["visit_cnt"]
        us_data = {}
        for j in post_data["included"]:
            if j["type"] == "Like":
                self.like = j["attributes"]["cnt"]
            elif j["type"] != "Follow":
                us_data["type"] = j["type"]
                us_data["username"] = j["attributes"]["username"]
                us_data["avatar"] = j["attributes"]["avatar"]
                us_data["follower"] = j["attributes"]["follower_cnt"]
        self.user_data = us_data
        file_link_all = post_data["data"]["attributes"]["file_link_all"]
        for i in file_link_all:
            d = {}
            d["quality"] = i["profile"]
            d["url"] = i["urls"][0]
            self.download_data.append(d)
    def download(self,dic:str,num_link:int) -> bytes:
        if num_link != None:
            l = self.download_data[num_link]["url"]
            bytes_down = requests.get(l,allow_redirects=True).content
            if dic == None:
                o = open(self.title+".mp4","wb")
                o.write(bytes_down)
                o.close()
            else:
                o = open(dic+".mp4","wb")
                o.write(bytes_down)
                o.close()
            return bytes_down
        else:
            l = self.download_data[0]["url"]
            bytes_down = requests.get(l,allow_redirects=True).content
            if dic == None:
                o = open(self.title+".mp4","wb")
                o.write(bytes_down)
                o.close()
            else:
                o = open(dic+".mp4","wb")
                o.write(bytes_down)
                o.close()
            return bytes_down