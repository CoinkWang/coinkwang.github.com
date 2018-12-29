---
layout: post
title: 解决Mac下ScreenFetch出现readlink错误问题
subtitle: 
author: Coink
date: 2018-12-28
categories:
tag:
- Tech
---

## Introduce

ScreenFetch是一个开源工具，用于在Linux终端中获取桌面截图的系统/主题信息。

项目地址：[https://github.com/KittyKatt/screenFetch](https://github.com/KittyKatt/screenFetch)



![mypc.png](https://i.loli.net/2018/12/29/5c26e7a686e31.png)



## bug

在Mac系统下，可以直接使用`brew install screenfetch`安装，虽然可以正常使用，却出现了两行报错：

```bash
readlink: illegal option -- f
usage: readlink [-n] [file ...]
```

搜索得知：MacOS下的BSD readlink与GUN readlink有区别，并没有-f参数，而screenfetch却调用了-f，导致抛出异常。网上的一般解决方案是安装coreutils，使用greadlink替代readlink。

我不太喜欢这个暴力解决方法，于是打算给该项目提个issue，发现已经有人[提过了](https://github.com/KittyKatt/screenFetch/issues/573)：



![issue.png](https://i.loli.net/2018/12/29/5c26e7af68675.png)



幸运的是，在一个月前，有人[修复了](https://github.com/KittyKatt/screenFetch/pull/602/commits/ae20cdcf048b7ea904567061e06f4d5be30f6c0b)这个问题，跟进查看：



![gitfix.png](https://i.loli.net/2018/12/29/5c26e9283abe3.png)



## fix

1. 使用greadlink替代readlink
2. 等待homebrew上的release版本更新
3. 直接从项目地址下载dev版本，改名放到环境变量中即可