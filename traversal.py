def print_tree_visual(node, indent="", last=True):
    if node is not None:
        # Print the current node with its visual branch
        print(indent + ("└── " if last else "├── ") + node.name, node.span)

        # Prepare the indent for child nodes
        indent += "    " if last else "│   "

        # Collect non-null children
        children = []
        if node.l:
            children.append(node.l)
        if node.r:
            children.append(node.r)

        # Recursively print each child
        for i, child in enumerate(children):
            is_last = i == len(children) - 1
            print_tree_visual(child, indent, is_last)
