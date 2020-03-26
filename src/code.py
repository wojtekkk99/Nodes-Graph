from typing import List


class Node:
    """
    Class represents Node.
    """
    def __init__(self, value: int, neighbour: List['Node']):
        """

        :param value: value of the node
        :param neighbour: list of the neighbours
        """
        self.value = value
        self.neighbour = neighbour

    def sum_value(self) -> int:
        """
        Counts sum of the values in subgraph
        :return: sum of values
        """
        return sum(find_subgraph(self))

    def medium_value(self) -> float:
        """
        Counts medium value in subgraph
        :return: medium value from subgraph
        """
        return self.sum_value() / len(find_subgraph(self))

    def median(self) -> int:
        """
        Counts median in subgraph
        :return: median from subgraph
        """
        subgraph = sorted(find_subgraph(self))
        return subgraph[int(len(subgraph)/2)] if len(subgraph) % 2 is 1 else \
            (subgraph[int(len(subgraph)/2)] + subgraph[int(len(subgraph)/2) - 1]) / 2


def find_subgraph(node: Node) -> List[int]:
    """
    Creates list with values from subgraph
    :param node: node for which we search subtree
    :return: list of values
    """
    def subgraph_list(visited: List[Node], node, sublist: List[int]) -> List[int]:
        """
        BFS search of element
        :param visited: list of visited nodes
        :param node: node for which we search subtree
        :param sublist: list of values
        :return: list of values
        """
        visited.append(node)
        sublist.append(node.value)
        for neighbour in node.neighbour:
            if neighbour not in visited:
                sublist = subgraph_list(visited, neighbour, sublist)
        return sublist

    return subgraph_list([], node, [])
