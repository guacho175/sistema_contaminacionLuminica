-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 27-11-2024 a las 01:12:55
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
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'Inspectores');

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
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

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
(33, 'Can add Detalle luminaria', 9, 'add_detalleluminaria'),
(34, 'Can change Detalle luminaria', 9, 'change_detalleluminaria'),
(35, 'Can delete Detalle luminaria', 9, 'delete_detalleluminaria'),
(36, 'Can view Detalle luminaria', 9, 'view_detalleluminaria'),
(37, 'Can add Persona', 10, 'add_persona'),
(38, 'Can change Persona', 10, 'change_persona'),
(39, 'Can delete Persona', 10, 'delete_persona'),
(40, 'Can view Persona', 10, 'view_persona'),
(41, 'Can add Representante legal', 11, 'add_representantelegal'),
(42, 'Can change Representante legal', 11, 'change_representantelegal'),
(43, 'Can delete Representante legal', 11, 'delete_representantelegal'),
(44, 'Can view Representante legal', 11, 'view_representantelegal'),
(45, 'Can add Titular', 12, 'add_titular'),
(46, 'Can change Titular', 12, 'change_titular'),
(47, 'Can delete Titular', 12, 'delete_titular'),
(48, 'Can view Titular', 12, 'view_titular'),
(49, 'Can add Proyecto', 13, 'add_proyecto'),
(50, 'Can change Proyecto', 13, 'change_proyecto'),
(51, 'Can delete Proyecto', 13, 'delete_proyecto'),
(52, 'Can view Proyecto', 13, 'view_proyecto'),
(53, 'Can add Fiscalización', 14, 'add_fiscalizacion'),
(54, 'Can change Fiscalización', 14, 'change_fiscalizacion'),
(55, 'Can delete Fiscalización', 14, 'delete_fiscalizacion'),
(56, 'Can view Fiscalización', 14, 'view_fiscalizacion'),
(57, 'Can add Reporte', 15, 'add_reporte'),
(58, 'Can change Reporte', 15, 'change_reporte'),
(59, 'Can delete Reporte', 15, 'delete_reporte'),
(60, 'Can view Reporte', 15, 'view_reporte');

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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$1PVXzjNheLASvZgP7Y6R6U$8q96A2yscg+p4SS6Oq0XRXrJmFf0gKwb1A1u212mA+g=', '2024-11-27 00:15:12.657169', 1, 'Admin', '', '', 'admin@admin.cl', 1, 1, '2024-11-27 00:11:52.638683'),
(2, 'pbkdf2_sha256$720000$vupa2Wjo2As7yIzFqubEnN$s+peZiA88n0UhiZkfQE2RuMuQppBlw1xmtR486KUBrM=', NULL, 0, 'Robert', '', '', '', 0, 1, '2024-11-27 00:18:57.000000');

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
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 2, 1);

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
-- Estructura de tabla para la tabla `detalleluminaria`
--

DROP TABLE IF EXISTS `detalleluminaria`;
CREATE TABLE IF NOT EXISTS `detalleluminaria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `tipo_lampara` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `marca` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `modelo` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `potencia` double NOT NULL,
  `fecha_instalacion` date NOT NULL,
  `cod_certificacion` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `fecha_certificacion` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `detalleluminaria`
--

INSERT INTO `detalleluminaria` (`id`, `cantidad`, `tipo_lampara`, `marca`, `modelo`, `potencia`, `fecha_instalacion`, `cod_certificacion`, `fecha_certificacion`) VALUES
(1, 12, 'Incandescente', 'SuperMArca', 'Modelito', 40, '2024-11-26', '123123123', '2024-11-26');

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
(1, '2024-11-27 00:16:44.120606', '1', '123123123', 1, '[{\"added\": {}}]', 9, 1),
(2, '2024-11-27 00:17:32.011761', '1', 'Represetante nom ApeRepre apemarepere', 1, '[{\"added\": {}}]', 11, 1),
(3, '2024-11-27 00:18:07.881843', '2', 'titu tituapepa tituapema', 1, '[{\"added\": {}}]', 12, 1),
(4, '2024-11-27 00:18:13.457565', '1', 'Faro, tipo de alumbrado: Ornamental ', 1, '[{\"added\": {}}]', 13, 1),
(5, '2024-11-27 00:18:57.783783', '2', 'Robert', 1, '[{\"added\": {}}]', 4, 1),
(6, '2024-11-27 00:26:16.128141', '1', 'Luxómetro', 1, '[{\"added\": {}}]', 7, 1),
(7, '2024-11-27 00:46:28.577733', '1', 'Inspectores', 1, '[{\"added\": {}}]', 3, 1),
(8, '2024-11-27 00:46:59.622845', '2', 'Robert', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(9, '2024-11-27 00:47:10.493485', '2', 'Robert', 2, '[]', 4, 1);

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
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

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
(9, 'proyectos', 'detalleluminaria'),
(10, 'proyectos', 'persona'),
(11, 'proyectos', 'representantelegal'),
(12, 'proyectos', 'titular'),
(13, 'proyectos', 'proyecto'),
(14, 'fiscalizacion', 'fiscalizacion'),
(15, 'fiscalizacion', 'reporte');

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
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-27 00:11:23.595021'),
(2, 'auth', '0001_initial', '2024-11-27 00:11:24.378986'),
(3, 'admin', '0001_initial', '2024-11-27 00:11:24.638533'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-27 00:11:24.649422'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-27 00:11:24.662520'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-27 00:11:24.772666'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-27 00:11:24.828651'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-27 00:11:24.903387'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-27 00:11:24.916348'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-27 00:11:24.976838'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-27 00:11:24.978891'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-27 00:11:24.988768'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-27 00:11:25.052404'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-27 00:11:25.117000'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-27 00:11:25.172080'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-27 00:11:25.184630'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-27 00:11:25.240622'),
(18, 'proyectos', '0001_initial', '2024-11-27 00:11:25.634563'),
(19, 'fiscalizacion', '0001_initial', '2024-11-27 00:11:25.894648'),
(20, 'mediciones', '0001_initial', '2024-11-27 00:11:26.127417'),
(21, 'sessions', '0001_initial', '2024-11-27 00:11:26.236692');

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
('m29yidr4t5cuwwo7nwabo0fs70k0g1li', '.eJxVjMEOwiAQRP-FsyFQQMGj934D2WUXqRpISnsy_rtt0oNe5jDvzbxFhHUpce08x4nEVWhx-u0Q0pPrDugB9d5kanWZJ5S7Ig_a5diIX7fD_Tso0Mu2VqjJWqXRI3vnQBsVst2CBr6cA6HVgAb9ENBlDIoSGdKQfHZI7L34fAHbDjhY:1tG5i4:1KaV1mObHg5ZlhdlcKEjuVd0ZLzfQShYT5dV48mWPqI', '2024-12-11 00:15:12.659775');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fiscalizacion`
--

DROP TABLE IF EXISTS `fiscalizacion`;
CREATE TABLE IF NOT EXISTS `fiscalizacion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `creado` datetime(6) NOT NULL,
  `proyecto_id` bigint NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fiscalizacion_proyecto_id_71907d10` (`proyecto_id`),
  KEY `fiscalizacion_usuario_id_4c184ee6` (`usuario_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `fiscalizacion`
--

INSERT INTO `fiscalizacion` (`id`, `creado`, `proyecto_id`, `usuario_id`) VALUES
(1, '2024-11-27 00:19:00.682750', 1, 2),
(2, '2024-11-27 00:20:48.767209', 1, 2),
(4, '2024-11-27 00:29:13.899185', 2, 2),
(6, '2024-11-27 01:00:29.096727', 1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instrumentomedicion`
--

DROP TABLE IF EXISTS `instrumentomedicion`;
CREATE TABLE IF NOT EXISTS `instrumentomedicion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tipo` varchar(1) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `marca` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `modelo` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `num_serie` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `instrumentomedicion`
--

INSERT INTO `instrumentomedicion` (`id`, `tipo`, `marca`, `modelo`, `num_serie`) VALUES
(1, '0', 'Marquita', 'Luxomodelo', '123123');

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
  `foto` varchar(100) COLLATE utf8mb3_spanish2_ci DEFAULT NULL,
  `creado` datetime(6) NOT NULL,
  `fiscalizacion_id` bigint NOT NULL,
  `instrumento_medicion_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `medicion_fiscalizacion_id_fcf6403b` (`fiscalizacion_id`),
  KEY `medicion_instrumento_medicion_id_95125e82` (`instrumento_medicion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `medicion`
--

INSERT INTO `medicion` (`id`, `tipo`, `latitud`, `longitud`, `temperatura`, `humedad`, `valor_medido`, `cumplimiento`, `observacion`, `foto`, `creado`, `fiscalizacion_id`, `instrumento_medicion_id`) VALUES
(1, '0', -29.905656, -71.274206, 44, 12, 3, NULL, 'we', 'medicion/medicion.png', '2024-11-27 00:26:37.786693', 1, 1),
(2, '0', 132, 132, 132, 132, 12, NULL, '123', 'medicion/medicion.png', '2024-11-27 01:01:03.980942', 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

DROP TABLE IF EXISTS `persona`;
CREATE TABLE IF NOT EXISTS `persona` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `run` varchar(15) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `nombre` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `a_paterno` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `a_materno` varchar(50) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `correo` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `direccion` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `creado` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`id`, `run`, `nombre`, `a_paterno`, `a_materno`, `correo`, `direccion`, `creado`) VALUES
(1, '1123123123', 'Represetante nom', 'ApeRepre', 'apemarepere', 'repreQcorreo.cl', 'direccion# 00', '2024-11-27 00:17:32.006682'),
(2, '31231231', 'titu', 'tituapepa', 'tituapema', 'titular@correo.cl', 'calle#titu', '2024-11-27 00:18:07.877217');

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
  `foto` varchar(100) COLLATE utf8mb3_spanish2_ci DEFAULT NULL,
  `creado` datetime(6) NOT NULL,
  `detalle_luminarias_id` bigint NOT NULL,
  `representante_legal_id` bigint NOT NULL,
  `titular_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_detalle_luminarias_id_dedf9604` (`detalle_luminarias_id`),
  KEY `proyecto_representante_legal_id_a960c619` (`representante_legal_id`),
  KEY `proyecto_titular_id_0f63ba6e` (`titular_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`id`, `nombre`, `latitud`, `longitud`, `tipo_alumbrado`, `descripcion`, `foto`, `creado`, `detalle_luminarias_id`, `representante_legal_id`, `titular_id`) VALUES
(1, 'Faro', -29.9055459, -71.2743113, 'o', 'Faro de La Serena', 'proyectos/27112024_003001.png', '2024-11-27 00:18:13.438254', 1, 1, 2),
(2, '123', 123, 123, 'v', '123', 'proyectos/proyecto.png', '2024-11-27 00:28:55.696569', 1, 1, 2);

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
-- Estructura de tabla para la tabla `representantelegal`
--

DROP TABLE IF EXISTS `representantelegal`;
CREATE TABLE IF NOT EXISTS `representantelegal` (
  `persona_ptr_id` bigint NOT NULL,
  PRIMARY KEY (`persona_ptr_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `representantelegal`
--

INSERT INTO `representantelegal` (`persona_ptr_id`) VALUES
(1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `titular`
--

DROP TABLE IF EXISTS `titular`;
CREATE TABLE IF NOT EXISTS `titular` (
  `persona_ptr_id` bigint NOT NULL,
  PRIMARY KEY (`persona_ptr_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `titular`
--

INSERT INTO `titular` (`persona_ptr_id`) VALUES
(2);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
