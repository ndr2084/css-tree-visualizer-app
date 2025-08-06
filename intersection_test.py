def test_intersection(node_a, node_b):
    encoder = 0b0000

    if (node_a.span[0] <= node_b.span[0] <= node_a.span[len(node_a.span)-1] and
            node_a.span[0] <= node_b.span[len(node_b.span)-1] <= node_a.span[len(node_a.span)-1]):
        encoder +=0b10
    if (node_b.span[0] <= node_a.span[0] <= node_b.span[len(node_b.span)-1] and
            node_b.span[0] <= node_a.span[len(node_a.span)-1] <= node_b.span[len(node_b.span)-1]):
        encoder +=0b01

    ##node_a is node_b and node_b is node_a
    if encoder == 0b11:
        print("ENCODER:", encoder, "\t", node_b.name, node_a.name, "SAME INTERVAL")
    ##node_b is subset of node_a
    if encoder == 0b10:
        print("ENCODER:", encoder, "\t", node_b.name, "SUBSET OF ", node_a.name)
    ##node_b is a superset of node_a
    if encoder == 0b01:
        print("ENCODER:", encoder, "\t", node_b.name, "SUPERSET OF", node_a.name)
    ##node_b and node_a are disjoint
    if encoder == 0b00:
        print("ENCODER:", encoder, "\t", node_b.name, "AND", node_a.name, "= DISJOINT ")

