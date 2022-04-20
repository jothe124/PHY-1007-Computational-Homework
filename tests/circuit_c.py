import os
import sys

# Append module root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from src.circuit import Circuit
from src.wire import Current, Wire
from src.world import World


WORLD_SHAPE = (125, 75)

WIRES = [
    Wire(start=(12, 12), stop=(12, 63), current=Current(x=0, y=1), voltage=4.5),
    Wire(start=(12, 63), stop=(105, 63), current=Current(x=1, y=0), voltage=4.5),
    Wire(start=(105, 63), stop=(113, 63), current=Current(x=1, y=0), voltage=-4.5),
    Wire(start=(113, 63), stop=(113, 12), current=Current(x=0, y=-1), voltage=-4.5),
    Wire(start=(113, 12), stop=(105, 12), current=Current(x=-1, y=0), voltage=-4.5),
    Wire(start=(105, 12), stop=(12, 12), current=Current(x=-1, y=0), voltage=4.5),
]




CIRCUIT = Circuit(wires=WIRES)



enviro_c = World(WORLD_SHAPE)
enviro_c.place(CIRCUIT)
enviro_c.compute()
enviro_c.show_all()