from network import Network


def main():
    linear = {
        "nodes": [0, 1, 2, 3, 4],
        "neighbours": [[1], [0, 2], [1, 3], [2, 4], [3]]
    }
    circle = {
        "nodes": [0, 1, 2, 3, 4],
        "neighbours": [[4, 1], [0, 2], [1, 3], [2, 4], [3, 0]]
    }
    star = {
        "nodes": [0, 1, 2, 3, 4],
        "neighbours": [[2], [2], [1, 3, 4], [2], [2]]
    }

    circle = {
        "nodes": [0, 1, 2, 3, 4],
        "neighbours": [[1], [2], [3], [4], [0]]
    }
    cur_topology = circle
    network = Network()
    network.simulate(cur_topology["nodes"], cur_topology["neighbours"])

    pass


if __name__ == '__main__':
    main()