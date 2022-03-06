from nltk.tokenize import word_tokenize
from collections import deque
import json
import numpy as np

# from app.query.service.query_processing.Logic_Operator import AND, OR, NOT
# from app.query.service.constant import N_ARTICLE
# from app.query.service.create_hash_table.Hash_Table import hash_table

from ..query_processing.Logic_Operator import AND, OR, NOT
from ..constant import N_ARTICLE
from ..create_hash_table.Hash_Table import hash_table

import re
from collections import deque

with open("D:/20211/Project I/Project-1-Reverse-Index-Search/data/list_dict.json") as f1:
    list_dict = json.load(f1)

list_dict = np.array(list_dict)
vocab=list_dict[:,0].reshape(len(list_dict),1)

class Stack():
    def __init__(self):
        self.__list = deque()

    def push(self, key):
        self.__list.append(key)

    def pop(self):
        return self.__list.pop()

    def peek(self):
        key = self.__list.pop()
        self.__list.append(key)
        return key

    def is_empty(self):
        return len(self.__list) == 0

    def __str__(self):
        return "[" + ", ".join(str(i) for i in self.__list) + "]"

    def __len__(self):
        return len(self.__list)


def precedence(token):
    """ precedence of supported operators """
    __precedence = {"&": 2, "|": 1}
    try:
        return __precedence[token]
    except:
        return -1


def is_left_bracket(token):
    """ returns true if token is left bracket """
    return token == "("


def is_right_bracket(token):
    """ returns true if token is right bracket """
    return token == ")"


def is_operator(token):
    """ return true if operator """
    return token == "&" or token == "|"


def infix_to_postfix(tokens):
    """ converts a infix query into postfix
    input : ['god', '&', '(', '~child', '|', 'mother', ')']
    output : ['god', '~child', 'mother', '|', '&']
    tokens: list of token in infix form
    return: same list of token in postfix form
    """
    st = Stack()
    postfix = list()

    for token in tokens:

        if is_left_bracket(token):
            # token is left bracket
            st.push(token)  # push token in to st

        elif is_right_bracket(token):
            # token is right bracket

            while (not st.is_empty()) and st.peek() != "(":
                key = st.pop()
                postfix.append(key)

            if not st.is_empty() and st.peek() != "(":
                return -1
            else:
                if st.is_empty():
                    return -1
                else:
                    st.pop()

        elif is_operator(token):
            # token is an operator
            while not st.is_empty() and (
                    precedence(token) <= precedence(st.peek())
            ):
                postfix.append(st.pop())

            st.push(token)

        else:
            # token is an operand
            postfix.append(token)

    while not st.is_empty():
        postfix.append(st.pop())

    return postfix


def evaluate_query(query_tokens):
    """
    query_tokens: list of query tokens in postfix form
    returns: list of matching documents
    """
    operands = Stack()
    for token in query_tokens:

        # if token is an operator
        # pop 2 elements from stack and apply it
        if is_operator(token):
            # pop right operand
            try:

                right_operand = operands.pop()

                # pop left operand
                left_operand = operands.pop()

                # perform operation
                result = operation(left_operand, right_operand, token)

                # push result back into the stack
                operands.push(result)
            except:
                # print("Invalid query")
                return -1

        else:
            # token is an operand, push it into stack
            operands.push(is_negative(token))

    if len(operands) != 1:  #
        # print("Invalid query")
        return -1
    return operands.peek()

def is_negative(token):
    """Check a token have negated or not
    token: token need to be checked
    return: list of docIDs does not contain that token
    """
    negate = False
    all_docID = [i for i in range(1001)]

    if token[0] == '~':
        negate = True
        token = token[1:]

    if token in vocab:
        # token in vocabulary
        posting = hash_table.lookup(token)

        if negate == True:
            posting = NOT(posting)

    else:
        # all documents does not contain that token
        if negate == True:
            posting = all_docID

        else:
            posting = list()

    return posting


def preprocess_query(query):
    # Remove white-space between "~" and operand
    query = re.sub(r"~\s+", "~", query)

    # Add white-space after "(" and before ")"
    query = re.sub(r"\(", " ( ", query)
    query = re.sub(r"\)", " ) ", query)

    # Add white-space around "|" and "&"
    query = re.sub(r"\|", " | ", query)
    query = re.sub(r"\&", " & ", query)

    # Convert query into lower form
    query = query.lower()

    return query

def operation(left, right, op):
    """ Performs specified operation
    left: left operand
    right: rigth operand
    token: operation to perform
    return: result of operation
    """
    # docID_left = hash_table.lookup(left)
    # docID_right = hash_table.lookup(right)
    if op == '&':
        return AND(left, right)

    elif op == '|':
        return OR(left, right)

    else:
        return list()


def search(query):
    query = preprocess_query(query)

    query_tokens = re.split(r"\s+", query.strip())

    query_tokens = infix_to_postfix(query_tokens)

    if query_tokens == -1:
        # print("Invalid query")
        return -1

    result = evaluate_query(query_tokens)

    if result == -1:
        # print("Invalid query")
        return -1

    return result

print (search ("david & ~beckham "))

