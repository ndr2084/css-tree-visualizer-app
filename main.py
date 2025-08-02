import re
from collections import defaultdict

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

#format the dom elements into key:value pairs
def format_elements(parsed_file):
    format = re.sub(r'[\s\S]*?(?=<body>)', '', parsed_file, flags=re.IGNORECASE)
    format = re.sub("<nav.*>", "<nav>", format)
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
    print(format_elements(file))

##TODO: add logic to add the missing closing tags, this will be done in organize_tags and maybe a helper function.
