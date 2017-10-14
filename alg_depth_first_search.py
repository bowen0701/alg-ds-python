from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

from ds_stack import Stack


def dfs(graph_dict, start_vertex):
    """Depth First Search algorith."""
    ls_stack = Stack()
    ls_stack.push([start_vertex])
    # print('ls_stack: {}'.format(ls_stack.show()))


def main():
    # Small word ladder graph.
    graph_dict = {
        'fool': {'cool', 'pool', 'foil', 'foul'},
        'foul': {'fool', 'foil'},
        'foil': {'fool', 'foul', 'fail'},
        'cool': {'fool', 'cool'},
        'fail': {'foil', 'fall'},
        'fall': {'fail', 'pall'},
        'pool': {'fool', 'cool', 'poll'},
        'poll': {'pool', 'pall', 'pole'},
        'pall': {'fall', 'pale', 'poll'},
        'pole': {'poll', 'pope', 'pale'},
        'pope': {'pole'},
        'pale': {'pall', 'pole', 'sale', 'page'},
        'sale': {'pale', 'sage'},
        'page': {'pale', 'sage'},
        'sage': {'sale', 'page'} 
    }
    pass

if __name__ == '__main__':
    main()
