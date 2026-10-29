from app.wallet.wallet_manager import wallet_manager



def test_phantom_connect():


    result = wallet_manager.connect_wallet(

        "phantom",

        "wallet_address"

    )


    assert result["status"] == "connected"
