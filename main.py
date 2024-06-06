def on_forever():
    gameplay.set_difficulty(EASY)
    gameplay.set_game_mode(CREATIVE, mobs.target(ALL_PLAYERS))
loops.forever(on_forever)

def on_forever2():
    myEntitySelector: mobEvents.EntitySelector = None
    mobEvents.set_limit(myEntitySelector, 30)
loops.forever(on_forever2)

agent.teleport_to_player()
player.say(":)")
agent.move(FORWARD, 10)