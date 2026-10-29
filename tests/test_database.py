from app.database.postgres import engine




def test_database():


    assert engine is not None
