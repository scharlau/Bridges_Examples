import os
from dotenv import load_dotenv

from bridges.bridges import *
from bridges.sl_element import *

load_dotenv()
BRIDGES_USERNAME = os.getenv('BRIDGES_USERNAME')
BRIDGES_API_KEY = os.getenv('BRIDGES_API_KEY')

bridges = Bridges(0, BRIDGES_USERNAME, BRIDGES_API_KEY)

sle0 = SLelement(e="Hello",label="Hello")
sle1 = SLelement(e="Wordl",label="World")

sle0.next = sle1

sle0.color = 'red'
sle1.color = 'blue'

sle0.get_link_visualizer(el=sle1).color = 'black'

bridges.set_data_structure(sle0)

bridges.visualize()