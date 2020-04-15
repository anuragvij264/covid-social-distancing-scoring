import sqlalchemy as db

engine = db.create_engine("")

def create_tables():

    conn = engine.connect()
    metadata = db.MetaData()

    images = db.Table('images',metadata,
                      db.Column('id', db.Integer()),
                      db.Column('timestamp',db.DateTime()),
                      db.Column('user',db.String()),
                      db.Column('media_url',db.String()),
                      db.Column('tweet_url',db.String()),
                      db.Column('output_dir',db.String())
 )
    metadata.create_all(engine)