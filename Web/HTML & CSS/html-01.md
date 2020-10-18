- [Resource Used](#resource-used)
- [Is HTML a language?:](#is-html-a-language)
- [Important HTML Tags:](#important-html-tags)
- [Attributes](#attributes)
  - [Classes](#classes)
  - [ID's](#ids)
  - [Naming & Semantics](#naming--semantics)
  - [camelCase vs kebab-case?](#camelcase-vs-kebab-case)
  - [What's a boilerplate project/code?](#whats-a-boilerplate-projectcode)
  - [Meta HTML](#meta-html)
  - [`Script`, `Style` and `Link`](#script-style-and-link)
# Resource Used

[Brian Holt's Notes on Web Dev](https://btholt.github.io/intro-to-web-dev-v2/)
# Is HTML a language?:

You don't run HTML. It's like English Language. English isn't a programming language, and similarly HTML is not a real programming language. It's just content and pictures on a page. You just state what you want.

# Important HTML Tags:


So let's explore some of the essential tag types.

h1, h2, h3, h4, h5, and h6 – Headings. These are the six levels of headings and subheadings you can have. You can see up top of this page we have HTML which is an h1 and then below that we have Types of Tags which is an h2. An h2 is a subheading to an h1. An h3 is a subheading to a h2. Some schools of thought say each page should only have one h1. I'm of the opinion that just use these as it feels appropriate to. Like formatting a Microsoft Word document, there's no "correct" way to do it, just different ways that make more or less sense. Example:
```html
<h1>Document Title</h1>.
```
p – Paragraph. You'll put a paragraph of text together inside of a p tag. Only text goes in p tags. Each one of these paragraphs is a p tag. Example: <p>A paragraph of text</p>.
a – Anchor. An a tag is a link to somewhere else. This is a link that goes nowhere. Every a tag needs a destination of where the link should take you. We'll talk about that in the Attributes section. Example: 
```html
<a href="https://www.frontendmasters.com">Frontend Masters</a>.
```
div – Short for division. A div is sort of like a cardboard box. It's not really anything by itself; it's more defined by what's in it. It's a generic container tag for grouping together other things. You'll use a lot of divs. Very useful with CSS. In general, you want to group together "like" things into a containing tag (like a div) to keep them together. If you have a website with a list of blog posts that each have paragraphs, titles, images, etc. you'll group each post together in a div or other container-type tag typically.
span – A container for small pieces of text. If a div is like a cardboard box, a span is like a Ziploc bag. It doesn't change the styling of anything by itself but it allows you use CSS and JavaScript later to make that text different in some way. Example: <p>Here is some text. <span>This text is in a span</span> but it doesn't look any different.</p>
ol, ul, and li – Both ol and ul represent lists. In fact, this list of various tags is a ul! A ul is an unordered list: it's a list of things that could be shuffled and still mean the same thing. If I asked you to list all the teams in a sports league, or all the characters on a TV show, those could be presented in any order. An ol is an organized list: what comes first matters. If I ask you to list out the ten most populous cities in the world, there is an order to that and changing the order makes the list incorrect. In either list, each item in the list is an li. Example: <ul><li>Bob</li><li>Eve</li><li>Alice</li></ul>
button – A … button. A button can be used by JavaScript to respond to a user clicking it, or it can be used by a form to signal a user has completed filling it and it should submit the data. Think of it like a doorbell to your house: you can put the doorbell button there but it's not going to do much unless you connect it to the buzzer. Example: <button>Click me!!</button>
img – An image. You use this to load images onto the page. This can be confusing because you can use CSS to bring in images too. The key difference is that when the image is apart of the content, like a diagram that shows data you're talking about or a picture that shows something from the article, it should be an img tag. If it's a nice background image or something that's for decoration of your website, use CSS. An img tag needs a src to say where the image is coming from and alt to say what is in the image for screen readers so that the image will still be useful to blind people, people who are hard of seeing, and Google and Bing search engines. img are always self-closing tags. Example: <img src="http://www.placepuppy.net/100/100" alt="an adorable puppy" />
input – Browser inputs. Sometimes you need to gather input from the user. Luckily for us, the browser is already really good at doing that. It gives us several types of inputs that you can use. One of the most common ones is the text input, seen here: 
you can type in me
. You can also have these input tags do numbers, dates, colors, checkboxes, radio buttons, and others. We'll explore them more later when we talk about forms. Inputs are always self-closing tags. Example: <input />.
textarea – Similar to an input but for a lot more text. You'd type long-form responses in here that could linebreaks in it (a linebreak happens when you hit "return" or "enter" on your keyboard.) Despite never having anything inside of a textarea, it is not a self-closing tag. HTML is a really old language and so we have to live with some old quirks. Example: <textarea></textarea>
select and option — Sometimes you want to limit a user to a certain group of options to select from. What country you're from, what month you were born in, etc. A select is a user-interactive input that a user can select an option from a dropdown menu. An option is one of the available options. Each option needs a value that will be sent back to the server if the user select that option. What's inside of the option is what shown to the user. Example: <select><option value="seattle">Seattle</option><option value="portland">Portland</option><option value="san-francisco">San Francisco</option></select>
form – A group of html tags related to gathering data from a user. This will be some combination of input, textarea, and select tags. You can then use this form element to send that data to your server. A form tag itself doesn't show anything; it's a just a container for the other tags. We'll use them more later. For now, just know they exist. Example: <form><input /><textarea></textarea></form>
table, tr, and td – Like making a table in Word or Excel. If you have a table of data, this is the best way to display it. Just for your context, we used to do terrible, awful things with tables to make websites, way back when. Because of that, some tutorial will tell you never ever use tables. That's not good either because when you have tabular data (something you would put into Excel) then tables are very useful. The table is the container for the whole table, tr represents a row, and td represents one cell in the table. Example: <table><tr><td>(0,0)</td><td>(1,0)</td></tr><tr><td>(0,1)</td><td>(1,1)</td></tr></table>
There are many, many, many more tags. This is just a highlight of some of the more useful, common ones.

# Attributes

## Classes
Classes are special attributes that can go on any tag, though some you won't use it with. While a class does nothing itself, it allows that tag to be found by your CSS and your JavaScript. Using our house analogy, you don't want to make a rule that says "all walls are south facing." It's nonsensical and you could never build a house that way. Instead, you'd make a rule that says "walls marked `south-facing-wall` are south facing." This is what classes allow you to do: they allow you to mark your HTML so you can write rules and code to govern them later. Let's see what that looks like.

```html
<div class="header">
  <h1 class="header-title">My Great Blog</h1>
</div>
<div class="blog-posts">
  <div class="post">
    <h1 class="post-title">When Not to Overextend House Metaphors</h1>
    <p class="post-text"> … </p>
  </div>
  <div class="post">
    <h1 class="post-title">Another Great Blog Post</h1>
    <p class="post-text"> … </p>
  </div>
</div>
```

## ID's
IDs are far less useful than classes. Whereas you'll be using classes everywhere and frequently, you should be using IDs very sparingly. As you see in our above blog-posts HTML, we can re-use classes like post and post-title. This is extremely important. As a coder, you want a piece of code and use it a lot. As coders, we want to write as little code as possible (which we'll explore why later, for now trust me.) For now, be satisfied that I get to write a little bit of code that governs post and have it affect every post on the page.

Let's contrast that with IDs. When you designate something with an ID, you're affirming that this is the only one of those on your website. Not even just that page, but your whole website. Sometimes that is useful; just not very often. Some other coders and tutorials will tell you to never use IDs; I think that's misguided. IDs are a sledgehammer. Most problems don't require a sledgehammer. However sometimes you have problems that need a sledgehammer and then you're really grateful that you have one.

So why do we have them? Well, they're really old and have been around forever so that's the mean reason. Another reason that is very useful about IDs is that I now can make a link that takes you directly to that ID in the page. Try clicking this link (it won't leave this page.)

```html
<div class="header">
  <h1 class="header-title">My Great Blog</h1>
</div>
<div class="blog-posts">
  <div id="house-metaphors-post" class="post">
    <h1 class="post-title">When Not to Overextend House Metaphors</h1>
    <p class="post-text"> … </p>
  </div>
  <div class="post">
    <h1 class="post-title">Another Great Blog Post</h1>
    <p class="post-text"> … </p>
  </div>
</div>
```

## Naming & Semantics

Generally, with classes, you want to name things semantically. This is a fancy word (often used when talking about HTML) that you want use tags and name things as close to what the thing does and not what it looks like.

## camelCase vs kebab-case?

The very reason we use kebab-case and not camelCase in HTML & CSS, is because, HTML is not case-sensitive, and so, camelCase loses all its significance when an HTML file gets on the web-browser.

## What's a boilerplate project/code?

A boilerplate code/project is a set of lines of code which we copy-paste from the previous project. In the HTML, this means the `head` tags, the `body` tags, etc:

## Meta HTML

```html
<!DOCTYPE html> 
<!-- The `lang` attribute is used to setup language -->
<html lang="en"> 
<!-- You can setup viewport in the head as well -->
  <head>
    <title>My amazing HTML Document</title>
  </head>
  <body>
    <h1>Check this out</h1>
    <!-- Your amazing HTML here -->
  </body>
</html>
```

## `Script`, `Style` and `Link`

`<script></script>, <style></style>, and <link />`
We're about to talk about CSS and JavaScript, but know they have the above three tags, `script, style, and link` are used for them, script being used for JavaScript and the latter two for CSS.