# Objective: Compare the structural and mechanical differences of both strategies in a racing scenario.
import asyncio
from time import ctime

async def runner(name, speed):
    await asyncio.sleep(speed)
    return f"{name} crossed line!"

async def main():
    # Case 1: Using gather() -> We must wait for All items to finish to get the ordered list
    print(f"{ctime()} --- Starting gather() approach (Unified Aggregation) ---")
    all_finishes = await asyncio.gather(runner("A", 0.5), runner("B", 2.0))
    print(f"{ctime()} Gather output: {all_finishes}\n")
    
    # Case 2: Using wait() -> We can break execution flow when the first item finishes
    print(f"{ctime()} --- Starting wait() approach (State control / Racing) ---")
    active_tasks = {asyncio.create_task(runner("A", 0.5)), asyncio.create_task(runner("B", 2.0))}
    
    done, pending = await asyncio.wait(active_tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"{ctime()} Wait output: The winner of the race is -> {list(done)[0].result()}")
    
    # Case 3: Cancel any remaining pending tasks to avoid unnecessary execution
    for t in pending:
        t.cancel()

asyncio.run(main())