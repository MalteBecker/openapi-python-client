from typing import Any, Dict, List, Optional, cast

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/tests/basic_lists/booleans".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[bool]]:
    if response.status_code == 200:
        response_200 = cast(List[bool], response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[bool]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[List[bool]]:
    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[List[bool]]:
    """Get a list of booleans"""

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[List[bool]]:
    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[List[bool]]:
    """Get a list of booleans"""

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
