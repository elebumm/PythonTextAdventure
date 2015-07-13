# PythonTextAdventure
A little fun project to help and teach ourselves how to code in Python

<b>SUMMARY</b>  
The PythonTextAdventure is a text-based game that features character creation and randomly generated content. Use typed commands to control your character and conquer various floors and navigate their rooms' obstacles, enemies and puzzles.

<b>DESIRED SIMULATION</b>  
This is how the game should play:  
<ul>
    <li>Users input commands into the console</li>
    <li>If typed correctly, the console displays appropriate output</li>
    <li>Output includes: environment, item, and character descriptions/statistics, unicode maps, combat events and dialogue
    <li>By interacting with the world in this manner, users hope to reach the ultimate goal: completion of the game</li>
</ul>

<b>ARCHITECTURE</b>  

The PythonTextAdventure uses a node & leaf system. Nodes are objects that can contain Leaf objects or other Node objects. In short, a Node is a container.

The game takes place on various grid-like Floors (Nodes) and each cell in the grid contains a Room (which is also a Node). Rooms contain the bulk of content: Items (Nodes or Leafs) and Creatures (Node objects, including the Player).

In exploring a combination of crafted and randomly generated Floors, the Player may encounter Events like combat with Creatures and special environment puzzles.
