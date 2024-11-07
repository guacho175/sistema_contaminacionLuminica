-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 04-11-2024 a las 15:56:15
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
) ENGINE=MyISAM AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

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
(25, 'Can add Sensor', 7, 'add_location'),
(26, 'Can change Sensor', 7, 'change_location'),
(27, 'Can delete Sensor', 7, 'delete_location'),
(28, 'Can view Sensor', 7, 'view_location'),
(29, 'Can add Instrumento de medición', 8, 'add_instrumentomedicion'),
(30, 'Can change Instrumento de medición', 8, 'change_instrumentomedicion'),
(31, 'Can delete Instrumento de medición', 8, 'delete_instrumentomedicion'),
(32, 'Can view Instrumento de medición', 8, 'view_instrumentomedicion'),
(33, 'Can add Medición', 9, 'add_medicion'),
(34, 'Can change Medición', 9, 'change_medicion'),
(35, 'Can delete Medición', 9, 'delete_medicion'),
(36, 'Can view Medición', 9, 'view_medicion'),
(37, 'Can add Detalle luminaria', 10, 'add_detalleluminarias'),
(38, 'Can change Detalle luminaria', 10, 'change_detalleluminarias'),
(39, 'Can delete Detalle luminaria', 10, 'delete_detalleluminarias'),
(40, 'Can view Detalle luminaria', 10, 'view_detalleluminarias'),
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
(53, 'Can add Cargo', 14, 'add_cargo'),
(54, 'Can change Cargo', 14, 'change_cargo'),
(55, 'Can delete Cargo', 14, 'delete_cargo'),
(56, 'Can view Cargo', 14, 'view_cargo'),
(57, 'Can add Institucion', 15, 'add_institucion'),
(58, 'Can change Institucion', 15, 'change_institucion'),
(59, 'Can delete Institucion', 15, 'delete_institucion'),
(60, 'Can view Institucion', 15, 'view_institucion'),
(61, 'Can add Inspector', 16, 'add_inspector'),
(62, 'Can change Inspector', 16, 'change_inspector'),
(63, 'Can delete Inspector', 16, 'delete_inspector'),
(64, 'Can view Inspector', 16, 'view_inspector');

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
(1, 'pbkdf2_sha256$720000$WFvdaZuGd0f6nmum3JWWTF$dCTEv+sCGPkfvOaHv/9PkyUbpweCwqYifHivJ/Vqxro=', '2024-11-04 14:10:15.287903', 1, 'Admin', '', '', 'Admin@asd.cl', 1, 1, '2024-11-04 14:09:49.277819');

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
(1, 'asd', 'dasdasd');

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
(1, 5, 'Poste', 'marquita', 'modelito', 78, '2024-11-04', 'asdasdq13', '2024-11-04', '2024-11-04 14:21:34.424386');

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
(1, '2024-11-04 14:16:54.652850', '1', 'asd dasdasd', 1, '[{\"added\": {}}]', 14, 1),
(2, '2024-11-04 14:17:06.536499', '1', 'Gabriela qwe', 1, '[{\"added\": {}}]', 15, 1),
(3, '2024-11-04 14:17:09.185370', '1', '5918345-4 Pedro Weird asdas', 1, '[{\"added\": {}}]', 16, 1),
(4, '2024-11-04 14:17:41.878027', '1', '0 12312312', 1, '[{\"added\": {}}]', 8, 1),
(5, '2024-11-04 14:20:26.670504', '1', 'Carla Weird Martin', 1, '[{\"added\": {}}]', 12, 1),
(6, '2024-11-04 14:20:55.977460', '1', 'Mara 132 qew', 1, '[{\"added\": {}}]', 11, 1),
(7, '2024-11-04 14:21:34.432386', '1', 'asdasdq13', 1, '[{\"added\": {}}]', 10, 1),
(8, '2024-11-04 14:21:37.294942', '1', 'El faro p Carla Mara', 1, '[{\"added\": {}}]', 13, 1),
(9, '2024-11-04 14:21:41.684734', '1', '-29.9055459 -71.2743113', 1, '[{\"added\": {}}]', 9, 1),
(10, '2024-11-04 14:44:16.673245', '2', '123.0 123.0', 1, '[{\"added\": {}}]', 9, 1);

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
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

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
(7, 'mapa', 'location'),
(8, 'catalogo_mediciones', 'instrumentomedicion'),
(9, 'catalogo_mediciones', 'medicion'),
(10, 'proyectos', 'detalleluminarias'),
(11, 'proyectos', 'representantelegal'),
(12, 'proyectos', 'titular'),
(13, 'proyectos', 'proyecto'),
(14, 'inspectores', 'cargo'),
(15, 'inspectores', 'institucion'),
(16, 'inspectores', 'inspector');

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
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-04 14:07:27.209804'),
(2, 'auth', '0001_initial', '2024-11-04 14:07:27.809972'),
(3, 'admin', '0001_initial', '2024-11-04 14:07:28.017799'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-04 14:07:28.017799'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-04 14:07:28.039771'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-04 14:07:28.132619'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-04 14:07:28.177200'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-04 14:07:28.227264'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-04 14:07:28.227557'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-04 14:07:28.277225'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-04 14:07:28.277225'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-04 14:07:28.293729'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-04 14:07:28.335556'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-04 14:07:28.384625'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-04 14:07:28.432860'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-04 14:07:28.447548'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-04 14:07:28.492646'),
(18, 'proyectos', '0001_initial', '2024-11-04 14:07:28.748449'),
(19, 'inspectores', '0001_initial', '2024-11-04 14:07:28.927114'),
(20, 'catalogo_mediciones', '0001_initial', '2024-11-04 14:07:29.150944'),
(21, 'mapa', '0001_initial', '2024-11-04 14:07:29.166566'),
(22, 'mapa', '0002_location_cumpl', '2024-11-04 14:07:29.228925'),
(23, 'sessions', '0001_initial', '2024-11-04 14:07:29.272170');

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
('ejwyspql78ntevjlyha1ekhh3mcgsxn9', '.eJxVjDsOwjAQBe_iGln-O6ak5wzWrnfBAeRIcVIh7k4ipYD2zcx7iwzrUvPaec4jibPQ4vS7IZQntx3QA9p9kmVqyzyi3BV50C6vE_Hrcrh_BxV63eqCkbz2CSwBmcja8w2DApdKxFhQ2SGaAa1KwW6OZyB23hcIzqikgvh8Afh6N_c:1t7xmZ:3c6YX2zxje5j-U-edR4UohMY-5viflwnMRBftQUQQsc', '2024-11-18 14:10:15.292274');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inspector`
--

DROP TABLE IF EXISTS `inspector`;
CREATE TABLE IF NOT EXISTS `inspector` (
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
  KEY `inspector_cargo_id_89fa0a6a` (`cargo_id`),
  KEY `inspector_institucion_id_9dad80e4` (`institucion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `inspector`
--

INSERT INTO `inspector` (`id`, `run`, `nombre`, `a_paterno`, `a_materno`, `correo`, `creado`, `cargo_id`, `institucion_id`) VALUES
(1, '5918345-4', 'Pedro', 'Weird', 'asdas', 'usuario@acme.cl', '2024-11-04 14:17:09.175428', 1, 1);

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
(1, 'Gabriela', 'qwe');

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
(1, '0', 'marquita', 'modelito', '12312312');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mapa_location`
--

DROP TABLE IF EXISTS `mapa_location`;
CREATE TABLE IF NOT EXISTS `mapa_location` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(250) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `address` varchar(250) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `lat` double NOT NULL,
  `lng` double NOT NULL,
  `cumpl` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicion`
--

DROP TABLE IF EXISTS `medicion`;
CREATE TABLE IF NOT EXISTS `medicion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cumplimiento` varchar(1) COLLATE utf8mb3_spanish2_ci DEFAULT NULL,
  `latitud` double NOT NULL,
  `longitud` double NOT NULL,
  `temperatura` double NOT NULL,
  `humedad` double NOT NULL,
  `valor_medido` double NOT NULL,
  `observacion` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `creado` datetime(6) NOT NULL,
  `inspector_id` bigint NOT NULL,
  `instrumento_medicion_id` bigint NOT NULL,
  `proyecto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `medicion_inspector_id_c61d9586` (`inspector_id`),
  KEY `medicion_instrumento_medicion_id_95125e82` (`instrumento_medicion_id`),
  KEY `medicion_proyecto_id_22862c37` (`proyecto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `medicion`
--

INSERT INTO `medicion` (`id`, `cumplimiento`, `latitud`, `longitud`, `temperatura`, `humedad`, `valor_medido`, `observacion`, `creado`, `inspector_id`, `instrumento_medicion_id`, `proyecto_id`) VALUES
(2, NULL, 123, 123, 1, 1, 12, 'as', '2024-11-04 14:44:16.654048', 1, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

DROP TABLE IF EXISTS `proyecto`;
CREATE TABLE IF NOT EXISTS `proyecto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `longitud` double NOT NULL,
  `latitud` double NOT NULL,
  `tipo_alumbrado` varchar(1) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `descripcion` varchar(500) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `nv_cumplimiento` varchar(1) COLLATE utf8mb3_spanish2_ci NOT NULL,
  `estado` int NOT NULL,
  `creado` datetime(6) NOT NULL,
  `detalle_luminarias_id` bigint NOT NULL,
  `representante_legal_id` bigint NOT NULL,
  `titular_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `proyecto_detalle_luminarias_id_dedf9604` (`detalle_luminarias_id`),
  KEY `proyecto_representante_legal_id_a960c619` (`representante_legal_id`),
  KEY `proyecto_titular_id_0f63ba6e` (`titular_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_spanish2_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`id`, `nombre`, `longitud`, `latitud`, `tipo_alumbrado`, `descripcion`, `nv_cumplimiento`, `estado`, `creado`, `detalle_luminarias_id`, `representante_legal_id`, `titular_id`) VALUES
(1, 'El faro', -71.2743113, -29.9055459, 'p', 'Faro cuadrado de concreto y punto de referencia de la ciudad terminado en 1951 ubicado en una playa popular.', '0', 0, '2024-11-04 14:21:37.283883', 1, 1, 1);

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
(1, '131231-1', 'Mara', '132', 'qew', 'calle Robert', 'galindez@gmail.com', '2024-11-04 14:20:55.974469');

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
(1, '1112.3-4', 'Carla', 'Weird', 'Martin', 'calle andy', 'a.aguirre@acme.cl', '2024-11-04 14:20:26.670504');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
