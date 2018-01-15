from __future__ import absolute_import
from __future__ import print_function
from __future__ import division


def bfs():
    pass


def main():
    # Small word ladder graph.
    graph_adj_d = {
        'fool': {'cool', 'pool', 'foil', 'foul'},
        'foul': {'fool', 'foil'},
        'foil': {'fool', 'foul', 'fail'},
        'cool': {'fool', 'pool'},
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


if __name__ == '__main__':
    main()
