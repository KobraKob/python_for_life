--JOINS are used to combine columns from two or more tables based on a related column between them.

--INNER JOIN
-- The INNER JOIN returns only the rows that have matching values in both tables. It's the most common type of join and acts like an intersection.


-- Create tables
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    grade_level INT
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_name VARCHAR(100),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Insert sample data
INSERT INTO students (student_id, student_name, grade_level) VALUES
(1, 'Alice', 10),
(2, 'Brian', 11),
(3, 'Carla', 10);

INSERT INTO enrollments (enrollment_id, student_id, course_name) VALUES
(101, 1, 'Mathematics'),
(102, 1, 'Biology'),
(103, 2, 'Chemistry');

--JOIN
select
	s.student_id,
	s.student_name,
	s.grade_level,
	e.course_name
from students as s
inner join enrollments as e
	on s.student_id = e.student_id



--Left Join
--A LEFT JOIN is a type of database operation that combines data from two tables, ensuring that all rows from the left (first) table are included in the result.
SELECT
    s.student_id,
    s.student_name,
    s.grade_level,
    e.course_name
FROM students AS s
LEFT JOIN enrollments AS e
    ON s.student_id = e.student_id;




-- Feature				INNER JOIN																	LEFT JOIN
-- Purpose				To return only the records where a match exists in both tables.				To return all records from the left table (Table A), and any matching records from the right table (Table B).
-- Matching Data		Only rows that have corresponding entries in the link column are included.	Matching rows are included.
-- Non-Matching Data	Excluded (If a student isn't enrolled, they are out).						Included (If a student isn't enrolled, they are still in the result, but the course columns show NULL).
-- Visual Analogy		The intersection of the two tables.	T										he entire first table plus the matching part of the second table.
