# DAG

import networkx as nx
import matplotlib.pyplot as plt
from sympy import parse_expr


def create_expression_dag(expression):
    G = nx.DiGraph()
    parsed_expr = parse_expr(expression, evaluate=False)

    def add_nodes_and_edges(expr):
        if expr.is_Atom:
            G.add_node(expr)
        else:
            for arg in expr.args:
                G.add_edge(expr, arg)
                add_nodes_and_edges(arg)

    add_nodes_and_edges(parsed_expr)

    return G


# expression = "2+3+5*2+2+3"
expression = "x * y - z + x * y"
dag = create_expression_dag(expression)

pos = nx.spring_layout(dag)
nx.draw(dag, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10)
plt.show()
