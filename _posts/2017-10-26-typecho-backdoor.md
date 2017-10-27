---
layout: post
title: Typecho任意代码执行漏洞笔记
subtitle: 又是反序列化
author: Coink 
date: 2017-10-26
categories: 
tag: 
- Science
---

前些日子听说了Typecho出了个挺严重的命令执行洞，挺庆幸自己早就转移到静态博客了（虽然也不会有人来打我就是），准备复现一下，比较大的漏洞刚出来的时候会有许多大牛和研究组写文章，学习资料还是蛮多的。

之后我熟练的执行了`jekyll new test`,我就说怎么在目录里找了半天没看到install.php........= =，我这智商，真他妈让人害怕。

默默删掉jekyll目录，去官网下了个稳定版的typecho，看了下版本，还是14年更新的（\var\Typecho\Common.php）



![](https://i.loli.net/2017/10/27/59f29d6eea09a.png)



而这个Bug在github上的修复commit是在1.1版本里



![](https://i.loli.net/2017/10/27/59f29d6f01a6b.png)



追溯一下代码，发现是2014年4月8日**Fix#219**的时候产生的问题代码，`commit:23b87aeb`



![](https://i.loli.net/2017/10/27/59f29ff96ef44.png)



看下这个issue：



![](https://i.loli.net/2017/10/27/59f2a0e790302.png)



也就是说，这个洞躺在这里三年才被人挖出来...



跟进代码找到问题点：（\install.php#L228-235）

```php
<?php
$config = unserialize(base64_decode(Typecho_Cookie::get('__typecho_config')));
Typecho_Cookie::delete('__typecho_config');
$db = new Typecho_Db($config['adapter'], $config['prefix']);
$db->addServer($config, Typecho_Db::READ | Typecho_Db::WRITE);
Typecho_Db::set($db);
?>
```
230行（修复前的非稳定版最后一版中是232行）使用了`unserialize`函数，这样只需要设置referer（网站URL），cookie设置__typecho_config的值，再加上一个finish参数，就能执行任意代码了。





跟进函数到理解透了再写。



