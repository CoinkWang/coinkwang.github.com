---
layout: post
title: Enable https for ur Githubpages
subtitle: 给你的GithubPages启用httpss
author: Coink 
date: 2016-06-24 00:00:00 
alert: 
    content: 本文由于时间久远，图床跑路，已无正常阅读意义，仅作存档使用
    type: alert-warning
---


# 为什么要给GithubPages启用HTTPS

~~鬼知道啊~~

# 实现

一个非常简单的解决方案：Kloudsec

更新：CloudFlare

# 步骤

https://kloudsec.com/github-pages/new

- 先注册账号

- 然后绑定你的github页面

![bind](http://7xread.com1.z0.glb.clouddn.com/3382c269-1440-468f-a2ab-a2516d245e1f)

- CNAME要改成你的域名，不能带协议

- 然后你得删掉你原来的解析记录，是删掉哈

- 解析Kloudsec提供的A记录

- 进入SETTING，填上你的githubpages可用ip，我是直接ping我的仓库地址得到的

![setting](http://7xread.com1.z0.glb.clouddn.com/bd47e62e-5a83-4b6a-aa6f-eb6555ce2684)

![ping](http://7xread.com1.z0.glb.clouddn.com/5f330ed9-a062-4268-975c-4db39df6c7f4)

~~（请无视屁股先锋~~

- 然后去Protection把能开的服务都开了，配置一下SSL

![](http://7xread.com1.z0.glb.clouddn.com/15ac0949-1a28-4139-8fab-3ce80762d3bb)

开上面俩就行了

![](http://7xread.com1.z0.glb.clouddn.com/7d651634-f316-4ead-8da4-b332ec6898d2)

访问你的网站看吧

# 最后还有一件事


如果你的一些资源不是相对url调用，甚至是http的话，会无法加载，其他没啥坑了





--------

7月更新：

收到一封邮件：
![SHUTDOWN](http://7xread.com1.z0.glb.clouddn.com/b62df5c8-ea87-4dbd-bf3c-8efc4f020b61)


8月，再见Kloudsec.

故转移到CloudFlare。（所以为什么不一开始就用CF？

---

更新：GithubPages已自带HTTPS，启用即可。