DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS beer;
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
-- TODO:
--   add:
--     "synonyms": "Guinness Draught",
--     "abv":"4.2",
--     "tags":["irish_dry_stout","dry_stout","stout"],
CREATE TABLE beer (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  description TEXT NOT NULL,
  number_of_review INTEGER DEFAULT 0,
  total_rating INTEGER DEFAULT 0
);
CREATE TABLE reivew (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  beer_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  comment TEXT,
  rating INTEGER DEFAULT 5 CHECK(
    rating BETWEEN 1 AND 5
  ),
  FOREIGN KEY (author_id) REFERENCES user (id),
  FOREIGN KEY (beer_id) REFERENCES beer (id)
);
