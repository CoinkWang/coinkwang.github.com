---
layout: post
title:  用JS和emoji点缀圣诞
subtitle: 
author: Coink
date: 2018-12-24
categories:
tag:
- Tech
---



首先是送自己一顶帽子：



![avatar_christmas.png](https://i.loli.net/2018/12/24/5c2053d8a4968.png)



然后放上一曲圣诞BGM：[Lost my pieces - 橋本由香利](https://music.163.com/#/song?id=583253)

看着大家幸福的笑脸，圣诞的意义就是这样呀。



扯远了，回来（



## 瞎说原理

浏览器的`window.location.hash`部分是可控的，通常用于控制页面内定位。我们可以通过控制hash，装饰一下url。



假设有这样一个url：

`https://example.com/index.html#hello`



获取location.hash可以得到：

![Snipaste_2018-12-24_11-20-10.png](https://i.loli.net/2018/12/24/5c20508415c50.png)



同理，用js对这部分进行操作即可。



*不过这么玩会有个小问题，由于H5的history特性，每刷新一次，history.back*都会更新，导致原本预期的浏览器“后退”操作失去效果（*



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



在线调试的时候记得勾上Disable cache



![cache.png](https://i.loli.net/2018/12/24/5c2074fb82092.png)





预览：



![index.gif](https://i.loli.net/2018/12/24/5c2052bc69a41.gif)





圣诞相关的emoji：



🎄 ⛄  🎁 ❄  🎅 👪 🎶 🔥 🔔 🌟 



圣诞快乐，大家。