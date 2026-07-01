# Program 8: Task Interleaving (Context Switching)
# Concept: Watching a single thread switch back and forth between two different workflows using create_task.

import asyncio
from time import time,ctime
from tracemalloc import start

async def kitchen_crew():
    print(f"{ctime()} -> [Chef] puts noodle in boiling water...")
    await asyncio.sleep(1)  # Simulating a time-consuming task (e.g., cooking).
    print(f"{ctime()} -> [Chef] strains the noodles!")

async def bar_crew():
    print(f"{ctime()} -> [Bar] starts grinding coffee beans...")
    await asyncio.sleep(1)  # Simulating a time-consuming task (e.g., preparing a drink).
    print(f"{ctime()} -> [Bar] pours espresso shot!")

async def main():
    task_kitchen = asyncio.create_task(kitchen_crew()) 
    task_bar = asyncio.create_task(bar_crew()) 
    

    await task_kitchen # Awaiting the task to ensure it completes before moving on.
    await task_bar # Awaiting the task to ensure it completes before moving on.

if __name__ == "__main__":
    asyncio.run(main())