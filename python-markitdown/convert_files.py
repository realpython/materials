from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("./data/markdown_syntax.docx")
print(result.markdown)
