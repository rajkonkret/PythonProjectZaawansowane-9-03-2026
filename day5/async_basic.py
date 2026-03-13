import time
import asyncio


async def count():
    print("Start!")
    await asyncio.sleep(3.5567)
    print("Koniec")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter()
    print(f"{__file__} wykonany w czasie {elapsed - s:.2f} s")
