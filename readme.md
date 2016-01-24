# What is Eventity?
Eventity is an Event based ECS system all about speed and ease of use, full of features that aren't specific to one use. Feel free to use Eventity in your next GUI, Game, Text adventure, anything really. It's all possible.

The ease of use comes from the "build once and forget" approach one has to take when using it. Say in the context of a game you have to draw all sprites. In any other approach you explicitly call a draw function on every bit and bob and you end up with a giant soup of draw calls, but in eventity, the correct approach would have you do nothing but register a system. And in that system you built once, will loop over all future entities that contain a position and an image without you have to say a thing.

Just imagine that, the only thing between you and getting a new image onto the screen is

```
j = ecs.new()
ecs.add(j, _position, x=50, y=30)
ecs.add(j, _image, path="./resource/image/player.png")
```
and Eventity will(with your intention, no magic on this one) apply all your logic to the player and draw it.

The overall ideology here is as follows:
- An entity is nothing but an ID and attached components
- A system is not tied to one entity, but loops over all entities with chosen components
- A component has no logic, only data
- A system will do nothing without being told to(outside its `set_up` constructor)

# Installation
`pip install eventity` or simply clone this repo and run `python setup.py install`

# Learning
All the information to learning eventity will be kept up to date in the [wiki](https://github.com/JonSnowbd/Eventity/wiki)
