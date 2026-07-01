# Program 5: Sequential Execution (The Wrong Way)
# Concept: Showing that simply awaiting one after another is still sequential (Synchronous behavior).

import asyncio
from time import time,ctime

async def serve_costomer(name):
    print(f"{ctime()} -> Cooking for {name}...")
    await asyncio.sleep(1)  # Simulating a time-consuming task (e.g., cooking).
    print(f"{ctime()} -> Served {name}!")

async def main():
    start = time()
    # Sequentially awaiting each customer, which is not efficient.
    await serve_costomer("A")
    await serve_costomer("B")

    print(f"Total time: {time() - start:.2f} seconds") #will be around 2 seconds since we are awaiting each customer sequentially.

if __name__ == "__main__":
    asyncio.run(main())