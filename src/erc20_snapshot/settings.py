from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = "aleph.im swapper"
    admin_email: str = "hello@aleph.im"
    # account_pkey: str = Field(..., env='ACCT_PKEY')
    # account_type: str = Field(..., env='ACCT_TYPE')
    aleph_channel: str = "TEST"
    aleph_api_server: str = "https://api2.aleph.im"
    token_symbol: str = "ALEPH"
    
    ethereum_api_server: str = None
    ethereum_token_contract: str = "0xC0134b5B924c2FCA106eFB33C45446c466FBe03e"
    ethereum_chain_id: int = 1
    ethereum_pkey: str = ""
    ethereum_min_height: int = 10225485
    ethereum_decimals: int = 18
    ethereum_swap_fee: int = 10
    
    class Config:
        env_file = '.env'

settings = Settings()
