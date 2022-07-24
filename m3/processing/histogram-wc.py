from wordcloud import WordCloud
from matplotlib import pyplot as plt

import pandas as pd


from collections import Counter
import json
import re

tweets = json.loads(open('../../dataset/lbiden.json').read())
stopwords = [x.replace("'", '') for x in open('stopwords').read().split()]

cleaner_reg = r"[^\w\s\-]+"

for i in range(len(tweets)):
	tweet = re.sub(cleaner_reg, '', tweets[i].lower())
	tweet = ' '.join([x for x in tweet.split() if x not in stopwords])
	tweets[i] = tweet


# tweets to words

vocabag = [x for i in tweets for x in i.split()]

bow = Counter(vocabag)

# print(bow.most_common(50))
# ////// wordcloud
# bow2text = ' '.join(vocabag)

# cloud = WordCloud().generate(bow2text)

# plt.imshow(cloud, interpolation='bilinear')
# plt.axis('off')
# plt.title('election')
# plt.show()


# /////// Histogram


d = pd.DataFrame(bow.most_common(150), columns=('words', 'frequency'))

figure, axis = plt.subplots(figsize=(25,25))

d.sort_values(by='frequency').plot.barh(x='words', y='frequency', ax=axis, color='black')

plt.show()