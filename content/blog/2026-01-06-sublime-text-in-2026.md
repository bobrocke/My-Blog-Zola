---
title: Sublime Text in 2026?
date: 2026-01-06
slug: 2026-01-06-sublime-text-in-2026
taxonomies:
  categories: ["Development"]
  tags: ["Sublime Text"]
draft: false
---

I was using [Sublime Text](https://www.sublimetext.com/) back in 2016, or so. After using [Atom](https://atom-editor.cc/), [VS Code](https://code.visualstudio.com/), and most recently [Zed](https://zed.dev/), I'm almost back to Sublime Text (now as version 4) again. Is Sublime Text truly a solid option in 2026?

<!--more-->

<figure style="float: right; width: 20%; margin: 1em 0em 1em 1em">
  <img src="/images/post-images/logos/sublime-logo.png" alt="Sublime HQ Logo" >
</figure>

Although I think Zed (written in Rust) is the future of native code editors, Zed is still relatively new. Sublime Text is plenty fast (it's written in C++), has a wealth of packages (even though some are getting pretty old and unmaintained), support on Discord is excellent, and is more easily customized than Zed.

## The Good

Sublime Text is "done", as in essentially feature complete. More modern features (things that came along after Sublime Text's foundation was established) are available as packages. LSP servers [can be connected](https://lsp.sublimetext.io/) by a number of different packages. And AI is supported by several packages which give access to GitHub Copilot, ChatGPT, and OpenAI. In truth, AI is not as fully supported as in Zed or Cursor, which were built with AI in mind.

Language support in Sublime Text is excellent. I often use [Liquid](https://shopify.github.io/liquid/), [Gotmpl](https://pkg.go.dev/html/template), and [Vento](https://vento.js.org/); all of their implementations as packages are better than those for Zed and even VS Code. The [ColorHelper](https://packagecontrol.io/packages/ColorHelper) package is excellent. And, to match Zed and VS Code, the [Terminus](https://packagecontrol.io/packages/Terminus) package adds a tightly integrated terminal pane.

<img src="/images/post-images/logos/zed-logo.png" alt="Zed Logo" style="float: left; width: 20%; margin: 1em 1em 1em 0em">

If a Zed extension exists for the programming language you use and you like the results of its syntax highlighting, all is well. But if you need to tweak something, get ready for a lot of studying. The tree-sitter parsers and grammar used by Zed are pretty tough to learn and Zed makes it hard to even tell what scope has been applied to which part of your code.

Sublime Text uses the old TextMate approach to syntax definitions (.tmLanguage), as does VS Code, but evolved to the newer .sublime-syntax. Both use regex to match parts of the code to specific scopes. Those scopes can then be styled by color schemes (.sublime-color-scheme) which are based on, and evolved, from the TextMate .tmTheme format. It's very easy to find what scope has been applied and then to edit the color scheme to taste.

My configuration for Sublime Text is every bit as good as Zed for my purposes.

## The Less Good

But it's not all a bed of roses. You can see a bit of Sublime Text's age in some of its interfaces. Here are the find and code completion panels (click to enlarge). The buttons and their size are perfectly functional, but old-school.

<figure style="float: left; width: 50%; margin: 1em 1em 1em 0em">
  <a class="glightbox" href="/images/post-images/2026/sublime-interface-find.png"><img src="/images/post-images/2026/sublime-interface-find.png" alt="Sublime Text Find Interface"></a>
  <figcaption>The Find Box</figcaption>
</figure>

<figure style="float: left; width: 50%; margin: 1em 1em 1em 0em">
  <a class="glightbox" href="/images/post-images/2026/sublime-interface-completion.png"><img src="/images/post-images/2026/sublime-interface-completion.png" alt="Sublime Text Completion Interface" ></a>
  <figcaption>The Code Completion Interface</figcaption>
</figure>

Keep an eye out for old packages meant for Sublime Text 3; some of those may not behave well in version 4. And, as you search for helpful packages, you'll start to notice many that are several years old. Sublime Text is no longer the modern darling of the developer community.

VS Code and Zed are free; Sublime Text costs $99 for a three-year license. After that, you must renew in order to continue getting updates. The good news is that one personal license covers all your computers and operating systems. The price makes Sublime Text an oddity in today's market, but it's not supported by large corporations (VS Code by Microsoft and Zed by $42 million in investor funding). You can see some of that lack of funding in the slow release cycle (the last update was in May).

After having said that Zed is the future, it's just not ready for me yet. My major complaints are all around language support for Vento, Gotmpl, and Liquid. None are excellent and none are as good as Sublime Text's. Perhaps I put too much weight on syntax coloring in the editor, but I find it makes the code easier to read and can often point out syntax errors before build time.

So, until, and if, Zed language support improves, it looks like it is, indeed, Sublime Text in 2026.
