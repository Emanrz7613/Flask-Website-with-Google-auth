-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema 3155_final_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema 3155_final_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `3155_final_project` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `3155_final_project` ;

-- -----------------------------------------------------
-- Table `3155_final_project`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`courses` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `subject` CHAR(4) NOT NULL,
  `course_num` CHAR(4) NOT NULL,  
  PRIMARY KEY (`course_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO courses (subject, course_num)
VALUES ('ITSC', '3155'), ('MATH', '1242'), ('ITSC', '1213'), ('ITIS', '3200');

-- -----------------------------------------------------
-- Table `3155_final_project`.`professors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`professors` (
  `professor_id` INT NOT NULL AUTO_INCREMENT,  
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`professor_id`)  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO professors (first_name, last_name)
VALUES ('Professor', 'One'), ('Professor', 'Two'), ('Professor', 'Three');

-- -----------------------------------------------------
-- Table `3155_final_project`.`professor_course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`professor_course` (
  `professor_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`professor_id`, `course_id`),
  INDEX `course_id_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `course_id`
    FOREIGN KEY (`course_id`)
    REFERENCES `3155_final_project`.`courses` (`course_id`),
  CONSTRAINT `professor_id`
    FOREIGN KEY (`professor_id`)
    REFERENCES `3155_final_project`.`professors` (`professor_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `3155_final_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,  
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO users (first_name, last_name, email)
VALUES ('Eric', 'Chaves', 'echaves@uncc.edu'), ('Ian', 'York', 'iyork@uncc.edu'), ('Ronnie', 'Johnston', 'rjohn249@uncc.edu'),
		('Dylan', 'D''''Eloia', 'ddeloia@uncc.edu'), ('Gabriel', 'Van Dreel', 'gvandree@uncc.edu');

-- -----------------------------------------------------
-- Table `3155_final_project`.`ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`ratings` (
  `rating_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `professor_id` INT NOT NULL,
  `rating` INT NOT NULL,
  `semester` VARCHAR(12) NOT NULL,
  `comments` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`rating_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `course_id_idx` (`course_id` ASC) VISIBLE,
  INDEX `professor_idx` (`professor_id` ASC) VISIBLE,
  CONSTRAINT `course`
    FOREIGN KEY (`course_id`)
    REFERENCES `3155_final_project`.`courses` (`course_id`),
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `3155_final_project`.`users` (`user_id`),
  CONSTRAINT `professor`
    FOREIGN KEY (`professor_id`)
    REFERENCES `3155_final_project`.`professors` (`professor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO ratings (user_id, course_id, professor_id, rating, semester, comments)
VALUES (1, 1, 1, 4, 'Spring 2023', 'half of course grade was based on tests, great if you are a good test taker'),
	(2,2,2,2, 'Fall 2022', 'I found this university class to be really engaging and thought-provoking - I learned so much!'),
    (3,3,3,3,'Spring 2023', 'The professor for this university class was fantastic - they were really passionate about the subject matter.'),
    (4,4,1,5,'Summer 2023', 'I was grateful for the opportunity to take this university class - it helped me develop new skills and perspectives.'),
    (5,1,2,2,'Spring 2023', 'This university class was challenging at times, but the material was so interesting that it was worth the effort.'),
    (1,2,3,1,'Fall 2022', 'The discussions we had in this university class were some of the most thought-provoking conversations I''''ve had in a long time'),
    (2,3,1,4, 'Spring 2023', 'I was surprised at how applicable the material in this university class was to my everyday life.');

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
