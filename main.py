import re
import pprint as pretty
from collections import defaultdict

class HtmlNode:
    def __init__(self, value, name):
        self.name = name
        self.span = [0] * 2
        self.span[0] = value
        self.children = []  # a list of TreeNode instances

    def add_child(self, child_node):
        self.children.append(child_node)

    def add_interval(self, value):
        self.span[1] = value
"""
    for key in nodes:
        print(nodes[key])
        for elements in nodes[key]:
            print(elements)
            print(nodes[key][elements])
"""

def create_tree(nodes):
    #print(nodes[0]["body"][0])
    length = nodes[0]["body"][1]
    #print(length)

    initial = 0

    for height in nodes:
       # print(nodes[key])
        for element in nodes[height]:
            print(element,":",nodes[height][element])
                #print("height:", height)
                #print("element:", element)
                #print(nodes[height][element])





def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

#format the dom elements into key:value pairs
def format_elements(parsed_file):
    format = re.sub(r'\s+', ' ', parsed_file) #flattens file to one line
    format = re.sub(r'[\s\S]*?(?=<body>)', '', format) #removes from beginning of file up to (not including) <body>)
    format = re.sub(r'</body>.*', '</body>', format) #deletes anything after </body>
    format = re.sub("<div.*?>", "<div>", format) #cleans up open div tag and adds closing tag
    format = re.sub("<nav.*?>", "<nav>", format) #cleans up open nav tag
    format = re.sub("<a.*?>", "<a>", format) #cleans up open a tag
    format = re.sub("<img.*?>", "<img> </img>", format) #cleans up open img tag and adds closing tag
    format = re.sub("<script.*?>", "<script> ", format) #cleans up open script tag and adds closing tag
    format = re.sub("<i[^mg]*?>", "<i> ", format) #cleans up open i tag and adds closing tag
    format = re.sub("(?<=>).*?(?=<)", " ", format) #deletes all text between elements
    return format

def organize_tags(format):
    index = 0
    closing_tags = defaultdict(list)
    opening_tags = defaultdict(list)
    element_list = format.split(" ")
    #print(element_list)
    for element in element_list:
        #print(element[1])
        if element[1] == "/":
            closing_tags[element].append(index)
            index += 1
            continue

        if element[1].isalpha():
            opening_tags[element].append(index)
            index += 1
            continue

        else:
            raise Exception(f"HTML element formatting error: start of tag neither [a-zA-z] nor /: {element}, {element[1]}")

    #pretty.pprint(opening_tags)
    #pretty.pprint(closing_tags)
    return element_list
    #create_element_nodes(element_list)

def create_element_nodes(element_list):
    height = 0
    span = 0

    # Inner dict factory: returns defaultdict(list)
    #inner_dict = lambda: defaultdict(list)

    # Outer dict: default value is a new inner dict
    #height_map = defaultdict(inner_dict)
    element_span = lambda: defaultdict(list)
    nodes = defaultdict(element_span)

    for element in element_list:

        if element[1].isalpha():
            #print(element, height)
            #element_height[height].append([element, span])
            nodes[height][element[1:len(element)-1]].append(span)
            height += 1

        if element[1] == "/":
            height -= 1
            #print(element, height)
            nodes[height][element[2:len(element)-1]].append(span)
            #element_height[height].append([element, span])
        span += 1
    #pretty.pprint(element_height)
    return nodes

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = read_file("/home/william/saas-landing-page/index.html")
    format = format_elements(file)
    element_list = organize_tags(format)
    nodes = create_element_nodes(element_list)
    #pretty.pprint(nodes)
    create_tree(nodes)





##TODO: add logic to add the missing closing tags, this will be done in organize_tags and maybe a helper function.
