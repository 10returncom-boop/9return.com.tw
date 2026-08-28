# 全台建案統計儀表板 | 9return.com.tw

台灣不動產公寓大廈報備資料開放平台，彙整全台 22 縣市公寓大廈報備資訊，提供縣市別、行政區別、個案建案的多維度統計與查詢。

## 網站功能

- **總覽指標**：全台建照/使用執照年度累計、待售新成屋、預售屋建案統計
- **縣市別主表**：每縣市一列，含六都/非六都標籤、建照/使照統計、待售宅數、預售戶數
- **鄉鎮市區子表**：點擊縣市展開各區建案件數、戶數、主要重劃區標註
- **個案建案明細庫**：建案名稱、縣市、行政區、地址、戶數、建物型態、管理組織、重劃區標記
- **8 縣市獨立子頁**：臺北市、新北市、桃園市、臺中市、臺南市、嘉義市、彰化縣、新竹市

## 資料涵蓋

| 項目 | 數量 |
|------|------|
| 公寓大廈報備筆數 | 37,225 筆 |
| 已涵蓋縣市 | 8 / 22 |
| 行政區 | 138 個 |
| 總戶數 | 697,070 戶 |
| 重劃區標記 | 22,495 棟 (60.5%) |

### 已涵蓋縣市

| 縣市 | 筆數 | 戶數 | 子頁 |
|------|------|------|------|
| 臺中市 | 12,004 | — | [counties/taichung.html](counties/taichung.html) |
| 臺北市 | 9,155 | — | [counties/taipei.html](counties/taipei.html) |
| 新北市 | 4,714 | — | [counties/newtaipei.html](counties/newtaipei.html) |
| 桃園市 | 3,191 | — | [counties/taoyuan.html](counties/taoyuan.html) |
| 臺南市 | 2,847 | — | [counties/tainan.html](counties/tainan.html) |
| 新竹市 | 2,536 | — | [counties/hsinchu.html](counties/hsinchu.html) |
| 嘉義市 | 1,624 | — | [counties/chiayi.html](counties/chiayi.html) |
| 彰化縣 | 1,117 | — | [counties/changhua.html](counties/changhua.html) |

### 待補縣市（14 個）

宜蘭縣、新竹縣、苗栗縣、南投縣、雲林縣、嘉義縣、屏東縣、臺東縣、花蓮縣、澎湖縣、金門縣、連江縣、基隆市、高雄市

> 後續若各縣市政府開放公寓大廈報備資料或伺服器恢復，可隨時匯入更新，不需改動網站架構。

## 專案結構

```
9return-com-tw/
├── index.html                  # 儀表板首頁（總覽＋縣市表＋個案庫）
├── CNAME                       # GitHub Pages 自訂網域
├── counties/                   # 各縣市獨立子頁
│   ├── taichung.html
│   ├── taipei.html
│   ├── newtaipei.html
│   ├── taoyuan.html
│   ├── tainan.html
│   ├── hsinchu.html
│   ├── chiayi.html
│   └── changhua.html
├── data/                       # 處理後 JSON 資料（網站讀取）
│   ├── overview.json           # 總覽指標
│   ├── county_stats.json       # 縣市別統計
│   ├── district_stats.json     # 行政區別統計
│   ├── case_db.json            # 個案建案明細庫
│   └── raw/                    # 原始 CSV 資料
│       └── 全台公寓大廈報備資料彙整_v2.1.csv
├── scripts/                    # 資料處理與網站建置腳本
│   └── build_dashboard.py      # CSV → JSON + HTML 產生器
├── docs/                       # 專案文件
│   ├── DATA_SOURCES.md         # 資料來源說明
│   └── UPDATE_GUIDE.md         # 資料更新與新增縣市指南
├── .gitignore
├── LICENSE
└── README.md
```

## 資料欄位說明

原始 CSV（v2.1）共 10 欄：

| 欄位 | 說明 |
|------|------|
| 縣市 | 所屬縣市（繁體中文） |
| 使照序號 | 使用執照序號 |
| 公寓大廈名稱 | 建案/社區名稱 |
| 行政區 | 鄉鎮市區 |
| 地址 | 完整地址 |
| 戶數 | 總戶數（部分縣市開放資料未提供） |
| 管理組織型態 | 管理委員會 / 區分所有權人會議 / 其他 |
| 建物型態 | 大樓 / 華廈 / 公寓 / 社區 / 其他（自動分類） |
| 重劃區標記 | 依名稱/地址關鍵字比對標註的重劃區 |
| 資料來源 | 彙整來源標記 |

## 技術架構

- **前端**：純靜態 HTML + CSS + JavaScript（無框架依賴）
- **圖表**：ECharts 5.6（CDN）
- **字體**：Noto Sans TC / Noto Serif TC（Google Fonts）
- **資料**：JSON 靜態檔案，由 Python 腳本從 CSV 產生
- **託管**：GitHub Pages（自訂網域 9return.com.tw）

## 本地預覽

```bash
# 進入專案目錄
cd 9return-com-tw

# 啟動簡易 HTTP 伺服器
python -m http.server 8080

# 瀏覽器開啟
# http://localhost:8080
```

## 重新建置網站

```bash
# 安裝依賴（僅需標準函式庫）
python scripts/build_dashboard.py

# 輸出：
#   data/overview.json
#   data/county_stats.json
#   data/district_stats.json
#   data/case_db.json
#   index.html
#   counties/*.html
```

## 資料來源

- 各縣市政府公寓大廈報備開放資料
- data.gov.tw 國家發展委員會資料開放平台
- 內政部建築管理資訊系統
- 實價登錄資料

詳見 [docs/DATA_SOURCES.md](docs/DATA_SOURCES.md)

## 更新紀錄

| 版本 | 日期 | 說明 |
|------|------|------|
| v2.1 | 2026-08-28 | 新增新竹市 2,536 筆（data.gov.tw）；新增建物型態、重劃區標記欄位；22 縣市架構 |
| v2.0 | 2026-08-28 | 7 縣市 34,689 筆彙整；儀表板上線 |
| v1.0 | 2026-08-28 | 臺中市公寓大廈分析網站 |

## 授權

本專案資料來自政府開放資料，依 [政府開放資料授權條款](https://data.gov.tw/license) 使用。
程式碼部分採 MIT 授權，詳見 [LICENSE](LICENSE)。

## 聯絡

- 網站：https://9return.com.tw
- 資料問題：歡迎發 Issue 或 Pull Request
