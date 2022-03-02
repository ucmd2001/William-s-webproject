這是一個簡單的作品集，我會把轉職上我學到的所有技能都放在這裡，希望能夠幫助到任何想要轉職的人。
This is a simple portfolio, I will put all the skills I have learned on the job transfer here, hoping to help anyone who wants to change jobs.

## 1.環境依賴及目錄
使用 
pyhton 3.10.0 環境
flask 21.2.3  網站架構
mongoDB  資料庫

```
project
│   README.md
│   app.py            #主程式    
│
└───static           #靜態檔案資料夾
│      style.css     #靜態CSS檔
│      
│   
└───product          #模組資料夾
│      
│   │   ptt_crawler.py    #PTT八卦版爬蟲
│   │   web_crawler.py    #PTT網頁板爬蟲
│   │   ajax_crawler.py    #Ajax網頁爬蟲-for Medium
│   │   stock_crawler.py    #漲停股爬蟲
│
└───templates    #Flask網頁模板資料夾
│
│   │   ajax_crawler.html    #ajax爬蟲網頁模板
│   │   error.html           #錯誤網頁模板
│   │   index.html           #首頁
│   │   member_system.html   #會員系統網頁模板
│   │   personal_info.html   #個人資訊網頁模板
│   │   ptt_crawler.html     #PTT八卦版爬蟲網頁模板
│   │   pwchange.html        #變更密碼網頁模板
│   │   setting.html         #個人資訊顯示網頁模板
│   │   stock_crawler.html   #漲停股爬蟲網頁模板
│   │   web_crawler.html     #PTT網頁爬蟲網頁模板


```


## 2.框架、資料庫及上傳網站。
使用的是python-Flask框架、MongoDB資料庫、以及使用Heroku上傳雲端。
如有任何問題可以mail至我的gmail會以最快速度回復 : ucmd2001@gmail.com


![Imgur](https://i.imgur.com/v2lLdNn.png)
<p align="center"> 首頁總覽 </p>


## 3.作品簡單描述
### 1.會員系統:
  使用的是MongoDB資料庫(Nosql)儲存檔案。
  你可以在其中使用登入、註冊及更新密碼功能。

步驟一:點選會員系統
![Imgur](https://i.imgur.com/rTurVZC.png)

步驟二:註冊，輸入您的暱稱、信箱、及密碼後即可註冊，註冊完後會跳出註冊成功視窗

步驟三:可在個人會員頁確認自己的會員資訊，及更改密碼
![Imgur](https://i.imgur.com/HHOidWU.png)
<p align="center"> 會員系統頁 </p>

![Imgur](https://i.imgur.com/z0cSnYm.png)
<p align="center"> 個人資訊頁 </p>

![Imgur](https://i.imgur.com/9FilPG0.png)
<p align="center"> 更改密碼頁 </p>

步驟四:登出後，會跳出登出視窗，可再次登入。


### 2.爬蟲:
  使用的是Beatifulsoup來開發爬蟲系統，爬好的檔案直接回傳在網頁上。
  可以將想要爬的網站丟在input內來直接使用爬蟲(有設定1S回傳，以免有人瘋狂F5導致爬的網站當機)

1.PTT_web爬蟲: 可輸入一般PTT不需要18+認證之網頁，直接爬取標題。

![Imgur](https://i.imgur.com/F34Lmq2.png)
  
2.PTT_八卦版爬蟲: 可輸入需要18+認證之網頁，爬取當前所有標題。(目前輸入亂碼會跳出預設值:PTT八卦版網頁，仍在除錯)
![Imgur](https://i.imgur.com/Fg3Ziek.png)

3.Ajax爬蟲:按下按鈕後可以直接抓取目前Medium網站之文章標題。
![Imgur](https://i.imgur.com/WZEq2yO.png)

4.漲停股爬蟲:按下按鈕後可以直接抓取富邦證卷上，結算後所有漲停股之代號及名稱。
![Imgur](https://i.imgur.com/5FduJqZ.png)


