# Usage
---
Eventity is an easy to use mix of Event, Entity, Component, and Systems. To get started all you need to do is import ecs from ECS.

`from eventity import ecs`

from here the world is your oyster. See subsections for information on each part of eventity.

## Entities

In Eventity, entities are nothing more than an object with an ID and various methods to handle their relations to various components, which in turn are sets of data.

To create a new entity:
`ecs.new()`

or, to create a useful Named entity:
`ecs.new("player")`

Accessing these entities are also super simple and inspired by Jquery:
`ecs("player")`

Entities are in charge of adding components to themselves via the method `add()`.
`ecs("player").add(PositionComponent)`

Or if you're getting fancy, you can chain both thew new and add methods:
`ecs.new("player").add(PositionComponent)`

You can also query Entities, with the `ecs.list([])` method. Forgoing parameters will simply return every entity

## Components

Components are sets of data attached to entities. they comprise most of what an entity is. This is for things like positions, velocities, images, speech, anything. They are simple, plain dictionaries:
```
PositionComponent = Component("position", x=0, y=0)
ecs("player").add(PositionComponent)
```
Easy right? Hmm.. Now what if you didn't want player to start at 0,0? Well, it's easy:

`ecs("player").add(PositionComponent, x=100, y=200)`

The optional kwargs let you override any component's data as its added.

## Systems

Well, we know the very basics of Entities and components. In a metaphor, I'd say Entities and Components are to Eventity what HTML and CSS are to Web development. They hold data but have no *real* interaction, no dynamic-ness.

Systems are of course Javascript in this metaphor, they're going to drive our application. lets write a system that'll move player along the x axis every 'tick' or update.

```
from eventity import ecs, System, Component

PositionComponent = Component("position", x=0, y=0)

class MovementSystem(System):
    def set_up(self, eventmanager):
        eventmanager.subscribe(self.move, "move")

    def move(self, data):
        for entity in self.ecs.list(["position"]):
            entity.position["x"] += 10
            print("moving " + entity.id + " to " + str(entity.position))

ecs.register(MovementSystem)

ecs.new("player").add(PositionComponent)

ecs.send("move")
ecs.send("move")
ecs.send("move")

```

Now, that wasn't *too* hard was it? Lets work through it.

`class MovementSystem(System):`
Here we extend System, which we imported from ECS, this handles a bit of the logic so you can keep your systems nice and clean.

```
def set_up(self, eventmanager):
    eventmanager.subscribe(self.move, "move")
```

For systems, this will be your new constructor. This gets called by `System`'s `__init__`. If we were to add a new entity with the position component, they too will get shifted 10 on their x axis. Give it a try!

Passed into `set_up()` is the internal private Event Manager. This is your one shot at talking to it, so make it count. In this case we ask it to run `self.move(data)` when `ecs` is sent the "move" trigger. You can have as many triggers on one system as you like, but try to keep Systems short and concise to what it does.

```
def move(data):
    for entity in self.ecs.list(["position"]):
        entity.position["x"] += 10
        print("moving " + entity.id + " to " + str(entity.position))
```

Here we define the class method that the eventmanager will call when it hears "move". With most of these methods you'd receive the target in the data packet you send with `ecs.send("move", amount = 30)` but in this case we have no specific target, so we'll just query `ecs` for all the entities within our limits with `self.entities()`

As you can see, all the data belonging to each component is neatly stored within the class attribute of the same name, as a dictionary, you can do anything you want with the data, just make sure you only adjust data of the components you specified.
