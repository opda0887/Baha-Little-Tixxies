Update: 2022/8/24  
Properties: Include shopee、momo、ruten、Amazon 4 types of online shop to search  
Notifications :  

----- *** Env setting *** -----  

1. Interpreter: Python 3.10.2 64-bit

2. Web Browser I use: Edge  
// can change to Chrome if you want, modify "webdriver.Edge" to "webdriver.Chrome" in code, and download google's webdriver

3. Need to install: selenium, PyAutoGUI, edge-driver 

4. selenium version: 4.2.0  
// type: "pip install selenium" in cmd to install the latest selenium  

5. PyAutoGUI version: 0.9.53  
// type: "pip install pyautogui" in cmd to install the latest pyautogui  

6. edge-driver version: depend on what Edge version you use  
// download edge-driver: https://developer.microsoft.com/zh-tw/microsoft-edge/tools/webdriver/

----- *** In code setting *** -----  

// in case you use Edge as browser  
1. executable_path= "where your -msedgedriver.exe- in your path"
// in case you use Chrome as browser 
2. executable_path= "where your -chromedriver.exe- in your path"  

example to change:  
    driver = webdriver.Edge(executable_path="C:\\folder\\chromedriver.exe")
