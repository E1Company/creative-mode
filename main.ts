loops.forever(function () {
    gameplay.setDifficulty(EASY)
    gameplay.setGameMode(
    CREATIVE,
    mobs.target(ALL_PLAYERS)
    )
})
loops.forever(function () {
    let myEntitySelector: mobEvents.EntitySelector = null
    mobEvents.setLimit(myEntitySelector, 30)
})
agent.teleportToPlayer()
player.say(":)")
agent.move(FORWARD, 10)
