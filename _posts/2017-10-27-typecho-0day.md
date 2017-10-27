---
layout: post
title: Typecho任意代码执行漏洞学习笔记
subtitle: 只是笔记，没有干货
author: Coink 
date: 2017-10-27
categories: 
tag: 
- Science
---

## 0x00 概

前些日子听说了Typecho出了个挺严重的命令执行洞，挺庆幸自己早就转移到静态博客了（虽然也不会有人来打我就是），准备复现一下，比较大的漏洞刚出来的时候会有许多大牛和研究组写文章，学习资料还是蛮多的。

之后我熟练的执行了`jekyll new test`（我正在用的静态博客创建站点命令）,我就说怎么在目录里找了半天没看到install.php........= =，我这智商，真他妈让人害怕。

## 0x01 跟踪

默默删掉jekyll目录，去官网下了个最新稳定版的typecho，看了下版本，还是14年更新的（\var\Typecho\Common.php）



![](https://i.loli.net/2017/10/27/59f29d6eea09a.png)



而这个漏洞在github上的修复commit是在1.1版本里



![](https://i.loli.net/2017/10/27/59f29d6f01a6b.png)



追溯一下代码，发现是2014年4月8日**Fix#219**的时候产生的问题代码，`commit:23b87aeb`



![](https://i.loli.net/2017/10/27/59f29ff96ef44.png)



看下这个issue：



![](https://i.loli.net/2017/10/27/59f2a0e790302.png)



恩...没看出啥，只是感觉这个洞躺在这里三年之久，有点恐怖...



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
230行（修复前的非稳定版最后一版中是232行）使用了`unserialize`函数，获取cookie里`__typecho_config`的值，base64解码后反序列化，接着删除了这条cookie，用`$config['adapter']`和`$config['prefix']`进行`Typecho_Db`实例化...好像后面不重要了，不管了。

这里比较奇怪的是这条名字叫config的cookie居然是base64加密过的，没想明白是要干啥

转入Typecho_Db的构造函数看到（var\Typecho\Db.php#L107-135）：

```php
/**
 * 数据库类构造函数
 * 
 * @param mixed $adapterName 适配器名称
 * @param string $prefix 前缀
 * @throws Typecho_Db_Exception
 */
public function __construct($adapterName, $prefix = 'typecho_')
{
    /** 获取适配器名称 */
    $this->_adapterName = $adapterName;

    /** 数据库适配器 */
    $adapterName = 'Typecho_Db_Adapter_' . $adapterName;

    if (!call_user_func(array($adapterName, 'isAvailable'))) {
        throw new Typecho_Db_Exception("Adapter {$adapterName} is not available");
    }

    $this->_prefix = $prefix;

    /** 初始化内部变量 */
    $this->_pool = array();
    $this->_connectedPool = array();
    $this->_config = array();

    //实例化适配器对象
    $this->_adapter = new $adapterName();
}
```


我们发现`$adapterName`经过了拼接处理，如果`$adapterName`是一个实例化的对象，便会触发~~膜法~~魔术方法`__toString()`，全局搜索一下发现了三处：



```php
Searching 229 files for "function __toString"

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Config.php:
  192       * @return string
  193       */
  194:     public function __toString()
  195      {
  196          return serialize($this->_currentConfig);

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Feed.php:
  221       * @return string
  222       */
  223:     public function __toString()
  224      {
  225          $result = '<?xml version="1.0" encoding="' . $this->_charset . '"?>' . self::EOL;

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Db\Query.php:
  486       * @return string
  487       */
  488:     public function __toString()
  489      {
  490          switch ($this->_sqlPreBuild['action']) {

3 matches across 3 files
```

有点懒，不想一条条跟进，查阅了一些资料，发现问题出自var\Typecho\Feed.php#L358：

```php+HTML
    <name>' . $item['author']->screenName . '</name>
```

由于item是可控的，只要让screenName从无法访问的属性读取数据，就能触发魔术方法`__get()`

搜索一下，找到了许多。。。

```php
Searching 229 files for "function __get"

C:\Users\Coink\Desktop\Sec\typecho\var\IXR\Client.php:
  208       * @return void
  209       */
  210:     public function __get($prefix)
  211      {
  212          return new IXR_Client($this->server, $this->path, $this->port, $this->useragent, $this->prefix . $prefix . '.');
  ...
  239       * @return void
  240       */
  241:     public function __getResponse()
  242      {
  243          // methodResponses can only have one param - return that
  ...
  262       * @return void
  263       */
  264:     public function __getErrorCode()
  265      {
  266          return $this->error->code;
  ...
  273       * @return void
  274       */
  275:     public function __getErrorMessage()
  276      {
  277          return $this->error->message;

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Config.php:
  143       * @return mixed
  144       */
  145:     public function __get($name)
  146      {
  147          return isset($this->_currentConfig[$name]) ? $this->_currentConfig[$name] : NULL;

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Date.php:
   97       * @return integer
   98       */
   99:     public function __get($name)
  100      {
  101          switch ($name) {

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Plugin.php:
  463       * @return Typecho_Plugin
  464       */
  465:     public function __get($component)
  466      {
  467          $this->_component = $component;

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Request.php:
  265       * @return mixed
  266       */
  267:     public function __get($key)
  268      {
  269          return $this->get($key);

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Widget.php:
  375       * @return mixed
  376       */
  377:     public function __get($name)
  378      {
  379          if (array_key_exists($name, $this->row)) {

C:\Users\Coink\Desktop\Sec\typecho\var\Typecho\Widget\Helper\Layout.php:
  325       * @return void
  326       */
  327:     public function __get($name)
  328      {
  329          return isset($this->_attributes[$name]) ? $this->_attributes[$name] : NULL;

10 matches across 7 files
```

去掉前几个浑水摸鱼的，还是有很多...

跟着大佬的足迹摸到var\Typecho\Request.php#L285-309：

```php
    /**
     * 获取实际传递参数
     *
     * @access public
     * @param string $key 指定参数
     * @param mixed $default 默认参数 (default: NULL)
     * @return mixed
     */
    public function get($key, $default = NULL)
    {
        switch (true) {
            case isset($this->_params[$key]):
                $value = $this->_params[$key];
                break;
            case isset(self::$_httpParams[$key]):
                $value = self::$_httpParams[$key];
                break;
            default:
                $value = $default;
                break;
        }

        $value = !is_array($value) && strlen($value) > 0 ? $value : $default;
        return $this->_applyFilter($value);
    }
```



最后执行了`_applyFilter($value)`，`$value`就是`_params[$key]`，也就是之前的`screenName`参数了。

接着跟`_applyFilter`，在L152-171：

```php
    /**
     * 应用过滤器
     *
     * @access private
     * @param mixed $value
     * @return mixed
     */
    private function _applyFilter($value)
    {
        if ($this->_filter) {
            foreach ($this->_filter as $filter) {
                $value = is_array($value) ? array_map($filter, $value) :
                call_user_func($filter, $value);
            }

            $this->_filter = array();
        }

        return $value;
    }
```



两个调用可控参数`$filter`和`$value`的函数`array_map`以及`call_user_func`就浮出水面了。

只要创建class，指定参数，序列化并且base64加密，payload便完成了。之后只需要设置`referer`，将payload其设置为`__typecho_config`的Cookie值，再加上一个`finish`参数，就能执行任意代码了。

## 0x02 作者解释

因为有人恶意揣测/无意中伤，Typecho开发者发文解释：[原地址](https://joyqi.com/typecho/about-typecho-20171027.html) 



![](https://i.loli.net/2017/10/27/59f3409aca73e.png)

对于不自动删除安装文件的解释：

![](https://i.loli.net/2017/10/27/59f341c0697af.png)



以及倾诉他的无奈：



![](https://i.loli.net/2017/10/27/59f34dcc7e91f.png)



## 0x03 思考

我很庆幸我是**细思**了的那些人之一。之前经历过守望先锋Diya事件，Wooyun事件，我已经不再是一个没事就吃瓜看节奏顺便推波助澜的sb了，我学会了独立思考，会管好自己的嘴（手），对自己的言论负责，遇到事情会先确认真实性。算是养成了一种好习惯吧。共勉。