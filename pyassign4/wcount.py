
#!/usr/bin/env python3



"""wcount.py: count words from an Internet file.



__author__ = "Xiaxinyi"

__pkuid__  = "1700017788"

__email__  = "1700017788@pku.edu.cn"

"""



import sys

import string

from urllib.request import urlopen

from urllib import error





def wcount(lines, topn=10):

    """

    count words from lines of text string, then sort by their counts

    in reverse order, output the topn (word count), each in one line.

    :param lines:text from the page

    :param topn: top n string to be print

    :return: a dict of the string and their number

    """

    original_l=lines.split()

    l=[]     #生成小写单词

    for i in original_l:

        l.append(i.lower())

    countdict={}    #储存单词和单词出现的数量

    for i in l:

        #用maketrans去掉标点

        intab = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

        outtab = ' ' * 32

        transtab = str.maketrans(intab, outtab)

        i = i.translate(transtab).strip()

        #判断是不是单词，并生成单词出现数量

        if i.isalpha():

            if i in countdict.keys():

                countdict[i]=countdict[i]+1

            else:

                countdict[i]=1

    lst=[]  #生成单词与单词数量的一一对应，以便对单词出现数量进行排序

    for k,v in countdict.items():

        lst.append((v,k))

        lst.sort(reverse=True)

    ans=''

    for i in range(topn):

        ans=ans+ str(lst[i][0])+"  "+str(lst[i][1])+"\n"

    return ans





def retrieve_page(url):

    """

    retrieve the page

    :param url: the url of the page to be process

    :return: the data of the page

    """

    try:

        with urlopen(url) as my_socket:  #打开网页，输出数据

            data=my_socket.read().decode()

            return data

    except error.HTTPError as he:        #HTTPError输出

        print(he.reason)

    except error.URLError as ue:         #URLError输出

        print(ue.reason)

    except Exception as e:               #其他错误输出

        print(e)





if __name__ == '__main__':

    """main model

    """

    # wrong format input

    if len(sys.argv) == 1 or len(sys.argv) >= 4:

        print('Usage: {} url [topn]'.format(sys.argv[0]))

        print('  url: URL of the txt file to analyze ')

        print('  topn: how many (words count) to output. If not given, will output top 10 words')

        sys.exit(1)

    # correct format input

    elif len(sys.argv)==3:                      #输入3个字符，即输入topn时

        web=str(sys.argv[1])

        jstr=retrieve_page(web)

        number=int(sys.argv[2])

        print(wcount(jstr,number))

    else:                                       #输入两个字符，topn默认为10

        web = str(sys.argv[1])

        jstr = retrieve_page(web)

        print(wcount(jstr))
