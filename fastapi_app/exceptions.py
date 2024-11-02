from fastapi import status, HTTPException


WalletDoesNotExist = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Такого кошелька не существует.'
)

InsufficientFunds = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Недостаточно средств на кошельке.'
)

OperationDoesNotExist = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Такой операции не существует.'
)

WrongData = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Неверные данные.'
)
