def test_intersection(node_a, node_b):
    encoder = 0b0000
    if (node_a.span[0] <= node_b.span[0] <= node_a.span[len(node_a.span)-1] and
            node_a.span[0] <= node_b.span[len(node_b.span)-1] <= node_a.span[len(node_a.span)-1]):
        encoder +=0b10
    if (node_b.span[0] <= node_a.span[0] <= node_b.span[len(node_b.span)-1] and
            node_b.span[0] <= node_a.span[len(node_a.span)-1] <= node_b.span[len(node_b.span)-1]):
        encoder +=0b01
    return encoder

def same_interval(node_a, node_b):
    if test_intersection(node_a, node_b)  == 0b11:
        print(node_b.name, node_a.name, "SAME INTERVAL")
        return True
    return False

def b_subset_of_a(node_a, node_b):
    if test_intersection(node_a, node_b) == 0b10:
        print(node_b.name, "SUBSET OF ", node_a.name)
        return True
    return False

def b_superset_of_a(node_a, node_b):
    if test_intersection(node_a, node_b) == 0b01:
        print(node_b.name, "SUPERSET OF", node_a.name)
        return True
    return False

def disjoint(node_a, node_b):
    if test_intersection(node_a, node_b)  == 0b00:
        print(node_b.name, "AND", node_a.name, "DISJOINT ")
        return True
    return False

##TODO: Correct the logic here

