-- MariaDB dump 10.19  Distrib 10.8.3-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: RESTO
-- ------------------------------------------------------
-- Server version	10.8.3-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `articles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `paragraphe` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `publicateur` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image_publicateur` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date` date DEFAULT NULL,
  `heure` time DEFAULT NULL,
  `nombre_commentaire` int(11) DEFAULT NULL,
  `is_avant` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_articles_date` (`date`),
  KEY `ix_articles_id` (`id`),
  KEY `ix_articles_is_avant` (`is_avant`),
  KEY `ix_articles_nombre_commentaire` (`nombre_commentaire`),
  KEY `ix_articles_publicateur` (`publicateur`),
  KEY `ix_articles_titre` (`titre`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articles`
--

LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` VALUES
(1,'Poisson ou viande','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.','https://img.delicious.com.au/K_6cPgtU/w1200/del/2017/05/pumpkin-and-sage-baked-gnocchi-46215-2.jpg','Lionel messi','https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt60a365a71ea654cf/610e7c67b7f122324347cef9/6c0ca137302d22f3e6681c2873db8098102ab1e0.jpg','2020-10-10','10:00:00',2000,1),
(2,'Manger des fruits','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.','https://img.delicious.com.au/K_6cPgtU/w1200/del/2017/05/pumpkin-and-sage-baked-gnocchi-46215-2.jpg','Lionel messi','https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt60a365a71ea654cf/610e7c67b7f122324347cef9/6c0ca137302d22f3e6681c2873db8098102ab1e0.jpg','2020-10-10','10:00:00',160,1),
(3,'C\'est sans risque','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.','https://img.delicious.com.au/K_6cPgtU/w1200/del/2017/05/pumpkin-and-sage-baked-gnocchi-46215-2.jpg','Jessica JS','https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt60a365a71ea654cf/610e7c67b7f122324347cef9/6c0ca137302d22f3e6681c2873db8098102ab1e0.jpg','2020-10-10','10:00:00',60,0),
(4,'Bon pour la santé','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.','https://img.delicious.com.au/K_6cPgtU/w1200/del/2017/05/pumpkin-and-sage-baked-gnocchi-46215-2.jpg','Jeriella','https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt60a365a71ea654cf/610e7c67b7f122324347cef9/6c0ca137302d22f3e6681c2873db8098102ab1e0.jpg','2020-10-10','10:00:00',4,1),
(5,'Un légume par jour','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.','https://img.delicious.com.au/K_6cPgtU/w1200/del/2017/05/pumpkin-and-sage-baked-gnocchi-46215-2.jpg','David Beckham','https://assets.goal.com/v3/assets/bltcc7a7ffd2fbf71f5/blt60a365a71ea654cf/610e7c67b7f122324347cef9/6c0ca137302d22f3e6681c2873db8098102ab1e0.jpg','2020-10-10','10:00:00',10,1);
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menus`
--

DROP TABLE IF EXISTS `menus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `categorie` enum('starter','main','pastry_drink') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prix` int(11) DEFAULT NULL,
  `description` varchar(250) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_avant` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_menus_nom` (`nom`),
  KEY `ix_menus_id` (`id`),
  KEY `ix_menus_is_avant` (`is_avant`),
  KEY `ix_menus_prix` (`prix`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menus`
--

LOCK TABLES `menus` WRITE;
/*!40000 ALTER TABLE `menus` DISABLE KEYS */;
INSERT INTO `menus` VALUES
(1,'Poisson farcie','main',20,'Poisson sauce avec des légumes',1),
(2,'Thé cao','pastry_drink',10,'Boisson naturel',1),
(3,'Café au lait','pastry_drink',20,'Boisson naturel',1),
(4,'Salade de pâte','starter',5,'Pour commencer la journée',1),
(5,'Steak ','main',100,'Plat chik',1),
(6,'Poulet Sauce','main',75,'Plat chik',0),
(7,'Poisson sauté à l\'ail','main',240,'Plat chik',0),
(8,'Poivre vert ','starter',100,'Pour commencer la journée',0),
(9,'Coca-cola GM','pastry_drink',15,'Boisson naturel',0),
(10,'Chocolat chaud','pastry_drink',10,'Boisson naturel',1),
(11,'Composé ','starter',50,'Pour commencer la journée',1);
/*!40000 ALTER TABLE `menus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservations`
--

DROP TABLE IF EXISTS `reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reservations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `prenom` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `mail` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telephone` varchar(15) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `date` date DEFAULT NULL,
  `heure` time DEFAULT NULL,
  `nombre` int(11) DEFAULT NULL,
  `statut` enum('annulee','reservee') COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_reservations_date` (`date`),
  KEY `ix_reservations_id` (`id`),
  KEY `ix_reservations_nombre` (`nombre`),
  KEY `ix_reservations_statut` (`statut`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservations`
--

LOCK TABLES `reservations` WRITE;
/*!40000 ALTER TABLE `reservations` DISABLE KEYS */;
INSERT INTO `reservations` VALUES
(1,'Karen','Rashford','landry.aps@gmail.com','0348121147','2020-06-10','20:10:00',8,'annulee'),
(2,'Karen','Rashford','landry.aps@gmail.com','0348121147','2021-06-10','20:10:00',2,'reservee'),
(3,'Karen','Rashford','landry.aps@gmail.com','0348121147','2019-06-10','20:10:00',2,'annulee'),
(4,'Karen','Rashford','landry.aps@gmail.com','0348121147','2019-05-10','20:50:00',2,'annulee');
/*!40000 ALTER TABLE `reservations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-26 17:16:22
