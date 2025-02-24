tools = ["Python", "Django", "Flask", "pandas", "NumPy"]
tools_set = {tool.lower() for tool in tools}

print(tools_set)
print("python".lower() in tools_set)
print("Pandas".lower() in tools_set)
print("Numpy".lower() in tools_set)
