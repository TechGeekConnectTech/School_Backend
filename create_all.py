import db.model.models
import db

def create_all():
    db.base_engine.echo=True
    db.Base.metadata.create_all(bind=db.base_engine)

if __name__ == '__main__':
    create_all()