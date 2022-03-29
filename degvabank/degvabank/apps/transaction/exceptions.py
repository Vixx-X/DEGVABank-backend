import enum

class TransactionError(enum.Enum):
    ERROR = 0
    INVALID_ORIGIN_ACCOUNT = 1
    DOCUMENT_ID_DID_NOT_MATCH_ORIGIN_ACCOUNT = 2
    INSUFICIENT_FUNDS = 3
    INVALID_ORIGIN_CARD = 4
    CVC_DID_NOT_MATCH_ORIGIN_CARD = 5
    EXP_DATE_DID_NOT_MATCH_ORIGIN_CARD = 6
    EXP_DATE_EXPIRED_ORIGIN_CARD = 7
    INSUFICIENT_CREDITS = 8
    INVALID_TARGET_ACCOUNT = 9
    DOCUMENT_ID_DID_NOT_MATCH_TARGET_ACCOUNT = 10
    INVALID_TARGET_CARD = 11
    EXP_DATE_DID_NOT_MATCH_TARGET_CARD = 12
    EXP_DATE_EXPIRED_TARGET_CARD = 13
    TRANSACTION_TOOK_TOO_LONG = 14
    UNKNOWN_TRANSACTION_ERROR = 15