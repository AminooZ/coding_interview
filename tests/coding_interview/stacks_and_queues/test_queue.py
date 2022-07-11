import pytest

from coding_interview.stacks_and_queues.queue import Queue
from tests.coding_interview.linked_lists.test_linked_lists import assert_node_equality


def assert_queue_equality(queue1: Queue, queue2: Queue):
    assert assert_node_equality(node1=queue1.first, node2=queue2.first)
    assert assert_node_equality(node1=queue1.last, node2=queue2.last)


class TestQueue:

    @pytest.mark.parametrize("items, new_item", [
        ([0, 1, 2, 3], 4),
        ([], 0)
    ])
    def test_add(self, items, new_item):
        queue = Queue.from_list(items=items)
        queue.add(item=new_item)
        items.append(new_item)
        assert_queue_equality(queue1=queue, queue2=queue.from_list(items=items))

    @pytest.mark.parametrize("items", [
        ([0, 1, 2, 3]),
        ([0])
    ])
    def test_remove(self, items):
        queue = Queue.from_list(items=items)
        queue.remove()
        assert_queue_equality(queue1=queue, queue2=queue.from_list(items=items[1:]))

    def test_remove_item_from_empty_queue_should_return_exception(self):
        with pytest.raises(AssertionError, match="Can not remove the top item from an empty queue"):
            queue = Queue()
            queue.remove()

    @pytest.mark.parametrize("items", [
        ([0, 1, 2, 3]),
        ([0])
    ])
    def test_peek(self, items):
        queue = Queue.from_list(items=items)
        assert queue.peek() == items[0]

    def test_peek_item_from_empty_queue_should_return_exception(self):
        with pytest.raises(AssertionError, match="Can not return the top item from an empty queue"):
            queue = Queue()
            queue.peek()

    @pytest.mark.parametrize("items, expected", [
        ([0, 1, 2, 3], False),
        ([], True)
    ])
    def test_is_empty(self, items, expected):
        queue = Queue.from_list(items=items)
        assert queue.is_empty() == expected

    @pytest.mark.parametrize("items", [
        # [],
        [0, 1, 2, 3, 4, 5]
    ])
    def test_to_list(self, items):
        assert Queue.from_list(items=items).to_list() == items
