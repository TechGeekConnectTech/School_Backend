import db.model.models
import db

def drop_all():
    db.base_engine.echo=True
    db.Base.metadata.drop_all(bind=db.base_engine)

if __name__ == '__main__':
    drop_all()