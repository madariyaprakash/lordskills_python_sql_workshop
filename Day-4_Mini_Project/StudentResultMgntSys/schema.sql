-- ============================================
-- Student Result Management System - Schema
-- ============================================

CREATE DATABASE IF NOT EXISTS student_result_db;
USE student_result_db;

-- Students table
CREATE TABLE IF NOT EXISTS students (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    roll_no     VARCHAR(20)  NOT NULL UNIQUE,
    department  VARCHAR(50)  NOT NULL,
    email       VARCHAR(100) NOT NULL UNIQUE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Marks table
CREATE TABLE IF NOT EXISTS marks (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    student_id  INT NOT NULL,
    subject     VARCHAR(50) NOT NULL,
    marks       INT NOT NULL CHECK (marks BETWEEN 0 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
);

-- ============================================
-- Sample Data (Optional - for testing)
-- ============================================

INSERT INTO students (name, roll_no, department, email) VALUES
('Rahul Sharma',   'CS101', 'CSE', 'rahul@example.com'),
('Priya Verma',    'CS102', 'CSE', 'priya@example.com'),
('Amit Patel',     'CS103', 'CSE', 'amit@example.com');

INSERT INTO marks (student_id, subject, marks) VALUES
(1, 'Python',    85),
(1, 'SQL',       90),
(1, 'OS',        78),
(2, 'Python',    92),
(2, 'SQL',       88),
(2, 'OS',        95),
(3, 'Python',    70),
(3, 'SQL',       65),
(3, 'OS',        72);
