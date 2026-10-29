from sqlalchemy.orm import Session


from app.database.models.trade import Trade

from app.database.models.ai_history import AIHistory

from app.database.models.wallet import WalletHistory




class Repository:



    def save_trade(
        self,
        db: Session,
        data
    ):


        trade = Trade(

            **data

        )


        db.add(

            trade

        )


        db.commit()


        db.refresh(

            trade

        )


        return trade





    def save_ai_history(
        self,
        db: Session,
        data
    ):


        history = AIHistory(

            **data

        )


        db.add(

            history

        )


        db.commit()


        db.refresh(

            history

        )


        return history





    def save_wallet(
        self,
        db: Session,
        data
    ):


        wallet = WalletHistory(

            **data

        )


        db.add(

            wallet

        )


        db.commit()


        db.refresh(

            wallet

        )


        return wallet



repository = Repository()
