from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import Wallet
from api.schemas import Operation
from exceptions import (
    OperationDoesNotExist,
    InsufficientFunds,
    WalletDoesNotExist,
    WrongData
)


async def get_wallet(wallet_id, session: AsyncSession):
    '''Get wallet by UUID.'''
    query = select(Wallet).where(Wallet.id == wallet_id)
    result = await session.execute(query)
    wallet = result.scalars().first()
    if not wallet:
        raise WalletDoesNotExist
    return wallet


async def add_wallet(wallet_balance, session: AsyncSession):
    '''Add new wallet.'''
    try:
        wallet = Wallet(balance=wallet_balance)
        session.add(wallet)
        await session.commit()
        await session.refresh(wallet)
        return wallet
    except:
        raise WrongData
    

async def get_wallets(session: AsyncSession):
    '''Get all wallets.'''
    query = select(Wallet)
    result = await session.execute(query)
    wallets = result.scalars().all()
    return wallets


async def put_wallet(wallet_id, operation: Operation, session: AsyncSession):
    '''Change wallet's balance.'''
    wallet = await get_wallet(wallet_id, session)
    if operation.operation_type.value == 'DEPOSIT':
        wallet.balance += operation.amount
        await session.commit()
        await session.refresh(wallet)
        return wallet
    if operation.operation_type.value == 'WITHDRAW':
        if wallet.balance >= operation.amount:
            wallet.balance -= operation.amount
            await session.commit()
            await session.refresh(wallet)
            return wallet
        raise InsufficientFunds
    raise OperationDoesNotExist
