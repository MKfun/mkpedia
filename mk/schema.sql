DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users ( 
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL,
    admin BOOL DEFAULT 0,

    profile_description TEXT,
    commit_n NUMBER
);

CREATE TABLE IF NOT EXISTS queue (
    username TEXT UNIQUE NOT NULL,
    hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS articles (
    title TEXT UNIQUE NOT NULL,
    data TEXT NOT NULL,
    made_by TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS messages (
    msgid INTEGER PRIMARY KEY AUTOINCREMENT,

    from_user TEXT NOT NULL,
    to_user TEXT NOT NULL,

    topic TEXT NOT NULL,
    data TEXT NOT NULL,

    answer_to INTEGER
);

INSERT INTO users VALUES("root", "ce5ca673d13b36118d54a7cf13aeb0ca012383bf771e713421b4d1fd841f539a", 1, "Рут-пользователь, мега-крут.", 0)
