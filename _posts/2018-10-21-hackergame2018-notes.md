---
layout: post
title: Hackergame2018 笔记
subtitle: 菊苣们玩梗和卖萌能力真的是绝了…
author: Coink
date: 2018-10-21
---


比赛题目的难度呈梯度上升，对于后面的题有些无从下手，我参考[官方wp ](https://github.com/ustclug/hackergame2018-writeups)以及其中提到的选手解题过程，在[题目存档](https://hack2018.lug.ustc.edu.cn/) 中继续解题并且记录在这里。持续更新中...

这次比赛之后，深感与菊苣们之间的基础知识差距，希望自己能多向菊苣们学习，不要再整天摸鱼了...



## 签到题

> 不用找了！签到题我已经放这里了！

前端修改maxlength，或改掉GET请求的参数

**flag{Hackergame2018_Have_Fun!}**



## 猫咪问答

> **铲屎官：**要铲屎吗？**@猫咪**
>
> **猫咪：**我是你直接@的？你这是在叫主子？我不想看见第二次。
>
> **猫咪：**喵的心里没点数？
>
> **一只路过的狗：**请各位铲屎官注意自己的身份和说话方式。**@全体成员**
>
> 为了不被骂，铲屎官再也不敢问任何问题了，下面这些简单的问题，也只能你自己来搜索解决。

回答5个问题

1. 中国科学技术大学的建校年份是？

   google得1958

2. 你研究过中国科大学号的演变史吗？现有一位 1992 年入学的博士生，系别为 11 系，学生编号为 26，请问 Ta 的学号是？

   google“中科大学号演变”

   [中国科大的学号演变史](http://aga.ustc.edu.cn/site/ustc_xyh/xyh/cnt/?id=18185)

   ![zkdbs.png](https://i.loli.net/2018/10/10/5bbdbced5a25d.png)

   推出9211B026

3. 视频《诺贝尔奖获得者和杰出科学家祝福科大60华诞》中，出现了多少位诺贝尔奖得主和世界顶尖科学家为中国科大六十周年华诞送上祝福？（数字）

   看视频，数数，一共9位

4. 在中国科大图书馆中，有一本书叫做《程序员的自我修养:链接、装载与库》，请问它的索书号是？

   中科大图书馆，查找图书得TP311.1/94

5. 我校 Linux 用户协会在大约三年前曾经举办过一次小聚，其主题是《白帽子大赛，黑客不神秘》，请问这次小聚使用的教室编号是？

   直接google“白帽子大赛，黑客不神秘”，会得到这次小聚的[演示文稿](http://home.ustc.edu.cn/~boj/whitehat/#/) ，但是翻遍了也没找到聚会地点，后来想到去 Linux 用户协会查找通知，得到3A202

   ![lug.png](https://i.loli.net/2018/10/10/5bbdbcb97ff3f.png)

**flag{G00G1E-is-always-YOUR-FRIEND}**



## 游园会的集章卡片

> 提示：flag 仅由 `0154agflPYHMGRCNE_{}` 这些字符组成。
>
> 我们经常被问一个问题：你们是从什么时候开始为 Hackergame 出题的？
>
> 其实我们全年都在出题，命题组成员来自各种各样的专业，在各种各样的地方，有各种各样不同的工作，闲暇之余~~（或者工作不饱和的时候，这个最好删掉）~~我们最大的乐趣就是互相出题给对方玩。
>
> 为了找到有趣的题目，我们需要源源不断的灵感，不管是在巴蜀人家二楼包厢 LUD（[注 1](https://lug.ustc.edu.cn/wiki/lug/events/start?s%5B%5D=lud)） 时，还是在北京食宝街的分米鸡，甚至是在武汉开往合肥的 D2256 列车上，我们会把讨论到的有趣的想法记录下来，作为下一次 Hackergame 的题目。
>
> 比如前几天，中国科学技术大学学生 Linux 用户协会在中区游园会摆摊招新（[注 2](https://lug.ustc.edu.cn/wiki/lug/contribute)），发现学校居然为每个参加游园会的同学准备了一张精美的集章卡片：
>
> ![card.jpg](https://i.loli.net/2018/10/15/5bc42ac6d8dbc.jpg)
>
> 到每个社团的摊位上收集盖章，到达一定数量就有礼品赠送。
>
> 突然一位同学灵机一动，不如写上 flag 然后撕碎！
>
> 附件就是撕碎的 flag，相信对中国科学技术大学校徽了如指掌的你很快就能将它还原。

拼图即可（物理）

思考了两节毛概课怎么做通用脚本拼图，后来在@[ProfFan](https://github.com/ustclug/hackergame2018-writeups/blob/master/players/ProfFan/README.md) 的答案中看到了 https://github.com/biswajitsc/jigsaw-solver，顿时感觉自己想得太简单了...

周末仔细研究一下他用的算法

**flag{H4PPY_1M4GE_PR0CE551NG}**



## 猫咪和键盘

> 谨以此题，献给所有被猫破坏的代码。
>
> 众所周知，猫咪最喜欢钻纸箱和趴键盘，其中钻纸箱没有太大的社会危害性，而趴键盘则是对人类的毁灭性打击。
>
> （想象一下这里配了猫钻纸箱和趴键盘的图）
>
> 写到一半的代码离奇消失，仅剩的代码也被搞得乱七八糟，愤怒的 D 同学刚要捉住罪魁祸首，准备好好揍它一顿，不料这时猫咪又突w13gcft4n kj87u6,/lp0o9--=l[



代码有明显的**竖直断层**，根据c++语法拼接即可，要注意文件下方代码较长，不过好在出题人在其他地方填充了空格。

相信现在不会还有人写代码使用非等宽字体了吧（

sublime和VSCode均可使用按下鼠标滚轮选择代码块，也有其他快捷键，例如mac下VSCode可以使用Shift+Option再选择。



![fix.png](https://i.loli.net/2018/10/13/5bc1a6da4cd8e.png)

​                                                                                                                      

拼好后（url是一篇关于C++实现类型安全的printf，也就是本题主体代码）：



```c++
/*      
 * name: typed_printf.cpp    
 * compile: g++ -std=c++17 typed_printf.cpp
 * title: type safe printf   
 * author: nicekingwei
 * url: aHR0cHM6Ly96anUtbGFtYmRhLnRlY2gvY3BwZHQtcHJpbnRmLw==    
 * related knowledge: 
 *  - value and type  
 *      value->value: function      
 *      type->value: parametric polymorphism      
 *      type->type: generic  
 *      value->type: dependent type 
 *  - auto     
 *  - if constexpr    
 */     
#include <iostream>   
#include <functional> 
#include <type_traits>
 
using namespace std;  
 
template<const char*format>  
static auto println() {      
    if constexpr (format[0]=='%') { 
 if constexpr (format[1]=='d') {    
     return [](int x){cout<<x<<endl;};     
 } else if constexpr (format[1]=='s') {    
     return [](const char* x){cout<<x<<endl;};    
 } else {      
     return "error";  
 }      
    } else {   
 return "error";      
    }   
}
 
struct unit_t {char x;};     
 
template<typename T,typename R>     
constexpr auto get_arg(R (*f)(T)){  
    return T{};
}
 
template<typename T>  
constexpr bool cont_takes_no_arg(T cont){  
    using cont_t = decay_t<T>;      
    using arg_type = decay_t<decltype(get_arg(cont))>;   
    return is_same<unit_t,arg_type>::value;
}
 
 
template<typename T,typename R,typename X,R (*cont)(X)>  
auto print_var(T x){  
    cout<<x;   
    return cont;      
}
 
template<typename T,typename R,typename X,R (*cont)(void)>      
auto print_var(T x){  
    cout<<x;   
    return cont();    
}
 
template<char c,typename R,typename X,R (*cont)(X)>      
auto print_const(X x){
    cout<<c;   
    return cont(x);   
}
 
template<char c,typename R,typename X,R (*cont)(void)>   
auto print_const(){   
    cout<<c;   
    return cont();    
}
 
 
template<typename R,typename X>     
constexpr auto cont_ret_type(R (*cont)(X)){
    return R{};
}
 
template<typename R>  
constexpr auto cont_ret_type(R (*cont)()){ 
    return R{};
}
 
template<typename R,typename X>     
constexpr auto cont_arg_type(R (*cont)(X)){
    return X{};
}
 
template<typename R>  
constexpr auto cont_arg_type(R (*cont)()){ 
    return unit_t{};  
}
 
unit_t print_nothing(){return unit_t{};}   
 
#define cont_ret_t decay_t<decltype(cont_ret_type(cont))>
#define cont_arg_t decay_t<decltype(cont_arg_type(cont))>
 
template<const char*format,int i>   
constexpr auto _typed_printf(){     
    if constexpr (format[i]=='%' && format[i+1] == 'd') {
 constexpr auto cont = _typed_printf<format,i+2>();      
 return print_var<int,cont_ret_t,cont_arg_t,cont>;
    } else if constexpr (format[i]=='%' && format[i+1] == 's') {
 constexpr auto cont = _typed_printf<format,i+2>();      
 return print_var<const char*,cont_ret_t,cont_arg_t,cont>;      
    } else if constexpr (format[i]!='\0') {
 constexpr auto cont = _typed_printf<format,i+1>();      
 return print_const<format[i],cont_ret_t,cont_arg_t,cont>;      
    } else {   
 return print_nothing;
    }   
}
 
#define def_typed_printf(f,str) constexpr static const char str_fmt##f[] = str; auto f = _typed_printf<str_fmt##f,0>(); 
 
#define ABC "FfQ47if9Zxw9jXE68VtGA" 
#define BAC "JDk6Y6Xc88UrUtpK3iF8p" 
#define CAB "7BMs4y2gzdG8Ao2gv6aiJ" 
 
int main(){    
    def_typed_printf(f_l_x_g_1, "%s%s%s%s");      
    f_l_x_g_1("fl")("a")("g")("{"); 
    def_typed_printf(a_a_a_a_a_a_a_a_a, "%s%s%s%s%s%s%d");      
    a_a_a_a_a_a_a_a_a(ABC)("")(BAC)("")(CAB)("")('}');   
    def_typed_printf(def_typed_printf_, "%s%d%s");
    def_typed_printf_("typed_printf")('_')("}");  
    return 0;  
}
```

跑一下得到flag，对运行环境有要求，我是在 [wandbox.org](https://wandbox.org/)运行的。

**flag{FfQ47if9Zxw9jXE68VtGAJDk6Y6Xc88UrUtpK3iF8p7BMs4y2gzdG8Ao2gv6aiJ125typed_printf95}**





## Word 文档

> 自从加入了 Doki Doki Linux Club ([注1](https://dokidokilinux.club/)），用上了 Linux，D 同学每天都能学到好多新东西。
>
> Linux 好是好，就是没有 Microsoft Office 系列软件，导致看学校的各种通知文件，填申请表等等都变得不那么方便，上次还差点因此错过了 7 号的会议。
>
> 突然有一天 D 同学的一个朋友告诉他，其实新版 Office 的文件格式是公开的！
>
> D 同学非常高兴，公开的文件格式或许意味着可以自己写程序来读取和编辑内容，再也不用切换系统或者开虚拟机了。
>
> D 同学追问这个朋友：那么这个文件格式具体是怎么样的呢？
>
> 朋友传来一个 OfficeOpenXML.docx。



知道文档是压缩包形式就好办了。flag里一个字符占一行，去掉回车查看：

![openoffice.png](https://i.loli.net/2018/10/10/5bbdea4a98c50.png)

**flag{xlsx,pptx,docx_are_just_zip_files}**



## 猫咪银行

> 这也是猫咪占领世界的计划之一，通过开设猫咪银行出售 flag 来学习人类割韭菜的技巧。

给了三种货币可以互相转化，我们看到CTB有10个，但是需要20个CTB才能获得flag，首先想到了条件竞争，拿burp尝试一下，然后发现自己没买burp，社区版不提供多线程功能，留下了贫穷的泪水...

一顿折腾发现无法条件竞争，干。

一个帐号只有十分钟的时效，就算是每分钟利滚利也不能达到翻倍，一定存在某种漏洞，猜测修改系统时间，看了下网页不是JS验证的时间，继续猜测是溢出，尝试了几个大数之后，得到负数年份，取出TDSU换取CTB购买flag即可。


**flag{Evil_Integer._Evil_Overflow.}**



彩蛋：CTB，RMX，TDSU的来源就是BTC，XMR和USTD。



## 黑曜石浏览器

> 请使用最新版黑曜石浏览器（HEICORE）打开。

heicore，看起来是在玩redcore的梗，看到浏览器想到修改User-Agent，抓包把Chrome改成HEICORE，不行，看来对版本号有要求。

搜索黑曜石浏览器，找到官网（后来看到别人吐槽百度搜不到，我跑去尝试了baidu，google，bing，duckduckgo，确实是只有baidu搜不到哈哈哈哈哈哈）

查看源码，结果网页崩溃了？？重试一下还是，嗷，原来是出题人挖的坑，直接view-source: 查看源码，没发现什么异常，多次刷新后发现官网是从index.html跳转到index.php的，查看index.html源码，比index.php多了一些槽点满满的JS：

```javascript
...

$("#download_link").click(function() {
    if (!window.loggedIn) {
        alert("仅差一步！请于登录后下载黑曜石浏览器。");
    } else {
        window.location.href="HEICORE.49.1.2623.213_installer_latest.exe";
    }
});

...

function isLatestHEICORE() {
	var ua = navigator.userAgent;
	var HEICORE_UA = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) HEICORE/49.1.2623.213 Safari/537.36";
	return ua === HEICORE_UA;
	
...
}
```

直接下载浏览器或修改UA，请求题目链接（非官网链接），得到flag

![heicore.png](https://i.loli.net/2018/10/10/5bbdec1598054.png)

这个版本号就是redcore用的Chrome版本号。

**flag{H3ic0re_49.1.2623.213_sai_kou}**



## 回到过去

> 那些发明Unix操作系统的大叔们怎么编辑文本文件呢？
>
> 据记载，他们使用一种叫做ed的神奇编辑器，而Unix Hater's Handbook对此有生动的描述：
>
> Ken Thompson has an automobile which he helped design. Unlike most automobiles, it has neither speedometer, nor gas gauge, nor any of the other numerous idiot lights which plague the modern driver. Rather, if the driver makes a mistake, a giant “?” lights up in the center of the dashboard. “The experienced driver,” says Thompson, “will usually know what’s wrong.”
>
> 也许是八十年代的某天，调皮的Lawrence正在使用他的DEC VT终端连接到一台大型Unix主机编辑文件——他是个机灵的家伙，使用ed的时候从不需要看屏幕的输出。只看他正在用ed写本题的flag。写了半天，兴高采烈的Lawrence接了个电话，关上ed才发现自己没有保存。
>
> 聪明的你能根据对他键盘的记录，还原出你要找的flag吗？
>
> **info ed** 命令对于没有使用过ed的你是十分有用的。
>
> Hint1：有多个字符串的话，就从上到下连成一行提交就好啦。
>
> Hint2：flag只接受数字和字母。



下载键盘历史，看一下

```bash
q
ed
a
flag{
.
a
44a2b8
a3d9b2

c44039
f93345
}
.
2m3
2m5
2m1
2
s/4/t
q
q
```

题目说是用ed编辑的，google学一下ed用法，用过vim的应该很好理解：

`a`(append), `i`(insert), `c`(change) 进入输入模式，符号点（.）从输入模式进入命令模式，d(delete)删除行，m(move)移动行，s替换，w保存，q退出。解析上面的键盘历史得到

**flag{t4a2b8c44039f93345a3d9b2}**

或者跟着命令敲一遍也行，释放键盘恢复（物理）魔法，当然要记得q之前w保存



## 我是谁

> 高中的时候，为了提高作文成绩，小 T 买了一本关于哲学的大众读物。虽然到最后，书确实是差不多看完了，但是并没有什么用。
>
> 在他看完这本书之后的某一天，小 T 做了一个梦，他梦见自己变成了一台服务器。作为阅读那本书的后遗症（之一），他不禁开始思考生命的本源之类乱七八糟的问题。到最后，他在纠结的，只有一件事情：
>
> 「我是谁？」

### 哲学思考

> 「我是谁？」
>
> 「我从哪里来？」
>
> 「将到哪里去？」
>
> 据说有这样三个有趣的哲学问题。
>
> 现在，请帮我回答第一个问题吧。
>
> Can you tell me **who I am**?

查看源代码，发现一条注释掉得main.js，访问发现。。404

尝试root，me，whoiam等各种口令无果，也没发现其他漏洞，故转向页面请求，观察network，发现Status Code为：

![sc.png](https://i.loli.net/2018/10/13/5bc2068113e0d.png)

输入TEAPOT，得到flag

**flag{i_canN0t_BReW_c0ffEE!}**

彩蛋：输入coffee看看...

> You said COFFEE? You sure?
>Maybe you should find someone else to brew coffee for you.

茶壶先生不高兴了 :(

### Can I help me?	

> Brewing tea is not so easy.
> Try using other *methods* to request this page.

抓包，尝试POST，得到提示

> The method "POST" is deprecated.
> See RFC-7168 for more information.

搜索RFC-716查看 Hyper Text Coffee Pot Control Protocol for Tea Efflux Appliances 
[THTCPCP-TEA](https://tools.ietf.org/html/rfc7168) 

采用BREW方法，提示

> Please check if there is anything missing in your header.

继续看文档，补全header（Content-Type: message/teapot），会返回茶的类型：

**昏  睡  红  茶**（划掉

```
Alternates: {"/the_super_great_hidden_url_for_brewing_tea/black_tea" {type message/teapot}}
```

继续请求，得到flag，给大佬递茶

**flag{delivering_tea_to_DaLa0}**


彩蛋：用WHEN方法（Hyper Text Coffee Pot Control Protocol中定义的）请求，会提示

> I'm NOT a coffee pot.
> Please, read RFC-7168, not RFC-2324.


## 家里有矿

> 提示：
>
> 1. 本题的浏览器“挖矿”只为演示性目的，几乎不占资源。我们不会以任何形式盗取或浪费大家电脑的算力。
>
> 2. 本题如果使用程序求解，对于普通配置的个人电脑，在解法正确且最优的情况下，求解程序的期望运行时间不会超过几分钟。
>
> Z 同学为了赶上区块链的热潮，自己潜心研究工作量证明（Proof of work）算法，并且发布了三种全新的电子货币。不仅如此，他还写了一个矿池。
>
> 给专业选手的注释：此题并非 web 题，解题过程不涉及注入、XSS、敏感文件泄露、弱类型等安全问题。

TODO

### sha1

### md5

### sha256



## 秘籍残篇

> >
> > Those who bear true belief in flxg shall fear no malbolge!
> >
> > -- La Divina FLXG Commedia
>
> FLXG 创始人 CWK 修为通玄, 万古罕有. 至今无敢直呼其名者, 皆以西文缩写代之.
>
> 据 *神 FLXG 曲* 载, CWK 为探 FLXG 之密, 曾 *排空驭气奔如电, 升天入地求之遍. 上穷碧落下尽黄泉, 两处茫茫而无可见.* 后其闭关九年, 又仗三尺长剑, 携一刀生宣, 闯 *但丁* 旧时幽路. 平荆棘, 暴霜露, 惊恶魑, 斩狱卒, 神鬼莫可当之.
>
> 每其行足七千里也, 元气化墨, 即为箧囊所藏, 凝之一字, 现诸纸上. 及至伊甸园, 经义已成十万八千字余矣. 当是时, 人间科技正高速发展, 上帝不得已, 将 2D 天空贴纸更为 3D, 故而旧道不通. CWK 举目四望, 但见群星闪烁. 扪参历井, 方知穷途将归.
>
> 归来后, 宣纸已自编纂成册, 即 *神 FLXG 曲* (曾藏于滑稽大学博物院, 现已佚失). 其中记载 CWK 种种经历此处且按下不提. 而 *Inferno: Malebolge* 一章, 以 [Malbolge](https://en.wikipedia.org/wiki/Malbolge) 语言书成. 虽晦涩难通, 所谓佶屈而聱牙, 然真义无穷, 实乃无上之道法.
>
> 江湖余此残篇, 而今公示于天下. 可否有所体悟, 且看诸君之造化.

### 滑稽Art

看到这样的缩进，开始以为是斐波那契缩进之类的东西，但是题目名里的Art让我想到了[ASCII Art](https://en.wikipedia.org/wiki/ASCII_art)，滑稽也肯定是图片才能表示，然而这玩意只有空格没有换行，没办法，只能自己补全换行（其实不补全直接缩放看也能看到一个歪歪扭扭的字符画）

看一下文本的信息，一共有154012个字符，最近正好在看RSA，就放到factordb里分解了一下，得到 2^2 · 139 · 277，常用等宽字体的宽高比一般为1:0.6，进行左右微调，最后发现这里用了1：0.5，最后每读556（2^2x139）个字符输出一个换行即可看到字符画。

```python
with open('./malbolge.txt', 'r') as f:
    while True:
        line = f.read(556)
        if not line:
            break
        with open('./huaJi.txt', 'a') as out:
            out.write(line + '\n')
```



![huaji.png](https://i.loli.net/2018/10/20/5bcaa89f88125.png)



flag在滑稽下面，flxg(废理兴工)也是个关于科大的梗，有兴趣可以搜一下。

**flxg{University_of_Ridiculous}**


### 天书易解

好难！TODO

## 猫咪遥控器

> **提示：flag 格式为 flag{......}，只包含字母，其中有且只有两个为大写字母。**
>
> 今天的 App Store 首页故事是《猫咪占领世界》([详情](https://itunes.apple.com/cn/story/id1435731237))。
>
> SERIOUSLY?
>
> D 同学不禁开始幻想被猫咪占领的世界：集中营里成群的铲屎官，密密麻麻的 Nepeta cataria（[Wikipedia](https://en.wikipedia.org/wiki/Catnip)）农田，随意摆放的纸箱子占满了道路……
>
> 想想就可怕，不过 D 同学知道人类还有终极秘密武器可以用——猫咪遥控器，有了猫咪遥控器，再多的猫咪也只会乖乖地听人类的话，哈哈哈哈哈～
>
> 下面是制作猫咪遥控器的技术总结，需要的原料有：
>
> - 5mW 6mm 点状激光二极管一个；
> - 锂电池一个；
> - 导线若干；
>
> 然后用导线将锂电池和激光二极管连接起来（这一步的目的是让二极管亮起来，不想二极管亮起来的同学可以不连），一个美味的猫咪遥控器就做好了。
>
> 猫咪遥控器的原理非常简单！撸猫学会曾经有论文给出过结论：[激光笔指向哪里，猫咪就会跑到哪里](https://ftp.ustclug.org/misc/cat_remote.mov)。
>
> 为了报复猫咪把自己的代码打乱（见：猫咪与键盘），D 同学把猫咪遥控器绑在可以上（UP）下（DOWN）左（LEFT）右（RIGHT）移动的三轴机械臂上，开始使用树莓派（一款基于 Linux 的单片机计算机）控制三轴机械臂，进而控制猫咪在草地上跑来跑去。
>
> 附件是树莓派上留下的调试输出信息，我们赶到现场时只剩下这个了。

给了一个seq.txt

```
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUUUUUUUUUUUULLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRLLLLLLLLLLLLLLLLLLLLLLLLRRRRDDDDDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRUUUUUUUULLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLUUUUUUUUUUUUUUUURRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUULLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRLLLLDDDDDDDDRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUUUUUUUUUUUUUULLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDUUUURRRRRRRRRRRRRRRRRRRRRRRRLLLLDDDDDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRRRRRRRRRRRRRLLLLUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUDDDDDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUUUUUURRRRRRRRLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDLLLLLLLLDDDDRRRRRRRRDDDDDDDDDDDDDDDDDDDDDDDDRRRRRRRRLLLLLLLLUUUUUUUUUUUUUUUUUUUUUUUULLLLLLLLUUUURRRRRRRRUUUURRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRDDDDRRRRDDDDRRRRDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUURRRRRRRRUUUUUUUURRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUUUUUURRRRRRRRRRRRUUUURRRRUUUURRRRRRRRRRRRRRRRDDDDRRRRDDDDRRRRDDDDDDDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLUUUURRRRUUUUDDDDLLLLDDDDDDDDRRRRDDDDRRRRDDDDRRRRRRRRRRRRUUUURRRRRRRRUUUUDDDDLLLLLLLLDDDDLLLLLLLLLLLLUUUULLLLUUUULLLLUUUUUUUURRRRUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUUUUUUUUUULLLLLLLLLLLLLLLLLLLLLLLLLLLLDDDDDDDDDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUURRRRRRRRUUUULLLLUUUUDDDDRRRRDDDDRRRRDDDDDDDDDDDDDDDDDDDDRRRRUUUUUUUUUUUURRRRUUUUUUUUDDDDDDDDRRRRDDDDDDDDDDDDRRRRUUUUUUUUUUUUUUUUUUUURRRRUUUURRRRUUUUDDDDLLLLDDDDRRRRRRRRRRRRUUUUUUUUUUUUUUUUDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUURRRRDDDDRRRRDDDDRRRRDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUURRRRUUUURRRRUUUURRRRDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUUUUUUDDDDUUUURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRLLLLLLLLLLLLLLLLUUUULLLLUUUULLLLLLLLDDDDLLLLDDDDLLLLDDDDDDDDDDDDRRRRDDDDRRRRDDDDRRRRRRRRUUUURRRRRRRRUUUUDDDDLLLLLLLLDDDDLLLLLLLLUUUULLLLUUUULLLLUUUUUUUURRRRRRRRRRRRRRRRRRRRRRRRUUUULLLLUUUUDDDDRRRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUUUUUULLLLLLLLLLLLLLLLLLLLDDDDDDDDUUUUUUUURRRRRRRRRRRRRRRRRRRRDDDDRRRRRRRRRRRRUUUULLLLUUUUDDDDRRRRDDDDRRRRDDDDDDDDDDDDDDDDDDDDRRRRUUUUUUUUUUUUUUUURRRRUUUUUUUUDDDDDDDDRRRRDDDDDDDDDDDDDDDDRRRRRRRRUUUUUUUUUUUUUUUURRRRUUUUUUUURRRRUUUUDDDDLLLLDDDDRRRRRRRRRRRRRRRRRRRRUUUUUUUUUUUUUUUULLLLLLLLRRRRRRRRDDDDDDDDDDDDDDDDDDDDRRRRRRRRDDDDLLLLLLLLDDDDDDDDDDDDDDDDDDDDLLLLLLLL

```

用matplotlib画图看看：

```python
#!/usr/bin/env python
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt 

map = "DDDDDDD..."

x = [0]
y = [0]

for path in map:
    if path is 'U':
        x.append(x[-1])
        y.append(y[-1]+1)
    elif path == "D":
        x.append(x[-1])
        y.append(y[-1]-1)
    elif path == "L":
        x.append(x[-1]-1)
        y.append(y[-1])
    elif path == "R":
        x.append(x[-1]+1)
        y.append(y[-1])

plt.plot(x,y)
plt.show()

```

![meow.png](https://i.loli.net/2018/10/13/5bc1a867e5cd8.png)



**flag{MeowMeow}**



## 她的诗

> 高中时候语文作文从未写满过 50 分的小 T，可能是脑子哪里抽了吧，考上大学之后竟然报名加入了学校的文学社。虽然小 T 写作真的很糟糕，但每周的作品分享会上，他还是坚持与他人一起分享创作，并且看上去……他似乎还是很开心的。
>
> 这一周，当小 T 还是像往常一样拿出自己的创作时，她走了过来，递给小 T 一张纸。这是她新写的诗吗？可为什么，纸上全是一些奇奇怪怪的字符？
>
> 「这是，什……什么东西啊？！」
>
> 她一言不发，只是在离开时，她回过头来，小声说道：
>
> 「我要提醒一下你，只纠结于字面意思是很费劲的，而且……你不会得到任何有用的结论。」
>
> ------
>
> 小 T 的友人，在听闻这件事情后，经过一段时间的分析，找到了这首诗的编码，并且帮他写了一个很短的程序来解码。只是……从解码出的内容来看，事情远没有他们想像得那么简单。
>
> 你能找到她想传达的真正的信息吗？



我们先看看脚本能不能跑：

啊嘞，居然没问题，得到解码后的诗句：

> There is something in this world
> that no one has ever seen before.
> It is gentle and sweet.
> Maybe if it could be seen,
> everyone would fight over it.
> That is why the world hid it,
> so that no one could get their hands
> on it so easily.
> However, someday, someone will find it.
> The person who deserves it the most
> will definitely find it.
> 
> ---
> 
> Do you like this school?
> I really, really love it.
> But nothing can stay unchanged.
> Fun things... Happy things...
> They can't all possibly stay unchanged.
> Even so,
> can you go on loving this place?
> 
> ---
> 
> Sometimes I wonder,
> what if this town was alive?
> What if it had thoughts and feelings
> like one of us?
> If it did,
> I think it would want to make the people
> who live here happy.
> 
> ---
> 
> Expectations are what you have
> when you have given up.
> Expectations are born from
> a despairingly large difference in skill.
> 
> ---
> 
> A joke only lasts for a moment,
> if it leaves a misunderstanding,
> it becomes a lie.
> 
> ---
> 
> If someone didn't have any pride,
> wouldn't they also be lacking
> in self-confidence?
> If someone was free of greed,
> wouldn't they have trouble
> supporting their family?
> And if people didn't envy one another,
> wouldn't they stop inventing new things?
> 
> ---
> 
> If I don't have to do it, I won't.
> If I have to do it, I'll make it.
> 
> ---
> 
> /* Here is the end of my poem.
> Have you ever found my FLAG? :) */



仔细阅读一下…怎么这么熟悉，开头不是[龙于虎](https://zh.wikipedia.org/wiki/TIGER%C3%97DRAGON%EF%BC%81)里高须龙儿开场独白吗，难道是跟动画名有关？先记录下来，TIGER×DRAGON！，继续观察其他段落，又发现了CLANNAD、冰菓…但是找不全啊摔(╯‵□′)╯︵┻━┻，看来方向不太对，换思路。（关于诗句来源作者给出了[详情](https://github.com/taoky/her_poem_fixed_version/blob/master/easter_egg/poem.zhCN.out)）

感觉这朋友是个二五仔，题干也提示“不要纠结字面意思”，看下脚本发现了

```
 begin 666 <data> 
```

玩过DOOM的我知道这个666和国内2333=666是不一样的...

google一下发现是UUencode，第一个字符是长度描述，如果写入字符后把长度缩短，就可以在每一行的末尾进行隐写了。

我们把全部的第一位拉到比较高的位置（Z），运行解密脚本，某些行的结尾会出现新的字符，拼接起来即可得到flag。

**flag{STegAn0grAPhy_w1tH_uUeNc0DE_I5_50_fun}**


## 猫咪克星

>  **通知：已发布备用地址。**
>
> 通知：已发布备用地址。
>
> 众所周知，猫怕黄瓜
>
> ![cat.gif](https://i.loli.net/2018/10/15/5bc42ca7792a7.gif)
>
> 你知道猫咪为什么怕黄瓜吗？
>
> 有一种说法是这是猫对蛇的原始恐惧，也就是说，如果一个东西足够像蛇，那么猫咪就会怕它。
>
> 进一步，如果你足够像蛇，猫就会怕你。
>
> 下面我们来扮演蟒蛇（Python）去吓猫。
>
> 蟒蛇是一种非常容易使用的编程语言，考验你像不像蟒蛇的标准就是给你一些 Python 3 表达式。如果你能正确计算出来，你就通过了验证。
>
> 赶快使用命令 `nc 202.38.95.46 12009` 来开始吧
>
> 备用地址：`nc 202.38.95.47 12009`

这个简单嘛！recvline然后eval不久好了嘛！

一分钟后：我艹这是什么在滚动不会是rm -rf 吧赶紧停下来

发现出题人很邪恶的在算式以外放了奇怪的东西，比如

```python
__import__('time').sleep(100)

__import__('os').system('find ~')

print('\\x1b\\x5b\\x33\\x3b\\x4a\\x1b\\x5b\\x48\\x1b\\x5b\\x32\\x4a')

exit()
```

这个小故事告诉我们，乱用eval是会出事的。（感谢出题人不rm -rf 之恩）

把以上几条替换成None，才能愉快的拿到flag

**flag{'Life_1s_sh0rt_use_PYTH0N'*1000}**




## 猫咪电路

> #大蒜日报社 科大分社 电
>
> 10 月 4 日，膨胀社的一篇报道在科技圈引起了轩然大波，据膨胀社报道：芒果，亚驴逊，超巨等多家公司被一个不到铅笔尖大小的西恩芯片植入了后门，其中客户不乏有米国政府敏感部门。
>
> 同时，膨胀社报道中提到的所有公司（芒果，亚驴逊，超巨）等都在极短的时间内积极予以否认：我不是，我没有，别瞎说啊.jpg
>
> 一方面是经过膨胀社 2000 名记者和多层编辑花了十几个月来组稿的报道，另一方面是罕见的多家大公司的驳斥，这其中的真真假假，吃瓜群众根本看不透。
>
> ![boom.png](https://i.loli.net/2018/10/15/5bc42ce2b646e.png)
>
> 虽然我们目前还没有搞到这个芯片的样本（搞到之后可能会加一道新题），但是我们准备了一个简单的红石电路给你逆向。
>
> 为了避免重新发明一个电路模拟器，我们使用了 Mojang AB 公司一款带有电路功能的著名沙盒式建造游戏 Minecraft 存档作为本题目的解题资料。
>
> 技术上来说，我们通过 Minecraft (版本：1.12.2) 存档提供了一个 40 个输入的红石电路，他们共同影响着信标的颜色，如果你通过调整输入，成功使得信标变绿，说明你已经破解了这个电路，请以 `flag{1010101010100010...0101010}` 的格式提交你的答案（1 代表激活，0 代表不激活）。
>
> **进入 Minecraft 之后的温馨提醒：**
>
> 1. 为了防止你没有红石电路基础，我们在出生地设置了一系列红石电路教程，希望可以帮上忙；
> 2. 为了防止你问这道题和猫咪有什么关系，我们在出生地放了一只猫（并且已经驯服）；
> 3. 按 `/` 键可以键入控制台命令，但是请不要键入 `/kill`，因为这样你会死；
> 4. 请不要通过 `/gamemode 0` 把自己的模式改为生存模式，否则你的电路会被苦力怕炸毁；
> 5. 请在解题结束后及时关闭该沙盒式建造游戏，否则你会花很多额外的时间；



没有买MC，找到一个存档编辑器叫MCedit，打开瞅瞅：

![mc.png](https://i.loli.net/2018/10/21/5bcc2759b469f.png)



左边是被炸毁的flag，盯着看了一会儿没有啥发现，（图中）左下角有红石电路教程，钻石上的应该就是需要解题的电路了，都是一些基本的门电路，画个图分组求解应该不难，mcedit实在太卡，我就不做了...



从官方那拿的flag：

**flag{0110101000111100101111111111111111111010}**



## FLXG 的秘密

> 公元 0xFB2 年, FLXG 正当其道.
>
> 没错, 在 CWK 的伟大倡导之下, 年份采用了更为先进的 16 进制表示. 中国滑稽大学也因为率先提出了 FLXG 的理论, 其世界超一流的院校的地位已经不可动摇. 而在肥宅路 98 号某个废弃的角落里 -- 实际上是两千年前一时风光无二, CWK 口中以考试分数为唯一目标的分院 -- 几名幸存的理论物理系跑男 (旧指为 GPA 而四处奔波的分院学生) 在饥寒交迫中, 企图谋划着最后的反抗.
>
> 实际上, 他们已经成功了. 多少代物理系的先辈们忍辱负重, 转入 CS, 就是为了制造出量子计算机, 试图攻破 FLXG 这个天衣无缝的理论. 这个计划已经实施了两千年, 而现在终于结成正果了. 世界上仅存的几位分院跑男, 他们已经掌握了 FLXG 最核心的秘密, 那是除了创始人 CWK 无人知晓的秘密, 那是失传千年的, 整个 FLXG 的唯一漏洞. 当年的 Nature, Science, 如今的 Engineer 期刊上不断有人试图找出这个纰漏, 然而所有人都失败了. (可惜也没人能够证明 FLXG 的绝对完美性) 因此 FLXG 有一段时间被认为是最接近真实的假设 -- 当然, 这是落后的理科思想所形成的结论. 所以, 正如你看到的这样, FLXG 已经成为了金科玉律一般的存在. 然而, 它的唯一漏洞, 在这一年, 已经这几名跑男找到了.
>
> 但是, 他们也是失败的. 分院和物院, 已经在滑稽大学的 FLXG 改革中消失, 所有留存的痕迹, 也成为校史馆中的笑料和反面教材. "什么? 你还跑过去找老师要分? 怕不是分院余孽.." 之前时时还能听到这样的嘲讽, 如今嘲讽的对象也越来越少, "分院跑男" 这种词已经被新版的 CWK 词典移到了附录里, 以后估计会被删掉的吧. 就算有人找到 FLXG 的秘密又怎么样呢, 再也不会有人去读物理了.
>
> 当然, 有唯一的一条出路, 就是设法把这条秘密发送到两千年前. 这样大家就能在 FLXG 的实施之前, 看到它的漏洞了, 也许就可以拯救分院和物院的命运了.
>
> 如今的技术发展, 虽然能够在一定程度上控制时空, 但是要把消息传回两千年前, 的确是不太靠谱. 何况两千年前的人类根本无法做出应答. 当然更关键的, 就是因果律的影响了. 传递消息的做法, 必须要瞒过因果律, 否则只会在过去的时间长河中开出一条小小的支流, 对于这个平行宇宙来说并无意义.
>
> 为了做到这一点, 他们几人把秘密用许多随机生成的锁保护起来, 最后连接成一个可以自动计算出秘密的程序 (他们为了存活也转行做 CS 了), 而这个程序运行起来需要 2000 年甚至更久. 之后, 他们再以四千年前的伏羲先天六十四卦将程序编码, 以此试图骗过因果律, 逆流而上, 成前人未有之壮举.
>
> 然而, 由于时间长河的冲刷, 这份信息仍然受到了损毁. 在 0x7E2 年的你, 能够解出 FLXG 的秘密吗?



### 来自未来的漂流瓶



![yin.png](https://i.loli.net/2018/10/21/5bcc2f0524284.png)





![yang.png](https://i.loli.net/2018/10/21/5bcc2f051d426.png)



![方位图表.png](https://i.loli.net/2018/10/21/5bcc302ce2107.png)



（截自wikipedia）



硬核脑洞，赛后看了很多资料和官方解释才弄懂，总结一下。

拉到文件最底端，能看到一些连起来的“坤”，而文件中一般会出现连续填充的只有0和f，查看坤的卦象，果然是全部一致。

仔细分析其他卦图，发现如果将阴阳作为0和1识别，可以表示二进制数据，写脚本全部替换写入二进制文件。（注意每一卦是从下向上识别的，阴代表0，阳代表1）

在文件的末尾找到flag

**flxg{Power_of_the_Hexagram}**



之后跟soha聊了一下，菊苣提醒了我...这就是base64的算法呀（扶额，用[@soha](https://github.com/ustclug/hackergame2018-writeups/blob/master/players/soha/secret_of_flxg.md)的脚本替换:

```js
let fs=require('fs');
let xianTian64Gua=[
    "坤","剥","比","观","豫","晋","萃","否",
    "谦","艮","蹇","渐","小过","旅","咸","遁",
    "师","蒙","坎","涣","解","未济","困","讼",
    "升","蛊","井","巽","恒","鼎","大过","姤",
    "复","颐","屯","益","震","噬嗑","随","无妄",
    "明夷","贲","既济","家人","丰","离","革","同人",
    "临","损","节","中孚","归妹","睽","兑","履",
    "泰","大畜","需","小畜","大壮","大有","夬","乾"
],base64Map='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';

let flxg=fs.readFileSync('flxg.txt').toString();
xianTian64Gua.forEach((v,i)=>flxg=flxg.replace(new RegExp(v,'g'),base64Map.charAt(i)));

fs.writeFileSync('newFlxg.bin',Buffer.from(flxg,'base64'));
```

可以更简单的得到结果。



### 难以参悟的秘密

file一下

```
flxg64.bin: gzip compressed data, was "1024.tar", last modified: Fri Aug 24 12:51:45 2018, from Unix, original size 12318720
```

发现是一个压缩文件，直接解压会报错。

TODO



## C语言作业

> 今天 C 语言课程的作业是写一个简单的计算器程序，我在 linux 上面只花了几分钟就写完了，大家可以下载我编译好的程序来使用。如果不想下载的话，我还专门提供了一个网络服务，大家可以在 linux 上面使用
>
> ```
> nc 202.38.95.46 12008
> ```
>
> 这条命令来连接。什么？你说你看到我服务器的家目录里有一个 flag 文件？这怎么可能？



给了源程序，丢到IDA里，看一下main和__init

![init.png](https://i.loli.net/2018/10/22/5bcd6371e4cf6.png)



注册了4个信号到__err函数上，分别是：

> 4) SIGILL：执行了非法指令. 通常是因为可执行文件本身出现错误, 或者试图执行数据段. 堆栈溢出时也有可能产生这个信号。

> 6) SIGABRT：调用abort函数生成的信号。

> 8) SIGFPE：在发生致命的算术运算错误时发出. 不仅包括浮点运算错误, 还包括溢出及除数为0等其它所有的算术的错误。

> 11) SIGSEGV：试图访问未分配给自己的内存, 或试图往没有写权限的内存地址写数据.



看起来计算器比较容易出现的错误应该是SIGFPE了，我们输入一个除以0的算式，发现程序进行了处理，google一下发现用MIN_INT/-1也会触发。接着看触发后会发生什么

看一下__err函数：

![err.png](https://i.loli.net/2018/10/22/5bcd6371dd8e6.png)



进入__err之后会让我们输入一个command（不允许带sh），然后用execlp不带参数的执行。

ls看到flag就在目录下，不能带参数所以cat用不了。

疯狂尝试其他命令，最后熟悉的帮助乌干达儿童出现了。在vim里用命令打开flag：

```
:open flag
```

flag文件里是:

> The real flag is in the file "-"

继续打开"-"这个文件，得到flag：

**flag{816484e67b21efd5de8f1661d180a007}**



## 加密算法和解密算法

>
> 提示：本题中使用的 base64 编码，采用已被广泛应用于各种场合的 RFC 4648 §5 标准。
>
> 小赵听到自己成为了信息安全大赛的创始人后感到非常吃惊：“我一个少院学生会的干事，怎么就成信息安全大赛的创始人了呢？”这也难怪，毕竟小赵后来成为了物理学院的学生。物理和信息安全，通常情况下可都是八杆子打不着的呢。
>
> 当然了，小赵作为物理学院的学生，和其他物理学院的学生一样，身上的浮躁劲儿可一点都不少，常常因为一点小成就而沾沾自喜。这不，因为个人安全上的不重视，小赵的某个学弟小郑，很快从小赵暗恋的女孩子手里拿到了小赵和她交流的加密算法的程序。小赵在得知此事后反而没有尽可能地息事宁人，反而公开宣称，由于解密算法目前没有公开，所以拿到了加密算法也没有什么用。看来小赵对于现代密码学，根本没什么全面深入的了解啊。
>
> 不过，即使小赵使用的是对称加密算法，分析出解密算法也并非易事——小赵对程序进行了混淆，而混淆的方法是使用 BrainFuck 虚拟机——这也正是小赵的底气所在。现在的任务是分析并读懂一段 BrainFuck 程序，从而将一段密文还原。
>
> 现在小郑将这一任务交给了跃跃欲试的你。快来挖掘小赵的黑历史吧！
>
> 更多信息请下载题目文件



## 王的特权

>
> 小王同学刚刚学会了 Rust 语言，今天拿着自己写的 BUG 来找老张同志。
>
> 老张：哟，小子学会写 Rust 了？
>
> 小王：没错，刚出炉的程序，而且只有我能运行！
>
> 老张：只有你能运行？我不信。
>
> 小王：不信你就试试呗！
>
> 小王放心地把程序交给了老张，并声称可以找任何人来帮忙。作为老张多年的好友，你能帮他破开「王的特权」的秘诀吗？
>
> 注意：
>
> - 做这道题，你可能需要准备 64 位 Linux 环境。
> - 做题时请保证网络畅通。**但这是为了避免直接拿到 flag 而给你的小小考验，预期解法与网络无关，请不要在这方面下工夫。**



## 她的礼物

> （在做这道题之前，你可能需要先完成题目「她的诗」的一部分。）
>
> 小 T 的生日就要到了，在一天前，他收到了她发的电子邮件。
>
> 「祝你生日快乐！……」庆生邮件的开头大概都是这个样子的。自从小 T 加入校文学社以来，她可没少给他带去惊吓。这家伙邮件里面又会写什么东西？
>
> 出乎他意料的是，这封邮件看起来挺正常的，除了结尾之外。
>
> 「另外呢，我写了一个小小的程序送给你，在里面藏了一些东西，不过运行它是需要密码的，密码我想想……哦，还记得上次我给你的那首诗吗？就是那首诗，用你朋友的脚本解密之后的第 10 行，然后啊我还要去赶路呢，就先写到这里吧，拜拜～」
>
> 附件看起来像是一个 Linux 下的可执行文件。理论上讲，把密码作为参数启动程序，就能看到她想要告诉小 T 的字符串了。不过……这家伙不会藏了什么 `rm -rf / --no-preserve-root`这种命令（注：请勿在自己的机器上执行此命令！）在里面吧？但小 T 又想，她不可能会做出这种事情的。



## 困惑的flxg小程序

> 在民间流传着这样一个传说，智慧的老者有一个神秘的魔镜，每当有人向老者提出自己的疑惑，老者将轻轻抚摸镜面，此时魔镜发出了古老的声音，诉说着做法的对错。无数的年轻人通过老者向魔镜请教，他们留下了一个个不朽的神话。过了很久很久……人们进入了工业时代，又过了很久进入了电器时代，随着人们对于自然理解，人们进入了原子能时代。人们似乎忘记了久远的传说。但是智者却以其他形式的方式再次出现在了人们的生活之中。小冉同学像是天之娇子，他在互联网上发现了一个这样的神秘程序，输入一段文字，神奇的程序会告诉你它是否正确。或许这就是21世纪的魔镜。魔镜里到底隐藏着多少不为人知的秘密，冉同学能发现这魔镜里的秘密吗?



## CWK的试炼

> **提示:**
>
> 1. **本题两个 flag 均由远程服务器提供.**
>
> 2. **本题两个 flag 均为有意义的字符串.**
>
> 3. **与服务器交互时请使用 UNIX 换行符.**
>
> 4. **这不是 HTTP 协议啊喂 (╯‵□′)╯︵┻━┻, nc 命令请了解一下.**
>
> *The CWK History Symposium* 会议上的一篇论文 *On the missing heritages of CWK* 里写道, “…CWK 并没有将他的修为与财富留给子嗣, 因为当时的 FLXG 并没有被世人所理解. 在无人知晓的时候, CWK 远游四海, 于一个孤岛上独自一人建立了一座巍峨宏伟的神庙, 并将有关 FLXG 的宝藏全部埋葬于此. 然后他又利用不为人知的技术, 使这座荒岛看起来平平无奇, 并且还能避开如今的 FLXG 雷达的探测. 根据当时联合国粮食与农业组织 (FAO) 的记录, 那几年太平洋西部海岸洋葱产量锐减. 我们由此推测 CWK 应该使用了当时比较冷门的一个西方魔法, 可以从洋葱中提取能量从而隐藏海域…”
>
> 当我偶然翻到这篇 paper 的时候, 脑子里电光火石般想起来, 自己曾经在滑稽大学图书馆中借走的一本 *信息安全导论* 中夹着的那一张羊皮纸. 这一瞬间, 我感觉自己的内心里充满了 flag… 没错, 一定是这样的. 这张古老的羊皮纸就是 CWK 留给滑稽大学最宝贵的遗产, 前往 FLXG 神庙的地图!
>
> 不愧是 CCF (China CWK Federation) 推荐的 A 类会议, 我一边想, 一边往下读, “…CWK 在神庙里设计了试炼, 只有通过的人才有资格成为他的继承人…**据说神庙的设计图被 CWK 用法力嵌入到了指向神庙的地图里.** 关于 CWK 的其他许多传闻逐渐都得到了验证, 而这张宝贵的地图却依旧只是传闻, 在历史上从未出现过…”
>
> 读至此处, 我心中热血沸腾, 恨不得立马出发, 去 FLXG 神庙一探究竟. 可是转念一想, CWK 出的题目往往都很坑, 又有些踌躇不前. 正好, 最近似乎滑稽大学要举办一个啥比赛, 不若投石问路, 让那些好奇的选手们先去探个险, 看看他们能不能从神庙中站着出来…

### 神庙设计图, Get!



### 此小技耳



##  Z 同学的 RSA

> [
> 坊间传言](https://www.quora.com/What-are-all-the-Jeff-Dean-facts) Jeff Dean 在面试 Google 的时候，曾根据公钥心算出 Google 私钥。当然大多数人都把这事当作笑话对待，但只有 Z 同学知道，这是真的。
>
> 根据国家计生委未公开的大数据统计，平均每 66666666 位少年少女中就有一位这样的天才，心算能力极为恐怖，可以在线性复杂度内分解任意长度的大整数，因为时间瓶颈主要在于把结果用笔写出来。中国科学技术大学少年班学院成立的主要目的，其实就是为了网罗这样的神童。每当这样的一位天才出现，国家就会将其秘密保护起来，送到国家高性能计算中心作为 ALU，而其同学却只是被告知出国。实际上，曾排 TOP500 榜单第一名的超算“神威-太湖之光”的主要算力其实是由两位这样的天才少年提供，剩余的 10649600 个核心则负责将通用的计算程序规约到大整数分解，以及处理输入输出等等外围工作。
>
> 后来，少年班学院的“冰球”，Z 同学的一个好朋友，在离开科大去北大做相关秘密研究之际，告诉了 Z 同学这个消息。Z 同学马上意识到 RSA 实际上并不安全，惊慌失措，立刻删掉了自己所有服务器上面的 RSA 公钥，大喊：“不能再公开 RSA 中的 n 了！我们必须立即以一种新的方式使用 RSA！”。在连续几个通宵的苦思冥想后，Z 同学写了一段 python 代码，用他改进过的 RSA 算法加密了一段消息。新的算法并没有透露 n，只给定了两个大整数：(p*q)^(p+q) 和 (p*q)^(p-q)，其中 ^ 是按位异或运算。
>
> “终于能睡个安稳觉了”，Z 同学如是想。在上床之前，Z 同学告诉你，除非这个新的算法有漏洞，否则不要打扰他的休眠。而喜欢恶作剧的你，能找到正当理由叫醒正在熟睡的 Z 同学吗？



## 数理基础扎实的发烧友

> 作为一个专业的HiFi发烧友，你不仅要会欣赏音乐，还要有扎实的数理基础，精通声学、电子、程序设计。请用你专业的HiFi知识解读题目所给的图片并得到flag。



## 一些宇宙真理

> 大学最关键的就是数学物理基础。除了数学物理基础之外，其他的都是数学物理原理的推论。像无线通信这样的东西，没有任何的原创性，一点儿原创性都没有，不需要任何思考，无非是一群工贼偷走了物理学家做的发电机，然后办了一些会议，让别的人 fork，照着这台机器模仿，做出来了就去拿什么爱拽补一的什么奖章。
>
> 换句话说，工科的原创性研究基本是没有的，无非就是到哪个地方去抄点东西。遇到什么工程难题，百度、谷歌，大不了到知乎上面提问。理科的研究人员是真正的思考者，而工科的研究人员无非是一群玩乐高玩具的人。这些玩具还不知道是从哪家小孩那里抢过来的。现在互联网通畅了，我看他想搞个轮子，就随便就近找个网站就有了。
>
> 最近一些新闻在讲，人工智能会逐步代替人类，我看工科人都首当其冲。只要我们写个自动连接搜索引擎的脚本，让它搜索“怎么做‘一些宇宙真理’这道题”，它自己东找到西找到，不用几分钟就能拼拼凑凑找到答案。我看这样的人工智能，也不用几行代码，又比工科人便宜，还比他们诚实可靠。
>
> 今天他们工科的人说什么有人发明了斯纳德，说这个东西特别好。我看啊，又是从哪里复制粘贴过来的。工科人怎么可能会从零开始呢？他们没有这个能力。
>
> ## 问题背景
>
> 我们先介绍问题背景。小工产生了一个哈希对 (H_1, H_2, X)，这些哈希对符合下面的三个条件。
>
> - 存在 R_1 是 H_1 的原像
> - 存在 R_2 是 H_2 的原像
> - R_1 = R_2 XOR X
>
> 小工希望向小理证明：它的这个哈希对 (H_1, H_2, X) 符合上述的条件；但是小工不希望告诉小理 R_1 和 R_2 是什么。
>
> 换句话说，我们需要两个性质：
>
> - 小理相信小工产生的哈希对符合上面的三个条件。
> - 小理不知道 R_1 和 R_2。
>
> ## 解决问题的方法：非交互式零知识证明
>
> 本题考虑一种方法 -- 非交互式零知识证明（Zero-Knowledge Succinct Non-Interactive Argument of Knowledge, zkSNARK）。这种证明方法在著名的区块链货币 Zcash 里面有充分应用，他可以实现完全匿名的区块链货币交易。未来，这种技术还会用于实现支持保密智能合约的区块链系统。
>
> zkSNARK 是这样工作的：小工知道有一个算法 F(H_1, H_2, X, R_1, R_2) 能够快速验证这个哈希对是否满足条件。他根据这个算法产生几个数字，而这几个数字就蕴含着证明哈希对满足条件的神秘力量，但是却能够隐藏 R_1 和 R_2。我们记这些数字为一个证明 v。
>
> 如果小工告诉小理 (H_1, H_2, X, v)，当小理对 v 和其他参数进行某些计算之后，小理就能够相信小工提供的 (H_1, H_2, X) 满足条件。在这个过程里面，R_1 和 R_2 没有泄露给小理。
>
> ## 回到这个问题
>
> 上述描述的过程里面，小理验证这个证明是否有效，需要一个校验密钥，这个密钥我们称为 vk。我们在压缩包 vkandproofs.zip 里面提供了这个文件。 我们产生了 40 个有效的证明和 40 个无效的证明。它们就混在这 80 个证明文件里面。
>
> 你现在需要补全这个 github repo 里面缺少的验证算法，然后利用这个验证算法来找出哪些证明是有效的。
>
> 如果第 i 个证明是有效的，那么我们记 b_i = 1，否则记 b_i = 0。flag 的格式为 flag{b_1 b_2 ... b_80}。
>
> 例如 flag 可能是 flag{11010101010101010101010101010101....1010101}
>
> ## 有关的代码
>
> <https://github.com/weikengchen/lightning_circuit>
>
> ## Hint
>
> ![Github](https://camo.githubusercontent.com/b34a1872f29015c70fbb373526c5b411d57047d6/68747470733a2f2f6173736574732d63646e2e6769746875622e636f6d2f696d616765732f6d6f64756c65732f6c6f676f735f706167652f4769744875622d4d61726b2e706e67)





## 对抗深渊

>
> 40万年后的一个平静下午，人类终将回想起，那无生命之物并未将永远安息，在诡秘的万古中即便死寂也会消逝。深渊终将降临。
>
> （剧情警告）
>
> 故事发生在深度纪元42年，人类社会彻底沦为一个被机器人统治的反乌托邦社会。在历史学家这个职业还没有消亡的年代，业界公认为机器人的真正崛起可以追述到200多年前。在那个欣欣向荣的时代，人类开始涉足一个卓越的科技领域————“深度学习”。论文发表数量在最初的几年如潮水般快速上涨，其影响很快超出了计算机领域本身，蔓延到物理化学医学生物能源等领域。随后不知道过了多少年，就当人类认为自己已经完全掌握了深度学习技术时，出现了一次大规模的机器人故障————因为深度学习算法的核心组件“神经网络”的黑箱性质，难以解释，所以这次事故的原因不明。随后故障规模的急剧增大引发了蝴蝶效应，像多米诺骨牌一样影响到了各个国家间的战略平衡，人类发动了第一次也可能是最后一次大规模机器人战争，战争中人类被迫将大量能源和资源投入到战争机器的研发上，即使各国都知道现在的技术并不真正可控。后来发生的事情已经鲜为人知，直到深度纪元开始，人类才意识到自己已经不是世界的主人。随后人类开始了连绵不断的希望渺茫的反抗，由于此时已经很少有人了解深度学习背后的原理，人类在抗争中处境艰难————是啊，在任何一个时代理解技术的人都远远少于享受技术的人。
>
> (下面是OJ式的故事写法)
>
> K，一个反抗者，认为反乌托邦世界最大的枷锁是对自由信息交换的限制，因此K一直希望能够通过数字传递给队友一些关键信息。K先试着使用隐写术和一般的加密算法，不过因为机器人尤其擅长密码学，这些操作都失败了。
>
> 在几周前，事情有了转机。K收到了某个不知名的同伴收集到的一些关键的代码（这个同伴之后消失了），并交代了一些参考资料：
>
> [Pytorch](https://pytorch.org/)
>
> [Examples](https://github.com/akshaychawla/Adversarial-Examples-in-PyTorch)
>
> **下面是重点内容**
>
> 此外他给了K一些和深度相关的关键代码（使用python语言，建议3.5及以上版本）：
>
> - `main.py`: 机器人内部使用的训练代码，训练后的参数用于识别信件上的手写数字。运行 `main.py` 来进行训练，训练结束（大概十几分钟）后将获得参数文件 `model.pth`。不过为了防止因为跨平台等原因造成参数不同，题目中附上了参数文件。
> - `adversarial.py`: 同伴完成一半的解决方案。
> - `target.png`: 实验目标图像，为一个灰度的‘6’。
>
> K需要参考 `main.py` 完成 `adversarial.py`。
>
> 解决方案希望解决的问题是：给定一个‘6’ （600*600像素），K能够使得这个图像人类看上去仍然是‘6’，但是机器阅读时会和其他数字混淆。另外机器有很强的反作弊装置，**将图像像素值归一化到[0,1]之后**，如果篡改超过以下 **任何一个** 程度就会被机器发现：
>
> - 篡改的像素数量超过总数量的 0.2%
> - 篡改前后的平均绝对误差（L1 loss）超过 0.001
> - 存在任何一个像素篡改的值的变化程度超过 0.2
>
> 为了方便解题，这部分检查已经内置到了 `adversarial.py` 中。K运行 `adversarial.py` 并顺利通过检查后，将生成的图片 `sample.png` 提交到本题对应的网站上就可以改变现实，获得flag。
>
> 请你帮助K完成这一部分内容。
>
> 注：此题需要参赛者了解和学习 python, pytorch, 数字图像处理, 机器学习&深度学习相关的知识。如果较长时间没有参赛者完成，我们可能会适当修改题目。此外，此题不涉及Web漏洞利用等。
>
> 解题网站：[link](http://202.38.95.46:12004/)

