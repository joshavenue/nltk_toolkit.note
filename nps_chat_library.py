import nltk
from nltk.corpus import nps_chat

chatroom = nps_chat.posts('10-19-20s_706posts.xml')

print(len(chatroom))

x = [w for w in chatroom]

print(' '.join(x[20]))

print(x[20].count('clap'))

## For XML files, there will many lists within the files, unlike txt file, there is only one giant list.
## To find sentences, you have to know where the word lay within which index
