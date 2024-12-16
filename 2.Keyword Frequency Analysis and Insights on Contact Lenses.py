# -*- coding: utf-8 -*-
"""
關鍵字分析
此程式主要透過資料清理、中文分詞和關鍵字提取等技術，分析留言中的常見詞彙和關鍵內容。
"""

import jieba
import jieba.analyse
import pandas as pd
import re

# --- 定義停用詞功能 ---
def load_stopwords(filepath='chinese.txt'):
    """讀取停用詞列表"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            stopwords = set(f.read().splitlines())
        return stopwords
    except FileNotFoundError:
        print(f"未找到停用詞檔案：{filepath}，將使用預設停用詞清單")
        return set(['的', '了', '在', '是', '有', '也', '就', '和', '不', '很', '會', '但', '都', '還', '我', '你', '他'])

# 載入停用詞
stopwords = load_stopwords()

# 讀取資料集
getdata = pd.read_csv('ptt資料.csv', encoding='utf-8-sig')
print(getdata.columns)  # 顯示資料欄位名稱，確認結構

# 篩選包含 '隱形眼鏡','隱眼' 的標題或內文
get_shirt_data = getdata[
    getdata['標題'].str.contains('隱形眼鏡|隱眼', na=False) |
    getdata['內文'].str.contains('隱形眼鏡|隱眼', na=False) |
    getdata['所有留言'].str.contains('隱形眼鏡|隱眼', na=False)
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

# --- 停用詞過濾 ---
def remove_stopwords(text, stopwords):
    """移除停用詞"""
    words = jieba.cut(text)
    return [word for word in words if word not in stopwords and word.strip()]

# 移除停用詞的文本
filtered_words = remove_stopwords(allstr, stopwords)
filtered_text = ' '.join(filtered_words)

# --- TF-IDF 提取關鍵字 ---
keywords_top = jieba.analyse.extract_tags(
    filtered_text,  # 使用移除停用詞的文本
    topK=100,  # 提取的關鍵字數量
    withWeight=True  # 是否輸出關鍵字的權重分數
)
print("關鍵詞（TF-IDF）前 100 名：")
for word, weight in keywords_top:
    print(f"{word}: {weight}")

# --- 土法煉鋼：詞頻統計 ---
df_words = pd.DataFrame(filtered_words, columns=['關鍵詞語'])  # 轉換為 DataFrame
df_value_counts = df_words['關鍵詞語'].value_counts()  # 統計每個詞語的出現次數

# 將統計結果轉換為 DataFrame 並重命名欄位
df_result = df_value_counts.reset_index()
df_result.columns = ['關鍵詞語', '出現次數']

# --- 輸出處理後的數據 ---
df_result.to_csv('關鍵詞詞頻分析.csv', encoding='utf-8-sig', index=False)
print("關鍵詞詞頻分析結果已儲存至 '關鍵詞詞頻分析.csv'。")
