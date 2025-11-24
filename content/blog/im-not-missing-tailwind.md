---
title: I'm Not Missing Tailwind
date: 2025-11-23
taxonomies:
  categories: [Web Development]
  tags: [CSS, Tailwind]
draft: true
---

While converting this site from [Hugo to Zola](@/blog/2025-11-16-converting-from-hugo-to-zola.md), I elected to dispense with Tailwind; partially because I wanted to try using plain CSS and partially because Zola and Tailwind don't make an easy pairing. Along the way, I discovered that I don't like Tailwind as much as I thought I did.

<!--more-->

For on thing, Tailwind classes get pretty verbose:

```html
<li>
  <a aria-current="page" aria-label="Page {{ $k }}" class="flex items-center justify-center px-4 h-10 leading-tight text-gray-400 bg-white border border-gray-300 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-600" role="button">{{ $k }}</a>
</li>
```

That makes it more difficult to understand just how an element is being styled. But worse than that, if those styles are applied in various places around the site to style multiple instances of the same element, it's very hard to be sure all the instances are the same. When the elements are first created, copying and pasting the styles works fine. But if changes have to be made later, consistency is a real problem.

Tailwind has the `@apply` directive to address this. You create a class of your choice and define it like this:

```css
.your-class {
@apply w-30 flex items-center justify-center px-4 h-10 leading-tight text-primary bg-lightest border border-gray-300 hover:bg-primary-highlight dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-red-600;
}
```

It works. But guess what? The more you de-clutter and de-duplicate your Tailwind classes, the more your code starts to look like regular CSS! You are back to coming up with class names and switching context from HTML to CSS files, which are things Tailwind tries to eliminate.

I don't like Tailwind's default color system, either, especially for gray or neutral colors. The steps between colors at the lightest and darkest ends of the spectrum have too little contrast. It's hard to tell one from the next one.

<img src="/images/post-images/tailwind-neutral-scale.png" alt="Neutral Scale" style="display: block; margin: 1em auto 1em auto">

You may not be able to tell, but there are 11 shades of neutral shown.

For this site I used 11 shades of neutral, too, but each step has a constant change in contrast so you can tell one from the other.

[This article](https://dev.to/finnhvman/grayscale-color-palette-with-equal-contrast-ratios-2pgl) got me started and [his codepen](https://codepen.io/finnhvman/pen/QWwYYwJ) allowed me to calculate each color value. I used a contrast ratio of 1.33 which gave me the 11 steps I wanted.

You can replace Tailwind's defaults, of course, but that gives up the simplicity of the system and you're back to regular CSS, again.

I do have a Hugo version of this site on standby in the event I need it, and I've used the `@apply` directive to simplify the styling for it. Maybe I'll leave it like that, but I do like the flexibility of regular CSS and that won't go out of style.
