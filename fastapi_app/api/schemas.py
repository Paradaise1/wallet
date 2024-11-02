from enum import Enum
from uuid import UUID as UUIDType

from pydantic import BaseModel


class OperationType(str, Enum):
    '''Validation for operation_type.'''
    deposit = 'DEPOSIT'
    withdraw = 'WITHDRAW' 


class Operation(BaseModel):
    '''Model for change wallet.'''
    operation_type: OperationType
    amount: int


class WalletCreate(BaseModel):
    '''Model for add wallet.'''
    balance: int


class WalletResponse(WalletCreate):
    '''Model for add wallet(s).'''
    id: UUIDType
