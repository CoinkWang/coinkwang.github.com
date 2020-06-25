---
layout: post
title: 123
subtitle: 原作者: Lea Verou, 授权翻译: Coink
author: Coink
date: 2020-06-24
alert: 
    content: 
    type: success
---

原文地址：https://lea.verou.me/2020/06/refactoring-optional-chaining-into-a-large-codebase-lessons-learned/

原作者:  Lea Verou

授权翻译：Coink

---

![https://memegenerator.net/img/instances/84759102/-.jpg](https://memegenerator.net/img/instances/84759102/-.jpg)

现在 [可选链操作符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/%E5%8F%AF%E9%80%89%E9%93%BE) 已被 [支持](https://caniuse.com/#feat=mdn-javascript_operators_optional_chaining)，我最终也决定用它来重构 [Mavo](https://mavo.io/)  (好好好，我们也提供了一个转译版本来适配旧浏览器，都坐下)。我从很久前就在等待这一刻，我觉得可选链操作符是自 箭头函数 和 模板字符串 以来，最重要的 JS 语法改进。没错，我认为它甚至比  async/await 还要重要，因为能被它改进的代码实在是太多了，属性访问操作几乎*遍布各处*。

首先，如果你还不知道什么是*可选链*，让我们先来了解一下。

你是否知道，不去检查 `foo`、`foo.bar`、`foo.bar.baz` 是否存在就直接取 `foo.bar.baz()` 是不可行的，会得到错误（error）吗？，所以调用之前要先做一些判断：

```javascript
if (foo && foo.bar && foo.bar.baz) {
    foo.bar.baz();
}
```

或者：

```javascript
foo && foo.bar && foo.bar.baz && foo.bar.baz();
```

有人甚至[“妙用（contort）”对象解构来试图解决这个问题](https://medium.com/@ismail9k/use-javascript-optional-chaining-today-f0b1d080b3c6)。但使用可选链操作符，你就可以直接：

```javascript
foo?.bar?.baz?.()
```

它支持普通属性访问，括号访问 （`foo?.[bar]`），甚至函数调用（`foo?.()`）。真贴心，对吧？？

是的，*大部分时候*，确实有**很多**代码可以用它来简化，很不可思议。

但是也有一些值得注意的东西。



## 需要寻找的片段

假设你决定继续进行代码重构。那么要寻找哪些东西呢？

当然最明显的：把  `foo && foo.bar` 替换成 `foo?.bar`。

还有他的条件判断版本，比如我们开头提到的，用 `if()` 对链的部分和整体进行检查。

还有一些其他场景：

### 三元运算

``` javascript
foo? foo.bar : defaultValue
```

现在可以改写为：

``` javascript
foo?.bar || defaultValue
```

或者用另一个新的操作符，[空值合并操作符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator)（*nullish coalescing operator*）：

``` javascript
foo?.bar ?? defaultValue
```

### 数组检查

```javascript
if (foo.length > 3) {
    foo[2]
}
```

现在变成了：

```javascript
foo?.[2]
```

要注意这并不能代替真正的数组检查，比如 `Array.isArray(foo)` 这样的。不要因为这么写更短就用鸭子类型（duck typing）把数组检查给替换掉了。我们[十多年前](http://perfectionkills.com/instanceof-considered-harmful-or-how-to-write-a-robust-isarray/)就不干这种事了。

### 正则表达式匹配

忘了这些吧：

```javascript
let match = "#C0FFEE".match(/#([A-Z]+)/i);
let hex = match && match[1];
```

这些也是：

```javascript
let hex = ("#C0FFEE".match(/#([A-Z]+)/i) || [,])[1];
```

现在只需要：

```javascript
let hex = "#C0FFEE".match(/#([A-Z]+)/i)?.[1];
```

在这种情况下，我甚至可以删掉两个实用函数（utility functions）并用可选链运算符替换他们的引用。

### 特征检测（feature detection）

在简单的情况下， `?. `可以替代特征检测，举个例子：

```javascript
if (element.prepend) element.prepend(otherElement);
```

变成：

```javascript
element.prepend?.(otherElement);
```

### 避免矫枉过正

这么修改也许看起来很诱人：

```javascript
if (foo) {
    something(foo.bar);
    somethingElse(foo.baz);
    andOneLastThing(foo.yolo);
}
```

改为:

```javascript
something(foo?.bar);
somethingElse(foo?.baz);
andOneLastThing(foo?.yolo);
```

*别这么干*. 这样会让 JS 运行时对  `foo` 的检查从一次变成三次。也许你会辩解：这些东西对性能表现的影响已经不重要了。但这会让阅读你代码的人不断重复：在他们的大脑里处理三次这个过程，而非一次。 而且一旦需要对 `foo` 添加其他属性访问，就得新增其他检查，而原来的写法只需要修改检查部分即可。

## 注意事项

### 赋值前依旧需要检查

也许你想像这样转换：

```javascript
if (foo && foo.bar) {
    foo.bar.baz = someValue;
}
```

变为:

```javascript
foo?.bar?.baz = someValue;
```

很遗憾，这样不行，会出错。 以下是我们代码库中的实际片段：

```javascript
if (this.bar && this.bar.edit) {
    this.bar.edit.textContent = this._("edit");
}
```

我开开心心地把他们重写为:

```javascript
if (this.bar?.edit) {
    this.bar.edit.textContent = this._("edit");
}
```

目前为止，一切都还行，代码运行良好。但我仔细一想，等一等... 我还需要条件判断吗？或许我可以直接：

```javascript
this.bar?.edit?.textContent = this._("edit");
```

坏了， `Uncaught SyntaxError: Invalid left-hand side in assignment`。这样不行，还是得要判断，实际上我也一直在这么做，我很高兴我在编辑器里使用了 ESLint 来在实际运行代码前就得到警告。

### 该放 ?. 的地方没放，不该放的地方放上了

需要注意，如果你在用可选链操作符重构一个很长的链，你经常需要插入很多个 `?.` 给每个可能存在或不存在的成员属性，否则一旦链返回了 `undefined` ，就会发生错误。

又或者，有时候你只是 *认为* 你做对了，但却把 `?.` 符放错了地方，

这是一个真实的例子。我刚开始是这样重构的：

```javascript
this.children[index]? this.children[index].element : this.marker
```

变为：

```javascript
this.children?.[index].element ?? this.marker
```

然后得到了一个 `TypeError: Cannot read property 'element' of undefined` 报错。 哦吼！之后我添加了一个 `?.` 来修复

```javascript
this.children?.[index]?.element ?? this.marker
```

虽然成功运行了，但引入了多余的步骤。评论有人指出，我只需要 *移动* 操作符即可：

```javascript
this.children.[index]?.element ?? this.marker
```

正如 [评论指出的](https://lea.verou.me/2020/06/refactoring-optional-chaining-into-a-large-codebase-lessons-learned/#comment-4963612068) ，在用可选链操作符替换数组长度检查时要格外小心，这可能对性能产生不利影响，因为对数组的越界访问在 V8 中属于负优化的代码（因为它会去检查原型链是否也具有这种属性，而不仅仅是确定数组中有没有这个索引）。

### 不细心可能会导致 bug

如果你和我一样，继续重构狂欢（refactoring spree），就很容易在一些单点引入可选链操作符之后，不经意间*改变了代码行为*，并且引入一些不容易注意到的 bugs。

#### null vs undefined

把 `foo && foo.bar` 替换成 `foo?.bar` 可能是最常见的场景。大多数情况下，它们工作结果一致，但并不代表全部情况。当 `foo` 的值是 `null` 时，前者返回  `null`，而后者返回 `undefined`。在需要区分的场景下，会导致 bug 潜入。这估计也是最此类重构最常见的引入问题。

#### 相等判断

在这样转变代码时要小心:

```javascript
if (foo && bar && foo.prop1 === bar.prop2) { /* ... */ }
```

转变成:

```javascript
if (foo?.prop1 === bar?.prop2) { /* ... */ }
```

在第一种情况下，条件条件只有在 `foo` and `bar` *都*为真的情况下才为真。然而在第二种情况下，如果 `foo` and `bar` 都为空值（nullish），条件判断也会为真，因为两边的操作数都返回了 `undefined`。

哪怕第二个操作数不含可选链操作符，这个bug都可能出现。只要它可能是 `undefined` ，就有意外相等的可能性。

#### 运算符优先级清单

还有一件值得注意的事：[可选链操作符的运算优先级比 `&&`高](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)。这在你替换同时使用了 `&&` 和相等判断 的表达式时，这显得尤为重要。（不）等号夹于 `?.` 和 `&&` 之间时，优先级低于前者，高于后者。

```javascript
if (foo && foo.bar === baz) { /* ... */ }
```

这里是什么在和 `baz` 相比较？ `foo.bar` 还是 `foo && foo.bar`? 因为 `&&` 的优先级比 `===` 低，它和下面的写法等价：

```javascript
if (foo && (foo.bar === baz)) { /* ... */ }
```

注意如果 `foo` 为假，那么后续的条件判断甚至不会被执行。但当我们用可选链操作符重构之后，这样就是在把 `(foo && foo.bar)` 和  `baz` 做比较：

```javascript
if (foo?.bar === baz) { /* ... */ }
```

当 `baz` 为 `undefined` 时，很明显能看到不同语义影响执行的结果。目前的情况下， `foo` 是空值（nullish）时，我们会进入条件判断，这时可选链操作符会返回 `undefined`，基本就是上面描述的情况。在其他大多数情况下，不会有很大的不同。但是，当使用*不等*运算符而不是相等运算符时，它仍然具有相同的优先级，这可能会非常糟糕。来比较这个：

```javascript
if (foo && foo.bar !== baz) { /* ... */ }
```

和这个:

```javascript
if (foo?.bar !== baz) { /* ... */ }
```

现在，每当`foo` 是空值（nullish）、`baz` 不是  `undefined` 时，我们都会进入条件判断！这细微的区别在边界情况都不容易被注意，更别提正常情况了！ 😱

#### 返回语句

比起仔细想清楚，我们更容易脑子一热忘记返回语句(Rather obvious after you think about it, but it’s easy to forget return statements in the heat of the moment. )。你不能做这样的替换：

```javascript
if (foo && foo.bar) {
    return foo.bar();
}
```

替换为:

```javascript
return foo?.bar?.();
```

第一种情况中，返回是有条件的，而第二种情况总是会返回。如果条件是函数中的最后一段语句，这不会引起问题，但如果不是，它就会改变控制流（control flow）。

#### 有时候，它也能解决 bug！

看一下我在重构过程中遇到的这段代码：

```javascript
/**
 * Get the current value of a CSS property on an element
 */
getStyle: (element, property) => {
    if (element) {
        var value = getComputedStyle(element).getPropertyValue(property);

        if (value) {
            return value.trim();
        }
    }
},
```

你能找到问题所在吗？如果  `value` 是一个空字符串（从上下文来看，它很可能是），函数会返回 `undefined`，因为空字符串值为假（falsy）！用可选链操作符重写就能解决这个问题：

```javascript
if (element) {
    var value = getComputedStyle(element).getPropertyValue(property);

    return value?.trim();
}
```

现在，如果 `value` 是一个空字符串，它会正确返回空字符串，并只会在 `value` 为空值（nullish）时返回 `undefined`。

#### 寻找调用变得更加困难了

Razvan Caliman 在 Twitter 上指出:

![twitter_screenshot](https://i.loli.net/2020/06/24/rizKMP79ONbuCRF.png)

感谢分享您的经验！

当在火狐开发者中工具使用可选链操作符时，我们必须考虑的一件事是，重构时，它会对方法在项目全局搜索中的结果造成影响，例如  `object.destory()` 之于  `object?.destory()` 。



## 后记

重构结束时，Mavo 轻便了 2KB 并且**减少**了 37 行代码。然而却让转译后的版本**多了** 79 行和 9KB(!)。

[这里是相关的commit](https://github.com/mavoweb/mavo/commit/a8fb2e1f8c478aa7110aaf13ade57a40825ec71e)，供您参考。我尽了最大努力，在此提交中不引入任何本次重构无关的东西，所以代码的 diff 部分可以当作可选链操作符的示例。它有 104 行添加项和 141 行删除项，我打赌它有大约 100 个实践中的可选链操作符例子。希望能帮上你的忙！

