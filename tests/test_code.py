import pytest
from src.code import Node


@pytest.fixture(scope='session')
def list_nodes_from_task():
    p1 = Node(2, [])
    p2 = Node(5, [])
    p3 = Node(3, [p1, p2])
    p4 = Node(5, [])
    p5 = Node(8, [p4])
    p6 = Node(2, [])
    p7 = Node(0, [p6, p5])
    p8 = Node(1, [])
    p9 = Node(7, [p8, p7])
    p10 = Node(5, [p9, p3])
    return [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]


@pytest.mark.parametrize(
    'node, result_sum', [
        (4, 13),
        (0, 2),
        (9, 38),
        (2, 10),
        (6, 15),
    ]
)
def test_sum_value(list_nodes_from_task, node, result_sum):
    assert list_nodes_from_task[node].sum_value() == result_sum


@pytest.mark.parametrize(
    'node, result_medium', [
        (4, 6.5),
        (0, 2),
        (9, 3.8),
        (2, 3.33),
        (6, 3.75),
    ]
)
def test_medium_value(list_nodes_from_task, node, result_medium):
    assert round(list_nodes_from_task[node].medium_value(), 2) == result_medium


@pytest.mark.parametrize(
    'node, result_median', [
        (4, 6.5),
        (0, 2),
        (9, 4),
        (2, 3),
        (6, 3.5),
    ]
)
def test_sum_value(list_nodes_from_task, node, result_median):
    assert list_nodes_from_task[node].median() == result_median
