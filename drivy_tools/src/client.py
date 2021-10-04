import random
from typing import Any, List

import httpx
from pydantic import BaseModel
from user_agent import generate_user_agent

from drivy_tools.state import state


class HTTPClient(BaseModel):
    client: Any = None
    async_enabled: bool = True
    proxies: List[str] = None

    async def _request(self, *args, **kwargs):
        method = kwargs.pop("method")
        kwargs["headers"] = kwargs.get("headers", {"User-Agent": generate_user_agent()})
        if state.config.DEFAULT.proxy_enabled:
            # kwargs["proxies"] = self.get_random_proxy()
            self.client.proxies = self.get_random_proxy()
        if self.async_enabled:
            resp = await getattr(self.client, method)(*args, **kwargs)
        else:
            resp = getattr(self.client, method)(*args, **kwargs)

        return resp

    def __init__(self, **data: Any):
        super().__init__(**data)
        timeout = data.pop("timeout", state.config.HTTPX.timeout)
        if self.async_enabled:
            max_keepalive_conn = data.pop("max_keepalive_connections", state.config.HTTPX.httpx_max_keepalive_conn)
            max_conn = data.pop("max_connections", state.config.HTTPX.httpx_max_conn)
            limits = httpx.Limits(max_keepalive_connections=max_keepalive_conn, max_connections=max_conn)
            self.client = httpx.AsyncClient(limits=limits, timeout=timeout)
        else:
            self.client = httpx.Client(timeout=timeout)

    def get_random_proxy(self):
        proxy = random.choice(self.proxies)
        return {"http": proxy, "https": proxy}

    async def get(self, *args, **kwargs):
        return await self._request(method="get", *args, **kwargs)

    async def post(self, *args, **kwargs):
        return await self._request(method="post", *args, **kwargs)

    async def path(self, *args, **kwargs):
        return await self._request(method="patch", *args, **kwargs)

    async def delete(self, *args, **kwargs):
        return await self._request(method="delete", *args, **kwargs)

    async def close(self):
        if self.async_enabled:
            await self.client.aclose()
        else:
            self.client.close()
