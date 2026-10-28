import re

text = "Hello, Ashutosh Kumar a brilliant person."
result = re.split(r'(\s)',text)
print(result)

result = [item for item in result if item.strip()]
print(result)