def test_intersection(node_a, node_b):
    encoder = 0b0000

    if (node_a.span[0] <= node_b.span[0] <= node_a.span[len(node_a.span)-1] and
            node_a.span[0] <= node_b.span[len(node_b.span)-1] <= node_a.span[len(node_a.span)-1]):
        encoder +=0b10
    if (node_b.span[0] <= node_a.span[0] <= node_b.span[len(node_b.span)-1] and
            node_b.span[0] <= node_a.span[0] <= node_b.span[len(node_b.span)-1]):
        encoder +=0b01

    if encoder == 0b11:
        print("encoder value:", encoder, "\t", node_b.name, node_a.name, "are the same interval")
    if encoder == 0b10:
        print("encoder value:", encoder, "\t", node_b.name, "is a subset of", node_a.name)
        if node_a.l is None:
            node_a.l = node_b
            print(node_a.l.name, "is now a child of", node_a.name)
        else:
            test_intersection(node_a.l, node_b)

    if encoder == 0b01:
        print("encoder value:", encoder, "\t", node_b.name, "is a superset of", node_a.name)

    if encoder == 0b00:
        print("encoder value:", encoder, "\t", node_b.name, "and", node_a.name, "are disjoint")
        print(node_b.name,"[", node_b.span[0], node_b.span[len(node_b.span)-1],"]")
        print(node_a.name,"[", node_a.span[0], node_a.span[len(node_a.span)-1], "]")



    return encoder
