def has_intersection(node_a, node_b):
    encoder = 0b0000

    if node_a.span[0] <= node_b.span[0] <= node_a.span[1]:
        encoder += 0b1000
    if node_a.span[0] <= node_b.span[1] <= node_a.span[1]:
        encoder +=0b0100
    if node_b.span[0] <= node_a.span[0] <= node_b.span[1]:
        encoder +=0b0010
    if node_b.span[0] <= node_a.span[0] <= node_b.span[1]:
        encoder +=0b0001

    if encoder == 0b1111:
        print("encoder value:", encoder, "\t", node_b.name, node_a.name, "are the same interval")
    if encoder == 0b1100:
        print("encoder value:", encoder, "\t", node_a.name, "consumes", node_b.name)
    if encoder == 0b0011:
        print("encoder value:", encoder, "\t", node_b.name, "consumes", node_a.name)
    if encoder == 0b0000:
        print("encoder value:", encoder, "\t", node_b.name, "and", node_a.name, "are disjoint")




    return encoder
