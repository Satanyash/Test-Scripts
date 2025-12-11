from sqlalchemy import create_engine, inspect
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:1234@localhost:5432/QA"
db = create_engine(db_connection_string)

def test_add():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("insert into subject(\"subject_id\", \"subject_title\") values (:new_id, :new_subject)")
    connection.execute(sql, {"new_id": 17, "new_subject": "Programming"})
    sql_statement = text("select * from subject where subject_title = :subject")
    result = connection.execute(sql_statement, {"subject": "Programming"})
    rows = result.mappings().all()
    row = rows[0]
    assert len(rows) == 1
    assert row['subject_title'] == "Programming"
    sql = text("delete from subject where subject_title = :title")
    connection.execute(sql, {"title": "Programming"})
    transaction.commit()
    connection.close()

def test_edit():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("update subject set subject_title = :new_title where subject_title = :title")
    connection.execute(sql, {"new_title": "RUSSIAN", "title": "Russian"})
    sql_statement = text("select * from subject where subject_title = :title")
    result = connection.execute(sql_statement, {"title": "RUSSIAN"})
    rows = result.mappings().all()
    row = rows[0]
    assert len(rows) == 1
    assert row['subject_title'] == "RUSSIAN"
    sql = text("update subject set subject_title = :new_title where subject_title = :title")
    connection.execute(sql, {"new_title": "Russian", "title": "RUSSIAN"})
    transaction.commit()
    connection.close()

def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("insert into subject(\"subject_id\", \"subject_title\") values (:new_id, :new_subject)")
    connection.execute(sql, {"new_id": 17, "new_subject": "Programming"})
    sql = text("select * from subject")
    list_old = connection.execute(sql)
    rows = list_old.mappings().all()
    len_old = len(rows)
    sql = text("delete from subject where subject_id = :id")
    connection.execute(sql, {"id": 17})
    sql = text("select * from subject")
    list_new = connection.execute(sql)
    rows = list_new.mappings().all()
    len_new = len(rows)
    assert len_old - len_new == 1
    transaction.commit()
    connection.close()