---
layout: post
title: 提上日程的ES2020新特性
subtitle: img原生懒加载、Promise.allSettled、Promise.any、空值合并运算符、可选链操作符、BigInt数据类型、import()、globalThis、matchAll()、Class的私有属性
author: Coink
date: 2020-02-16
alert: 
    content: 所有进度截至本文成文时间。你看到这里的时候已经在使用这些特性也说不定哦
    type: success
---



### glance

前两天刷推，看到了一些非常令人愉悦的 ES2020 新特性，以及HTML标准新特性：

标准仍在变动，请关注 tc39 中 finished 部分：[tc39/proposals/finished-proposals.md](https://github.com/tc39/proposals/blob/master/finished-proposals.md)

- img原生懒加载 (HTML 标准 merged)
- Promise.allSettled (ES2020)
- Promise.any (目前处于stage3)
- 空值合并运算符  (ES2020)
- 可选链操作符  (ES2020)
- BigInt数据类型  (ES2020)
- import()  (ES2020)
- globalThis  (ES2020)
- String.prototype.matchAll  (ES2020)
- Class的私有变量

记录一下。

#### native img lazy-loading

草案与2018年被提出，前几天被merge到HTML标准中了。

```html
<img loading="lazy"/> <!-- loaded lazily -->
<img loading="eager"/> <!-- loaded immediately -->
```

支持 img 和 iframe，很顶。

#### Promise.allSettled、Promise.any

当前的 Promise 中已有一些方法，例如：all()，race() 等，草案中的两种方法可以让开发者更便捷的使用Promise：

- Promise.allSettled 会在新的 Promise 数组全部完成以后返回，其中包含组中每个 Promise 的执行结果。

```javascript
const p1 = Promise.resolve(1);
const p2 = new Promise((resolve, reject) => setTimeout(reject, 100, 'foo'));

Promise.allSettled([p1,p2]).
  then((res) => console.log(res))

// [
//   Object { status: "fulfilled", value: 1},
//   Object { status: "rejected", reason: "foo"}
// ]
```

- Promise.any (**目前处于Stage3**) 同样接受一个 iterable 对象，只要其中一个 promise 完成，就立刻返回已完成的 promise。

  这个方法和 race() 的区别在于，race 返回第一个“结果”，可能是 resolved，亦可能是 rejected，any() 会忽略掉所有被拒绝的 promise，直到“完成”一个。

#### 空值合并运算符 Nullish Coalescing Operator

>  **空值合并运算符（`??`）**是一个逻辑运算符。

俩问号，用来判断左侧是否为 null 或 undefined，如果是，就返回右侧操作数，否则返回左边。

之前我们一般使用逻辑运算符来实现这个功能，例如：

```javascript
let foo = '';
let bar = foo || 'Hello!'; // "Hello"
```

这样确实可以实现在foo为 null 和 undefined 的时候将 "Hello" 赋值给 bar，但由于是逻辑运算符，当 foo 为任意“逻辑非”的值时，例如false、0、空字符串、NaN，都会将右值赋值，显然不是我们想看到的。

新的空值合并运算符就可以解决这个问题：

```javascript
let foo = '';
let bar = foo ?? 'Hello!'; // ''
```

#### 可选链操作符

在我们不确定某个值是否存在时，例如：

```javascript
let id = user && user.info && user.info.id;
let name = user && user.info && user.info.getName && user.info.getName();
```

这样的校验十分必要，否则在数据非预期情况下，就会出现 `Uncaught TypeError:` 的错误

于是可选链操作符就登场了，大大简化了逻辑：

```javascript
let id = user?.info?.id;
let name = user?.info?.getName.?();
```

当试图访问的对象不存在时，左值会设为 undefined，这时可以配合 ?? 操作符来设置默认值：

```javascript
let nickname = user?.info?.nick_name ?? 'NickName'
```

#### BigInt 数据类型

js 巨坑之一：目前的数值都保存成了 64 位浮点数，导致 js 在一些运算精度方面很吃亏，也不能表示太大的数字。

BigInt 可以解决这个问题。BigInt 通过数字后加 n 表示：

```javascript
let maxSafeInt = Number.MAX_SAFE_INTEGER; // 9007199254740991
let bigNumA = BigInt(maxSafeInt); // 9007199254740991n

maxSafeInt + 2; // 9007199254740992 有误
bigNumA + 2n; // 9007199254740993n 正确

// 支持十六进制、八进制等
const hugeHex = BigInt("0x1fffffffffffff"); // ↪ 9007199254740991n
```

需要注意几点：

1. BigInt 都是有符号的，所以无法使用 ```>>>(无符号右移)``` 。
2. 为了兼容asm.js，不能使用单目(+)运算符。
3. BigInt为整，计算产生的小数部分会被省略。

对于 Number 来说：

1. 不能混合运算

   ```javascript
   1n + 1; // Uncaught TypeError: Cannot mix BigInt and other types, use explicit conversions
   ```

2. 不严格相等，但宽松相等

   ```javascript
   0n === 0 // false
   0n == 0 // true
   ```

3. 可以比较，可以排序，但sort传函数参时如果设计混合计算，发生错误

   ```javascript
   2 > 1n // true
   
   [111,333n,2,5n,4].sort() // [111, 2, 333n, 4, 5n] 注意默认是ascii顺序
   [111,333n,2,5n,4].sort((a,b)=>a-b) // Uncaught TypeError: Cannot mix BigInt and other types, use explicit conversions
   ```

   ```(a,b)=>a-b ``` 是一种便捷的排序方式，通过 Number 的差值符号来实现正序、倒叙，但在 BigInt 和 Number 的混合数组中，计算会发生错误，应该使用比较写法：

   ```javascript
   [111,333n,2,5n,4].sort((a,b)=>{
   	if (a<b) return -1;
   	if (a>b) return 1;
   	return 0;
   })
   // [2, 4, 5n, 111, 333n] 大小升序
   ```

#### 动态 Import

在ES2020之前的设计中，import 语句会被引擎在编译时处理，于是从根本上就无法实现动态加载。

而新的提案的 import() 函数支持了动态加载，这是一个运行时脚本，所以可以实现按需加载、条件加载等功能：

```javascript
let useMyMath = true;
if (useMyMath) {
  const myMath = await import('./myMath.js');
  console.log(myMath.add(1, 2));
} else {
  console.log(1 + 2);
}
```

#### globalThis

全局对象在 JS 的不同环境中的获取方式有很大区别：

- Web浏览器中 window、self、frames
- WebWorker 中的 self
- Node 里的 global
- 非严格模式下的 this

真是令人头大，于是ES2020引入了 **globalThis** 关键字，用于统一不同环境下的全局对象访问。

#### String.prototype.matchAll

>  **`matchAll()`** 方法返回一个包含所有匹配正则表达式的结果及分组捕获组的迭代器。

我正则比较菜，还是看 [MDN](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll) 吧

#### Class 的私有属性

以 `#` 作为开头，可以将方法、 变量等设为私有：

```javascript
class Foo {
  #info = "Hello"
  greet() { console.log(this.#info) }
}

let foo = new Foo()
foo.greet() // "Hello"
foo.#info // Uncaught SyntaxError: Private field '#info' must be declared in an enclosing class
```