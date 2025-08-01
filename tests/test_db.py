from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models
from app.database import Base

def test_log_saved():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    db = Session()
    db.add(models.RequestLog(wallet_address="TGzzB15h8YHHkeeEYoqEhK4nMxuU3cje6k"))
    db.commit()

    assert db.query(models.RequestLog).count() == 1
