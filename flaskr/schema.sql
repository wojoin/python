-- DROP TABLE IF EXISTS entries;
CREATE table entries(
  id INTEGER PRIMARY KEY autoincrement,
  title text NOT NULL,
  'text' text NOT NULL
);