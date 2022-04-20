import os
import sys

# Append module root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from src.circuit import Circuit
from src.wire import Current, Wire
from src.world import World


WORLD_SHAPE = (75, 75)

WIRES = [
    Wire(start=(12, 12), stop=(12, 63), current=Current(x=0, y=1), voltage=4.5),
    Wire(start=(12, 63), stop=(38, 63), current=Current(x=1, y=0), voltage=4.5),
    Wire(start=(38, 63), stop=(63, 63), current=Current(x=1, y=0), voltage=-4.5),
    Wire(start=(63, 63), stop=(63, 12), current=Current(x=0, y=-1), voltage=-4.5),
    Wire(start=(63, 12), stop=(38, 12), current=Current(x=-1, y=0), voltage=-4.5),
    Wire(start=(38, 12), stop=(12, 12), current=Current(x=-1, y=0), voltage=4.5),
]
CIRCUIT = Circuit(wires=WIRES)



enviro_a = World(WORLD_SHAPE)
enviro_a.place(CIRCUIT)
enviro_a.compute()
enviro_a.show_all()