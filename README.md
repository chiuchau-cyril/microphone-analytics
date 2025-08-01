# 麥克風頻譜分析器

一個用於分析和視覺化麥克風音頻數據的網頁應用程式。支援即時頻譜顯示、瀑布圖視覺化和歷史數據分析。

## 主要功能

### spectrum-analyzer-improved.html - 頻譜瀑布圖分析器（推薦）
- 📊 **即時頻譜顯示** - 查看當前選中的頻譜數據
- 📈 **平均頻譜分析** - 計算並顯示所有頻譜的平均值
- 🌊 **頻譜瀑布圖** - 視覺化頻譜隨時間的變化
- 🎮 **互動式控制** - 使用滑動條選擇特定頻譜，支援播放動畫
- 📍 **Hover 顯示** - 滑鼠移到圖表上顯示精確的頻率和振幅值
- 📁 **自動載入** - 自動載入 `teraterm.csv` 檔案

### 其他工具

#### spectrum-analyzer.html - 基礎頻譜分析器
- 頻譜幀導航
- 動畫播放功能
- 峰值頻率檢測

#### spectrum-waterfall.html - 瀑布圖專用視覺化
- 專注於瀑布圖顯示
- 支援大量頻譜數據

#### realtime-audio-monitor.html - 即時音頻監測器
- 即時波形顯示
- 適合監測連續數據流

## 使用方法

### 方法一：使用本地伺服器（推薦）

1. 在終端機中執行：
   ```bash
   python3 server.py
   ```

2. 在瀏覽器中打開：
   ```
   http://localhost:8000
   ```

3. 點擊任一 HTML 檔案即可使用

### 方法二：直接開啟檔案

1. 直接在瀏覽器中開啟任一 HTML 檔案
2. 手動點擊「載入 CSV 檔案」按鈕選擇 teraterm.csv

## CSV 數據格式

### 頻譜分析器格式
支援的 CSV 格式用於頻譜數據（0-2047 Hz）：
- 格式 1: `序號→頻率,振幅`
- 格式 2: `頻率,振幅`

系統會自動檢測頻率從大跳到小的情況（例如從 2047 跳到 0），將其識別為新的頻譜數據。

### 音頻波形格式
用於波形顯示的格式：
```
1→858560
2→1249,-2109440
3→1250,-2106400
...
```
- 每行格式：`行號→索引,音頻值`
- 音頻值是第二個數字（逗號後面的值）

## 功能說明

### 互動操作
- **滑鼠滾輪**：縮放波形
- **拖曳**：平移視圖
- **按鈕控制**：重置縮放、切換顯示模式等

### 數據分析
- 峰值檢測
- 平均值計算
- RMS（均方根）值
- 動態範圍（dB）

## 系統需求

- 現代瀏覽器（Chrome、Firefox、Safari、Edge）
- Python 3（如果使用本地伺服器）

## 疑難排解

如果遇到「CORS」錯誤：
1. 使用提供的 `server.py` 啟動本地伺服器
2. 或者手動選擇 CSV 檔案而不依賴自動載入

如果圖表無法顯示：
1. 檢查 CSV 檔案格式是否正確
2. 在瀏覽器控制台查看錯誤訊息
3. 確保數據中有有效的數值

## 部署到 Vercel

1. Fork 此專案到你的 GitHub
2. 在 [Vercel](https://vercel.com) 中導入此專案
3. 選擇要部署的分支（通常是 main）
4. 部署設定使用預設值即可
5. 部署完成後即可通過 Vercel 提供的 URL 訪問

### Vercel 配置建議
- 框架預設：Other
- 構建命令：留空（純靜態網站）
- 輸出目錄：留空（使用根目錄）

## 技術棧

- HTML5/CSS3
- JavaScript (ES6+)
- Chart.js - 圖表視覺化庫
- Python - 本地開發伺服器

## License

MIT License