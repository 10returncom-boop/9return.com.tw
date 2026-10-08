# 9return.com.tw 欣矩陣 ∞ 欣媒體 — 完整規格書 ＆ 變數表

> 用途：作為全站樣式、主題、元件、響應式與導覽的唯一參考依據，方便直接修改。
> 目錄：`D:\_WWW_325_public\9return.com.tw`　線上：`https://9return.com.tw/`
> 品牌：欣矩陣 ∞ 欣媒體　Slogan：沒有做不到，只有想不到　最後更新：2026-10-04

---

## 1. 專案概覽

- **性質**：跨產業垂直內容站點 × SEO／AEO／GEO 數位行銷整合平台（商業形象站）。
- **技術**：純靜態 HTML + 4 支 CSS（base／layout／components／pages）+ JS，無後端。
- **字型**：Noto Serif TC（標題襯線）＋ Noto Sans TC（內文），經 feishu CDN 載入。
- **全站風格基調**：預設「典雅墨色 × 香檳金」深色主題；咖啡棕按鈕、香檳金強調、墨綠點綴。
- **聯絡**：張書欣　Tel +886-968-222201　Line：331.today。

---

## 2. 檔案／目錄結構

```
9return.com.tw/
├── index.html        首頁（9return.com.tw/）
├── services.html     服務項目總覽（含 #sites/#seo/#marketing/#update 錨點）
├── pricing.html      報價方案
├── cases.html        成功案例（含篩選）
├── seo.html          SEO·AEO·GEO 知識頁
├── about.html        關於我們
├── contact.html      聯絡我們
├── css/base.css        色彩 token（:root ＋ [data-theme=light]）、reset、字型、clamp
├── css/layout.css      header／導覽／drawer／麵包屑／hero／footer
├── css/components.css  按鈕／卡片／時間軸／報價／表格／FAQ／表單
├── css/pages.css       各頁專用微調（含內頁標題咖啡底白字）
└── assets/           hero-elegant.webp、bg-wall.webp、favicon.svg 等
```

---

## 3. 主題機制總表（重要）

| 頁面 | 主題機制 | 預設 | 切換方式 | 變數所在 |
|---|---|---|---|---|
| 全站 7 頁 | `data-theme="dark"`／`"light"` 雙主題 | **深色**（`<html data-theme="dark">`） | header `#themeToggle` 按鈕 `onclick="window.Theme.toggle()"` 切 html 上的 data-theme | `:root`（深色）＋ `[data-theme="light"]`（淺色覆寫） |

> 說明：`:root` 為深色（`color-scheme:dark`）；`[data-theme="light"]` 整組覆寫為象牙米白。切換鈕在 `.header-actions`，日／月圖示由 CSS 互換（`.icon-sun`／`.icon-moon`）。`<meta name="color-scheme" content="dark light">`。

---

## 4. 全站變數表（CSS Custom Properties）

變數集中在 `css/base.css`。

### 4.1 深色 `:root`（預設，典雅墨色 × 香檳金）

| 變數 | 值 | 用途 |
|---|---|---|
| `--bg-0` | `#14120E` | 頁面底（深墨） |
| `--bg-1` | `#1C1915` | 提升面／header 毛玻璃底 |
| `--bg-2` | `#241F18` | 卡片面 |
| `--bg-3` | `#2C2620` | hover 面 |
| `--ink` | `#F3EDE0` | 主文字（暖米白） |
| `--ink-dim` | `#B7AB96` | 次要文字 |
| `--ink-faint` | `#857A65` | 弱提示 |
| `--line` | `rgba(243,237,224,.13)` | 邊框線 |
| `--line-strong` | `rgba(243,237,224,.26)` | 強邊框 |
| `--warm` | `#D4B064` | 香檳金（強調） |
| `--warm-bright` | `#E2C277` | 亮金 |
| `--coffee` | `#6F4A2E` | 咖啡（按鈕統一底色） |
| `--coffee-2` | `#8A5E3A` | 咖啡亮 |
| `--cool` | `#7FAF9E` | 墨綠 |
| `--cool-bright` | `#9CC7B6` | 亮墨綠 |
| `--ok-warm` | `rgba(212,176,100,.13)` | 金淺底 |
| `--ok-cool` | `rgba(127,175,158,.15)` | 綠淺底 |
| `--ok-warm-2` | `rgba(226,194,119,.09)` | 金更淺 |
| `--ok-cool-2` | `rgba(156,199,182,.09)` | 綠更淺 |
| `--shadow` | `0 28px 70px -30px rgba(0,0,0,.62)` | 陰影 |
| `--header-bg` | `rgba(20,18,14,.78)` | header 底（毛玻璃） |
| `--bg-veil` | `rgba(20,18,14,.94)` | 背景圖罩紗 |

### 4.2 淺色 `[data-theme="light"]`（象牙米白覆寫）

| 變數 | 值 | | 變數 | 值 |
|---|---|---|---|---|
| `--bg-0` | `#F5EFE3` | | `--warm` | `#A17B35` |
| `--bg-1` | `#FAF5EA` | | `--warm-bright` | `#B58F45` |
| `--bg-2` | `#FFFFFF` | | `--coffee` | `#6F4A2E` |
| `--bg-3` | `#EDE5D3` | | `--coffee-2` | `#8A5E3A` |
| `--ink` | `#2B251A` | | `--cool` | `#2F6356` |
| `--ink-dim` | `#6E6452` | | `--cool-bright` | `#3B7A6B` |
| `--ink-faint` | `#9B907A` | | `--shadow` | `0 26px 64px -32px rgba(90,70,40,.34)` |

> 淺色另覆寫 `--line`（rgba(43,37,26,.13)）、`--line-strong`、`--ok-*`、`--header-bg`（rgba(245,239,227,.86)）、`--bg-veil`（rgba(245,239,227,.92)）。咖啡棕 `--coffee/--coffee-2` 深淺兩主題相同。

---

## 5. 元件規格

### 5.1 按鈕 `.btn`
- 膠囊 `border-radius:999px`、padding `.78rem 1.5rem`。
- `.btn-primary`：`linear-gradient(135deg,var(--coffee-2),var(--coffee))` 白字；hover 上移＋提亮。
- `.btn-line`：咖啡底白邊；`.btn-sm` 縮小。Header CTA `.btn-cta` 同咖啡漸層。

### 5.2 Header 與導覽
- `.site-header`：sticky、`backdrop-filter:blur(14px)`、底 `--header-bg`。
- `.nav-main` 桌面導覽 `min-width:900px` 才顯示；手機用 `.drawer` 右側抽屜。
- `#themeToggle`：切換深／淺主題。

### 5.3 卡片／案例／服務支柱
- `.card`：`bg-1`、圓角 18、hover 上浮＋陰影。
- `.case-card`：案例卡，`.case-thumb` 4:3 圖＋標籤；`.chip.hot` 金色。
- `.pillar`：服務支柱卡，`.ico` 金色漸層方塊。

### 5.4 時間軸／報價／表格／FAQ
- `.timeline`：grid 三欄（節點 90px／軸 22px／內容），金色節點＋漸層軸。
- `.price-card`：報價卡；`.featured` 金色漸層邊框＋「最受歡迎」徽章；`min-width:880px` 三欄。
- `table.compare`：對照表，`.yes` 金、`.no` 灰。
- `.faq-item`：手風格展開。

### 5.5 Hero
- `.hero`：背景 `assets/hero-elegant.webp` cover；`.hero-brand` 咖啡底白字膠囊（含漣漪逐字動畫）。
- 內頁 `.page-hero h1`、`.section-head h2`：咖啡漸層底白字膠囊（pages.css 統一易讀性）。

### 5.6 Footer
- `.site-footer`：`bg-1`；`min-width:860px` 四欄 grid；`.to-top` 右下角金色圓鈕。

---

## 6. 響應式／手機規格（斷點總表）

| 斷點 | 規則 |
|---|---|
| `min-width:900px` | `.nav-main` 桌面導覽顯示；`.grid.cols-3/cols-4` 3／4 欄 |
| `min-width:880px` | `.pricing-grid` 報價三欄 |
| `min-width:860px` | `.split` 兩欄；`.footer-top` 四欄；`.def-grid` 三欄 |
| `min-width:720px` | `.clamp`／`.clamp-narrow` 容器左右留白加大 |
| `min-width:640px` | `.stat-grid` 四欄；`.form-grid.two` 兩欄；`.grid.cols-2/cols-4` 兩欄 |
| `max-width:600px` | `.tl-row` 時間軸欄位縮為 66px 16px 1fr |

---

## 7. 導覽／連結規格

- 每頁 `canonical`／`og:url` 指向 `https://9return.com.tw/<頁>`。
- 主選單：首頁／服務項目／報價方案／成功案例（下拉）／SEO·AEO·GEO／關於我們／聯絡我們。
- 成功案例下拉連結大量指向站外子站（`9return.com.tw/zeng-hou-yi-bells/`、`331.today`、`zootecture.com`、`petlogic.org` 等）。
- 全站選單也提供 header popover `.menu-popover`（手機 drawer）。

---

## 8. 修改指引（速查）

- **改主色**：動 `:root`（深色）與 `[data-theme="light"]`（淺色）對應變數；按鈕主色看 `--coffee/--coffee-2`，強調看 `--warm/--warm-bright`。
- **改按鈕**：`.btn-primary`／`.btn-cta` 用 `--coffee` 漸層。
- **改背景**：body 疊 `assets/bg-wall.webp`＋`--bg-veil` 罩紗；hero 用 `assets/hero-elegant.webp`。
- **改斷點**：第 6 節各 `@media`。

---

## 9. 已知事項／待決

- 成功案例下拉內多個連結仍指向 `9return.com.tw/index.html` 佔位（未接上真實子站）。
- 字型經第三方 CDN（miaoda.feishu.cn）載入，離線或 CDN 異時會 fallback 系統字型。
