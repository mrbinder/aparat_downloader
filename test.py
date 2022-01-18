from AparaT_CL import aparat

link = input("\naparat link : ")

apa = aparat(link)

print("\n\nuploader user data >"+
      "\n type : "+apa.user_data["type"]+
      "\n user name : "+apa.user_data["user_name"]+
      "\n follower : "+apa.user_data["follower"]+
      "\n avatar url : "+apa.user_data["avatar"])

print("\n\npost data >"+
      "\n title : "+apa.title+
      "\n like : "+apa.like+
      "\n seen : "+apa.seen+
      "\n description : "+apa.description)

txt = "\n"
r = 0
for i in apa.download_data:
    txt += "\n("+str(r)+") quality : "+i["quality"]
    r+=1
print(txt)

select = int(input("selcet mode > "))

print("\ndownloading ...")

file_saved_name = apa.download(num_link=select)

print("download completed\nsaved in "+file_saved_name)


#location = input("File save location : ")
#apa.download(dic=location,num_link=int(select)) -> save in inputed location
#
#---------------------------------------------------------
#
#apa.download() -> download the low quality and save in Default location(Script execution location)