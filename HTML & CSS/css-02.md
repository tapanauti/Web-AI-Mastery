- [The Cascade](#the-cascade)
- [Specificity](#specificity)
  - [Adding 2 classes to a selector](#adding-2-classes-to-a-selector)
    - [Another Example](#another-example)
    - [Conclusion:](#conclusion)
- [ID's and !important](#ids-and-important)
  - [ID's](#ids)
- [Pseudo Class Selectors:](#pseudo-class-selectors)
- [PseudoElements](#pseudoelements)
- [Wild-Card Selector](#wild-card-selector)

# The Cascade

```css
<style>
  .title {
    color: red;
  }

  .title {
    color: green;
  }
</style>
<h1 class="title">Cool Title</h1>
```

Result:

<h1 class="title" style="color:green">Cool Title</h1>

> The above is a green title

# Specificity

## Adding 2 classes to a selector

```css
<style>
  .main-brand-3.title-3 {
    color: red;
  }

  .title-3 {
    color: green;
  }
</style>
<h1 class="title-3 main-brand-3">Branding here</h1>
```

This how you add two classes to one selector. Notice there's no space between the two class names (that means something else.) The selector `.main-brand.title` will only match a tag that has both classes. If has only one of the two, it will not match. As you may imagine, since it has two classes, it's more specific, and therefore it wins.

### Another Example

```css
<style>
  .title-4 {
    color: orange;
  }

  h1 {
    color: green;
  }
</style>
<h1 class="title-4">Another h1</h1>

```

This one is less obvious. Now we have to understand specificity even more. A class is considered more specific than a tag. So a class selector "overpowers" a tag selector. It's more specific. Therefore, even though the h1 selector comes last, the .title wins because it's more specific. This is why it's useful to do everything using classes; you don't need to worry about these specificity wars if everything is equal and try to have it some you don't have conflicting rules (which is not always possible.)

A useful but imperfect way to think about this is to think of specificity like a number. The class is like the tens digit, and the tag is like the ones digit. So something with one class selector would have a number 10 specificity and something with one tag selector would a specificity of 1. The bigger number wins. This is imperfect because one class selector is still bigger than 10 tag selectors, but it's a useful mental device to quickly evaluate mentally which tag is more specific.

Consider this:

```css
<style>
  h1.main-brand-5 {
    color: red;
  }

  .main-brand-5.title-5 {
    color: orange;
  }

  .main-brand-5 {
    color: green;
  }
</style>
<h1 class="title-5 main-brand-5">Another Example</h1>
```

The first selector, `h1.main-brand` is how you select both a tag and a class at the same time. As you may imagine, this is more specific than the third selector, `.main-brand`. If you remember our shortcut trick, the first selector would be `11`, the second would be `20`, and the last would be `10`, making the second selector the most specific, and indeed it is. The first selector isn't a good idea to do; using a tag and a class is usually a bad idea and means you're likely doing something weird in your code. I'm just showing you because it does happen in a lot in existing code.

Similarly, `.animal .dog` would mean that the proerty applies to a tag with a class of `dog`, which is present inside the the class of `animal`.

### Conclusion:

```html
<style>
  .animal.dog {
    color: green;
  }

  .animal .dog {
    color: red;
  }
</style>

<body>
  <div class="animal">
    <div></div>
  </div>
</body>
```

# ID's and !important

## ID's

```css
<style type="text/css">
  #site-brand {
    color: red;
  }

  h1.nav-head.nav-main.other-useful-class {
    /*
     * this class is way too specific; never have a class selector so long
     * it's ridiculous and just to illustrate a point
     */
    color: green;
  }
</style>
<h1 id="site-brand" class="nav-head nav-main other-useful-class">The Brand of my Website</h1>
```

Don't use these. Don't use these. Don't use these.

Because the specificity of ID's is very high. Consider this, if a tag is `1`, a class is a `10`, then an ID is `100`. And even further, an `!important` tag has the specificity of `1000`.

# Pseudo Class Selectors:

A typical example:

```css
<style>
  .hover-example {
    width: 100px;
    height: 100px;
    background-color: limegreen;
    color: white;
  }
  .hover-example:hover {
    background-color: crimson;
    width: 150px;
    height: 150px;
  }
</style>
<div class="hover-example">Hover your mouse over me</div>
```

> \*\* Its specificity is similar to that of a class.

[The best Link for Pseudo Class Selectors](https://css-tricks.com/pseudo-class-selectors/)

# PseudoElements

the basic idea is that you can CSS to add additional content/stylings to the HTML.

Typical Example: ::before

```css
div::before {
  content: "before";
}
div::after {
  content: "after";
}
```

This happens inside the HTML:

```html
<div>
  before
  <!-- Rest of stuff inside the div -->
  after
</div>
```

[PseudoElements](https://css-tricks.com/almanac/selectors/a/after-and-before/)

# Wild-Card Selector

```css
* {
  font-weight: 400;
}
```

`*` is called a `wild-card selector`. This applies the rule to everything inside the HTML. It's specificity is `1`.
