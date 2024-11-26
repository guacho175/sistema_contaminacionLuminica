-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 20-11-2024 a las 01:34:09
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `ds1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Instrumento de medición', 7, 'add_instrumentomedicion'),
(26, 'Can change Instrumento de medición', 7, 'change_instrumentomedicion'),
(27, 'Can delete Instrumento de medición', 7, 'delete_instrumentomedicion'),
(28, 'Can view Instrumento de medición', 7, 'view_instrumentomedicion'),
(29, 'Can add Medición', 8, 'add_medicion'),
(30, 'Can change Medición', 8, 'change_medicion'),
(31, 'Can delete Medición', 8, 'delete_medicion'),
(32, 'Can view Medición', 8, 'view_medicion'),
(33, 'Can add Detalle luminaria', 9, 'add_detalleluminarias'),
(34, 'Can change Detalle luminaria', 9, 'change_detalleluminarias'),
(35, 'Can delete Detalle luminaria', 9, 'delete_detalleluminarias'),
(36, 'Can view Detalle luminaria', 9, 'view_detalleluminarias'),
(37, 'Can add Representante legal', 10, 'add_representantelegal'),
(38, 'Can change Representante legal', 10, 'change_representantelegal'),
(39, 'Can delete Representante legal', 10, 'delete_representantelegal'),
(40, 'Can view Representante legal', 10, 'view_representantelegal'),
(41, 'Can add Titular', 11, 'add_titular'),
(42, 'Can change Titular', 11, 'change_titular'),
(43, 'Can delete Titular', 11, 'delete_titular'),
(44, 'Can view Titular', 11, 'view_titular'),
(45, 'Can add Proyecto', 12, 'add_proyecto'),
(46, 'Can change Proyecto', 12, 'change_proyecto'),
(47, 'Can delete Proyecto', 12, 'delete_proyecto'),
(48, 'Can view Proyecto', 12, 'view_proyecto'),
(49, 'Can add Cargo', 13, 'add_cargo'),
(50, 'Can change Cargo', 13, 'change_cargo'),
(51, 'Can delete Cargo', 13, 'delete_cargo'),
(52, 'Can view Cargo', 13, 'view_cargo'),
(53, 'Can add Institucion', 14, 'add_institucion'),
(54, 'Can change Institucion', 14, 'change_institucion'),
(55, 'Can delete Institucion', 14, 'delete_institucion'),
(56, 'Can view Institucion', 14, 'view_institucion'),
(57, 'Can add Usuario', 15, 'add_usuario'),
(58, 'Can change Usuario', 15, 'change_usuario'),
(59, 'Can delete Usuario', 15, 'delete_usuario'),
(60, 'Can view Usuario', 15, 'view_usuario'),
(61, 'Can add Fiscalización', 16, 'add_fiscalizacion'),
(62, 'Can change Fiscalización', 16, 'change_fiscalizacion'),
(63, 'Can delete Fiscalización', 16, 'delete_fiscalizacion'),
(64, 'Can view Fiscalización', 16, 'view_fiscalizacion'),
(65, 'Can add Reporte', 17, 'add_reporte'),
(66, 'Can change Reporte', 17, 'change_reporte'),
(67, 'Can delete Reporte', 17, 'delete_reporte'),
(68, 'Can view Reporte', 17, 'view_reporte');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$K1fQIgJzlgxoMW56veB0A3$7IcNwsEbVt0xCKWdGkHqPTKKH19Wf7xKfvQMntfp3o8=', '2024-11-16 21:18:44.213432', 1, 'Admin', '', '', 'admin@admin.ad', 1, 1, '2024-11-16 21:18:28.780994');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargo`
--

DROP TABLE IF EXISTS `cargo`;
CREATE TABLE IF NOT EXISTS `cargo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `descripcion` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `cargo`
--

INSERT INTO `cargo` (`id`, `nombre`, `descripcion`) VALUES
(1, 'Inspector', 'asd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalle_luminarias`
--

DROP TABLE IF EXISTS `detalle_luminarias`;
CREATE TABLE IF NOT EXISTS `detalle_luminarias` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `tipo_lampara` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `marca` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `modelo` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `potencia` double NOT NULL,
  `fecha_instalacion` date NOT NULL,
  `cod_certificacion` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `fecha_certificacion` date NOT NULL,
  `creado` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `detalle_luminarias`
--

INSERT INTO `detalle_luminarias` (`id`, `cantidad`, `tipo_lampara`, `marca`, `modelo`, `potencia`, `fecha_instalacion`, `cod_certificacion`, `fecha_certificacion`, `creado`) VALUES
(1, 123, 'we', 'qwwe', 'we', 123, '2024-11-16', 'qwe', '2024-11-16', '2024-11-16 21:33:09.232476');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb3_spanish2_ci,
  `object_repr` varchar(200) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb3_spanish2_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-11-16 21:33:09.253109', '1', 'qwe', 1, '[{\"added\": {}}]', 9, 1),
(2, '2024-11-16 21:33:32.726142', '1', 'legal ll lll', 1, '[{\"added\": {}}]', 10, 1),
(3, '2024-11-16 21:33:48.075299', '1', 'titu tt tt', 1, '[{\"added\": {}}]', 11, 1),
(4, '2024-11-16 21:36:23.106603', '1', 'Faro, tipo de alumbrado: Peatonal ', 1, '[{\"added\": {}}]', 12, 1),
(5, '2024-11-16 21:36:54.353139', '1', 'Inspector asd', 1, '[{\"added\": {}}]', 13, 1),
(6, '2024-11-16 21:37:05.197933', '1', 'SMD smd', 1, '[{\"added\": {}}]', 14, 1),
(7, '2024-11-16 21:37:07.493444', '1', '1212 asdasd12 asd assd', 1, '[{\"added\": {}}]', 15, 1),
(8, '2024-11-16 21:37:11.860423', '1', 'Faro, asdasd12 assd', 1, '[{\"added\": {}}]', 16, 1),
(9, '2024-11-16 22:10:41.318185', '1', 'Luxómetro', 1, '[{\"added\": {}}]', 7, 1),
(10, '2024-11-16 22:10:47.005225', '1', '0 0.5', 1, '[{\"added\": {}}]', 8, 1),
(11, '2024-11-19 00:43:12.126955', '2', '0 2.0', 1, '[{\"added\": {}}]', 8, 1),
(12, '2024-11-19 01:01:48.208839', '3', '1 3.0', 1, '[{\"added\": {}}]', 8, 1),
(13, '2024-11-19 01:02:20.706681', '4', '1 1.0', 1, '[{\"added\": {}}]', 8, 1),
(14, '2024-11-19 02:44:17.411781', '3', '1 3.0', 3, '', 8, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'mediciones', 'instrumentomedicion'),
(8, 'mediciones', 'medicion'),
(9, 'proyectos', 'detalleluminarias'),
(10, 'proyectos', 'representantelegal'),
(11, 'proyectos', 'titular'),
(12, 'proyectos', 'proyecto'),
(13, 'usuarios', 'cargo'),
(14, 'usuarios', 'institucion'),
(15, 'usuarios', 'usuario'),
(16, 'fiscalizacion', 'fiscalizacion'),
(17, 'fiscalizacion', 'reporte');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-16 21:16:50.583050'),
(2, 'auth', '0001_initial', '2024-11-16 21:16:51.245362'),
(3, 'admin', '0001_initial', '2024-11-16 21:16:51.575098'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-16 21:16:51.586261'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-16 21:16:51.593820'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-16 21:16:51.707455'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-16 21:16:51.786831'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-16 21:16:51.853516'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-16 21:16:51.868055'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-16 21:16:51.927067'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-16 21:16:51.929085'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-16 21:16:51.939257'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-16 21:16:51.999528'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-16 21:16:52.051774'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-16 21:16:52.101943'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-16 21:16:52.115257'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-16 21:16:52.167751'),
(18, 'usuarios', '0001_initial', '2024-11-16 21:16:52.350966'),
(19, 'proyectos', '0001_initial', '2024-11-16 21:16:52.612668'),
(20, 'fiscalizacion', '0001_initial', '2024-11-16 21:16:52.859028'),
(21, 'mediciones', '0001_initial', '2024-11-16 21:16:53.041096'),
(22, 'sessions', '0001_initial', '2024-11-16 21:16:53.092740'),
(23, 'mediciones', '0002_medicion_foto_alter_medicion_fiscalizacion_and_more', '2024-11-19 17:22:33.453880'),
(24, 'proyectos', '0002_proyecto_foto', '2024-11-19 17:50:34.732169');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb3_spanish2_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('kbyvsxnlz5ea1a10tx0ktlj3llhpeyc4', '.eJxVjEEOwiAQAP_C2ZClFLA9evcFxpBl2Vi0BVPak_Hv2qQHvc5M5iU8rsvg18qzT1H0QonDLwtID86biHfMtyKp5GVOQW6J3G2V5xJ5PO3t32DAOmxbDkTWNqjhaDrjQDtlmFmZ2NjYdMFQR8gEoQVwrQELxrBymjTGwPCdThwTpZK5-oWnZ5lx5Cr6y_X9ATk1QaM:1tDIkI:AXw4HouXqYND0k3Kah1kPoAyOYteSH44z52fpmcO2lw', '2024-12-03 07:33:58.021201');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fiscalizacion`
--

DROP TABLE IF EXISTS `fiscalizacion`;
CREATE TABLE IF NOT EXISTS `fiscalizacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `creado` datetime(6) NOT NULL,
  `proyecto_id` bigint NOT NULL,
  `usuario_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fiscalizacion_proyecto_id_71907d10` (`proyecto_id`),
  KEY `fiscalizacion_usuario_id_4c184ee6` (`usuario_id`)
) ENGINE=MyISAM AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `fiscalizacion`
--

INSERT INTO `fiscalizacion` (`id`, `creado`, `proyecto_id`, `usuario_id`) VALUES
(1, '2024-11-16 21:37:11.851221', 1, 1),
(31, '2024-11-20 01:32:53.012910', 4, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `institucion`
--

DROP TABLE IF EXISTS `institucion`;
CREATE TABLE IF NOT EXISTS `institucion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `descripcion` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `institucion`
--

INSERT INTO `institucion` (`id`, `nombre`, `descripcion`) VALUES
(1, 'SMD', 'smd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instrumento_medicion`
--

DROP TABLE IF EXISTS `instrumento_medicion`;
CREATE TABLE IF NOT EXISTS `instrumento_medicion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(1) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `marca` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `modelo` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `num_serie` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `instrumento_medicion`
--

INSERT INTO `instrumento_medicion` (`id`, `tipo`, `marca`, `modelo`, `num_serie`) VALUES
(1, '0', 'qweweqewqwe', 'asd', 'asd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicion`
--

DROP TABLE IF EXISTS `medicion`;
CREATE TABLE IF NOT EXISTS `medicion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(1) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `latitud` double NOT NULL,
  `longitud` double NOT NULL,
  `temperatura` double DEFAULT NULL,
  `humedad` double DEFAULT NULL,
  `valor_medido` double NOT NULL,
  `cumplimiento` varchar(1) COLLATE utf8mb3_spanish2_ci DEFAULT NULL,
  `observacion` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `creado` datetime(6) NOT NULL,
  `fiscalizacion_id` bigint NOT NULL,
  `instrumento_medicion_id` bigint NOT NULL,
  `foto` varchar(100) COLLATE utf8mb3_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `medicion_fiscalizacion_id_fcf6403b` (`fiscalizacion_id`),
  KEY `medicion_instrumento_medicion_id_95125e82` (`instrumento_medicion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `medicion`
--

INSERT INTO `medicion` (`id`, `tipo`, `latitud`, `longitud`, `temperatura`, `humedad`, `valor_medido`, `cumplimiento`, `observacion`, `creado`, `fiscalizacion_id`, `instrumento_medicion_id`, `foto`) VALUES
(1, '0', -29.905656, -71.274206, 25, 54, 0.5, NULL, 'qweqwe', '2024-11-16 22:10:46.993231', 1, 1, 'medicion/medicion.png'),
(10, '0', 1, 1, 1, 1, 1, NULL, '1', '2024-11-19 06:45:44.605873', 1, 1, 'medicion/medicion.png'),
(11, '0', 2, 2, 2, 2, 2, NULL, '22', '2024-11-19 06:53:11.756795', 1, 1, 'medicion/medicion.png'),
(12, '0', 3, 3, 3, 3, 3, NULL, '3', '2024-11-19 06:54:17.991227', 1, 1, 'medicion/medicion.png'),
(13, '0', 4, 4, 4, 4, 4, NULL, '4', '2024-11-19 07:07:35.353241', 1, 1, 'medicion/medicion.png'),
(14, '0', 4, 4, 4, 4, 4, NULL, '4', '2024-11-19 07:10:57.471628', 1, 1, 'medicion/medicion.png'),
(15, '0', 5, 5, 5, 5, 5, NULL, '5', '2024-11-19 07:15:07.544224', 1, 1, 'medicion/medicion.png'),
(16, '0', 6, 6, 6, 6, 6, NULL, '6', '2024-11-19 07:15:23.590375', 1, 1, 'medicion/medicion.png'),
(19, '0', 7, 7, 7, 7, 7, NULL, '7', '2024-11-19 07:54:48.838719', 1, 1, 'medicion/medicion.png'),
(20, '0', 8, 8, 8, 8, 8, NULL, '8', '2024-11-19 07:58:43.921505', 1, 1, 'medicion/medicion.png'),
(28, '0', 1, 1, 1, 1, 1, NULL, '1', '2024-11-20 01:33:06.900058', 31, 1, 'medicion/medicion.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

DROP TABLE IF EXISTS `proyecto`;
CREATE TABLE IF NOT EXISTS `proyecto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `latitud` double NOT NULL,
  `longitud` double NOT NULL,
  `tipo_alumbrado` varchar(1) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `descripcion` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `creado` datetime(6) NOT NULL,
  `detalle_luminarias_id` bigint NOT NULL,
  `representante_legal_id` bigint NOT NULL,
  `titular_id` bigint NOT NULL,
  `foto` varchar(100) COLLATE utf8mb3_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_detalle_luminarias_id_dedf9604` (`detalle_luminarias_id`),
  KEY `proyecto_representante_legal_id_a960c619` (`representante_legal_id`),
  KEY `proyecto_titular_id_0f63ba6e` (`titular_id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`id`, `nombre`, `latitud`, `longitud`, `tipo_alumbrado`, `descripcion`, `creado`, `detalle_luminarias_id`, `representante_legal_id`, `titular_id`, `foto`) VALUES
(1, 'Faro', -29.9055459, -71.2743113, 'p', 'Le farou', '2024-11-16 21:36:23.087945', 1, 1, 1, 'proyectos/20112024_005337.jpg'),
(4, 'aaa', 1, 1, 'v', 'asdasdzxaas', '2024-11-19 19:13:28.231214', 1, 1, 1, 'proyectos/20112024_004549.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reporte`
--

DROP TABLE IF EXISTS `reporte`;
CREATE TABLE IF NOT EXISTS `reporte` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `creado` datetime(6) NOT NULL,
  `fiscalizacion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reporte_fiscalizacion_id_6e6a2f3a` (`fiscalizacion_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `representante_legal`
--

DROP TABLE IF EXISTS `representante_legal`;
CREATE TABLE IF NOT EXISTS `representante_legal` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `run` varchar(15) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `a_paterno` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `a_materno` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `direccon` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `correo` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `creado` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `representante_legal`
--

INSERT INTO `representante_legal` (`id`, `run`, `nombre`, `a_paterno`, `a_materno`, `direccon`, `correo`, `creado`) VALUES
(1, '12312313', 'legal', 'll', 'lll', 'lalala', 'alla@laal.cl', '2024-11-16 21:33:32.722688');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `titular`
--

DROP TABLE IF EXISTS `titular`;
CREATE TABLE IF NOT EXISTS `titular` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `run` varchar(15) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `a_paterno` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `a_materno` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `direccon` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `correo` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `creado` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `titular`
--

INSERT INTO `titular` (`id`, `run`, `nombre`, `a_paterno`, `a_materno`, `direccon`, `correo`, `creado`) VALUES
(1, '123123', 'titu', 'tt', 'tt', 'tt', 'tt@ss.cl', '2024-11-16 21:33:48.072294');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `run` varchar(15) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `a_paterno` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `a_materno` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `correo` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `creado` datetime(6) NOT NULL,
  `cargo_id` bigint NOT NULL,
  `institucion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_cargo_id_f8845872` (`cargo_id`),
  KEY `usuario_institucion_id_fc051b5b` (`institucion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `run`, `nombre`, `a_paterno`, `a_materno`, `correo`, `creado`, `cargo_id`, `institucion_id`) VALUES
(1, '1212', 'asdasd12', 'asd', 'assd', 'asd@asda.cl', '2024-11-16 21:37:07.481905', 1, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
