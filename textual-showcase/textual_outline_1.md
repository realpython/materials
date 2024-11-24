# Instructions
This is a **Package Showcase (PS)**. It's a regular article and follows all **regular pipeline** steps.
Package showcases should introduce the reader to one particular package. It could be a standard library module/package, but possibly more often a popular or up-and-coming third-party library available on PyPI.
The showcase articles should be **short** and quick to write, and allow us to **rank early** for interesting SEO opportunities. As we build more content around a package, we can also use the showcase as a kind of hub linking to more in-depth tutorials and step-by-step projects. This article should work as a reader's first encounter with the package.
A showcase article should be **practical** and show the readers a few small, self-contained, interesting examples. The article should introduce the readers to some of the capabilities of the package, and whet the reader's appetite for more. The showcase article will typically _not_ display all features of a package. Note that the practical examples should be _much_ smaller than a typical step-by-step project.
The keyphrase will often be `python <package_name>` although you can use a different one if SEO research brings up better alternatives.
During work on this article, you and your reviewers should be conscious of keeping the scope small. If you find other interesting features of the package that can be exposed during research for this article, feel free to add a proposal for an in-depth tutorial about the package or a step-by-step project exploring a specific use case further.
---
# Outline
## Who is this article for?
The ‘ideal reader’ will be familiar with basic Python syntax and the idea of classes. They will be interested in learning about a UI framework that depends only on the capabilities of the text terminal.

## How will learning about this package benefit your ideal reader?
They will become aware of the Textual TUI, a lightweight and attractive alternative to the numerous other UI frameworks, one that has low hardware requirements and can be used in a system with limited or no graphics capabilities, eg with a Raspberry Pi or over SSH.

## Which (approximately three) features will you highlight in this showcase?
- Textual widgets, including at least the most commonly useful widgets such as buttons, checkboxes, input fields and screens
- Textual layouts, and the use of Textual CSS in separating layout from functionality 
- Textual’s widget library and opportunities for extending it
- Textual’s event-driven architecture – how to use event handlers and callbacks
- Textual’s Screen API

## Which features of the package will you explicitly NOT cover?
- Extending the widget library
- How the event loop is implemented

## Title Ideas
- Python Textual: Build Beautiful UIs in the Terminal
- Textual: Build a Beautiful UI With Text

## Code Examples
A “Hello Textual” example to illustrate the basics of creating a Textual app.
A layout example with static labels and styles defined in code.
A similar example, but the styles and layout defined in external TCSS.
An interactive example using buttons and DOM queries.

## Outline / Main Sections
The Python Textual library provides a powerful and flexible framework for building text-based user interfaces (TUIs). It offers a range of features that allow developers to create interactive and engaging console applications. (Some advantages of TUIs - low resource requirements, work over SSL, good replacement for any CLI app...)
### Installing Textual
 `$ python -m venv venv`
`. venv/bin/activate`
`$ python -m pip install textual[dev]`
- Explain why we are installing the [dev] variant. (This variant includes the Textual a)
 Note that textual is built on `rich` (Link to `rich` showcase article).

 ### Your first Textual app
Walk through a simple “Hello Textual” application to introduce the App class and the its compose method.
(example: basic Textual app)
Textual apps can be run in a text terminal, or in the browser.

### Exploring Textual's widgets
Textual offers a wide variety of pre-built widgets, such as buttons, checkboxes, input fields, progress bars, and more.
#### Static and Labels
#### Buttons
#### Inputs
#### Advanced widgets 
 With Textual, you can apply different styles to text, such as foreground and background colors, bold, italic, and underline styles, and more. Textual fully supports Unicode characters, allowing you to display and handle text in various languages, symbols, and emojis. This makes it suitable for internationalization and localization.
(Example: display styled static text and emojis using Python code only.)
(example: show buttons and textboxes in a simple layout)
(example: show an input field interacting with checkboxes and a progress bar, explaining  how to use DOM queries to reference them in code)
Show how to use the Textual console for development and debugging. (TBD - if textual[dev] is going to be a problem in iOS, we may have to ignore the Textual console)

### Laying out your Textual UI
Textual's widgets can be nested and combined to create intuitive user interfaces and mimimize code re-use. Container classes help to structure your layout, and support multiple views, split panes, and more. With TCSS, you can separate the visual layout of your application from its logic. 
#### Vertical and Horizontal containers
#### Grid container 
#### Docking widgets

### Styling your application with Textual
Textual implements a modified and simplified subset of Cascading Style Sheets (CSS), and styles can be modified dynamically, enabling you to create responsive, visually appealing interfaces with a minimum of code. Textual supports all the rich text styling options of the `rich` library, incuding text colors and attributes, frames and emojis, and even animations.  
(Example: display styles implemented externally using a .tcss file)

### Interactive Programming With Events and Callbacks

#### Using Callbacks for Interactivity
Textual is not just a component toolkit, but an application framework that provides classes and services for building fully-fledged applications. Its event-driven programming model lets you define callbacks for various events, such as key presses, mouse clicks, and timer events. This facilitates building interactive and responsive TUIs.
(example: radio-buttons, timer  and progress bar in a dynamic display)

### Conclusion
In this tutorial, you have seen some of the capabilities of Textual. Alongside its support for rich text display and styling, Textual is an application framework with its own event loop and support for user interaction.
#### Next steps
The examples you have seen here will have given you some idea of the power and versatility of Textual. But there's a lot more to discover about this framework! There's a full tutorial at the Textualize website, along with the official Textual guide. Will McGugan, the developer of Rich and Textual, was interviewed on the Real Python podcast. It's worth noting that Textual has come a long way since this interview!

==========================================================


Charles de VilliersOct 17, 2024, 9:21 PM
Hi@leodanispozoramos ,
Thanks for taking over!
I didn't mean to say that Textual is a GUI framework (I wanted to present it as an alternative to GUI frameworks) but that probably wasn't clear from my outline. Absolutely yes, it is a TUI framework and I’ll make that clearer in the text.
I think the target reader needs to be at an intermediate level to understand how to use the framework (eg extending and composing classes). But you’re right that understanding the asyncio/generator machinery is not really necessary - I can just mention it in passing, or leave it out altogether.
Reading the guidance for showcase articles at the top of this page, I’m not really sure how comprehensively I should cover the features. The guidance heading asks for “approximately three” features to highlight, but your list and sample TOC seem pretty comprehensive. If we’re presenting selected features: I’d argue that creating an app isn’t really a “feature” (as it’s the whole point of the framework), but perhaps the most important features from your list would be (some examples of) the widgets, layouts, and events. One could throw in some actions too. Or do you feel that we need to cover all the features?
Code examples - do you mean short snippets to illustrate specific features? I did provide some code in https://github.com/realpython/materials/tree/textual-showcase/textual-showcase/ but those were “larger” examples - perhaps a little too large for a “showcase” article? I certainly plan to run up some shorter code examples for individual widgets, etc.
Yes, I do need to show how to create apps first!
I’ll skip the custom widgets and reactive properties, you’re right that those don’t really belong in a showcase.
I’m away until Thursday, but I’ll let you have some draft code next Friday. Meanwhile please let me know your thoughts on the above?
Edit
•
Add link as attachment
•
Delete
Leodanis Pozo RamosOct 17, 2024, 5:25 PM
@charlesdevilliers Hey!
I took over doing an outline review for this article. Here are my comments:
Who is this article for?
 
    • Would it be okay to say that Textual is a TUI framework instead of a GUI framework? I guess that the boundary isn't clear because Textual provides most of the widgets and functionalities that a GUI framework normally has. However, the apps run in a terminal window and that's an important difference.
    • We need to define the target reader's level: beginner, intermediate, or advanced. In this regard, topics like generators and asynio are kind of advanced topics.
How will learning about this package benefit your ideal reader?
 
    • Benefits are more like: being able to create TUI apps with Textual
    • Fact check: Textual seems to be a TUI framework rather than a GUI framework. So, can Textual be a real replacement for something like PySide6 or Tkinter?
    • If Textual is a TUI framework, then it'd be a good replacement for CLI apps because it provides a UI that's more friendly than a CLI.
Which (approximately three) features will you highlight in this showcase?
Would it be okay something like the following?
    • Creating an app
    • Widgets (the most commonly used)
    • Layouts
    • Actions
    • Events, callbacks
    • Screens
    • Textual CSS
Title Ideas
 
    • The titles reinforce the idea that Textual is a TUI framework. So, we should have uniform terminology throughout the article. We already have an article that uses Textual and it classifies it as a TUI framework: Build a Contact Book App With Python, Textual, and SQLite – Real Python
Code Examples
 
    • It'd be great to have the first draft of some of the planned code examples so that we can provide some feedback at this early stage. (However, it's not a showstopper requirement)
Outline / Main Sections
In general, the reader will benefit from sections that explain the main features of Textual as a TUI library. The section on features provides a compact list of those features.
In general terms, we could have a TOC that looks something like the following:
    • Installing Textual
    • Creating and Running a First App
    • Exploring Textual’s Widgets
        ◦ Labels
        ◦ Buttons
        ◦ Inputs
        ◦ ...
    • Laying Out Textual UIs
        ◦ Vertical Layouts
        ◦ Horizontal Layouts
        ◦ Grid Layouts
        ◦ Dock Layouts
        ◦ ...
    • Styling Textual UIs
    • Handling Events and Callbacks
    • Managing Screens
In the section on creating and running the app, we can consider the terminal and the browser.
The styling section can be moved up depending on our needs.
Note: The TOC above is just a suggestion. I just guess that a showcase article should show what the library has to offer.
Here are comments about the outline:
    • Here, we're starting that Textual is a TUI framework.
    • The textual[dev] can be problematic in zsh, which is the default shell in macOS.
    • We probably need to start by showing how to create apps before we start styling them.
    • Would it be okay to call them widgets rather than pre-built components? The library's doc call them widgets?
    • Not sure we need to dive into creating our own widgets since this is a showcase.
    • Reactive properties seems like an advanced topic. Would it be worth to discuss it in a showcase article?
 
Thanks for putting the outline together. Please, let me know if you have any questions.
Leodanis

