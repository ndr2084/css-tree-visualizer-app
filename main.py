import re
from collections import defaultdict


def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

#remove all elements before <body>
def parse_file(formatted_file, keyword):
    keyword_index = file.index(keyword)
    formatted_file = file[keyword_index:]
    print(formatted_file)
    return formatted_file

#strips tags down to their element name only
def format_file(file):
    file = re.findall("<.*>", file)
    return file


#format the dom elements
def format_elements(parsed_file):
    format = re.sub("<nav.*>", "<nav>", parsed_file)
    format = re.sub("<a.*>", "<a>", format)
    format = re.sub("<script.*>", "<script> </script>", format)
    format = re.sub("<img.*>", "<img></img>", format)
    format = re.sub("<i.*>", "<i>", format)
    format = re.sub("<div.*>", "<div>", format)
    format = re.sub(r'\s+', ' ', format)
    format = re.sub(r'(?<=>)\w+.(?=<)' , ' ', format) #deletes words existing between elements
    format = re.sub(r'</body>.*', '</body>', format) #deletes anything after </body>
    organize_tags(format)
    return format

def organize_tags(format):
    index = 0
    closing_tags = defaultdict(list)
    opening_tags = defaultdict(list)
    element_list = format.split(" ")
    print(element_list)
    for element in element_list:
        if element[1] == "/":
            closing_tags[element].append(index)
        opening_tags[element].append(index)
        index += 1
    print (opening_tags)
    print (closing_tags)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = read_file("/home/william/saas-landing-page/index.html")

    formatted_file = format_file(file)
    parsed_file = parse_file(formatted_file, "<body>")
    print(format_elements(parsed_file))

##TODO: add logic to add the missing closing tags, this will be done in organize_tags and maybe a helper function.
