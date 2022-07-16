-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sociedad_de_panes
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema sociedad_de_panes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sociedad_de_panes` DEFAULT CHARACTER SET utf8 ;
USE `sociedad_de_panes` ;

-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`careers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`careers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`collegues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`collegues` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NULL,
  `adress` VARCHAR(200) NULL,
  `district` VARCHAR(155) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user` VARCHAR(30) NULL,
  `code` INT NULL,
  `num_wp` INT NULL,
  `password` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `career_id` INT NOT NULL,
  `collegue_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_careers1_idx` (`career_id` ASC) VISIBLE,
  INDEX `fk_users_collegues1_idx` (`collegue_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_careers1`
    FOREIGN KEY (`career_id`)
    REFERENCES `sociedad_de_panes`.`careers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_collegues1`
    FOREIGN KEY (`collegue_id`)
    REFERENCES `sociedad_de_panes`.`collegues` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`locations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `day` VARCHAR(15) NULL,
  `location` VARCHAR(65) NULL,
  `reference` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `collegue_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_locations_collegues1_idx` (`collegue_id` ASC) VISIBLE,
  CONSTRAINT `fk_locations_collegues1`
    FOREIGN KEY (`collegue_id`)
    REFERENCES `sociedad_de_panes`.`collegues` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`posts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(155) NULL,
  `content` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_posts_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_posts_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `sociedad_de_panes`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `content` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_comments_posts1_idx` (`post_id` ASC) VISIBLE,
  CONSTRAINT `fk_comments_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `sociedad_de_panes`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `sociedad_de_panes`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`post_categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`post_categories` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(145) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`post_categories_has_posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`post_categories_has_posts` (
  `post_category_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  PRIMARY KEY (`post_category_id`, `post_id`),
  INDEX `fk_post_categories_has_posts_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_post_categories_has_posts_post_categories1_idx` (`post_category_id` ASC) VISIBLE,
  CONSTRAINT `fk_post_categories_has_posts_post_categories1`
    FOREIGN KEY (`post_category_id`)
    REFERENCES `sociedad_de_panes`.`post_categories` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_post_categories_has_posts_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `sociedad_de_panes`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`reactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`reactions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`reactions_has_posts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`reactions_has_posts` (
  `reaction_id` INT NOT NULL,
  `post_id` INT NOT NULL,
  PRIMARY KEY (`reaction_id`, `post_id`),
  INDEX `fk_reactions_has_posts_posts1_idx` (`post_id` ASC) VISIBLE,
  INDEX `fk_reactions_has_posts_reactions1_idx` (`reaction_id` ASC) VISIBLE,
  CONSTRAINT `fk_reactions_has_posts_reactions1`
    FOREIGN KEY (`reaction_id`)
    REFERENCES `sociedad_de_panes`.`reactions` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reactions_has_posts_posts1`
    FOREIGN KEY (`post_id`)
    REFERENCES `sociedad_de_panes`.`posts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`reactions_has_comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`reactions_has_comments` (
  `reaction_id` INT NOT NULL,
  `comment_id` INT NOT NULL,
  PRIMARY KEY (`reaction_id`, `comment_id`),
  INDEX `fk_reactions_has_comments_comments1_idx` (`comment_id` ASC) VISIBLE,
  INDEX `fk_reactions_has_comments_reactions1_idx` (`reaction_id` ASC) VISIBLE,
  CONSTRAINT `fk_reactions_has_comments_reactions1`
    FOREIGN KEY (`reaction_id`)
    REFERENCES `sociedad_de_panes`.`reactions` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reactions_has_comments_comments1`
    FOREIGN KEY (`comment_id`)
    REFERENCES `sociedad_de_panes`.`comments` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sociedad_de_panes`.`careers_has_collegues`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `sociedad_de_panes`.`careers_has_collegues` (
  `career_id` INT NOT NULL,
  `collegue_id` INT NOT NULL,
  PRIMARY KEY (`career_id`, `collegue_id`),
  INDEX `fk_careers_has_collegues_collegues1_idx` (`collegue_id` ASC) VISIBLE,
  INDEX `fk_careers_has_collegues_careers1_idx` (`career_id` ASC) VISIBLE,
  CONSTRAINT `fk_careers_has_collegues_careers1`
    FOREIGN KEY (`career_id`)
    REFERENCES `sociedad_de_panes`.`careers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_careers_has_collegues_collegues1`
    FOREIGN KEY (`collegue_id`)
    REFERENCES `sociedad_de_panes`.`collegues` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
