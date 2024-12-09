# -*- coding: utf-8 -*-
"""
消費者關鍵字分析
此程式主要透過資料清理、中文分詞和關鍵字提取等技術，分析消費者留言中的常見詞彙和關鍵內容。
"""

import jieba
import jieba.analyse
import pandas as pd
import re

# 讀取資料集
getdata = pd.read_csv('ptt資料.csv', encoding='utf-8-sig')
print(getdata.columns)  # 顯示資料欄位名稱，確認結構

# 篩選包含 '隱形眼鏡','隱眼' 的標題或內文
get_shirt_data = getdata[
    getdata['標題'].str.contains('隱形眼鏡', '隱眼', na=False) |
    getdata['內文'].str.contains('隱形眼鏡', '隱眼', na=False) |
    getdata['所有留言'].str.contains('隱形眼鏡', '隱眼', na=False)
]

# 填補空值，避免 NaN 引起的錯誤
get_shirt_data['標題'] = get_shirt_data['標題'].fillna('')
get_shirt_data['內文'] = get_shirt_data['內文'].fillna('')
get_shirt_data['所有留言'] = get_shirt_data['所有留言'].fillna('')

# 合併所有相關文本內容為單一字符串
all_text = get_shirt_data['標題'].sum() + get_shirt_data['內文'].sum() + get_shirt_data['所有留言'].sum()

# 取代/移除無意義字元
replaceList = [
    'span', 'https', 'com', 'imgur', 'class', 'jpg', 'f6', 'href', 'rel',
    'nofollow', '.', 'target', 'blank', 'hl', 'www', 'cc', 'tw', 'XD', 'f3',
    'f2', 'reurl', 'Re', 'http', 'amp', 'content', 'type', 'user', 'ipdate',
    '[', ']', '{', '}', '(', ')', '"', "'", '/', '\n', ',', '！', '？', '～',
    '…', '★', '＠', 'QQ', '&', '→', '+', '，', '的', '=', '>', '<', '：', '我',
    ':', '是', '了', '有', '。', '也', '就', 'a', '後', '都', '在', '很', '、', '不',
    '會', '但', '可以', '做', '說', '_', 'noopener', 'noreferrer', '-', '1', '(', ')', '2', '?', '!', '3', ' '
]

# 將資料中的無意義字元進行替換
allstr = ''.join(getdata['內文'].fillna(''))  # 合併所有留言的內文，處理 NaN 值為空字串
for i in replaceList:
    allstr = allstr.replace(i, '')  # 遍歷替換字元

# --- TF-IDF 提取關鍵字 ---
# 使用 TF-IDF 演算法，提取出重要的關鍵詞
keywords_top = jieba.analyse.extract_tags(
    allstr,  # 要分析的文本
    topK=100,  # 提取的關鍵字數量
    withWeight=True  # 是否輸出關鍵字的權重分數
)
print("關鍵詞（TF-IDF）前 100 名：")
for word, weight in keywords_top:
    print(f"{word}: {weight}")

# --- 土法煉鋼：詞頻統計 ---
# 使用 jieba 進行中文分詞，統計詞頻
words = jieba.cut(allstr)  # 分詞操作
df_words = pd.DataFrame(list(words), columns=['關鍵詞語'])  # 轉換為 DataFrame
df_value_counts = df_words['關鍵詞語'].value_counts()  # 統計每個詞語的出現次數

# 將統計結果轉換為 DataFrame 並重命名欄位
df_result = df_value_counts.reset_index()
df_result.columns = ['關鍵詞語', '出現次數']

# --- 輸出處理後的數據 ---
# 保存詞頻分析結果到 CSV 檔案
df_result.to_csv('關鍵詞詞頻分析.csv', encoding='utf-8-sig', index=False)
print("關鍵詞詞頻分析結果已儲存至 '關鍵詞詞頻分析.csv'。")
