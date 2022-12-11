import requests
import os
from bs4 import BeautifulSoup


def sendRequest(url):
    try:
        imgPage = requests.get(url)

    except Exception as e:
        print("error:", e)
        return False

    # check status code
    if (imgPage.status_code != 200):
        return False

    return imgPage


def checkImg(url):
    img = sendRequest(url)

    if (img == False):
        return False

    if not img.content[:4] == b'\xff\xd8\xff\xe0':  # jpeg starts with \xff\xd8\xff\xe0
        return False

    return True


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}

image_tas = input("輸入你需要幾頁的份量(一頁可能又很多張)：")
nipo_index = 0

for i in range(int(image_tas)):

    response = requests.get(
        f'https://forum.gamer.com.tw/C.php?page={i+1}&bsn=60076&snA=6429036&gothis=89069355#89069355', headers=headers)
    if response.status_code == 200:
        print("Page"+str(i+1)+f'請求成功：{response.status_code}')
    else:
        print("Page"+str(i+1)+f'請求失敗：{response.status_code}')

    soup = BeautifulSoup(response.text, "lxml")

    results = soup.find_all("a", {"class": "photoswipe-image"})  # 可設定 limit

    image_links = [result.get("href") for result in results]  # 取得圖片來源連結

    for index, link in enumerate(image_links):

        # print(link)
        # 判斷圖片是否無效：
        check = checkImg(link)

        if (check):
            if not os.path.exists("littleTitties"):
                os.mkdir("littleTitties")  # 建立資料夾

            img = requests.get(link)  # 下載圖片

            with open("littleTitties\\" + "Titty-" + str(nipo_index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
                file.write(img.content)  # 寫入圖片的二進位碼
            nipo_index += 1
