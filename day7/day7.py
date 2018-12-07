import networkx as nx
import re

def read_file():
    first = set()
    second = set()
    G = nx.DiGraph()
    prog = re.compile("Step ([A-Z]) must be finished before step ([A-Z]) can begin.")
    with open("input.txt") as f:
        lines = f.readlines()
    for line in lines:
        r = prog.match(line.strip())
        if not r.group(1) in G:
            G.add_node(r.group(1))
        if not r.group(2) in G:
            G.add_node(r.group(2))
        if not G.has_edge(r.group(1),r.group(2)):
            G.add_edge(r.group(1),r.group(2))
        first.add(r.group(1))
        second.add(r.group(2))
    return (G,first- second)

def duration(step):
    return 60+ord(step)-64

if __name__ == "__main__":
    G,starter = read_file()
    path = list()
    to_visit = sorted(starter,reverse=True)

    while len(to_visit) > 0:
        node = to_visit.pop()
        path.append(node)
        neighbours = G[node]
        for n in neighbours:
            if not n in to_visit and not n in path:
                allCompleted = True
                for u,v in G.in_edges(nbunch=n):
                    if not u in path:
                        allCompleted = False
                if allCompleted:
                    to_visit.append(n)
        to_visit = sorted(to_visit,reverse=True)
    print("".join(path))

    end_letter = path[-1]
    path = list()
    to_visit = sorted(starter,reverse=True)
    
    second = 0
    workers = list()
    # Trabajo Actual, segundo que termina
    workers.append(['.',0])
    workers.append(['.',0])
    workers.append(['.',0])
    workers.append(['.',0])
    workers.append(['.',0])
    def full_workers(workers):
        full = True
        for w in workers:
            if w[0] == ".":
                full = False
        return full
    end = False
    while not end:
        if len(to_visit) == 0 or full_workers(workers):
            second += 1
        for i in range(0,len(workers)):
            if workers[i][1] <= second:
                if workers[i][0] != ".":
                    path.append(workers[i][0])
                    neighbours = G[workers[i][0]]
                    for n in neighbours:
                        if not n in to_visit and not n in path:
                            allCompleted = True
                            for u,v in G.in_edges(nbunch=n):
                                if not u in path:
                                    allCompleted = False
                            if allCompleted:
                                to_visit.append(n)
                    to_visit = sorted(to_visit,reverse=True)
                if workers[i][0] == end_letter:
                    print("Finish point")
                    print("Seconds: %d" % second)
                    end = True
                if len(to_visit) > 0:
                    node = to_visit.pop()
                    workers[i][1] = second+duration(node)
                    workers[i][0] = node
                else:
                    workers[i][0] = "."
        
        


