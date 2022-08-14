from main import download_img
page = 0
sub_page = 0
img_id = 4997 #start
img_id_temp = ""   
latest_last_img = 4996 #end

def opdt_link_download():
    link = "https://optc-db.github.io/api/images/full/transparent/" + str(page) + "/" + str(sub_page) + "00/" + img_id_temp + ".png"
    return link

#while img_id_temp <= 4996:
while page <= 5:
    if img_id < 10:
        img_id_temp = "000" + str(img_id)
    elif img_id < 100:
        img_id_temp = "00" + str(img_id)
    elif img_id < 1000:
        img_id_temp = "0" + str(img_id)
    else:
        img_id_temp = str(img_id)

    if int(img_id_temp) > latest_last_img:
        #print(img_id_temp)
        break
    
    sub_page = [*img_id_temp][1]

    img_url = opdt_link_download()
    #print(img_url)
    download_img(img_url)

    img_id += 1
    
    page = img_id // 1000

