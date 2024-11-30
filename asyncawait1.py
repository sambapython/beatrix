from time import sleep
import threading 
import os
import asyncio
import requests
import aiohttp
url = "http://localhost:8000/randomDepartment"
async def fun1():
    print("fun1 started")
    print(threading.current_thread().name)
    print(os.getpid())
    #await asyncio.sleep(10)
    async with aiohttp.ClientSession() as session:
        print("calling department API")
        await session.get(url)
        print("Done with department API call")
    #await requests.get(url)
    
    print("fun1 ended")
    
async def fun2():
    print("fun2 started")
    print(threading.current_thread().name)
    print(os.getpid())
    await asyncio.sleep(5)
    print("fun2 ended")
    
async def main():
    # Await the result of asyncio.gather to ensure the tasks are run concurrently
    await asyncio.gather(fun1(), fun2())
    
if __name__ == "__main__":
    asyncio.run(main())
