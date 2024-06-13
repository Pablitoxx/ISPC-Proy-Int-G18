-- MySQL Script generated by MySQL Workbench
-- Thu Jun 13 18:17:57 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema reserva_rest
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema reserva_rest
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `reserva_rest` DEFAULT CHARACTER SET utf8mb4 ;
USE `reserva_rest` ;

-- -----------------------------------------------------
-- Table `reserva_rest`.`restaurante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reserva_rest`.`restaurante` (
  `restaurante_id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `calle` VARCHAR(45) NULL DEFAULT NULL,
  `numero` INT(11) NULL DEFAULT NULL,
  `tipo_de_comida` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`restaurante_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `reserva_rest`.`mesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reserva_rest`.`mesa` (
  `mesa_id` INT(11) NOT NULL AUTO_INCREMENT,
  `capacidad` INT(11) NULL DEFAULT NULL,
  `disponibilidad` TINYINT(1) NULL DEFAULT NULL,
  `restaurante_id` INT(11) NOT NULL,
  PRIMARY KEY (`mesa_id`),
  INDEX `rest_mes_fk` (`restaurante_id` ASC) VISIBLE,
  CONSTRAINT `rest_mes_fk`
    FOREIGN KEY (`restaurante_id`)
    REFERENCES `reserva_rest`.`restaurante` (`restaurante_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 33
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `reserva_rest`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reserva_rest`.`usuarios` (
  `usuario_id` INT(11) NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `contraseña` VARCHAR(45) NULL DEFAULT NULL,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Apellido` VARCHAR(45) NULL DEFAULT NULL,
  `telefono` INT(11) NOT NULL,
  PRIMARY KEY (`usuario_id`),
  UNIQUE INDEX `email` (`email` ASC) VISIBLE,
  UNIQUE INDEX `Nombre` (`Nombre` ASC) VISIBLE,
  UNIQUE INDEX `Apellido` (`Apellido` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table `reserva_rest`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `reserva_rest`.`reserva` (
  `reserva_id` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `hora` TIME NOT NULL,
  `usuario_id` INT(11) NOT NULL,
  `restaurante_id` INT(11) NOT NULL,
  PRIMARY KEY (`reserva_id`),
  INDEX `usu_res_fk` (`usuario_id` ASC) VISIBLE,
  INDEX `rest_res_fk` (`restaurante_id` ASC) VISIBLE,
  CONSTRAINT `rest_res_fk`
    FOREIGN KEY (`restaurante_id`)
    REFERENCES `reserva_rest`.`restaurante` (`restaurante_id`),
  CONSTRAINT `usu_res_fk`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `reserva_rest`.`usuarios` (`usuario_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4;

select * from reserva;
select * from mesa;

INSERT INTO restaurante (nombre, calle, numero, tipo_de_comida)
VALUES  ('Bohemia Mexican', 'Av Pueyrredon', 1345, 'Mexicana'),
		('Bohemia Chinese', 'Gral Paz', 72, 'China'),
        ('Bohemia Arabian', 'Av 24 de Septiebre', 791, 'Arabe'),
        ('Bohemia Burguer', 'Obispo Trejo', 1200, 'Hamburguesa'),
        ('Bohemia Italian', 'Av Colon', 2840, 'Italiana'),
        ('Bohemia Indian', 'Rondeu', 439, 'India'),
        ('Bohemia Grill', 'Rafael Nuñez', 3248, 'Parrilla'),
        ('Bohemia Fish & Shellfish', 'Sucre', 2504, 'Pescado y Marisco');


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
