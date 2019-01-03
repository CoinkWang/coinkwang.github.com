---
layout: post
title: 基于Rime的鼠须管输入法配置记录
subtitle: 朙月拼音-简化字
author: Coink
date: 2018-10-08
categories:
tag:
- Tech
---



# 何谓Rime

[Rime Input Method Engine · 中州韻輸入法引擎](https://rime.im/) ，关于命名可以看[这篇文章](https://rime.im/blog/2016/04/14/qna-in-mtvu/) 。在各家输入法被曝光搜集用户隐私信息后，我开始寻找开源的输入产品，结识了这款文墨气息浓厚的输入引擎，支持的输入方式相当多，配置起来也很有趣。

![rime.png](https://i.loli.net/2018/10/08/5bbb65acac5bf.png)



# 安装

此处仅讨论鼠须管（Rime on Mac）的安装和配置，Windows下的产品名为“小狼毫”，安装方式不同，不过config是通用的。

用brew安装：

```bash
brew cask install squirrel
```
# 配置

```bash
cd ~/Library/Rime
```

这里存放着输入法的配置文件，刚摸索配置时直我接修改了defult等配置文件，意图确实达到了。直到有一天我安装了更新，一切还原之后才知道，默认文件更新时是会被覆写的。

!Warning! : 配置时不要直接修改默认配置文件，正确的方式是新建 *.custom.yaml 格式的配置文件，优先级是高于默认的。

![custom.png](https://i.loli.net/2018/10/08/5bbb707ca692d.png)



配置文件，写几条朙月拼音-简化字常用的，更多配置请参阅文档。

配置文件以patch形式打上去，一个文件只需一个patch，文件对缩进要求很高。

我设置了每页10个候选字，留下了朙月拼音简体和繁体使用，然后把 "[" 和 "]" 作为翻页。

```yaml
# default.custom.yaml
# 设定备选词数量，定义输入方案

patch:
  menu/page_size: 10

  schema_list:
    # - schema: luna_pinyin
    # - schema: cangjie5
    # - schema: luna_pinyin_fluency
    - schema: luna_pinyin_simp
    - schema: luna_pinyin_tw

  key_binder/bindings:
    - when: paging
      accept: bracketleft
      send: Page_Up
    - when: has_menu
      accept: bracketright
      send: Page_Down

```

我的样式：

![shuxuguan.png](https://i.loli.net/2018/10/08/5bbb73cee23d6.png)

```yaml
# squirrel.custom.yaml
# 自定义样式,配色

patch:
  style:
    color_scheme: dark_temple # 默认皮肤在squirrel.yaml中查看
    horizontal: true # 水平/竖直显示
    inline_preedit: true
    corner_radius: 5
    border_height: 0
    border_width: 0
    line_spacing: 1
    spacing: 5  # space between preedit and candidates in non-inline mode
    #candidate_format: '%c. %@ '
    font_face: 'Lucida Grande'
    #font_point: 18 
    #label_font_face: 'STHeitiTC-Medium'
    #label_font_point: 18a
```

添加了特殊符号的输入，默认可以输入的符号写在symbols.yaml中，已经足够大部分情况使用了

![bg.png](https://i.loli.net/2018/10/08/5bbb77627063e.png)

![jm.png](https://i.loli.net/2018/10/08/5bbb77627a063.png)



```yaml
# luna_pinyin_simp.custom.yaml

patch:
      "punctuator/import_preset": symbols
      "recognizer/patterns/punct": "^/([A-Z|a-z]*|[0-9]|10)$"
```





# 生僻字

对于生僻字，自带的字体并没有支持全部汉字，会显示为方框加问号，可以通过在配置文件中过滤生僻字解决。本着未雨绸缪的原则，还是建议安装 [花园明朝](http://fonts.jp/hanazono) 字库，将生僻字显示出来，以备不时之需。



# 词库

用惯了有联想词功能的输入法，再转用纯净的Rime，会有力不从心之感，Rime会根据用户输入动态调整词频率，刚开始用便是白板一片，输入有些费力。所幸Rime可以导入词库，但使用前最好先了解一下Rime词库的设计理念和构造，随意使用会导致卡顿，降低输入效率，此处为[解释与教程](http://tieba.baidu.com/p/2757690418) 。

Rime 擴充詞庫：https://github.com/rime-aca/dictionaries  跟着README走即可。注意修改luna_pinyin_simp.custom.yaml的时候不能直接覆盖掉自己的源文件，而是要将两个文件结合起来。

