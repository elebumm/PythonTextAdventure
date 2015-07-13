# PythonTextAdventure
A little fun project to help and teach ourselves how to code in Python

##Summary##
The PythonTextAdventure is a text-based game that features character creation and randomly generated content. Use typed commands to control your character and conquer various floors and navigate their rooms' obstacles, enemies and puzzles.

##Desired Simulation##
This is how the game should play:  
<ul>
    <li>Users input commands into the console</li>
    <li>If typed correctly, the console displays appropriate output</li>
    <li>Output includes: environment, item, and character descriptions/statistics, unicode maps, combat events and dialogue
    <li>By interacting with the world in this manner, users hope to reach the ultimate goal: completion of the game</li>
</ul>

##Architecture##

The PythonTextAdventure uses a node & leaf system. Nodes are objects that can contain Leaf objects or other Node objects. In short, a Node is a container.

The game takes place on various grid-like Floors (Nodes) and each cell in the grid contains a Room (which is also a Node). Rooms contain the bulk of content: Items (Nodes or Leafs) and Creatures (Node objects, including the Player).

In exploring a combination of crafted and randomly generated Floors, the Player may encounter Events like combat with Creatures and special environment puzzles.

##Guidelines##

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

###About RoomBase and Subclasses###

Rooms contain the bulk of game objects. A Room can have Item objects and Creature objects as children. The Player can interact with these and any related Events in a single Room depending on their location.

RoomBase defines properties and methods common to all classes.

Room is used for manually crafted Rooms. Every aspect of a Room can be tweaked.

RandomRoom allows you to fill entire Floors with Rooms that are randomly populated with enemies and loot.

Since you sacrifice control with RandomRoom, RandomRoom has several subclasses with different contents. Examples: Enemy-filled combat rooms. A room with already dead, lootable enemies. Minor treasure rooms. PuzzleEvent rooms. Dead-ends. Trap & trick rooms.

###About Events###
