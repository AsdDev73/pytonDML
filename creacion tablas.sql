-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema acceso_datos_2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema acceso_datos_2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `acceso_datos_2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `acceso_datos_2` ;

-- -----------------------------------------------------
-- Table `acceso_datos_2`.`almacenes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acceso_datos_2`.`almacenes` (
  `Almacenes_id` INT NOT NULL AUTO_INCREMENT,
  `Espacio` VARCHAR(45) NULL DEFAULT NULL,
  `Ubicación` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`Almacenes_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `acceso_datos_2`.`proveedores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acceso_datos_2`.`proveedores` (
  `Proveedores_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Dirección` VARCHAR(45) NULL DEFAULT NULL,
  `Teléfono` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Proveedores_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `acceso_datos_2`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acceso_datos_2`.`productos` (
  `Productos_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Precio` DOUBLE NULL DEFAULT NULL,
  `Descripción` VARCHAR(45) NULL DEFAULT NULL,
  `Proveedores_Proveedores_id` INT NULL DEFAULT NULL,
  `Almacenes_Almacenes_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Productos_id`),
  INDEX `Proveedores_Proveedores_id` (`Proveedores_Proveedores_id` ASC) VISIBLE,
  INDEX `Almacenes_Almacenes_id` (`Almacenes_Almacenes_id` ASC) VISIBLE,
  CONSTRAINT `productos_ibfk_1`
    FOREIGN KEY (`Proveedores_Proveedores_id`)
    REFERENCES `acceso_datos_2`.`proveedores` (`Proveedores_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `productos_ibfk_2`
    FOREIGN KEY (`Almacenes_Almacenes_id`)
    REFERENCES `acceso_datos_2`.`almacenes` (`Almacenes_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `acceso_datos_2`.`categorías`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acceso_datos_2`.`categorías` (
  `Categorías_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Descripción` VARCHAR(45) NULL DEFAULT NULL,
  `Productos_Productos_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Categorías_id`),
  INDEX `Productos_Productos_id` (`Productos_Productos_id` ASC) VISIBLE,
  CONSTRAINT `categorías_ibfk_1`
    FOREIGN KEY (`Productos_Productos_id`)
    REFERENCES `acceso_datos_2`.`productos` (`Productos_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `acceso_datos_2`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acceso_datos_2`.`clientes` (
  `Dni` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Apellidos` VARCHAR(45) NULL DEFAULT NULL,
  `Teléfono` INT NULL DEFAULT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `Dirección` VARCHAR(45) NULL DEFAULT NULL,
  `direccion` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`Dni`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `acceso_datos_2`.`gerentes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acceso_datos_2`.`gerentes` (
  `Gerentes_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Edad` INT NULL DEFAULT NULL,
  `Teléfono` INT NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`Gerentes_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `acceso_datos_2`.`empleados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acceso_datos_2`.`empleados` (
  `Empleados_id` INT NOT NULL AUTO_INCREMENT,
  `Nombre` VARCHAR(45) NULL DEFAULT NULL,
  `Apellido` VARCHAR(45) NULL DEFAULT NULL,
  `Puesto` VARCHAR(45) NULL DEFAULT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `Teléfono` INT NULL DEFAULT NULL,
  `Gerentes_Gerentes_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Empleados_id`),
  INDEX `Gerentes_Gerentes_id` (`Gerentes_Gerentes_id` ASC) VISIBLE,
  CONSTRAINT `empleados_ibfk_1`
    FOREIGN KEY (`Gerentes_Gerentes_id`)
    REFERENCES `acceso_datos_2`.`gerentes` (`Gerentes_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `acceso_datos_2`.`pedidos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `acceso_datos_2`.`pedidos` (
  `Pedidos_id` INT NOT NULL AUTO_INCREMENT,
  `Fecha_pedido` VARCHAR(45) NULL DEFAULT NULL,
  `Estado_pedido` VARCHAR(45) NULL DEFAULT NULL,
  `Precio` DOUBLE NULL DEFAULT NULL,
  `Clientes_Dni` INT NULL DEFAULT NULL,
  `Empleados_Empleados_id` INT NULL DEFAULT NULL,
  `Productos_Productos_id` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Pedidos_id`),
  INDEX `Clientes_Dni` (`Clientes_Dni` ASC) VISIBLE,
  INDEX `Empleados_Empleados_id` (`Empleados_Empleados_id` ASC) VISIBLE,
  INDEX `Productos_Productos_id` (`Productos_Productos_id` ASC) VISIBLE,
  CONSTRAINT `pedidos_ibfk_1`
    FOREIGN KEY (`Clientes_Dni`)
    REFERENCES `acceso_datos_2`.`clientes` (`Dni`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `pedidos_ibfk_2`
    FOREIGN KEY (`Empleados_Empleados_id`)
    REFERENCES `acceso_datos_2`.`empleados` (`Empleados_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `pedidos_ibfk_3`
    FOREIGN KEY (`Productos_Productos_id`)
    REFERENCES `acceso_datos_2`.`productos` (`Productos_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
