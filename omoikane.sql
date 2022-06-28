create table questions (
  id int AUTO_INCREMENT PRIMARY KEY,
  choiceWord varchar(255) NOT NULL,
  words varchar(255) NOT NULL,
  userId int NOT NULL,
  schoolYear int NOT NULL,
  subject varchar(255) NOT NULL,
  field varchar(255) NOT NULL
  );

insert into questions(choiceWord, words, userId, schoolYear, subject, field) VALUES ('織田信長', '本能寺の変,1582年,明智光秀',1, 6, '04', 'so102');
{"choiceWord": "徳川家康","words":"武田信玄,上杉謙信,毛利元就","userId":2,"schoolYear":3, "subject":"04", "field":"so102"}