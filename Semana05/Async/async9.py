import asyncio

async def fetch_data():
      print('start fetching')
      await asyncio.sleep(2)
      print('done fetching')
      return {'data': 1}

async def print_numbers():
      for i in range(10):
          print(i)
          await asyncio.sleep(0.25)

async def main():
      pass

asyncio.run(main())