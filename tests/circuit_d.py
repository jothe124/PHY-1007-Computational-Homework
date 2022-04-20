import os
import sys

# Append module root directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from src.circuit import Circuit
from src.wire import Current, Wire
from src.world import World


WORLD_SHAPE = (75, 75)

WIRES = [
    Wire(start=(12, 12), stop=(12, 37), current=Current(x=0, y=1), voltage=-4.5),
    Wire(start=(12, 37), stop=(12, 63), current=Current(x=0, y=1), voltage=4.5),
    Wire(start=(12, 63), stop=(37, 63), current=Current(x=1, y=0), voltage=4.5),
    Wire(start=(37, 63), stop=(50, 63), current=Current(x=1, y=0), voltage=2.25),
    Wire(start=(50, 63), stop=(63, 63), current=Current(x=1, y=0), voltage=-2.25),
    Wire(start=(37, 63), stop=(37, 37), current=Current(x=0, y=-1), voltage=2.25),
    Wire(start=(37, 37), stop=(37, 12), current=Current(x=0, y=-1), voltage=-2.25),
    Wire(start=(63, 63), stop=(63, 12), current=Current(x=0, y=-1), voltage=-2.25),
    Wire(start=(63, 12), stop=(37, 12), current=Current(x=-1, y=0), voltage=-2.25),
    Wire(start=(37, 12), stop=(12, 12), current=Current(x=-1, y=0), voltage= -4.5),
]




CIRCUIT = Circuit(wires=WIRES)



enviro_d = World(WORLD_SHAPE)
enviro_d.place(CIRCUIT)
enviro_d.compute()
enviro_d.show_all()