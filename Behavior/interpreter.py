# Aim: Parsing
# Constitution: AbstractExpression, TerminalExpression(Leaf), NonterminalExpression(Node), Client, Context

from abc import ABC, abstractmethod


# Exception
class InterpreterException(Exception):
    pass


# Context
class Context:

    def __init__(self, text):
        self.__tokens = text.split()
        self.__idx = 0

    @property
    def tokens(self):
        return self.__tokens

    @property
    def idx(self):
        return self.__idx

    @idx.setter
    def idx(self, idx):
        self.__idx = idx

    def delete_token(self, start, end):
        del self.__tokens[start: end]


# AbstractExpression
class Node(ABC):

    @abstractmethod
    def parse(self, context: Context):
        pass


# NonterminalExpression
class ProgramNode(Node):

    def parse(self, context: Context):
        try:
            while context.idx < len(context.tokens):
                idx = context.idx
                current_token = context.tokens[idx]

                if current_token == '+':
                    node = PlusNode()
                elif current_token == '-':
                    node = MinusNode()
                elif current_token == '*':
                    node = MultiplyNode()
                elif current_token == '/':
                    node = DivideNode()
                else:
                    context.idx += 1
                    continue
                answer = node.parse(context)
                context.delete_token(idx - 2, idx + 1)
                context.tokens.insert(idx - 2, answer)
                context.idx = idx - 1
            if len(context.tokens) == 1:
                return context.tokens[0]
            else:
                raise InterpreterException('Something is wrong...')
        except:
            raise InterpreterException('Something is wrong...')


# TerminalExpression
class PlusNode(Node):

    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx-2]) + int(context.tokens[idx-1])


class MinusNode(Node):

    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx-2]) - int(context.tokens[idx-1])


class MultiplyNode(Node):

    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx-2]) * int(context.tokens[idx-1])


class DivideNode(Node):

    def parse(self, context: Context):
        idx = context.idx
        return int(context.tokens[idx-2]) / int(context.tokens[idx-1])


context = Context('2 1 *')
node = ProgramNode()
print(node.parse(context))
