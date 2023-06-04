CREATE TABLE "movements" (
	"id"	INTEGER UNIQUE,
	"date"	TEXT NOT NULL,
	"time"	INTEGER NOT NULL,
	"base"	TEXT NOT NULL,
	"amount_base"	REAL NOT NULL,
	"quote"	TEXT NOT NULL,
	"amount_quote"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
	)