import datetime
from typing import List

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship, Session

from models import InvalidContextError
from models.db import AppDBBase, session_scope

"""
Stack -> List[Operand]
"""

class _Operand(AppDBBase):
    """Operand to store in the stack for RPN calculator."""
    __tablename__ = 'operand'

    pk = Column(Integer, primary_key=True)

    # Connect the operands to the stack with the foreign key.
    calc_id = Column(Integer, ForeignKey('stack.calc_id'))

    # Mechanism for ordering the operands in the stack.
    # Not sure if the order of the operands in the list in stack are preserved.
    # This could be an underlying DB implementation question. It works for now
    # so not going to play with ordering.
    stack_idx = Column(DateTime, default=datetime.datetime.utcnow)

    # Actual value that is stored on the stack.
    operand = Column(Float)
    stack = relationship('Stack', back_populates='operands')

    def __init__(self, *, operand: float):
        self.operand = operand


class Stack(AppDBBase):
    """DB Stack with refernce to operands."""
    __tablename__ = 'stack'

    calc_id = Column(Integer, primary_key=True)

    # Maintain the relationship the the operands in the list.
    operands = relationship('_Operand', back_populates='stack', cascade='all, delete, delete-orphan')

    @staticmethod
    def find_stack(id_: int, session: Session):
        stack = session.query(Stack).filter(Stack.calc_id == id_).one_or_none()
        if not stack:
            raise InvalidContextError()

        return stack

    @staticmethod
    def start():
        with session_scope() as session:
            new_stack = Stack()
            session.add(new_stack)
            session.commit()
            calc_id = new_stack.calc_id
            return calc_id

    @staticmethod
    def stacks():
        with session_scope() as session:
            stacks = session.query(Stack).all()
            return stacks

    @staticmethod
    def stack(*, id_: int) -> List[float]:
        with session_scope() as session:
            stack = Stack.find_stack(id_, session)

            return [o.operand for o in stack.operands]

    @staticmethod
    def delete(*, id_: int):
        with session_scope() as session:
            stack = Stack.find_stack(id_, session)
            if stack:
                session.delete(stack)
            session.commit()

    @staticmethod
    def push(*, operand: float, id_: int) -> float:
        with session_scope() as session:
            stack = Stack.find_stack(id_, session)

            stack.operands.append(_Operand(operand=operand))
            session.commit()

            return operand

    @staticmethod
    def pop(*, id_: int) -> float:
        with session_scope() as session:
            stack = Stack.find_stack(id_, session)

            # This list of operands seems to be in the right order.   If it isn't then
            # the query to the DB can be modified to order by the Operand stack_idx (DateTime)
            # or the list can be sorted in Python.
            operand = stack.operands.pop()
            session.commit()

            return operand.operand

    @staticmethod
    def peek(*, id_: int) -> float:
        with session_scope() as session:
            stack = Stack.find_stack(id_, session)

            # Same discussion about ordering.
            return stack.operands[-1].operand
