import kuzu
import os

def main() -> None:
    # Create an empty on-disk database and connect to it
    os.system("del demo.db")
    os.system("rmdir /s /q demo_db")
    db = kuzu.Database("demo_db")
    conn = kuzu.Connection(db)

    # Create schema

    conn.execute("CREATE NODE TABLE User(name STRING, age INT64, PRIMARY KEY (name))")
    conn.execute("CREATE NODE TABLE City(name STRING, population INT64, PRIMARY KEY (name))")
    conn.execute("CREATE REL TABLE Follows(FROM User TO User, since INT64)")
    conn.execute("CREATE REL TABLE LivesIn(FROM User TO City)")

    if not os.path.exists(r"data\follows.csv"):
        os.system(r"curl https://github.com/kuzudb/kuzu/raw/master/dataset/demo-db/csv/follows.csv -o data\follows.csv")
    if not os.path.exists(r"data\city.csv"):
        os.system(r"curl https://github.com/kuzudb/kuzu/raw/master/dataset/demo-db/csv/city.csv -o data\city.csv")
    if not os.path.exists(r"data\user.csv"):
        os.system(r"curl https://github.com/kuzudb/kuzu/raw/master/dataset/demo-db/csv/user.csv -o data\user.csv")
    if not os.path.exists(r"data\lives-in.csv"):
        os.system(r"curl https://github.com/kuzudb/kuzu/raw/master/dataset/demo-db/csv/lives-in.csv -o data\lives-in.csv")



    # Insert data
    conn.execute(r'COPY User FROM "data/user.csv"')
    conn.execute(r'COPY City FROM "data/city.csv"')
    conn.execute(r'COPY Follows FROM "data/follows.csv"')
    conn.execute(r'COPY LivesIn FROM "data/lives-in.csv"')

    # Execute Cypher query
    response = conn.execute(
        """
        MATCH (a:User)-[f:Follows]->(b:User)
        RETURN a.name, b.name, f.since;
        """
    )
    while response.has_next():
        print(response.get_next())

main()