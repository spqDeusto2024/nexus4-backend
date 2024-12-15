-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: nexus4
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `empleo`
--

DROP TABLE IF EXISTS `empleo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `empleo` varchar(50) DEFAULT NULL,
  `edad_minima` int DEFAULT NULL,
  `id_estancia` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_estancia` (`id_estancia`),
  CONSTRAINT `empleo_ibfk_1` FOREIGN KEY (`id_estancia`) REFERENCES `estancia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleo`
--

LOCK TABLES `empleo` WRITE;
/*!40000 ALTER TABLE `empleo` DISABLE KEYS */;
INSERT INTO `empleo` VALUES (1,'Recepcionista',18,1),(2,'Limpiador',21,2),(3,'Mantenimiento',25,3),(4,'Cocinero',18,4),(5,'Gerente',30,5);
/*!40000 ALTER TABLE `empleo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estancia`
--

DROP TABLE IF EXISTS `estancia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estancia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `personas_actuales` int DEFAULT NULL,
  `capacidad_max` int DEFAULT NULL,
  `recurso_id` int DEFAULT NULL,
  `capacidad_maxima_alcanzada` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `recurso_id` (`recurso_id`),
  CONSTRAINT `estancia_ibfk_1` FOREIGN KEY (`recurso_id`) REFERENCES `recurso` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estancia`
--

LOCK TABLES `estancia` WRITE;
/*!40000 ALTER TABLE `estancia` DISABLE KEYS */;
INSERT INTO `estancia` VALUES (1,'Estancia A','Habitacin',2,4,1,0),(2,'Estancia B','Apartamento',3,6,2,0),(3,'Estancia C','Suite',1,3,3,0),(4,'Estancia D','Casa',5,8,4,0),(5,'Estancia E','Oficina',0,10,5,0);
/*!40000 ALTER TABLE `estancia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `familia`
--

DROP TABLE IF EXISTS `familia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `familia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `apellido` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `familia`
--

LOCK TABLES `familia` WRITE;
/*!40000 ALTER TABLE `familia` DISABLE KEYS */;
INSERT INTO `familia` VALUES (1,'Gomez'),(2,'Martinez'),(3,'Perez'),(4,'Lopez'),(5,'Fernandez');
/*!40000 ALTER TABLE `familia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inquilino`
--

DROP TABLE IF EXISTS `inquilino`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inquilino` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `nacimiento` timestamp NULL DEFAULT NULL,
  `muerte` timestamp NULL DEFAULT NULL,
  `familia_id` int DEFAULT NULL,
  `empleo_id` int DEFAULT NULL,
  `roles_id` int DEFAULT NULL,
  `id_estancia` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `familia_id` (`familia_id`),
  KEY `empleo_id` (`empleo_id`),
  KEY `roles_id` (`roles_id`),
  KEY `id_estancia` (`id_estancia`),
  CONSTRAINT `inquilino_ibfk_1` FOREIGN KEY (`familia_id`) REFERENCES `familia` (`id`),
  CONSTRAINT `inquilino_ibfk_2` FOREIGN KEY (`empleo_id`) REFERENCES `empleo` (`id`),
  CONSTRAINT `inquilino_ibfk_3` FOREIGN KEY (`roles_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `inquilino_ibfk_4` FOREIGN KEY (`id_estancia`) REFERENCES `estancia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inquilino`
--

LOCK TABLES `inquilino` WRITE;
/*!40000 ALTER TABLE `inquilino` DISABLE KEYS */;
INSERT INTO `inquilino` VALUES (1,'Juan Perez','Residente','2023-05-10 10:00:00',NULL,1,1,1,1),(2,'Maria Lopez','Visita','1995-08-15 08:30:00',NULL,2,2,2,2),(3,'Carlos Gomez','Trabajador','1987-03-22 14:20:00',NULL,3,3,3,3),(4,'Ana Fernandez','Residente','2000-11-12 09:00:00',NULL,4,4,4,4),(5,'Luis Martinez','Residente','1990-01-05 18:45:00',NULL,5,5,5,5);
/*!40000 ALTER TABLE `inquilino` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recurso`
--

DROP TABLE IF EXISTS `recurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recurso` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  `capacidad_min` int DEFAULT NULL,
  `capacidad_max` int DEFAULT NULL,
  `capacidad_actual` int DEFAULT NULL,
  `capacidad_maxima_alcanzada` tinyint(1) DEFAULT NULL,
  `capacidad_minima_alcanzada` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recurso`
--

LOCK TABLES `recurso` WRITE;
/*!40000 ALTER TABLE `recurso` DISABLE KEYS */;
INSERT INTO `recurso` VALUES (1,'Recurso A',5,20,10,0,0),(2,'Recurso B',3,15,14,0,0),(3,'Recurso C',10,30,25,0,0),(4,'Recurso D',8,25,5,0,0),(5,'Recurso E',2,10,2,0,0);
/*!40000 ALTER TABLE `recurso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Administrador'),(2,'Usuario'),(3,'Supervisor'),(4,'Empleado'),(5,'Invitado');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `fullname` varchar(50) DEFAULT NULL,
  `age` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (3,'marina','$2b$12$D7B8ijPdPeEIprdydEvegu7m0RfYgSy1gmxPWd8jETj4pj1HZASwW'),(4,'admin','$2b$12$fThiOnyMfPfcF/fzQ1oceO6UwrvqGOKY8oVFg20UhfqIGLVIeb73G'),(5,'admin','$2b$12$ItepWO3R2VK.i42PxVLDGONwzzIfNzFxALNkgefIryUY2/4aR/UeG'),(6,'marina','$2b$12$i6cwBaQOpksdVQKgmvzzR.oMtl9usQ0Ja1s0FZilBVmsWADneKlv2');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-15 16:31:32