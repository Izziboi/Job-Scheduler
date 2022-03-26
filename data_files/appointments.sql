BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "access" (
	"adminid"	INTEGER NOT NULL UNIQUE,
	"adminname"	TEXT NOT NULL UNIQUE,
	"adminpin"	NUMERIC NOT NULL UNIQUE,
	PRIMARY KEY("adminid" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "customers" (
	"adminid"	INTEGER NOT NULL UNIQUE,
	"jobdate"	NUMERIC NOT NULL,
	"customername"	TEXT NOT NULL,
	"customeraddress"	TEXT NOT NULL,
	"customerphone"	BLOB NOT NULL,
	"jobtype"	TEXT NOT NULL,
	"workingwith"	TEXT NOT NULL,
	PRIMARY KEY("adminid" AUTOINCREMENT)
);
INSERT INTO "access" VALUES (1,'Izzi',1212);
INSERT INTO "access" VALUES (2,'Nelly',1313);
INSERT INTO "access" VALUES (3,'Muanya',1414);
INSERT INTO "customers" VALUES (1,'28.08.2021','Israel Etu','Hasen 38','017626331093','Cleaning','Alone');
INSERT INTO "customers" VALUES (2,'29.08.2021','Nelly Etu','Ngodo','08068549127','Gardening','Ekene');
INSERT INTO "customers" VALUES (3,'28.08.2021','Muanya Etu','Okogeri','07061190525','Trashing','Anayo');
COMMIT;
