# 词云图
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud
from os import path
localpath=path.dirname(__file__)  #获取当前工作路径
#获取文件，注意这里要看编码格式
text = open(localpath+r'/cd.txt','r',encoding='UTF-8').read()
#剪切单词
text_cut=jieba.cut(text)
#单词拼接
result=' '.join(text_cut)

#生成次云图
wc = WordCloud(
    #字体路径
    font_path=localpath+ r'/simhei.ttf',
    #背景颜色
    background_color='white',
    #图片宽度
    width=500,
    height=350,
    #字体的大小
    max_font_size=50,
    min_font_size=10,
)
#生成词云图片
wc.generate(result)
plt.imshow(wc)
plt.axis('off')
plt.show()
