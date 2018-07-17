import pytest

# ToDo: Sort out the PyTest import mechanism inorder to import ModelDataClass to use for type hinting.
# ModelDataClass = namedtuple('ModelData', ('calc', 'calc_id'))  From conftest model fixture.
# from .conftest import ModelDataClass
from models import OperandError, InvalidContextError


def test_values_add_success(model):
    # given
    x = 1
    y = 2

    # when (add)
    model.calc.push(operand=x, id_=model.calc_id)
    model.calc.push(operand=y, id_=model.calc_id)
    r = model.calc.add(id_=model.calc_id)

    # then
    assert x + y == r


def test_values_multiple_add_success(model):
    # given
    x = 1
    y = 2
    z = 3

    # when (add)
    model.calc.push(operand=x, id_=model.calc_id)
    model.calc.push(operand=y, id_=model.calc_id)
    r = model.calc.add(id_=model.calc_id)
    model.calc.push(operand=z, id_=model.calc_id)
    r = model.calc.add(id_=model.calc_id)

    # then
    assert x + y + z == r


def test_values_multiple_push_add_success(model):
    # given
    x = 1
    y = 2
    z = 3

    # when (add)
    model.calc.push(operand=x, id_=model.calc_id)
    model.calc.push(operand=y, id_=model.calc_id)
    model.calc.push(operand=z, id_=model.calc_id)
    model.calc.add(id_=model.calc_id)
    r = model.calc.add(id_=model.calc_id)

    # then
    assert x + y + z == r


def test_values_sub_success(model):
    # given
    x = 3
    y = 2

    # when (add)
    model.calc.push(operand=x, id_=model.calc_id)
    model.calc.push(operand=y, id_=model.calc_id)
    r = model.calc.sub(id_=model.calc_id)

    # then
    assert x - y == r


def test_values_multiple_sub_success(model):
    # given
    x = 3
    y = 2
    z = 1

    # when (add)
    model.calc.push(operand=x, id_=model.calc_id)
    model.calc.push(operand=y, id_=model.calc_id)
    model.calc.sub(id_=model.calc_id)
    model.calc.push(operand=z, id_=model.calc_id)
    r = model.calc.sub(id_=model.calc_id)

    # then
    assert x - y - z == r


def test_values_multiple_push_sub_success(model):
    # given
    x = 3
    y = 2
    z = 1

    # when (add)
    model.calc.push(operand=x, id_=model.calc_id)
    model.calc.push(operand=y, id_=model.calc_id)
    model.calc.push(operand=z, id_=model.calc_id)
    model.calc.sub(id_=model.calc_id)
    r = model.calc.sub(id_=model.calc_id)

    # then
    assert (x - (y - z)) == r


def test_result_success(model):
    # given
    x = 1
    y = 2

    # when (add)
    model.calc.push(operand=x, id_=model.calc_id)
    model.calc.push(operand=y, id_=model.calc_id)
    model.calc.add(id_=model.calc_id)
    r = model.calc.result(id_=model.calc_id)

    # then
    assert x + y == r


def test_value_add_missing_first_operand_fail(model):
    # given

    # when (add - only one operand)
    with pytest.raises(OperandError) as e:
        r = model.calc.add(id_=model.calc_id)

    assert "Stack empty.  Missing first operand." == str(e.value)


def test_value_add_missing_second_operand_fail(model):
    # given
    x = 1

    # when (add - only one operand)
    model.calc.push(operand=x, id_=model.calc_id)
    with pytest.raises(OperandError) as e:
        r = model.calc.add(id_=model.calc_id)

    assert "Stack empty.  Missing second operand." == str(e.value)


def test_push_bad_context_fail(model):
    # given
    x = 1

    # when (push bad context)
    with pytest.raises(InvalidContextError):
        model.calc.push(operand=x, id_=-1)


def test_pop_bad_context_fail(model):
    # given
    x = 1
    y = 2

    # when (add bad context)
    model.calc.push(operand=x, id_=model.calc_id)
    model.calc.push(operand=y, id_=model.calc_id)
    with pytest.raises(InvalidContextError):
        model.calc.add(id_=-1)


def test_result_bad_context_fail(model):
    # given

    # when (result bad context)
    with pytest.raises(InvalidContextError):
        model.calc.result(id_=-1)