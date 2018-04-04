---
layout: post
title: 已知公钥的RSA破解
subtitle: 
author: Coink
date: 2018-04-04
categories:
tag:
- Science
---

简单记录一下对于不安全的RSA加密文件，已知公钥的破解过程。

RSA算法原理：

[RSA算法原理（一）](http://www.ruanyifeng.com/blog/2013/06/rsa_algorithm_part_one.html)

[RSA算法原理（二）](http://www.ruanyifeng.com/blog/2013/07/rsa_algorithm_part_two.html)

已知公钥和密文：

![pub.png](https://i.loli.net/2018/04/04/5ac4e0e397451.png)

![data.png](https://i.loli.net/2018/04/04/5ac4e0e3a78c8.png)



先导入公钥：(需要PyCrypto)

```python
from Crypto.PublicKey import RSA
r = open('public.key').read()
pub = RSA.importKey(r)
```

获取n和e1：

```python
n=long(pub.n) #n = 98432079271513130981267919056149161631892822707167177858831841699521774310891L
e1=long(pub.e) #e1 = 65537L
```

读取密文，进制转换一下：

```python
f = open('encrypted.message').read().encode('hex')
f = '0x'+f
f = int(f,16)
```



接下来需要用msieve把n分解为两个质数的乘积：



![sp180404_224318.png](https://i.loli.net/2018/04/04/5ac4e4a0023a0.png)

p = 302825536744096741518546212761194311477
q = 325045504186436346209877301320131277983

进行大数运算要用到gmpy

```python
import gmpy
```

用gmpy.invert()计算出私钥e2：

```python
e2 = long(gmpy.invert(e1,(p-1)*(q-1)))
```

拿到私钥就可以解密密文了：

```python
data = pow(f,e2,n)
```

转换后输出(需要libnum)

```python
print(libnum.n2s(data))
```

或者直接手动：

```python
print(('0'+hex(data)[2:][:-1]).decode('hex'))
```

![sp180404_231019.png](https://i.loli.net/2018/04/04/5ac4eb08360ed.png)



