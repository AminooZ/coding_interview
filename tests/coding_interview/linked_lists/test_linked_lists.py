import pytest

from coding_interview.linked_lists.linked_lists import LinkedList, Node


def assert_node_equality(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None or node2 is None:
        return False
    else:
        while node1.next and node2.next:
            return node1.value == node2.value and assert_node_equality(
                node1=node1.next,
                node2=node2.next
            )
        return node1.value == node2.value


def assert_linked_list_equality(linked_list1, linked_list2):
    assert assert_node_equality(node1=linked_list1.head, node2=linked_list2.head)


class TestNode:

    @pytest.mark.parametrize("value", [x for x in range(5)])
    def test_value_init(self, value):
        node = Node(value=value)
        assert node.value == value

    @pytest.mark.parametrize("next", [Node(value=x) for x in range(5)])
    def test_next_init(self, next):
        node = Node(next=next)
        assert assert_node_equality(node.next, next)


class TestLinkedList:

    @pytest.mark.parametrize("value", [x for x in range(5)])
    def test_head_init(self, value):
        linked_list = LinkedList(value=value)
        assert linked_list.head.value == value
        assert linked_list.head.next is None

    @pytest.mark.parametrize("value", [x for x in range(5)])
    def test_append_to_tail(self, value):
        linked_list = LinkedList(value=1)
        linked_list.append_to_tail(value=value)
        node = linked_list.head
        while node.next:
            node = node.next
        assert node.value == value

    @pytest.mark.parametrize("linked_list,value, expected", [
        (LinkedList.from_list(values=[1, 2, 3, 4, 5]), 1,
         LinkedList.from_list(values=[2, 3, 4, 5])),
        (LinkedList.from_list(values=[1, 2, 3, 4, 5]), 3,
         LinkedList.from_list(values=[1, 2, 4, 5])),
        (LinkedList.from_list(values=[1, 2, 3, 3, 5]), 3,
         LinkedList.from_list(values=[1, 2, 3, 5])),
        (LinkedList.from_list(values=[1, 2, 3, 4, 5]), 5,
         LinkedList.from_list(values=[1, 2, 3, 4])),
        (LinkedList.from_list(values=[1, 2, 3, 4, 5]), 6,
         LinkedList.from_list(values=[1, 2, 3, 4, 5]))
    ])
    def test_delete(self, linked_list, value, expected):
        linked_list.delete(value=value)
        assert_linked_list_equality(linked_list, expected)

    @pytest.mark.parametrize("values", [
        [0],
        [0, 1, 2, 3, 4, 5]
    ])
    def test_to_list(self, values):
        assert LinkedList.from_list(values=values).to_list() == values
