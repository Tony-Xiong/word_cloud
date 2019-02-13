# coding: utf-8
import jieba
from wordcloud import WordCloud,STOPWORDS
from scipy.misc import imread # 处理图像的函数
import matplotlib.pyplot as plt

# 读取文本文件
text = open('words.txt', 'rb').read()
# 对文本进行分词
cut_text = ''.join(jieba.cut(text))
# 读取图片
color_mask = imread('bg.jpg')
# 生成词云
cloud = WordCloud(font_path='msyh.ttc',# 这里是导入字体，因为我是采用英文的，所有不导入也并不影响，若是中文的或者有其他的字符需要自己选择合适的字体包
                  background_color="white",
                  mask=color_mask,
                  max_words=2000,
                  max_font_size=80)
word_cloud = cloud.generate(cut_text)

# 输出图片
plt.axis('off')
plt.imshow(word_cloud)
plt.show()