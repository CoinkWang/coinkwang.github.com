---
layout: post
title: JavaScript 原型链污染攻击及实践
subtitle: JavaScript Prototype Pollution
author: Coink
date: 2020-01-29
alert: 
    content: 阅读本文需要... 我也不知道多少分钟 (๑•̀ㅂ•́)و✧
    type: success
tag: 
    - tech
---



### 前置知识
#### JS中的类与实例

JS 通过 **new关键字** 或 **`Object.create()`** 来进行对象实例的创建：

 ```javascript
function Bird() {
  // Bird类的构造函数
	this.wings = 2 //属性
}

let bird = new Bird()
 ```

我们熟知的 Array、String、Math  其实都是JS核心中的全局对象，它们和其他所有对象一样，都属于 Object 对象的实例，当然，也继承了它的所有属性与方法。

ES6 中引入了 class 语法，但本质只是一种**语法糖**，并没有改变 JS 原有基于原型的继承，也没有引入新的继承模型。

#### prototype 与 \_\_proto\_\_

回到上面的例子，如果类中有方法，实例会继承：
```javascript
function Bird() {
	...
	this.sing = function() {console.log('a~~~')}
}

let bird = new Bird()
bird.sing() // a~~~
```

但这种继承方式会在**每次**新建对象时传递一次构造函数中的方法，实际上方法独立存在于实例中，而不是类中。

而使用 prototype（原型）来进行继承，可以将方法放在类的原型中，子类实例自动继承：

```javascript
function Bird() {
	...
}
  
Bird.prototype.sing = function() {console.log('a~~~')}
 
let bird = new Bird()
foo.sing() // a~~~
```

prototype 是怎样实现继承的呢？这里涉及一个属性：\_\_proto\_\_

调用一个实例对象内部的方法或属性时，js引擎会首先在对象内部查找，若找不到，则会继续从对象的\_\_proto\_\_属性中查找，若这次依然没找到，则会去访问\_\_proto\_\_的\_\_proto\_\_，如此循环直到找到需要的东西，或是找到尽头——Object的\_\_proto\_\_为null，这样链式的调用被称为**原型链**。这里的 \_\_proto\_\_ 就指向类的原型（prototype）。

![Snipaste_2020-01-30_18-01-30.png](https://i.loli.net/2020/01/30/iA6ZeaTR7wMDpFx.png)

```javascript
bird.__proto__ === Bird.prototype // true
```

### 原型链污染

#### what & why

既然 \_\_proto\_\_ 指向的是类的原型，那么修改实例的 \_\_proto\_\_ ，是否会影响类本身呢？

答案是会，修改 \_\_proto\_\_ 实际上就是修改类的prototype。

早已有人用这种特性来实现Object等内置对象的拓展，当然，并不推荐这样做：

> **错误实践：扩展原生对象的原型**
>
> 经常使用的一个错误实践是扩展 `Object.prototype` 或其他内置原型。
>
> 这种技术被称为猴子补丁并且会破坏封装。尽管一些流行的框架（如 Prototype.js）在使用该技术，但仍然没有足够好的理由使用附加的非标准方法来混入内置原型。
>
> 扩展内置原型的**唯一**理由是支持 JavaScript 引擎的新特性，如 `Array.forEach`。

我们来尝试一下：

```javascript
bird.__proto__.hungry = 'yes!' // 修改原型
bird.hungry  // 'yes!'

let another_bird = new Bird()
another_bird // Bird {wings: 2}
another_bird.hungry // 'yes!'
```

可以看到，虽然 another_bird 并没有 hungry 这个属性，但却可以从原型链中找到这个属性并返回，说明 Bird 类被修改，新增了 hungry 这个属性。

如果我们再向上一层呢？

```javascript 
bird.__proto__.__proto__.hungry = 'yes!'

let im_a_obj = {}
im_a_obj.hungry // 'yes!'
```

啊哦，这下影响大了，js中所有的对象都拥有了 hungry 这个属性，这可不妙。

这样可以通过控制对象原型，从而影响所有同类对象的行为，被称为**原型链污染**。

#### how

现在我们知道了控制对象的 \_\_proto\_\_ ，即可影响该实例的父类，那么要如何控制 \_\_proto\_\_ 呢？

JS中针对对象的复制分为**浅拷贝**和**深拷贝**，简单来说，浅拷贝只是将指向对象的指针复制了过去，不论如何拷贝，这些拷贝都指向同一个引用，一旦被修改，所有引用都会变化；而深拷贝，则是要将目标对象完完全全的“克隆”一份，占据自己的内存空间。

实现深拷贝，一种常见的方式是：递归遍历需要复制对象的所有属性，并且全部赋值给新的空对象，实际上就是将一个空对象和目标对象进行合并。

看一个例子：

```javascript
function merge(target, source) {
    for (let key in source) {
        if (key in source && key in target) {
            merge(target[key], source[key])
        } else {
            target[key] = source[key]
        }
    }
}
```

通过递归将 source 内的属性复制给目标 target ，此处key可控，如果我们将“\_\_proto\_\_”作为一个key呢？

```javascript
let testObj = {"hey":1 ,"__proto__": {"hello": 1}}
for (let key in testObj){console.log(key)} //hey hello
```

可以看到，直接使用"\_\_proto\_\_"作为键名时，会被当作本对象的原型，从而进入遍历，获取到hey和hello两个键。所以应该如何将"\_\_proto\_\_"作为键名传进去呢？

**TODO** 不同的pollyfill会影响吗？

让我们观察一下 ```JSON.parse```方法。该方法可以将JSON**字符串**解析为值或对象，由于是从字符串解析而来，"\_\_proto\_\_"自然就与其他键名没有区别了。

```javascript
let testObj = JSON.parse('{"hey":1 ,"__proto__": {"hello": 1}}')
for (let key in testObj){console.log(key)} //hey __proto__
```

我们对构造好的 testObj 进行合并

```javascript
merge({},testObj)

let innocentObj = {}
innocentObj.hello // 1
```

成了，现在所有的 Object 对象都被污染上 hello 这个属性了。

#### 另一种实现

除了通过控制 \_\_proto\_\_ 来实现漏洞，还有另一种方法：重载构造函数。

当我们将```constructor```和```prototype```嵌套作为键名时：

```javascript
let testObj = JSON.parse('{"constructor": {"prototype": {"hello": 1}}}')
merge({},testObj)

let innocentObj = {}
innocentObj.hello // 1
```

实例 constructor 的 prototype ，和实例的\_\_proto\_\_指向一致。由于 merge 操作的解析是递归的，这种方式同样也会污染 Object。

### 漏洞利用

#### Lodash

Lodash 中就有这样的 merge 实现，并且被发现存在漏洞（**CVE-2019-10744**）影响版本 < 4.17.12，看一下[修复方式](https://github.com/lodash/lodash/commit/e77d68121ff00ba86b53eed5893d35adfe94c9dd#diff-0874e5f9b48ed68be725d581f7d72647R6602)：

![1.png](https://i.loli.net/2020/01/31/coERXxVakMwCt3D.png)

![2.png](https://i.loli.net/2020/01/31/afZFsTC5w9Vkeln.png)

1. 在赋值取 key 的过程中，需要进行判断，key不能为"\_\_proto\_\_"或"constructor"。
2. sourceURL可能被注入，需要用```hasOwnProperty```判断sourceURL是否是本身属性，而非原型链上的属性。并且对sourceURL进行过滤，防止恶意输入进行命令执行。

此漏洞拓展：[P牛的一道CTF题](https://www.leavesongs.com/PENETRATION/javascript-prototype-pollution-attack.html#0x05-code-breaking-2018-thejs)。注意评论中有个附加trick，在实际利用过程中，污染原型链会导致一些业务bug或flag泄漏，需要循环删除污染的属性。

### Anti

1. 业务逻辑中进行严格的过滤，不接受"\_\_proto\_\_"、"constructor"作为键名，并且在涉及代码执行的地方，过滤危险代码。

2. 使用[```hasOwnProperty```](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/hasOwnProperty)来判断属性是否直接来自于目标，这个方法会忽略从原型链上继承到的属性。

3. 在处理 json 字符串时进行判断，过滤敏感键名， ajv 这个库就是这样做的。
4. 使用 ```Object.create(null)``` 创建没有原型的对象。
5. 直接使用 Map 结构。
6. 用```Object.freeze(Object.prototype)```冻结Object的原型，使Object的原型无法被修改。



### Referer

[继承与原型链（MDN）](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

[深入理解 JavaScript Prototype 污染攻击](https://www.leavesongs.com/PENETRATION/javascript-prototype-pollution-attack.html)

[[翻译+笔记]nsec2018-JS原型链污染攻击](https://cyto.top/2019/04/16/translation-js-prototype-pollution-attack-nsec2018/)



