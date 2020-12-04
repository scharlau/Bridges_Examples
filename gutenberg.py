'''
An example of generating a tree from a book list.
It would be interesting to build a recursive version.
This combines a tree example http://bridgesuncc.github.io/tutorials/Tree.html 
with the basic Gutenberg example http://bridgesuncc.github.io/tutorials/Data_Guttenberg.html 
'''

import os
from dotenv import load_dotenv
from bridges.bridges import *
from bridges.tree_element import *
from bridges.data_src_dependent.data_source import *
import sys
import random

def main():
    args = sys.argv[1:]

    load_dotenv()
    BRIDGES_USERNAME = os.getenv('BRIDGES_USERNAME')
    BRIDGES_API_KEY = os.getenv('BRIDGES_API_KEY')

    bridges = Bridges(1, BRIDGES_USERNAME, BRIDGES_API_KEY)
    bridges.set_title('Gutenberg Book Example')
    bridges.set_description('Display a book either to console and as a tree')

    # get the guttenberg book meta data
    book_list = get_gutenberg_book_data()

    # get the first book
    book1 = book_list[random.randrange(len(book_list))]
    book2 = book_list[random.randrange(len(book_list))]

    # create tree elements
    t0 = TreeElement(e=book_list, label = 'book list')
    t1 = TreeElement(e=book1.title, label = book1.title)
    t2 = TreeElement(e=book1.name, label=book1.name)
    t3 = TreeElement(e=book1.genre, label=book1.genre)
    t4 = TreeElement(e=book2.title, label = book2.title)
    t5 = TreeElement(e=book2.name, label=book2.name)
    t6 = TreeElement(e=book2.genre, label=book2.genre)

    # add links to children
    t0.add_child(t2)
    t2.add_child(t1)
    t2.add_child(t3)
    t0.add_child(t5)
    t5.add_child(t4)
    t5.add_child(t6)

    # set visual attributes
    t0.color='red'
    t0.opacity = 0.4

    t0.get_link_visualizer(t2).color = 'blue'
    t0.get_link_visualizer(t5).color = 'yellow'
    t2.get_link_visualizer(t1).color = 'green'
    t2.get_link_visualizer(t3).color = 'purple'
    t5.get_link_visualizer(t4).color = 'green'
    t5.get_link_visualizer(t6).color = 'purple'
    
    # set visualiser type
    bridges.set_data_structure(t0)

    # visualise the tree
    bridges.visualize()

    # print details to console
    print(book1.title)
    print(book1.name)
    print(book1.genre)
    print(book2.title)
    print(book2.name)
    print(book2.genre)

if __name__ == "__main__":
        main()
