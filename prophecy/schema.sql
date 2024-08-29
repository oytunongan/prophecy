CREATE TABLE studentsnew (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    id INTEGER,
    house TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE assignments (
    id INTEGER,
    student_name TEXT,
    house TEXT,
    PRIMARY KEY(id)
);
