xinetd-wrapper
===

嗨，修網安的同學

這邊的專案是將 python code 接上網路，如果不想用的話可以直接刻一個 socket ~~我覺得自己刻一個 socket 比較快~~

## 使用步驟

1. 安裝 Docker

- Windows: https://hub.docker.com/editions/community/docker-ce-desktop-windows
- Linux: `curl -fsSL https://get.docker.com | sh`
- macOS: https://docs.docker.com/docker-for-mac/install/

2. 安裝 docker-compose
https://docs.docker.com/compose/install/

3. 將你的 python 程式碼放到 `chal/bin/` 並且命名為 `serve.py`

4. 執行 `docker-compose up -d`

5. 結素
結果應該長這樣
![](https://github.com/racterub/xinetd-wrapper/blob/master/screenshot.png)
