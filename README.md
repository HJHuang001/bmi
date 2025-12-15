# bmi
計算BMI網頁，並能提供健康建議

## 簡介
這是一個使用 Python + Flask 實作的簡單 BMI 網頁應用，輸入體重與身高後會顯示 BMI 值、分類並給出一般性健康建議。

## 環境與執行 (macOS / zsh)
1. 建議建立虛擬環境並啟用：

```bash
python3 -m venv venv
source venv/bin/activate
```

2. 安裝需求：

```bash
pip install -r requirements.txt
```

3. 執行應用：

```bash
python app.py
# 或者使用 FLASK_APP：
# export FLASK_APP=app.py
# flask run
```

4. 開啟瀏覽器並前往 `http://127.0.0.1:5000`。

此專案僅供學習/參考用途，具體健康或醫療建議請洽專業人士。
