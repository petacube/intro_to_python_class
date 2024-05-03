from dask.distributed import Client

client = Client()  # normal blocking client

async def f():
    future = client.submit(lambda x: x + 1, 10)
    result = await client.gather(future, asynchronous=True)
    return result

client.sync(f)
