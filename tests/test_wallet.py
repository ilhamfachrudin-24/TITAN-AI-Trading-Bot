from app.wallet.manager import wallet_manager




def test_wallet():


    result = wallet_manager.check_wallet(

        "solana",

        "example_address"

    )


    assert result is not None
