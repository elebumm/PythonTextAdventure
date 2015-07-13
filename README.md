# PythonTextAdventure
A little fun project to help and teach ourselves how to code in Python

##SUMMARY##
The PythonTextAdventure is a text-based game that features character creation and randomly generated content. Use typed commands to control your character and conquer various floors and navigate their rooms' obstacles, enemies and puzzles.

##DESIRED SIMULATION##
This is how the game should play:  
<ul>
    <li>Users input commands into the console</li>
    <li>If typed correctly, the console displays appropriate output</li>
    <li>Output includes: environment, item, and character descriptions/statistics, unicode maps, combat events and dialogue
    <li>By interacting with the world in this manner, users hope to reach the ultimate goal: completion of the game</li>
</ul>

##ARCHITECTURE##

The PythonTextAdventure uses a node & leaf system. Nodes are objects that can contain Leaf objects or other Node objects. In short, a Node is a container.

The game takes place on various grid-like Floors (Nodes) and each cell in the grid contains a Room (which is also a Node). Rooms contain the bulk of content: Items (Nodes or Leafs) and Creatures (Node objects, including the Player).

In exploring a combination of crafted and randomly generated Floors, the Player may encounter Events like combat with Creatures and special environment puzzles.

##GUIDELINES##

###About Node and Leaf###
The Node & Leaf system is simple and effective. Node's important methods relate to modifying it's children (add_child, remove_child, etc.). Several top-level classes inherit from Node and Leaf so they can contain other Node & Leaf objects. See below.

###About GameMap and Floor###
GameMap functions as map visualization. GameMap also contains the Floor classes which store and organize Room objects as Node children.

Every Floor has a goal. Anything from completing a puzzle to surviving waves of enemies is possible.

Once you complete this goal, navigate to the special Exit room to ascend to the next Floor.

Ascend all Floors to win.

Each Floor has at minimum 2 Rooms.

The Entrance is a safe zone. Here you can recover and interact with the only friendly NPCs in the game. These are special vendors which aid you in your trials.

The Exit allows you to ascend to the next floor. The Elevator in this room cannot be used until the Floor goal is met.

###About Events###
