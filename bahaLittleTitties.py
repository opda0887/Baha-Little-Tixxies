import requests
import os
from bs4 import BeautifulSoup
# 原始網址：https://forum.gamer.com.tw/C.php?page=1&bsn=60076&snA=6429036&gothis=89069355#89069355


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
    # 檢查圖片是否無效
    img = sendRequest(url)

    if (img == False):
        return False

    if not img.content[:4] == b'\xff\xd8\xff\xe0':  # jpeg 開始於 \xff\xd8\xff\xe0
        return False

    return True


# 設定 User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Cookie': '',  # 輸入你的cookie (根據：login_token.php)
}

image_tas = input("輸入你需要幾頁的份量(一頁可能又很多張)：")
titty_index = 0  # 計算第幾張圖片

for i in range(int(image_tas)):

    response = requests.get(
        f'https://forum.gamer.com.tw/C.php?page={i+1}&bsn=60076&snA=6429036&gothis=89069355#89069355', headers=headers)

    # 確認是否爬取成功
    if response.status_code == 200:
        print("Page"+str(i+1)+f' 請求成功：{response.status_code}')
    else:
        print("Page"+str(i+1)+f' 請求失敗：{response.status_code}')

    soup = BeautifulSoup(response.text, "lxml")

    results = soup.find_all("a", {"class": "photoswipe-image"})  # 可設定 limit

    image_links = [result.get("href") for result in results]  # 取得圖片來源連結

    for index, link in enumerate(image_links):

        # 判斷圖片是否無效：
        check = checkImg(link)

        if (check):
            if not os.path.exists("littleTitties"):
                os.mkdir("littleTitties")  # 建立資料夾

            img = requests.get(link)  # 下載圖片

            with open("littleTitties\\" + "Titty-" + str(titty_index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
                file.write(img.content)  # 寫入圖片的二進位碼
            titty_index += 1

print("圖片下載已結束，可去 littleTitties 檔案裡查看圖片")
