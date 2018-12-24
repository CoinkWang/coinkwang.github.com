---
layout: post
title:  用JS和emoji点缀一下这个圣诞
subtitle: 
author: Coink
date: 2018-12-24
categories:
tag:
- Tech
---



## 原理

浏览器的`window.location.hash`部分是可控的，通常用于控制页面内定位。我们可以通过控制hash，装饰一下url。



假设有这样一个url：

`https://example.com/index.html#hello`



获取location.hash可以得到：

![Snipaste_2018-12-24_11-20-10.png](https://i.loli.net/2018/12/24/5c20508415c50.png)



同理，用js对这部分进行操作即可。



## 实现

```js
setInterval(function () { window.location.hash = "🎄"; }, 1000);
setInterval(function () { window.location.hash = "🎁"; }, 2000);
```



当然文字也是可以的

```js
setInterval(function () { window.location.hash = "Merry"; }, 1000);
setInterval(function () { window.location.hash = "Christmas"; }, 2000);
```



预览：



![index.gif](https://i.loli.net/2018/12/24/5c2052bc69a41.gif)





圣诞相关的emoji：



🎄 ⛄  🎁 ❄  🎅 👪 🎶 🔥 🔔 🌟 



圣诞快乐呀，大家。