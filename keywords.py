help("keywords")
import keyword
print(keyword.kwlist)
test = keyword.iskeyword('elif')
length = len(keyword.kwlist)
print(test)
print(length)