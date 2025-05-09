def findGraph(nodes):
    processed_graphs = [[]]

    for i in range(len(nodes)):
        parts = nodes[i].split('/')
        for k in range(len(processed_graphs)):
            for j in range(1, len(parts)):
                g = [n for n in processed_graphs[k]]
                g.append(parts[j])
                processed_graphs.append(g)
            processed_graphs[k].append(parts[0])

    return processed_graphs

if __name__ == '__main__':
    nodes = ['1', '2', '3.0/3.1/3.2', '4.0', '5.0']
    print(findGraph(nodes))
    
    nodes = ['1', '2', '3.0/3.1/3.2', '4.0', '5.0/5.1']
    print(findGraph(nodes))

    nodes = ['Priyansha', 'Sharma', 'P/S']
    print(findGraph(nodes))

    nodes = ['1/2/3/4']
    print(findGraph(nodes))

    nodes = ['1', '/']
    print(findGraph(nodes))

    nodes = ['1', '/2']
    print(findGraph(nodes))

