from main import *

if __name__ == '__main__':
    file = read_file("/home/william/saas-landing-page/index.html")
    format = format_elements(file)
    element_list = organize_tags(format)
    dicts = create_element_dict(element_list)
    node_list = create_nodes(dicts)
    #dicts = sort_nodes(dicts)
    tree = build_tree(HtmlNode(None, None), node_list, 0 )


    #pretty.pprint(nodes)
