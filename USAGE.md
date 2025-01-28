<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from latitudesh_python_sdk import Latitudesh
import os

with Latitudesh(
    bearer=os.getenv("LATITUDESH_BEARER", ""),
) as latitudesh:

    res = latitudesh.api_keys.get_api_keys()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from latitudesh_python_sdk import Latitudesh
import os

async def main():
    async with Latitudesh(
        bearer=os.getenv("LATITUDESH_BEARER", ""),
    ) as latitudesh:

        res = await latitudesh.api_keys.get_api_keys_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->