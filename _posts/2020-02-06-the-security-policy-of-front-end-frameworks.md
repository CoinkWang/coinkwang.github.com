---
layout: post
title: 探索主流前端框架的安全模型
subtitle: Angular、React、Vue
author: Coink
date: 2020-02-06
tag: 
    - tech
---



### Perface

在前端逐框架逐渐兴起后，开发者似乎轻松了许多。MVVM 框架带来了诸多便利，不过最终产出在本质上还是 Web 前端，由于 Web 与用户交互的特性，其中所隐藏的安全隐患不可忽视。

前端在整个 Web 应用中，负责数据的处理与展示，以及承担用户与后端交互的媒介。通过参考主流前端框架中采取的安全策略，一方面，可以协助我们更好的使用框架；另一方面，也能够提示我们，在脱离框架时，应该如何应对所面对的安全问题。

可以预见的是，当 WebAssembly 这个潘多拉盒子打开后，前端安全将会面临更加严峻的考验。但今天，先讨论一下我所接触过的三个前端框架：Angular、React 以及 Vue，看看它们在前端安全方面，都做了哪些保障。

### Vue

#### 转义

Vue 在处理模版绑定的数据、以及动态绑定数据时，会对内容进行转义，也就是 HTML 实体编码，例如：

```HTML
<script>alert(1)</script>
```

会被转义成：

```HTML
&lt;script&gt;alert(&quot;hi&quot;)&lt;/script&gt;
```

处理过后，无论是通过双括号绑定还是 `v-bind` 中的可控内容，都不会引入恶意闭合的代码，保证了安全性。

但并不是进行转义就是绝对安全了：

对于 `v-bind:href` ，Vue 并不会对传入的 url 地址进行过滤，这时可能被传入恶意 js 伪协议，形如`javascript:`。所以在接收用户输入，或是渲染 url 时候，也应该进行过滤，Vue 文档给出了一个推荐：[sanitize-url](https://www.npmjs.com/package/@braintree/sanitize-url)，它的作用就是将 url 中可能有害的部分进行过滤，例如：

```javascript
sanitizeUrl('jAvasCrIPT:alert(document.domain)'); // 'about:blank'
sanitizeUrl(decodeURIComponent('JaVaScRiP%0at:alert(document.domain)')); // 'about:blank'
```

同时又不会影响正常 url 和无害伪协议：

```javascript
sanitizeUrl('www.example.com'); // 'www.example.com'
sanitizeUrl('mailto:hello@example.com'); // 'mailto:hello@example.com'
```

#### 注入 HTML

当然，并不是任何时候都会对符号进行转义，当我们**真的**需要通过注入渲染 HTML 时，可以使用以下方式（来自Vue文档）：

- 使用模板：

  ```html
  <div v-html="userProvidedHtml"></div>
  ```

- 使用渲染函数：

  ```javascript
  h('div', {
    domProps: {
      innerHTML: this.userProvidedHtml
    }
  })
  ```

- 使用基于 JSX 的渲染函数：

  ```HTMl
  <div domPropsInnerHTML={this.userProvidedHtml}></div>
  ```

这部分内容不会被转义，所以在开发时要特别留意，不能在沙盒以外渲染 UGC。

#### 注入样式

Vue 中，用户可以绑定 Style ，这其中也隐藏着安全问题。例如攻击者可以通过透明 CSS 来进行点击欺骗，或是伪造登陆页面钓鱼。

Vue 推荐开发者只允许在沙盒内进行 CSS 控制，或是通过对象语法，只控制属性“值”：

```HTML
<a
  v-bind:href="sanitizedUrl"
  v-bind:style="{
    color: userProvidedColor,
    background: userProvidedBackground
  }"
>
  click me
</a>
```

#### 注入 JavaScript

渲染用户提供的 JS 是非常危险的，除非使用沙盒（例如我们常用的在线预览工具CodePen）进行隔离。

#### 其他

总的来说，Vue 推荐开发者针对用户输入进行过滤，不要随意渲染 UGC。

Vue 推荐开发者去学习 XSS 、 CSRF 的相关知识，前后端配合，使用 CSRF Token 等方式进行协作，保障安全。

### React 

与上文提到 Vue 中的常见问题一样，React 的渲染机制也存在容易造成 XSS 的问题，React 的做法也是如此：

#### 转义

React 支持的 JSX 语法可以将用户内容渲染，因为 React 默认会对内容进行转义，以HTML实体编码进行输出（来自[官方文档](https://zh-hans.reactjs.org/docs/introducing-jsx.html#jsx-prevents-injection-attacks)）：

```JSX
const title = response.potentiallyMaliciousInput;
// 直接使用是安全的：
const element = <h1>{title}</h1>;
```

#### 注入 HTML

React 中对于 `innerHTML` 的替换方法名称是有所**警示**的： `dangerouslySetInnerHTML` ，但是 React 能做的也只有用 `dangerous` 来“警示”，毕竟框架并不知道你的真正意图。

#### SSR on React

SSR 的常见做法是预先传递一些数据，可能存在 UGC，如果不加过滤直接`JSON.stringify`解析，也会导致问题。来看 Redux 是怎么做的（通过一些前些年的漏洞分析得知，Redux 刚开始是没有对`preloadedState`进行replace处理的，具体可以查看[The Most Common XSS Vulnerability in React.js Applications](https://medium.com/node-security/the-most-common-xss-vulnerability-in-react-js-applications-2bdffbcc1fa0)）：

```js
function renderFullPage(html, preloadedState) {
  return `
    <!doctype html>
    <html>
      <head>
        <title>Redux Universal Example</title>
      </head>
      <body>
        <div id="root">${html}</div>
        <script>
          // WARNING: See the following for security issues around embedding JSON in HTML:
          // https://redux.js.org/recipes/server-rendering/#security-considerations
          window.__PRELOADED_STATE__ = ${JSON.stringify(preloadedState).replace(
            /</g,
            '\\u003c'
          )}
        </script>
        <script src="/static/bundle.js"></script>
      </body>
    </html>
    `
}
```

React 也推荐使用 [serialize-javascript](https://github.com/yahoo/serialize-javascript) 来对输入进行无害化处理。

### Angular

Angular 对于安全性的[文档](https://angular.cn/guide/security)比较详细。

#### 过滤

>  为了系统性的防范 XSS 问题，Angular 默认把所有值都当做不可信任的。 当值从模板中以属性（Property）、DOM 元素属性（Attribte)、CSS 类绑定或插值等途径插入到 DOM 中的时候， Angular 将对这些值进行无害化处理（Sanitize），对不可信的值进行编码。
>
> **Angular 的模板同样是可执行的**：模板中的 HTML、Attribute 和绑定表达式（还没有绑定到值的时候）会被当做可信任的。 这意味着应用必须防止把可能被攻击者控制的值直接编入模板的源码中。永远不要根据用户的输入和原始模板动态生成模板源码！ 使用[离线模板编译器](https://angular.cn/guide/security#offline-template-compiler)是防范这类“模板注入”漏洞的有效途径。

Angular 定义了四个安全环境 - HTML，样式，URL，和资源 URL：

- **HTML**：值需要被解释为 HTML 时使用，比如当绑定到 `innerHTML` 时。
- **样式**：值需要作为 CSS 绑定到 `style` 属性时使用。
- **URL**：值需要被用作 URL 属性时使用，比如 `<a href>`。
- **资源 URL**的值需要作为代码进行加载并执行，比如 ` <script src> ` 中的 URL。

Angular 会对前三项中种不可信的值进行无害化处理，但不能对第四种资源 URL 进行无害化，因为它们可能包含任何代码。在开发模式下， 如果在进行无害化处理时需要被迫改变一个值，Angular 就会在控制台上输出一个警告。

Angular 不推荐用户直接使用 DOM API，用户应尽量使用模板。

#### 可信任的值

对于已经审查过，并且功能确实需要注入的情况下，Angular 提供了这些方法：

- `bypassSecurityTrustHtml`
- `bypassSecurityTrustScript`
- `bypassSecurityTrustStyle`
- `bypassSecurityTrustUrl`
- `bypassSecurityTrustResourceUrl`

开发者要明白前缀提示的意义，切勿滥用这些方法。

#### HTTP 层漏洞

Angular 包含了一个 HttpClient，在使用时，其中包含了基于 CSRF-TOKEN 的防御机制，详细做法请参考：[安全：XSRF 防护](https://angular.cn/guide/http#security-xsrf-protection)。当然，也是需要后端配合的。

### What I learnd

1. 说来说去，最重要的还是：输入输出过滤。入库前、输出前，**全部**都应该进行无害化过滤/转义。最好使用白名单，若不放心可以引入辅助库，不要想当然的去过滤单个关键词（例如只过滤 `javascript` ，就可以用 `jAvAsCrIpT` 绕过）。
2. 框架推送漏洞更新补丁的时候尽快更新掉。
3. SSR 的输入渲染之前也需要检查。

### Useful links

[Angular Guide - Security](https://angular.cn/guide/security)

[Vue.js 文档 - 安全](https://cn.vuejs.org/v2/guide/security.html)


