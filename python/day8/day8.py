from collections import deque



def read_node(start,numbers):
    length = 2
    child_nodes = numbers[start]
    metadata_entries = numbers[start+1]
    children = list()
    while child_nodes > 0:
        child_node = read_node(start+length,numbers)
        children.append(child_node)
        length += child_node["length"]
        child_nodes -= 1
    metadata = list()
    while metadata_entries > 0:
        metadata.append(numbers[start+length])
        length += 1
        metadata_entries -= 1
    node = dict([("length",length),("metadata",metadata),("children",children)])
    return node
        


def read_file(file):
    with open(file) as f:
        line = f.readline()
    numbers = [int(x) for x in line.split()]
    G = read_node(0,numbers)
    return G

def node_value(N):
    if len(N["children"]) == 0:
        return sum(N["metadata"])
    else:
        s = 0
        for i in N["metadata"]:
            if i-1 < len(N["children"]):
                s += node_value(N["children"][i-1])
        return s
        

def day8(file):
    G = read_file(file)

    to_visit = deque()
    to_visit.append(G)
    metadata_sum = 0
    while len(to_visit) > 0:
        N = to_visit.popleft()
        metadata_sum += sum(N["metadata"])
        to_visit.extend(N["children"])
    #print("METADATA SUM: %d" % metadata_sum)
    #print("NODE VALUE: %d" % node_value(G))
    return metadata_sum,node_value(G)
