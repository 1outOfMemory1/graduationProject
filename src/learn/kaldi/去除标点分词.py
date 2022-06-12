import re
# pip install zhon

import jieba
from zhon.hanzi import punctuation


# print(punctuation)
a = "今天天气不错，要不要出去玩玩。"
a = re.sub('[%s]+' % punctuation, "", a) # 完成去除标点

words = jieba.lcut(a)
print(words)