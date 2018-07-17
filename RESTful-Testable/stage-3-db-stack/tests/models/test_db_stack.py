import pytest

from models.db import session_scope
from models.db_stack import Stack, _Operand

operand_data = [1, 2]


@pytest.fixture
def calc_id() -> int:
    calc_id = Stack.start()
    yield calc_id
    Stack.delete(id_=calc_id)


@pytest.fixture
def one_operand_calc_id(calc_id: int) -> int:
    Stack.push(operand=operand_data[0], id_=calc_id)
    return calc_id


def test_add_new_stack_pass():
    # given

    # when
    calc_id = Stack.start()

    # then
    stacks = Stack.stacks()
    assert 1 == len(stacks)
    assert 1 == calc_id

    # when (delete the stack)
    Stack.delete(id_=calc_id)

    # then
    stack = Stack.stacks()
    assert 0 == len(stack)


def test_push_pass(calc_id: int):
    # given
    x, y = 1, 2

    # when (push first operand)
    operand_x = Stack.push(operand=x, id_=calc_id)
    operand_y = Stack.push(operand=y, id_=calc_id)

    # then
    assert x == operand_x
    assert y == operand_y

    operands = Stack.stack(id_=calc_id)
    assert x == operands[0]
    assert y == operands[1]


def test_pop_pass(one_operand_calc_id: int):
    calc_id = one_operand_calc_id
    # given

    # when (push operand)
    operand = Stack.pop(id_=calc_id)

    # then
    assert operand_data[0] == operand

    # check that the stack is empty.
    stack = Stack.stack(id_=calc_id)
    assert 0 == len(stack)


def test_peek_pass(one_operand_calc_id: int):
    calc_id = one_operand_calc_id
    # given

    # when (push operand)

    # then
    operand = Stack.peek(id_=calc_id)
    assert operand_data[0] == operand

    # check that the stack is empty.
    stack = Stack.stack(id_=calc_id)
    assert 1 == len(stack)


def test_cascading_delete_pass():
    # given
    x = 1

    # when
    calc_id = Stack.start()
    Stack.push(operand=x, id_=calc_id)
    Stack.delete(id_=calc_id)

    # then
    stacks = Stack.stacks()
    assert 0 == len(stacks)

    # Check to make sure that the operands are removed through cascading delete.
    with session_scope() as session:
        operands = session.query(_Operand).filter(_Operand.calc_id == calc_id).all()

        assert 0 == len(operands)
