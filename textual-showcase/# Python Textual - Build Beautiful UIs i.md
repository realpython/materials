# Python Textual - Build Beautiful UIs in the Terminal

## Getting to Know the Python Textual Library

A brief introduction to the document.

## Installing Textual
 `$ python -m venv venv`
`. venv/bin/activate`
`$ python -m pip install textual[dev]`
- Explain why we are installing the [dev] variant. (This variant includes the Textual a)
 Note that textual is built on `rich` (Link to `rich` showcase article).

## Creating Your First Textual App
Walk through a simple “Hello Textual” application to introduce the App class and the its compose method.
(example: basic Textual app)
Textual apps can be run in a text terminal, or in the browser.

## Exploring Textual's Widgets
Textual offers a wide variety of pre-built widgets, such as buttons, checkboxes, input fields, progress bars, and more.
 With Textual, you can apply different styles to text, such as foreground and background colors, bold, italic, and underline styles, and more. Textual fully supports Unicode characters, allowing you to display and handle text in various languages, symbols, and emojis. This makes it suitable for internationalization and localization.
(Example: display styled static text and emojis using Python code only.)
(example: show buttons and textboxes in a simple layout)
(example: show an input field interacting with checkboxes and a progress bar, explaining  how to use DOM queries to reference them in code)
Show how to use the Textual console for development and debugging. (TBD - if textual[dev] is a problem in iOS, we may have to ignore the Textual console)

## Laying Out Your Textual UI
Textual's widgets can be nested and combined to create intuitive user interfaces and mimimize code re-use. Container classes support multiple views, split panes, and more. With TCSS, you can separate the visual layout of your application from its logic. 
### Vertical and Horizontal Containers
### Grid container    

## Styling Your Application With Textual
Textual implements a modified and simplified subset of Cascading Style Sheets (CSS), and styles can be modified dynamically, enabling you to create responsive, visually appealing interfaces with a minimum of code. Textual supports all the rich text styling options of the `rich` library, incuding text colors and attributes, frames and emojis, and even animations.  
(Example: display styles implemented externally using a .tcss file)

## Interactive Programming With Events and Callbacks
◦ Using Callbacks for Interactivity
Textual is not just a component toolkit, but an application framework that provides classes and services for building fully-fledged applications. Its event-driven programming model lets you define callbacks for various events, such as key presses, mouse clicks, and timer events. This facilitates building interactive and responsive TUIs.
(example: radio-buttons, timer  and progress bar in a dynamic display)

## Conclusion
In this tutorial, you have seen some of the capabilities of Textual. Alongside its support for rich text display and styling, Textual is an application framework with its own event loop and support for user interaction.

## Next Steps
The examples you have seen here will have given you some idea of the power and versatility of Textual. But there's a lot more to discover about this framework! There's a full tutorial at the Textualize website, along with the official Textual guide. Will McGugan, the developer of Rich and Textual, was interviewed on the Real Python podcast. It's worth noting that Textual has come a long way since this interview!

