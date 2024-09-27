DROP TABLE IF EXISTS questions_mapper;
DROP TABLE IF EXISTS current_session;

CREATE TABLE question_mapper (
    Id integer PRIMARY KEY AUTOINCREMENT,
    skill text,
    file_name text
    ); 

CREATE TABLE current_session (
    Id integer PRIMARY KEY AUTOINCREMENT,
    file_name text
    );

INSERT INTO question_mapper (skill, file_name) VALUES ('finance', 'financial_questions.json'); 
