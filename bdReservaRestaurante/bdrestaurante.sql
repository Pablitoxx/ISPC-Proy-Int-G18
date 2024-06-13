-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Restaurante
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Restaurante
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Restaurante` DEFAULT CHARACTER SET utf8 ;
USE `Restaurante` ;

-- -----------------------------------------------------
-- Table `Restaurante`.`Mesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Restaurante`.`Mesa` (
  `idMesa` INT NOT NULL,
  `Disponibilidad` TINYINT NULL,
  `Capacidad` INT NULL,
  PRIMARY KEY (`idMesa`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Restaurante`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Restaurante`.`Usuario` (
  `idUsuario` INT NOT NULL,
  `CorreoElectronico` VARCHAR(45) NULL,
  `Nombre` VARCHAR(45) NULL,
  `Contraseña` VARCHAR(45) NULL,
  PRIMARY KEY (`idUsuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Restaurante`.`Reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Restaurante`.`Reserva` (
  `idReserva` INT NOT NULL,
  `Fechayhora` DATETIME NULL,
  `Usuario_idUsuario` INT NOT NULL,
  `Mesa_idMesa` INT NOT NULL,
  PRIMARY KEY (`idReserva`, `Usuario_idUsuario`, `Mesa_idMesa`),
  INDEX `fk_Reserva_Usuario_idx` (`Usuario_idUsuario` ASC) VISIBLE,
  INDEX `fk_Reserva_Mesa1_idx` (`Mesa_idMesa` ASC) VISIBLE,
  CONSTRAINT `fk_Reserva_Usuario`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `Restaurante`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reserva_Mesa1`
    FOREIGN KEY (`Mesa_idMesa`)
    REFERENCES `Restaurante`.`Mesa` (`idMesa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
