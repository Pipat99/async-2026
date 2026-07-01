import asyncio
from time import time, ctime


async def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!")


async def customer_task(customer):
    print(f"{ctime()}   [Task-{customer}] Taking Order ...")
    await asyncio.sleep(1)
    print(f"{ctime()}   [Task-{customer}] Taking Order ...Done!")

    print(f"{ctime()}   [Task-{customer}] Cooking Spaghetti ...")
    await asyncio.sleep(1)
    print(f"{ctime()}   [Task-{customer}] Cooking Spaghetti ...Done!")

    print(f"{ctime()}   [Task-{customer}] Manage Bar for Drink ...")
    await asyncio.sleep(1)
    print(f"{ctime()}   [Task-{customer}] Manage Bar for Drink ...Done!")

    print(f"{ctime()}   [Task-{customer}] All served!\n")


async def main():
    start_time = time()
    customers = ["A", "B", "C"]

    # Step 1: Greet customers one by one (sequential)
    for customer in customers:
        await greet_diners(customer)

    print(f"\n{ctime()} --- All customers greeted. Scheduling independent Async Tasks! ---\n")

    # Step 2: Run each customer's private workflow concurrently
    tasks = [customer_task(customer) for customer in customers]
    await asyncio.gather(*tasks)

    duration = time() - start_time
    print(f"{ctime()} Finished Entire Restaurant Operation in {duration:.2f} seconds.")


if __name__ == "__main__":
    asyncio.run(main())