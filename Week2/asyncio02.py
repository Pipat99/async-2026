# Program 2: The Coroutine Object
# Concept: Seeing that calling an async def function creates an "Object" but does not execute it yet.

import asyncio

async def greet():
    print("Hello!")

coro_object = greet()  # This creates a coroutine object but does not execute it.

print(type(coro_object))  # This will print the coroutine object representation.

coro_object.close()  # This will close the coroutine object, preventing it from being awaited or executed.