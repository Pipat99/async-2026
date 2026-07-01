# Program 10: Extracting Return Values from Tasks
# Concept: Accessing returned results from completed Task objects using .result() or direct assignment.

import asyncio

async def calculate_bill(costumer, base_price):
    print(f"Calculating reciept for Costumer {costumer}...")
    await asyncio.sleep(1)
    final_price = base_price * 1.07
    return final_price

async def main():

    task_a = asyncio.create_task(calculate_bill("A", 100)) 
    task_b = asyncio.create_task(calculate_bill("B", 200)) 
    
    print(f'Main program can do other things while Task A and Task B run in background.')

    # Awaiting the tasks to ensure they complete before moving on.
    result_a = await task_a
    result_b = await task_b

    print(f"Costumer A's final bill: ${result_a:.2f}")
    print(f"Costumer B's final bill: ${result_b:.2f}")
    print(f"Costumer Total Revenue: ${result_a + result_b:.2f}")

if __name__ == "__main__":
    asyncio.run(main())