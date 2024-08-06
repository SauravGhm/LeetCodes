
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(3)
    print("World printed after 3 secs")

async def main():
    await say_hello()

#Run the main function 
asyncio.run(main())

