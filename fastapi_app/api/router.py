from typing import List
from uuid import UUID as UUIDType

from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from api.crud import add_wallet, get_wallet, put_wallet, get_wallets
from api.schemas import Operation, WalletCreate, WalletResponse
from constans import EXPIRE_TIME
from database import get_async_session


router = APIRouter(
    prefix='/api/v1',
    tags=['API']
)


@router.post(
        '/wallets/{WALLET_UUID}/operation/', response_model=WalletResponse)
@cache(expire=EXPIRE_TIME)
async def update_wallet_balace(
    wallet_uuid: UUIDType,
    operation: Operation,
    session: AsyncSession = Depends(get_async_session)
):
    wallet = await put_wallet(wallet_uuid, operation, session)
    return wallet


@router.get('/wallets/{WALLET_UUID}/', response_model=WalletResponse)
@cache(expire=EXPIRE_TIME)
async def get_wallet_info(
    wallet_uuid: UUIDType,
    session: AsyncSession = Depends(get_async_session)
):
    wallet = await get_wallet(wallet_uuid, session)
    return wallet


@router.post('/wallets/', response_model=WalletResponse)
@cache(expire=EXPIRE_TIME)
async def post_wallet(
    wallet: WalletCreate, 
    session: AsyncSession = Depends(get_async_session)
):
    wallet = await add_wallet(wallet.balance, session)
    return wallet


@router.get('/wallets/', response_model=List[WalletResponse])
@cache(expire=EXPIRE_TIME)
async def get_wallets_info(session: AsyncSession = Depends(get_async_session)):
    wallets = await get_wallets(session)
    return wallets
