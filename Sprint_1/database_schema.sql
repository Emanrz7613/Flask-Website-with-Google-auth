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
-- Table `3155_final_project`.`departments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`departments` (
  `department_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`department_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `3155_final_project`.`professors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`professors` (
  `professor_id` INT NOT NULL AUTO_INCREMENT,
  `deparment_id` INT NOT NULL,
  `first_name` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`professor_id`),
  INDEX `department_id_idx` (`deparment_id` ASC) VISIBLE,
  CONSTRAINT `department_id`
    FOREIGN KEY (`deparment_id`)
    REFERENCES `3155_final_project`.`departments` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `3155_final_project`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`courses` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `subject` CHAR(4) NOT NULL,
  `course_num` CHAR(4) NOT NULL,
  `course_title` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`course_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `3155_final_project`.`professor_course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`professor_course` (
  `professor_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  PRIMARY KEY (`professor_id`, `course_id`),
  INDEX `course_id_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `professor_id`
    FOREIGN KEY (`professor_id`)
    REFERENCES `3155_final_project`.`professors` (`professor_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `course_id`
    FOREIGN KEY (`course_id`)
    REFERENCES `3155_final_project`.`courses` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `3155_final_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`users` (
  `user_id` INT NOT NULL,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `3155_final_project`.`ratings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `3155_final_project`.`ratings` (
  `rating_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `course_id` INT NOT NULL,
  `rating` INT NOT NULL,
  `semester` VARCHAR(12) NOT NULL,
  `comments` VARCHAR(255) NULL,
  PRIMARY KEY (`rating_id`),
  INDEX `user_id_idx` (`user_id` ASC) VISIBLE,
  INDEX `course_id_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `3155_final_project`.`users` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `course`
    FOREIGN KEY (`course_id`)
    REFERENCES `3155_final_project`.`courses` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
