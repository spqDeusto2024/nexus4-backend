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
INSERT INTO `usuarios` VALUES (3,'marina','$2b$12$D7B8ijPdPeEIprdydEvegu7m0RfYgSy1gmxPWd8jETj4pj1HZASwW'),(4,'admin','$2b$12$fThiOnyMfPfcF/fzQ1oceO6UwrvqGOKY8oVFg20UhfqIGLVIeb73G'),(5,'admin','$2b$12$ItepWO3R2VK.i42PxVLDGONwzzIfNzFxALNkgefIryUY2/4aR/UeG'),(6,'marina','$2b$12$i6cwBaQOpksdVQKgmvzzR.oMtl9usQ0Ja1s0FZilBVmsWADneKlv2'),(7,'marina','$2b$12$K/RQVkb0cRQ.fUlmpxp4euFLezqELQ/1lPoDUqQMqeg4bUjl7IP22'),(8,'UsuarioPrueba','$2b$12$LmDjREa2orwlYj65ymEVGeCAi8fS8cpIe2hnt78LLXgyO2Itj4REe'),(9,'UsuarioPrueba','$2b$12$Z0zy/LykqR5tYFySMsiTzOQf4lXeZg4aiqz9F0I9gkR4SYsFpUIPS'),(10,'UsuarioPrueba','$2b$12$9QYI1uEjfEJ4YXOhpa9cne019uUf4IqTMSl5RqKxUboexbchQYLUW'),(11,'UsuarioPrueba','$2b$12$GskUtGmK0g4tcoyNh8kq7eXxcZYgZ451iCNsRd2R4bJ8x4F3qeScW'),(12,'UsuarioPrueba','$2b$12$/tyoJrRcVQTT3fGLBaiuD.BVVfEahQP7UgGa9cusy1FMCmPgwvj/W'),(13,'UsuarioPrueba','$2b$12$Maiax1rJxHaSYDqZ7wY30OAmf2Yme7fnJHwoY/Yocp8wcX2zu7tHy'),(14,'UsuarioPrueba','$2b$12$WgGU.bICvc/R8/zul5rMEuMOfoSY7FLnjkpiP9UE4FBe4FI.iuZha'),(15,'UsuarioPrueba','$2b$12$V/aNMe7t9xq.ITJqrwmHOeZHbGCBDZbbHwWG366HzTeQ1O93Ar7Gy'),(16,'UsuarioPrueba','$2b$12$vgT3tmVvVq6Ld.CIkxt5bu2NmnG.LZoIl5uRoISTqlotYMSAq0G2C'),(17,'UsuarioPrueba','$2b$12$3E.NoWL6szqmobh86a.h2.elOWGumWEidhFF.dpUWrDKsaH3PqVfW'),(18,'UsuarioPrueba','$2b$12$qI/eC.2K7ShaMNiltZTEVO5pxNm4dyAD6/93xGVf3E7HL8CxUNv3W'),(19,'UsuarioPrueba','$2b$12$iq6K/TXerFZeIsnSAs56h.ziJpu4jdxpqfc83El3ERXM5t4MFAq9a'),(20,'UsuarioPrueba','$2b$12$gUYC5nIkf3t1HZC.oTck2Od8l.eKY9CJEnBvT7krepGbIY/6wEll.'),(21,'UsuarioPrueba','$2b$12$GLKFUZyOCZ9RxTMLwVHIBOAJ8RD5aGBtIeKvUHa4pG1rk2KnCrYvS'),(22,'UsuarioPrueba','$2b$12$p.HA0XiOeU7zn0HtE591nu4n7HYQxMNcoAUTb8/SZEev.MxoYvpny'),(23,'UsuarioPrueba','$2b$12$swQ3/Phyj7U2mYHHND1XQeCmsVQYt.2lYQZ00lEnUis/d0LoOftZ6'),(24,'UsuarioPrueba','$2b$12$qEOv.6ih5vC1k0nSFDURF.lRwFwBmTk0uCLEsAhVo0XeQA67/4Xnm'),(25,'UsuarioPrueba','$2b$12$2tJzOopZ82wCAOzttvDkJurKmBCYaPhU9UNNJi4YW4fDLvrn.UOi2'),(26,'UsuarioPrueba','$2b$12$ixuYiRMOgJ8jMlvjK3Yu2.CidLxliG8iCDVkixhafoOyfstfAMzk6'),(27,'UsuarioPrueba','$2b$12$a0JYDUzlmdA6Sx6Ps0gaEuxazSv1MnTSX.DcotKQJ91Nq67gSEcvW'),(28,'UsuarioPrueba','$2b$12$T/RGStIe/6EVBh3mnQ8VueQTN9Wk7PcJegqoqgMqNk4aK1tcL4gAS'),(29,'UsuarioPrueba','$2b$12$Nj35P6VDuFoB09Uppx5QMOaOR3/dD5FBMXk1G5fed7d0vRkdQ50RO'),(30,'UsuarioPrueba','$2b$12$iLdm2WTy7WMZwOqYnRD/DeUXxcv6NsidZ6A3sqwP2x69S82M8fps.'),(31,'UsuarioPrueba','$2b$12$F17gyFEG1WkWOWtASRIUP.TURx2lxKoZ45NJNZrj416t5y17kOstG'),(32,'UsuarioPrueba','$2b$12$GyGHiMrHyWSX6tgsWikubegCnnbAwJrjGJgZ/4qXLguqq6v53c/a6'),(33,'UsuarioPrueba','$2b$12$DMlFEsarzds41o.oKRVGM.Rg/5V92l1JAwUGGvjqWgiJyDbRoRjB.'),(34,'UsuarioPrueba','$2b$12$3KMvozYEQg4DTGnjV4uv0OtLQaLoSNEYzSOpbl/Iy4OpVY9GB.mIW'),(35,'UsuarioPrueba','$2b$12$KiE3VsRlEIjrgQFr/05HjexK7sTONVQybSHmYkA08pB20TdQOlQPe'),(36,'UsuarioPrueba','$2b$12$KmrDUlSQvRjP8m/sZGjp2uVYdc8lBosWyiTsZlIbRmhWgBDElLob.'),(37,'UsuarioPrueba','$2b$12$IYawujKD5Eqbh875oDYYBeq4GKT08h3FmtNGeON0mfJs5LvviJ7N6'),(38,'UsuarioPrueba','$2b$12$BEJUCmM7JSLCq6E8bGQXve86qA2LvjpTCr13sMqMeOH7jupSj8V52'),(39,'UsuarioPrueba','$2b$12$yWNl6qnMP801Z7QWmwNace2nKaUaYrmnxZXYfYbbtfLH1eNmk2sae'),(40,'UsuarioPrueba','$2b$12$a18xUg4NLziF1P91QM6lvu1R9vqAodfoBQDP5bpNzNG9bVxXYnGvu'),(41,'UsuarioPrueba','$2b$12$jiqsogLT3vJf2bKLEPTlRe1bbyVJoO8eg1dlAs14nemz0pE5.SaA6'),(42,'UsuarioPrueba','$2b$12$hJV.wNtYLdaeOyXA8GFJH.RU8b7P71VjiiFakiAIeuOx2F0vAsdX6'),(43,'UsuarioPrueba','$2b$12$74BSBKWiL0jVOmgY5DN6vuIiHa4euvJVm3T5HuHtbNI0L6rOazyQi'),(44,'UsuarioPrueba','$2b$12$nOXLcIhjD7toGXf0WDSVSeTuAhjd0vA8RyHb5PlxFdmavey7Zn9ga'),(45,'UsuarioPrueba','$2b$12$GKE2riFf35STNLDh1nYZK.kxKn9H0XF.qk66.scveLkPnHWQVR7Z6'),(46,'UsuarioPrueba','$2b$12$Nrz3OvydXSXCRyHTRXYPOu9riOXB8P6B4hI5fXBLt29q8/oTxFFSy'),(47,'UsuarioPrueba','$2b$12$1NFjTE4JOZwHF6DL9y1CEuULMmUbWxDtIDCMMAEOdGKM7wF1eZSxS'),(49,'UsuarioPrueba','$2b$12$Kz8nD0o/fO4s0RbFUgSVZu9Rl6Ys21t9PSam5sH1nGwie1OyLBBze'),(50,'UsuarioPrueba','$2b$12$LKizErYhw0TmzDYnCVnLFuuaw/ir/syvHwKH8lVRZxQMeQVIFhhiO'),(51,'UsuarioPrueba','$2b$12$hIidADuYe9FndmXWbyTuB.SGDiwuvxPDYgL4Q5.o63jeObCzux.CC'),(52,'UsuarioPrueba','$2b$12$v1jntYlI2GzbeJiMh0PNp.FeuWFprAxM2SDkX9mf2LYtyQQmqZiQC'),(53,'UsuarioPrueba','$2b$12$RdFZ8mNXFSX77BGIH6zOu./3dNHV8IhgmzD7N9KqeZ2L3KM37NBJi'),(54,'UsuarioPrueba','$2b$12$ZsZUO2xzCDnV6PsvgVsxpeUXGLGF3HILUbuylmbchJhCsgo3HrZu.'),(56,'UsuarioPrueba','$2b$12$CaC.4K7DIYTwtt5G60.uyOirF2FJ2KPyYi2DYDVYsdlnUOQFCsycm'),(57,'UsuarioPrueba','$2b$12$4myzjcRmwuT4GUUvP00DnOojPpjFhVKLKpdYh1EuUS9kwuHWE8sOq'),(58,'UsuarioPrueba','$2b$12$ANRmuHCmZGhjRFZ2V3LS1.2Snx/VyHQ95cczinrxHpEspLHnzVhKq'),(59,'UsuarioPrueba','$2b$12$JcaIuOcMkO6kcJzJzaxdxu8thaEAp5DSsprbZtEmW8oAgwFK0BuN6'),(60,'UsuarioPrueba','$2b$12$mxf1dGmHPo6M.m7zgt27EOav/aHRL/1eZQTrmU9J7xdXpkQ0Xwuei'),(61,'UsuarioPrueba','$2b$12$luanploBLvzr8jDfLMtIye9qCEonJaXJ4aT2h6ZmLDkV.T0B8CSrC'),(62,'UsuarioPrueba','$2b$12$yy59.tjZTHSeQcpSlstki.1xJ4cLoYth74rUrZvhHRnFTwm.MX70K'),(63,'UsuarioPrueba','$2b$12$rrrI8w9OijkhJObVg/yQVOvECAz6lDmXB3anP0PufbFP5ALvD8DeW'),(65,'UsuarioPrueba','$2b$12$vlzsgghnblz1ZoWLzQqU..B/VsGaGeAHOgDlJ.GpzindSBS8JNrfy'),(66,'UsuarioPrueba','$2b$12$tZNXv0YCIa1kcSlVka/mYub37hmKLul.eMFUhY1VWPaLT3bB1xwoS'),(67,'UsuarioPrueba','$2b$12$ycI6GP4oqZssMDKeuVrZru0XCDsyfRNOaaAjwUElmTds.6e/LTAnW'),(68,'UsuarioPrueba','$2b$12$7W7NPT2UL19fzhzPjmxiA.ORaf9ONV8lba2NJ3y1LAP53ORQP1fU.'),(69,'UsuarioPrueba','$2b$12$29cxLUCySm8lcS0RVLqbc.bqOSUZB4nAxmAjD3/3lg52PWYhbbC8i'),(70,'UsuarioPrueba','$2b$12$xLAb.xlLol95I0IzDWMQaeDmc5S6RRTiIM4Hvkj/87lW2STZPxWNS'),(71,'UsuarioPrueba','$2b$12$52/zogZrDs6HfU4dzGVYIOsJT32MnePJHh995fx4k4VzsACYwnEoK'),(73,'UsuarioPrueba','$2b$12$mzgH/iVLHHL20uklCyLZo.vF0ijOhfPG4wtJnRuZSRY1HCYqn7Cfi'),(74,'UsuarioPrueba','$2b$12$u4c0XECetnhXwGwB4n9EVe7M0i4Xwg6v0VMBLXsYOWLoJkN3ji0KK'),(75,'UsuarioPrueba','$2b$12$9VlBPCS44W.2NP0uybxH.e.5zJwBn4hW4UNAv5gzSkbk3gsPGMxUy'),(76,'UsuarioPrueba','$2b$12$INQvYdvuTBhklojLTO/T3eAt4F0O0sxUn.Lhp91VEPqMjQjLrK.lC'),(77,'UsuarioPrueba','$2b$12$rFmfXuXe6y6aCvqKNfVUwehtuICF613Mo.7EHBYS/rlQqKZmx2QtK'),(78,'UsuarioPrueba','$2b$12$kpOzxp3.bXsbuxnozC.Os.SRbZRCvxs2F8heSnRvJdI9bUOb4CybW'),(79,'UsuarioPrueba','$2b$12$w.Rh0Wd0KlOwK5nZYI6oBO5ITv.Ulr4pwKhUVhiFI92HscyZZAY/O'),(80,'UsuarioPrueba','$2b$12$pPLCuSYnFNBgFbXGjzGVqujVn8h6Q7Hl5Mp1H6F655hdkaYRWwHqu'),(81,'UsuarioPrueba','$2b$12$moata5bR9Q5fP9nGia33OutUGGNqLVOgMtqBPc4uLrQzkEQ0CBRCy'),(82,'UsuarioPrueba','$2b$12$OffOCQ6vDDwbOVfYKstv1uNl4zpRdFj/PuYSK1.vPvtPqACbr91zm'),(83,'UsuarioPrueba','$2b$12$6xG7AmsJbkNk7GRW1XRhTenKK3Qd9tUKX5rFKvx0VDYKkH.nxqFRe'),(84,'UsuarioPrueba','$2b$12$UM5CyHMH4Uicvpl6h24hzOG4JZBepDpkf6chpKJ1de8A.aITF1PDm'),(85,'UsuarioPrueba','$2b$12$Thiy5jk9xSNcrFh/24vY8OWq7mG.4QtEjBUUTRXQ0Qr.MYOd5gOCK'),(86,'UsuarioPrueba','$2b$12$nXrx7prvOPHE.S6CG5v0dOAA5kf2ywdfgTQPGBHU8QGF132SdGqMG'),(87,'UsuarioPrueba','$2b$12$HAu1/kwstLXyXEx6nlcOLuYBb1IwZjSQG9QP2k7.GZOYNbo7sPjqS'),(88,'UsuarioPrueba','$2b$12$RY0eEarmOJfNMjef/AHX5utb.xkOBPOhZLSxYQi8EuIwykwNK.LJi'),(89,'UsuarioPrueba','$2b$12$kKDxA7WXiNA295XsOKgPk.nNPD/inAW7RjBhPkM3ccl7Ex7TzlL7u'),(90,'UsuarioPrueba','$2b$12$WvxlL3eRPtjYKWuEetuE5OU1oFioRi7h00tTrV2yxZ1zJcLUrxlHC'),(91,'UsuarioPrueba','$2b$12$Ymth/Ge4RqhWZxcRyL24nufORTJWMf57GpVER9qSxhl.hgE1avyB6'),(92,'UsuarioPrueba','$2b$12$WN.sfNrv1zTWB2LRXf8bTeEwMJtwwmk6fpKWqMV9K0nAFF753e0JW'),(93,'UsuarioPrueba','$2b$12$eQ1CU3GXtTgVQ1oZEQJrku.kSg.aNnhy2TasYnHltkomDrMwDzV5.'),(94,'UsuarioPrueba','$2b$12$ZuzE1GfUeGRjFNGvEW8gQOMQjJ84y7Effpuo4EoFFjn6bSNEP9UB2'),(95,'UsuarioPrueba','$2b$12$L8lfnhpGpvieKcB/lgRiVuTRSAkmrF.opMzMpxQ3kmBWUZLtOP.pq'),(96,'UsuarioPrueba','$2b$12$RHyBDIdaHO.9x9l7qyMbtu0nGrQfUz.MSSIoalWXYYurW8n2wP16m'),(97,'UsuarioPrueba','$2b$12$r9cexrSbxGOXTGP.3xDrIuDe262irgEOmRFgPmoejovLK95H6Aguu'),(98,'UsuarioPrueba','$2b$12$g9pT7xdIpiHHAoq.drJ.M.f1XVnnIagZMt8h2D75X09/126EblYp.'),(99,'UsuarioPrueba','$2b$12$s.ObUAHxhaLKzgdclLYHlO3tWOViOqOeb5IygcEsIsVvyLkwT28FS'),(100,'UsuarioPrueba','$2b$12$u1yTuqmkwl/IQgsPKJdDcujo6PJnGrYMImx6Uh8uuQpZFabBcZ3P.'),(101,'UsuarioPrueba','$2b$12$UbXIhXHYbsiQ8YbJAZN5uuPntyI5QmX5T0cQp3vSAKiUqExa13O/G'),(102,'UsuarioPrueba','$2b$12$3qg3YqjO2Y2ig2uvxRbi5udVMwTndL4gzrx0Ye4/gFHOCZrzWoR/S'),(103,'UsuarioPrueba','$2b$12$JbUti8gLMLPp7cAV9Sr.ueJV2StmnEJyBbv2.I6kGuQnXMz9TmaDC'),(104,'UsuarioPrueba','$2b$12$oBEA/zazYVg4N7mbQu2XcO5OEd/P8Wce1XX0qnHBo3vrJNsiybzCa'),(105,'UsuarioPrueba','$2b$12$LZ3.fRcwkAgiU6xQaXuQQebn.Yylmvnag.FiJYz6hcUNTjZnUR2ca'),(106,'UsuarioPrueba','$2b$12$EhHpHjqcVO1hJTu5TR3sw.aRUE4iCQc1uPhXsgKzb7jD4JGk2GmYe'),(107,'UsuarioPrueba','$2b$12$5kzh3yJaskzdTyZWIiwvlOe9YDyefi/bTBWy8cvlnZl3WWZEM2PHq'),(108,'UsuarioPrueba','$2b$12$HOJFG9ozjAj9dXeK3DJoq.JE63rjAIB1L2bCelXShpvQIVo3VRJ0y'),(109,'UsuarioPrueba','$2b$12$hRFvcdcSpFkcz2kb/XwiAOzswlgSfqdh8m76rMID9cn2e7V1CDGde'),(111,'UsuarioPrueba','$2b$12$BdNZLEeZBxh1xN/JcDcajuFMQMF0iLeq4x06swGWcZ4YoYzSkE8Ty'),(112,'UsuarioPrueba','$2b$12$rmEl6qpBdRztkT/q/5zmxOO2f6lhh9NOkfmuot7LmfdaK3SI9Ukjm'),(113,'UsuarioPrueba','$2b$12$qLDG/xW3tjugeaj3anwNHuYQxbTLXQaaPyQVqjL8sVFebhEb8JZ76'),(114,'UsuarioPrueba','$2b$12$yR/.oQqTMQIlVr1IzCR2F.jKmm.akOei/eCxX1ZgluHvETzFXcnsa'),(115,'UsuarioPrueba','$2b$12$qFRtGu0lM6dp4DyaH5sEvuop2Vz/tNJ2aPyq0TRT8R.2/eCf5qxre'),(116,'UsuarioPrueba','$2b$12$66IrWjECKtlkeu1G..Ac8uN/QD0Y643Xwtb1wI4GNqyv/LJPWuJm6'),(117,'UsuarioPrueba','$2b$12$L7wdBFNoXyZzpg4IROMGK.r8EKC8KQG5TSiJ.rQt3yVMdmjOVPyZG'),(118,'UsuarioPrueba','$2b$12$e5ybi.kwm81vUeRYG.Y20Oe3xzI0jAR.LPv4f3yXoS03LczreMypS'),(119,'UsuarioPrueba','$2b$12$jClE8Z1M1oiUqoWBUsbY7ebOqz6j/FlMiCMIZeuDoaqgpO3P23lxK'),(120,'UsuarioPrueba','$2b$12$F0TuQQvaEg0gz1izyIuUvucP8d5aHUflZAQd/caoBTC9SiCk0Ogsa'),(121,'UsuarioPrueba','$2b$12$UAvn3g3CIljZ2dEj8VFqduew01e.zlnMa/rTGrps/E6btG.orkqoW'),(122,'UsuarioPrueba','$2b$12$Wz7MOIW/WVKlQka2xHHeJuSmbxbyzf47GHSNp8.5mLoW8O5kAxvfq'),(123,'UsuarioPrueba','$2b$12$A6aSNHM4nAnigUck2QK5H.CnC9kbc1iMUrV/4W.k6jPxxyqiQRGv2'),(125,'UsuarioPrueba','$2b$12$/S9ENwbQsKesluAt99q36.mKVRDhLT7rgBeDy22wRM5Rsz3Bgsrta'),(126,'UsuarioPrueba','$2b$12$796YJBtHnyV4mrtwjRPQEOZ4bl.NQp5e8Q750VrgkMtFhzturq5GK'),(127,'UsuarioPrueba','$2b$12$f9Stin3yJdIs3npmDCMNQO9Hv3kj8s8VDIlpXaj3n3crraXT1DJfS'),(128,'UsuarioPrueba','$2b$12$OifwLAPh5WKnQMuhoeelOurLOD0CgevAWrIUE3KhS5GL.2WaY70fq'),(129,'UsuarioPrueba','$2b$12$xqptP4wUealF43TaPTwBwOVd4VW9Sh56sAUNz2bYjopBRKinDqH3q'),(130,'UsuarioPrueba','$2b$12$T1BVhgE41YmXFg9phcxIauFy/K9P.SM/hhOaWcAZHSlJnSvZW8OJ2'),(131,'UsuarioPrueba','$2b$12$oTIAg.Q.RYwfWoEO.D4RL.6uYc6uNZHXgV9d93o5gJleTzj37Z1PC'),(132,'UsuarioPrueba','$2b$12$bUGHnL7c78eEfW.vVtWMueMitoNNlLFpZrUsv9fxerGgUSmXONfsq'),(133,'UsuarioPrueba','$2b$12$t1TRo1V2qThla8ZPb.hPT.nUsCqE3lZt6FYetOQEwPvSvtYNlXhpS'),(134,'UsuarioPrueba','$2b$12$NfNRawgWKCdYpcR2ukc1cuUJKP3SOEndKqpsKFhJNdVKNt2IdTJkW'),(135,'UsuarioPrueba','$2b$12$Iy8XYQWkThSO.ZooYplhe./OaruC9zDtmz0OpP3mEwFGS7wmelZha'),(136,'UsuarioPrueba','$2b$12$Rb.i8Irshc/impi/SdDuPe1FCsJ8K2cZh4EAQRp8F7HQlokpAJ/C.'),(137,'UsuarioPrueba','$2b$12$FwUC64T.nAmfLA1NZMFqn.6Kg5swWDtuQ30KxG3pXUaU.VsPDiLgG'),(138,'UsuarioPrueba','$2b$12$YKKtWEhSWmf0ml/MbYuCoeq9tGQkxf8lol6VkPygI37No3qq3CNRe'),(139,'UsuarioPrueba','$2b$12$3b/yR/SpQl0x6Db6p0Fxm.byYehoaRUSkCqYeIhcTssbChaccaYl6'),(140,'UsuarioPrueba','$2b$12$S4nlYA2sziBl.DPkayR5fuyY6L0Ea08Dsd/MZeIJDwi3AdJtUOiUK'),(141,'UsuarioPrueba','$2b$12$STn1mNpgZOlWomrF.8P4iOgMerHN6v2x5.6hLWQbGNXTJr2jV62x.'),(142,'UsuarioPrueba','$2b$12$o4P1SWJdR/BBXu8pzM.OquhkvVo/GdvY3EpQ5muxj3V6H3tyFGpGG'),(143,'UsuarioPrueba','$2b$12$gfIV6egNKJR81sGtizTmsu6XeVRN559DobimazkTjaXPcFperLfOm'),(145,'UsuarioPrueba','$2b$12$wv0e6AqIKHXk0KFwCOwe6ulGAU7igookg8vJ6o3RBw/DeB2mRrEsi'),(146,'UsuarioPrueba','$2b$12$L0wGg8IiLQYdEDbsngtDM.0eMO.ti7CKowWjSF9s.aRTG4jbAQ3oO'),(147,'UsuarioPrueba','$2b$12$UK7rY6na7W6Bim5l0BHo5eT9VaHF1Z72jLT/SVN1JKA6j.HiNJRFm'),(148,'UsuarioPrueba','$2b$12$NC0D9yxSQxsqPgLvG.eLa.VdvJZiW9nkOKbsR0YedH945lz4Gz/ou'),(149,'UsuarioPrueba','$2b$12$DqpaC6uomxNBgfpeRUkaFOtW7dZ.6FE3RTHP1ru85D6gx9v79Z9y.'),(150,'UsuarioPrueba','$2b$12$BFNG//KFzk0KIdT2P2G.NOIzxqZgLFqyN4VgVTn1OMIBQYepVRSKW'),(152,'UsuarioPrueba','$2b$12$Be3RRzjvxEzaOzDCBgA6VOcpHysvptzLk2p3RlvrEGRyPiHGcDMty'),(153,'UsuarioPrueba','$2b$12$hlWzYTy5HqtCWY1bvOsnZ.6uZI/iqqYbJII.jQOothJGDO5pMso/O'),(154,'UsuarioPrueba','$2b$12$7P3TpldVq32KYBWN1.3qA.ELPwKXs1SWeJEwmoEd89wBXiLE911fG'),(155,'UsuarioPrueba','$2b$12$kf2UC8z377TS4ugtVOa/jO5yMk.5jtAUaH5NzQA1uaiAzgI4uIg42'),(156,'UsuarioPrueba','$2b$12$sdNCNvAP7kDhrmHoUQcVsOHLEDgakUXiv/aDdthAlo3OwQkcgtHDC'),(157,'UsuarioPrueba','$2b$12$i8dYo2h38bWqhogPuonHuu3ZF.k50eOg64FByN.JwMl23bHMYnfg.'),(158,'UsuarioPrueba','$2b$12$7.WbiZwIcJM3lzu6Hn1dYug.r/Rl86wdhYTFeojPiW9KbWjPmBPAe'),(159,'UsuarioPrueba','$2b$12$Lkumw5SMjxsURpzKb7tq7uxqXsTKxDgHu4A0o.LsHJ6UkvyAYcVv2');
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
