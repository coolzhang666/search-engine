from copy import deepcopy


def deal_graph(filename):
    edges = dict()
    in_degree = dict()
    # 读取文件
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.read().split("\n")

    for line in lines:
        if len(line) <= 0:
            continue
        content = line.split("\t")
        flag = edges.get(content[0])
        if not flag:
            edges[content[0]] = list()
            edges.get(content[0]).append(content[1])
        else:
            flag.append(content[1])

    nodes = list(edges.keys())

    for i in nodes:
        for j in edges.get(i):
            flag = in_degree.get(j)
            if not flag:
                in_degree[j] = []
                in_degree.get(j).append(i)
            else:
                in_degree.get(j).append(i)

    out_degree = deepcopy(edges)

    return nodes, edges, in_degree, out_degree


def page_rank(nodes, in_degree, out_degree, d, cg):
    N = len(nodes)
    pr = dict()
    for n in nodes:
        pr[n] = (1 - d) / N

    while True:
        flag = True
        for a in pr:
            try:
                x = 0
                # pr_temp[a] = (1.0 - d) * pr[a] + d * sum([(pr[b] / len(out_degree[b])) for b in in_degree[a]])
                for b in in_degree[a]:
                    x += pr[b] / len(out_degree[a])
                pr[a] = (1.0 - d) * pr[a] + d * x

                if flag:
                    if abs(pr[a] - x) > cg:
                        flag = False

            except KeyError:
                continue
        if flag:
            break

    return pr


if __name__ == "__main__":
    result = deal_graph("files/test.txt")
    c = page_rank(result[0], result[2], result[3], 0.85, 1e-6)
    print("结果为：")
    print(c)
