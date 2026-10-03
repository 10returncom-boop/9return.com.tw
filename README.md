# 欣矩陣 ∞ 欣媒體 — 商業多頁官網（含報價與成功案例）

> 版本：V1 ｜ 建置日期：2026-10-03 ｜ 專案編號：325_101
> 主體網站：https://9return.com.tw/ ｜ 設計規劃開發：張書欣

## 一、專案定位

為「欣矩陣 ∞ 欣媒體」打造的**商業多頁官網**，核心任務是呈現其跨產業垂直內容站點佈局 × 數位行銷 × SEO/AEO/GEO 整合能力，並把官方既有的 **22 個內容站點當作成功案例**，同時提供透明報價頁。設計走**典雅高級風**（象牙米白 × 深墨 × 香檳金 × 墨綠、襯線排印、細緻金線與留白），做出與眾不同、完整且利於流量的商業官網。

## 二、頁面清單（7 頁）

| 檔案 | 頁面 | 重點 |
| --- | --- | --- |
| `index.html` | 首頁 | Hero、數字統計、四大服務支柱、閉環流程、精選案例、FAQ、CTA |
| `services.html` | 服務項目 | 六大服務、合作流程時間軸 |
| `pricing.html` | 報價方案 | 基礎/進階/旗艦三方案、方案比較表、報價說明、FAQ |
| `cases.html` | 成功案例 | 22 個跨產業垂直站點、分類篩選（可點擊造訪原站） |
| `seo.html` | SEO·AEO·GEO | 三概念定義、我們怎麼做、FAQ（內容行銷獲取長尾流量） |
| `about.html` | 關於我們 | 品牌故事、操盤手張書欣、品牌歷程時間軸 |
| `contact.html` | 聯絡我們 | 聯絡資訊卡、需求表單（前端 mailto） |

## 三、目錄結構

```
325_101_欣矩陣欣媒體_商業官網_含報價與成功案例_V1/
├── index.html / services.html / pricing.html / cases.html / seo.html / about.html / contact.html
├── css/
│   ├── base.css        # 色彩 token（日夜）、Reset、字體層級、Clamp 流式工具
│   ├── layout.css      # Header / 導覽 / 側邊欄 / 麵包屑 / Footer / Hero / Section
│   ├── components.css  # 卡片 / 按鈕 / 時間軸 / 表格 / FAQ / 報價 / 表單 / 動效
│   └── pages.css       # 各頁專用微調
├── js/
│   ├── config.js       # 全站共用設定（品牌 / 聯絡 / 導覽 / 案例分類 / 統計）
│   ├── utils.js        # 主題切換、側邊欄、捲動顯現、FAQ、案例篩選、回到頂部
│   └── main.js         # 頁面初始化
├── assets/             # hero-main / bg-main / 22 張案例卡 / favicon.svg
├── sitemap.xml / robots.txt
├── _gen_site.py / _gen_pages.py / _gen_cases.py   # 生成腳本（後續擴頁用）
└── README.md
```

> 註：7 個內頁由 `_gen_site.py` 從 index.html 抽取共用 Header/Footer 批次生成，確保全站外觀一致；後續增頁只需在 `_gen_pages.py` 註冊 spec 後重跑腳本。

## 四、功能特色

- **日夜主題切換**：手動切換（localStorage 記憶）＋ 跟隨系統偏好（prefers-color-scheme）
- **側邊欄 Drawer**：手機／窄螢幕選單，含導覽與聯絡資訊
- **麵包屑 Breadcrumb**：全內頁具備，利於 SEO 與導覽
- **Breathe Clamp 組件**：∞ 符號呼吸動效 + clamp() 流式字體與排版
- **案例分類篩選**：cases.html 依 6 大產業即時篩選（原生 JS，無依賴）
- **豐富 UI 元件**：glow-card、時間軸（grid 三列對齊）、報價表、比較表、FAQ 手風琴
- **響應式**：桌面／平板／手機多斷點（案例網格 3→2→1、報價 3→1、比較表橫向捲動）
- **防呆**：鍵盤 focus 可見、reduced-motion 支援、語意化 HTML5

## 五、SEO / AEO / GEO 策略

- **SEO**：每頁獨立 title/description/keywords/canonical、Open Graph、Twitter Card；語意化 HTML5（header/nav/main/article/section/footer）；`sitemap.xml`＋`robots.txt`；案例圖片含描述性 alt
- **AEO**：首頁與 seo 頁埋設 `FAQPage` JSON-LD、直接回答型內容結構，利於精選摘要與語音助理
- **GEO**：全站 `Organization` 實體資訊一致（名稱/電話/Logo/Line）、`Service`、`OfferCatalog`、`BreadcrumbList` 結構化資料，建立可被生成式 AI 引用的權威實體
- 各頁 JSON-LD：Organization、WebSite、Service、OfferCatalog、FAQPage、ContactPage

## 六、圖影素材與提示詞

- **主視覺**：首頁 hero 不再使用賽博霓虹圖，改為典雅 CSS 背景（象牙米白/深墨底 + 頂部細金線 + 柔金暈染 + 置中品牌 ∞），品牌 ∞ 以香檳金呈現並帶細膩呼吸
- **hero-main.webp**：原賽博霓虹主視覺（純黑橙紫 ∞）已自首頁移除，保留於 `assets/` 供日後備用，未再引用
- **bg-main.webp**：木質鋼琴與躲在琴鍵後的奶牛貓，呼應內容中的音樂與療癒主題
- **22 張案例卡**（1024×1024）：直接取自官方內容站點卡片圖，涵蓋編鐘、藝廊、寵物、房地產、占星、虛擬試衣、Infucoco 奇幻等主題
- **favicon.svg**：∞ 符號 + 香檳金漸變，內嵌於頁面
- 網站動畫提示詞與影片：本專案以靜態官網為主；如需動畫/CF，另行產出後補記於本 README

## 七、報價說明（誠實聲明）

`pricing.html` 中價格標示為「參考價，專案估價」，為合理市場參考區間（NT$38,000 / 88,000 / 168,000 起），並於頁面註明**實際以正式估價單為準**、價格含稅與付款方式於估價單載明。正式對外前請以實際報價更新為準。

## 八、已知限制

- `contact.html` 表單為前端展示，送出後以 `mailto:` 開啟寄件視窗；正式上線需串接後端收件或表單服務
- 案例中標示「會員制規劃中」的站點連結暫指向 `index.html`，上線後請更新為正式網址
- Email 預設 `hello@9return.com.tw`，請依實際信箱更新
