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

    max_keepalive_connections: int = None
    max_connections: int = None

    async def _request(self, *args, **kwargs):
        method = kwargs.pop("method")
        kwargs["headers"] = kwargs.get("headers", {"User-Agent": generate_user_agent()})

        if self.async_enabled:
            max_keepalive_conn = (
                self.max_keepalive_connections
                if self.max_keepalive_connections
                else state.config.HTTPX.httpx_max_keepalive_conn
            )
            max_conn = self.max_connections if self.max_connections else state.config.HTTPX.httpx_max_conn
            limits = httpx.Limits(max_keepalive_connections=max_keepalive_conn, max_connections=max_conn)
            proxies = self.get_random_proxy() if state.config.DEFAULT.async_enabled else None
            async with httpx.AsyncClient(limits=limits, timeout=state.config.HTTPX.timeout, proxies=proxies) as client:
                resp = await getattr(client, method)(*args, **kwargs)
        else:
            proxies = self.get_random_proxy() if state.config.DEFAULT.async_enabled else None
            with httpx.Client(timeout=state.config.HTTPX.timeout, proxies=proxies) as client:
                resp = getattr(client, method)(*args, **kwargs)
        return resp

    def get_random_proxy(self):
        proxy = random.choice(self.proxies)
        if not proxy.startswith("http://"):
            proxy = "http://" + proxy
        return {"http://": proxy, "https://": proxy}

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
