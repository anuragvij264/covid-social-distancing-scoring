import sqlalchemy as db

engine = db.create_engine("mysql+mysqldb://user:password@0.0.0.0:3308/db")

def create_tables():

    conn = engine.connect()
    metadata = db.MetaData()

    images = db.Table('images',metadata,
                      db.Column('id', db.Integer()),
                      db.Column('timestamp',db.DateTime()),
                      db.Column('user_name',db.String()),
                      db.Column('media_url',db.String()),
                      db.Column('tweet_url',db.String()),
                      db.Column('output_dir',db.String())
 )
    metadata.create_all(engine)


def insert(table_name : str,vals,conn):


    query  = db.insert(table_name).values()
    result = conn.execute(query)

    return result


if __name__=='__main__':
    create_tables()

