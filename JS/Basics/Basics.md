- [1. Why to Learn JavaScript?](#1-why-to-learn-javascript)
    - [Why is JavaScript the future?](#why-is-javascript-the-future)
  - [This is an important questions that need to be answered before diving in.](#this-is-an-important-questions-that-need-to-be-answered-before-diving-in)
- [2. How does a web-page work anyway?](#2-how-does-a-web-page-work-anyway)
    - [🎐 Another Analogy](#-another-analogy)
- [3. What is JavaScript?](#3-what-is-javascript)
  - [3.1. The definition:](#31-the-definition)
    - [3.1.1. Explanation](#311-explanation)
- [4. A Briefer History of JavaScript](#4-a-briefer-history-of-javascript)
- [5. How does JS run? Is it Interpreted or Compiled?](#5-how-does-js-run-is-it-interpreted-or-compiled)
- [6. Why is it called a “Scripting Language” ?](#6-why-is-it-called-a-scripting-language-)
- [7. Why the name JavaScript?](#7-why-the-name-javascript)
- [8. What is ECMA Script, LiveScript?](#8-what-is-ecma-script-livescript)
- [9. What is V8 Engine? What is Spider-Monkey?](#9-what-is-v8-engine-what-is-spider-monkey)
- [10. What to do from here?](#10-what-to-do-from-here)

# 1. Why to Learn JavaScript?

### Why is JavaScript the future?

## This is an important questions that need to be answered before diving in.

In the future, I believe there would be only 2 languages that would be ruling the software-world: JavaScript & Python. (I know it's quite far-fetched, but just listen to my arguments.)

Ofcourse, there are a multitude of languages used for hardware programming, production & engineering, education, medical sciences, military, space research and many other domains. But, every software that a non-technical "common man" uses, irrespective of its domain, would move to the cloud, and would use Machine Learning to make things easier and more automated.

The world is moving towards a dcentralized, cloud-based, microservice architecture. Let me explain what that means.

So, when you say that softwares would run on the cloud, this just means, that your browsers work as the Operating System for your software applications. For example, Microsoft Excel works on Windows 10 and MacOS Operating System. But Google Docs, runs inside the Chrome Browser. So, Chrome Browser becomes the Operating System for running a software like Google Docs.

Since 2015, there are 100s (if not 1000s) of companies shifting moving their entire softwares to the cloud. In the future, I believe almost every software: from entertainment to education, from health to food, would run on the web, inside the browser.

When this happens, there's going to be only 1 language that rules everything. And thats JavaScript (atleast for now).

There are already a lot of JavaScript Frameworks, and new are coming up to make JavaScript Development easier for developers, and it does not make sense to develop a project using Vanilla (pure) JavaScript. But it's really important to understand the core concepts of JavaScript, so that you can pickup any JavaScript Framework now, or in the future, and quite easily catch up.

# 2. How does a web-page work anyway?

I‘m sure you‘ve seen a Create-Account Page, on any website: ![Login UI Page](./media/UI_1.jpg)

In the above image:

1. There is a toggle-button group, asking whether you are a “Brand/Business” or
   an “Agency”
2. There are 4 text-fields, which ask for your personal details.
3. There are 2 checkboxes, which ask whether you agree to the terms and whether
   you want to sign up to newsletter
4. And finally, there is the “Create Account” Button.

Now let’s look at this image from the Web-Browser‘s Perspective (Take Google
Chrome for example):

1. There is an HTML Code which tells the browser the following:
   1. The page contains 3 labels, 2 toggle-buttons, 4 text-fields, 2 checkboxes
      and a submit-button.
   2. There is a parent “div”(group) which contains all the above components,
      and some child “div(s)” which separate groups of components(there is a div
      for the toggle-buttons, text-fields and checkboxes)
2. There is a CSS code which tells the browser:
   1. That the highlight color for all those components is blue
   2. The font-family is Montserrat
   3. The text-color is gray
   4. And many more attributes like spacing, width and height, margin, padding
      etc. of the components.
3. Finally, there is another piece of code (JavaScript) that tells the browser:
   1. What to do when the user clicks on “Agency” Toggle Button
   2. Which error message to display when all the text-fields are not filled
      correctly.
   3. What to do when “Sign up” Checkbox is checked/unchecked.
   4. And finally, what action(s) to take when “Create Account” button is
      clicked.

> ### 🎐 Analogy
> #### If a web-page is compared to a human body, then:
> **HTML** is the skeletal system of the body. **CSS** is the muscles, skin, hair, (everything that makes the body attractive and not just a bunch of bones stuck together.) Finally, **JavaScript** is the brain of the body. The skeletal system and muscles of the body may be amazing in themselves, but without the brain, they‘re of no use. The brain sends instructions and commands to the body parts to behave and function in a certain manner.

### 🎐 Another Analogy
> #### If a web-page is compared to a house, then:
> To build a house, you need some tools (Text Editor, Browser, Command-Line etc.). Once you have your tools ready, you then need the building materials: the 2x4s, the shingles, the dry wall, windows, doors, carpets. After you bought the building materials, you use your tools, to build a bare-bone house. This is the HTML. However, this house does not look pretty and is not functional. It's not going to have any color or any sort of elaborate structures. It's going to be bland, inert, and boring. Likewise, you can create a website that's just HTML, but it's going to be a black-and-white document with no style or interactivity. 
> In order to arrange the style, and generally make the house beautiful and useful, you are going to have some blueprints. These blueprints are a set of rules: the 2x4 goes here, the shingle goes on the roof, paint a particular wall blue, and a window goes here.You define a bunch of rules that dictates that if some item matches this condition, then some rule is applied to it. If it is a 9x15 wall, it goes on the south side of the house. This is the CSS of your house, or the cascading style sheets. CSS is a series of rules that define that if you are an HTML thing that matches this condition, then apply some style to it. If you are the first paragraph in an article, your font size is 25px and your font color is blue.
> Okay, so now we have a well arranged and nice looking house. Now, being the modern age and me wanting all the gadgets, I want to install a whole slew of smart home devices. I want it so when I pull in the driveway with my smart-enabled car that the garage door opens, the lights turn on, the thermostat turns on the heat, the TV is set to continue my favorite TV show, and the smart cooker begins cooking dinner. I am adding behavior to my house; I am adding a layer of programming on top of what exists. This is like frontend, or client-side, JavaScript. It's adding a layer of behavior on top of your website. Do you want to pop up a message if a user clicks a button? Do you want to refresh the stock-ticker on the page so it's accurate? Do you want to change the picture that's showing on your page every few seconds? These are things you'd typically do with JavaScript. And like all the smart home devices, having JavaScript on your page isn't always necessary. These website, for example, wouldn't need any JavaScript whatsoever because it's just showing information and not really interactive (links are an HTML thing, you don't need JavaScript for them.) It does have JavaScript because it makes it easier for me but it'd be easy to do with zero JavaScript.
> To recap:
> 1. The HTML is the structure. It's going to contain all the text, the various images tied to the text, and it will generally group things together. Just like the drywall in your house, HTML doesn't do anything other than exist. It relies on other things to do things for it and to it.
> 2. The CSS is the blueprint. It's all the rules of what goes where, what color it is, what size it is, what font it is, what the decorative background images are, like HTML, CSS doesn't do anything, it's just a set of rules that describe what things go where and how they look.
> 3. The frontend / client JavaScript is the smart home. It's all the cool pre-programmed stuff you can tell your house to do. JavaScript is what can change the HTML and CSS to react to various stimuli.
> 4. The backend code (we'll still use JavaScript) is the pizza place. It's a place where we can request things from and it will send back what we ask for. Or we can send things to it, like when you upload a new photo to your social media account. One server serves many clients, just like one pizza place serves many homes.

# 3. What is JavaScript?

JavaScript was initially created to make web pages “alive” and interactive
(having complex animations, clickable buttons, popup menus, etc.).

They can be written right in a web page’s HTML and run automatically as the page
loads.

```html
<html>
  <head>
    <title>My First Page</title>
  </head>
  <body>
    <!-- Create a button, which shows on the HTML Page -->
    <button type="button" onClick="firstFunction()">Click Me!</button>

    <!-- Script tag tells HTML that there's a JavaScript Code here-->
    <script>
      // Function Definition of *firstFunction*
      function firstFunction() {
        alert("Hello World");
      }
    </script>
  </body>
</html>
```

The programs in this language are called scripts. Scripts are provided and
executed as plain text. They don’t need special preparation or compilation to
run.

In this aspect, JavaScript is very different from another language called Java.

## 3.1. The definition:

JavaScript is a high-level, interpreted or JIT compiled, prototype-based, multi-paradigm dynamic language with a non-blocking event loop concurrency model.
JavaScript® (often shortened to JS) is a lightweight, interpreted, or
just-in-time compiled object-oriented language with first-class functions. While
it is well-known as the scripting language for Web pages, many non-browser
environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat.

JS is a prototype-based, multi-paradigm, single-threaded, dynamic language,
supporting object-oriented, imperative, and declarative (e.g. functional
programming) styles.

---

### 3.1.1. Explanation

Let’s go over all those terms one-by-one:

Firstly, JS (From now on, I will be referring to JavaScript® as **JS** for
simplicity) is a language that

> 🧩 Explanation:

# 4. A Briefer History of JavaScript

The first mainstream browser “Mosaic” was developed in Jan 1993, by Marc
Andreessen for UNIX Systems. Later that year in September, it found its way on
to Macintosh and Windows.

But there was no JavaScript yet.

Later on, Marc went about to co-found the company “Netscape”. And within a
couple of years, The Netscape Navigator already had 80% of the browser market
share.

Marc realised that websites needed to be more dynamic and that just HTML and CSS
could not suffise that. Developers needed a glue language to add aliveness and
interactivity to websites.

A man named Brenden Eich was hired for the job.

And 10 days later, JavaScript was born. Well, it wasn‘t called JavaScript back
then, it was called “Mocha”.

It had syntax like Java, First-Class functions like Scheme, Dynamic Typing like
Lisp, and Prototypal Inheritance like Self.

Mocha was eventually renamed to “LiveScript” and shipped with the first beta
releases of Netscape 2.0. But then in December 1995, they renamed it to
JavaScript, because it sounded like the cool lightweight cousin to the hottest
programming language of the day, Java!

In 1990, Sir Tim Berners Lee developed the first internet browser on a NeXT
Computer System.

But, nobody knew what the internet was back then.

# 5. How does JS run? Is it Interpreted or Compiled?

Let‘s first understand the basic difference between an interpreted language and
a compiled language.

> 📚 Interpreted Language: A programming language, wherein code is executed line
> by line. The interpreter looks at every line, and if it‘s syntax is valid, it
> will execute, and otherwise give a runtime error. Python is a famous
> interpreted language.

> 📚 Compiled Language: A programming Language, wherein code is converted into a
> machine understandable code by a compiler and then executed by the system.
> JAVA is a famous compiled language. The compiler converts the `.java` code
> into a `.bin` file, which is then executed by the JVM (Java Virtual Machine).

JS was initially launched as an interpreted language. But today, it‘s a
technology affecting every single human being on the planet, and the way JS runs
in the browser has significantly changed. JavaScript is now universally
JIT(Just-In-Time) compiled, either to bytecode (like Java and C#), or directly
to machine code (like C and C++). And modern engines offer an optimization
phase, similar to most traditional compiled languages.

V8 Engine, which runs on the Chrome Browser as well as the Node Environment
compiles JavaScript directly to native machine code before executing it.

Even the SpiderMonkey Engine (Firefox) includes a just-in-time compiler (JIT)
that compiles JavaScript to machine code.

JavaScript tells a browser what to do and how to process things just the same
way that a shell script, php, or any other scripting language does for their
respective hosts.

# 6. Why is it called a “Scripting Language” ?

A scripting/extension language is a programming language that allows some
control of a single (or many) software application(s). Languages chosen for
scripting purposes are often much higher-level than the language used by the
host application. The idea of a scripting language is one that instructs a host
to carry out a series of actions (a lot like an actor reading from a script).

In simpler terms, JavaScript is not a programming language in strict sense.
Instead, it is a scripting language because it uses the browser to do the work.
Eg.:- If you command an image to be replaced by another one, JavaScript tells
the browser to go do it. And so, the programs written in this language are
called scripts. They can be written right in a web page’s HTML and run
automatically as the page loads.

# 7. Why the name JavaScript?

# 8. What is ECMA Script, LiveScript?

# 9. What is V8 Engine? What is Spider-Monkey?

# 10. What to do from here?

