import pytest

from coding_interview.stacks_and_queues.stack import Stack
from tests.coding_interview.linked_lists.test_linked_lists import assert_node_equality


def assert_stack_equality(stack1, stack2):
    assert assert_node_equality(node1=stack1.top, node2=stack2.top)


class TestStack:

    @pytest.mark.parametrize("items, new_item", [
        ([0, 1, 2, 3], 4),
        ([], 0)
    ])
    def test_push(self, items, new_item):
        stack = Stack.from_list(items=items)
        stack.push(item=new_item)
        items.append(new_item)
        assert_stack_equality(stack1=stack, stack2=Stack.from_list(items=items))

    @pytest.mark.parametrize("items", [
        ([0, 1, 2, 3]),
        ([0])
    ])
    def test_pop(self, items):
        stack = Stack.from_list(items=items)
        stack.pop()
        assert_stack_equality(stack1=stack, stack2=Stack.from_list(items=items[:-1]))

    def test_pop_empty_stack_should_return_exception(self):
        with pytest.raises(AssertionError, match="Can not remove the top item from an empty stack"):
            stack = Stack()
            stack.pop()

    @pytest.mark.parametrize("items", [
        ([0, 1, 2, 3]),
        ([0])
    ])
    def test_peek(self, items):
        stack = Stack.from_list(items=items)
        assert stack.peek() == items[-1]

    def test_peek_empty_stack_should_return_exception(self):
        with pytest.raises(AssertionError, match="Can not return the top item from an empty stack"):
            stack = Stack()
            stack.peek()

    @pytest.mark.parametrize("items, expected", [
        ([0, 1, 2, 3], False),
        ([], True)
    ])
    def test_is_empty(self, items, expected):
        stack = Stack.from_list(items=items)
        assert stack.is_empty() == expected

    @pytest.mark.parametrize("items", [
        [],
        [0, 1, 2, 3, 4, 5]
    ])
    def test_to_list(self, items):
        assert Stack.from_list(items=items).to_list() == items
