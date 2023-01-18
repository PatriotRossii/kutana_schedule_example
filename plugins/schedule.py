from kutana import Plugin

plugin = Plugin("TestPlugin")

# Prints egg every 5 seconds
@plugin.schedule(5)
async def egg_printer():
    print("Its Egg!")

# Prints apple every second
@plugin.schedule(1)
async def apple_printer():
    print("Its Apple!")
