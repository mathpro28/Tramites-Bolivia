-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 03, 2024 at 05:02 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `organization_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `organizations`
--

CREATE TABLE `organizations` (
  `organization_id` int(11) NOT NULL,
  `denominacion` varchar(255) DEFAULT NULL,
  `sigla` varchar(50) DEFAULT NULL,
  `objetivo_entidad` varchar(500) DEFAULT NULL,
  `url_sitio_web` varchar(255) DEFAULT NULL,
  `organization_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `organizations`
--

INSERT INTO `organizations` (`organization_id`, `denominacion`, `sigla`, `objetivo_entidad`, `url_sitio_web`, `organization_name`) VALUES
(1, NULL, NULL, NULL, NULL, 'Organization 1'),
(2, NULL, NULL, NULL, NULL, 'Organization 2'),
(3, NULL, NULL, NULL, NULL, 'Organization 3'),
(4, NULL, NULL, NULL, NULL, 'Organization 4'),
(5, NULL, NULL, NULL, NULL, 'Organization 5'),
(6, NULL, NULL, NULL, NULL, 'Organization 6'),
(7, NULL, NULL, NULL, NULL, 'Organization 7'),
(8, NULL, NULL, NULL, NULL, 'Organization 8'),
(9, NULL, NULL, NULL, NULL, 'Organization 9'),
(10, NULL, NULL, NULL, NULL, 'Organization 10'),
(11, NULL, NULL, NULL, NULL, 'Organization 11'),
(12, NULL, NULL, NULL, NULL, 'Organization 12'),
(13, NULL, NULL, NULL, NULL, 'Organization 13'),
(14, NULL, NULL, NULL, NULL, 'Organization 14'),
(15, NULL, NULL, NULL, NULL, 'Organization 15'),
(16, NULL, NULL, NULL, NULL, 'Organization 16'),
(17, NULL, NULL, NULL, NULL, 'Organization 17'),
(18, NULL, NULL, NULL, NULL, 'Organization 18'),
(19, NULL, NULL, NULL, NULL, 'Organization 19'),
(20, NULL, NULL, NULL, NULL, 'Organization 20'),
(21, NULL, NULL, NULL, NULL, 'Organization 21'),
(22, NULL, NULL, NULL, NULL, 'Organization 22'),
(23, NULL, NULL, NULL, NULL, 'Organization 23'),
(24, NULL, NULL, NULL, NULL, 'Organization 24'),
(25, NULL, NULL, NULL, NULL, 'Organization 25'),
(26, NULL, NULL, NULL, NULL, 'Organization 26'),
(27, NULL, NULL, NULL, NULL, 'Organization 27'),
(28, NULL, NULL, NULL, NULL, 'Organization 28'),
(29, NULL, NULL, NULL, NULL, 'Organization 29'),
(30, NULL, NULL, NULL, NULL, 'Organization 30'),
(31, NULL, NULL, NULL, NULL, 'Organization 31'),
(32, NULL, NULL, NULL, NULL, 'Organization 32'),
(33, NULL, NULL, NULL, NULL, 'Organization 33'),
(34, NULL, NULL, NULL, NULL, 'Organization 34'),
(35, NULL, NULL, NULL, NULL, 'Organization 35'),
(36, NULL, NULL, NULL, NULL, 'Organization 36'),
(37, NULL, NULL, NULL, NULL, 'Organization 37'),
(38, NULL, NULL, NULL, NULL, 'Organization 38'),
(39, NULL, NULL, NULL, NULL, 'Organization 39'),
(40, NULL, NULL, NULL, NULL, 'Organization 40'),
(41, NULL, NULL, NULL, NULL, 'Organization 41'),
(42, NULL, NULL, NULL, NULL, 'Organization 42'),
(43, NULL, NULL, NULL, NULL, 'Organization 43'),
(44, NULL, NULL, NULL, NULL, 'Organization 44'),
(45, NULL, NULL, NULL, NULL, 'Organization 45'),
(46, NULL, NULL, NULL, NULL, 'Organization 46'),
(47, NULL, NULL, NULL, NULL, 'Organization 47'),
(48, NULL, NULL, NULL, NULL, 'Organization 48'),
(49, NULL, NULL, NULL, NULL, 'Organization 49'),
(50, NULL, NULL, NULL, NULL, 'Organization 50'),
(1927, 'Pro – Bolivia', 'PRO-BOL', 'administrar registrar proteger manera eficaz eficiente transparente regimen propiedad intelectual componentes manera oportuna', 'http://senapi.gob.bo', NULL),
(1928, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1929, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1930, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1931, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1932, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1933, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1934, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1935, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1936, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1937, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1938, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1939, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1940, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1941, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1942, 'Servicio Nacional de Propiedad Intelectual', 'SENAPI', 'administrar registrar proteger manera eficaz eficiente transparente regimen propiedad intelectual componentes manera oportuna', 'http://senapi.gob.bo', NULL),
(1943, 'Ministerio de Educación de Bolivia', 'MINEDU', 'diseñar implementar ejecutar politicas estrategias educativas inclusivas equitativas intraculturales interculturales plurilingües cientificas tecnica tecnologica calidad participacion social ambito territorial comunitario productivo descolonizador trave sistema educativo plurinacional', 'www.minedu.gob.bo', NULL),
(1944, 'Servicio Nacional de Propiedad Intelectual', 'SENAPI', 'administrar registrar proteger manera eficaz eficiente transparente regimen propiedad intelectual componentes manera oportuna', 'http://senapi.gob.bo', NULL),
(1945, 'Servicio Nacional de Propiedad Intelectual', 'SENAPI', 'administrar registrar proteger manera eficaz eficiente transparente regimen propiedad intelectual componentes manera oportuna', 'http://senapi.gob.bo', NULL),
(1946, 'Servicio Nacional de Propiedad Intelectual', 'SENAPI', 'administrar registrar proteger manera eficaz eficiente transparente regimen propiedad intelectual componentes manera oportuna', 'http://senapi.gob.bo', NULL),
(1947, 'Servicio Nacional de Propiedad Intelectual', 'SENAPI', 'administrar registrar proteger manera eficaz eficiente transparente regimen propiedad intelectual componentes manera oportuna', 'http://senapi.gob.bo', NULL),
(1948, 'Consejo Nacional del Cine', 'CONACINE', 'lograr crecimiento cultura audiovisual marco diversidad social boliviana', 'http://www.conacinebolivia.com.bo/', NULL),
(1949, 'Consejo Nacional del Cine', 'CONACINE', 'lograr crecimiento cultura audiovisual marco diversidad social boliviana', 'http://www.conacinebolivia.com.bo/', NULL),
(1950, 'Servicio Nacional de Meteorología e Hidrología', 'SENAMHI', 'entidad rectora actividad meteorologica hidrologica actividades afines institucion tecnico cientifica presta servicios especializados contribuyen desarrollo sostenible plurinacional bolivia proporciona informacion hidrometeorologica usuarios informacion sistemas medioambientales ciudado madre tierra ambito nacional internacional participa vigilancia atmosferica mundial junto entidades afines nivel', 'http://www.senamhi.gob.bo', NULL),
(1951, 'Servicio Nacional de Meteorología e Hidrología', 'SENAMHI', 'entidad rectora actividad meteorologica hidrologica actividades afines institucion tecnico cientifica presta servicios especializados contribuyen desarrollo sostenible plurinacional bolivia proporciona informacion hidrometeorologica usuarios informacion sistemas medioambientales ciudado madre tierra ambito nacional internacional participa vigilancia atmosferica mundial junto entidades afines nivel', 'http://www.senamhi.gob.bo', NULL),
(1952, 'Instituto Boliviano de la Ceguera', 'IBC', 'instituto boliviano ceguera institucion publica personalidad juridica propia autonomia gestion tecnica legal administrativa objetivos ma importantes rehabilitacion habilitacion persona ciegas puedan lograr forma individual vida desarrollar potencialidades lograr objetivos basados igualdad oportunidades equiparacion condiciones inclusion plenum sociedad', 'www.ibc.gob.bo', NULL),
(1953, 'Instituto Boliviano de la Ceguera', 'IBC', 'instituto boliviano ceguera institucion publica personalidad juridica propia autonomia gestion tecnica legal administrativa objetivos ma importantes rehabilitacion habilitacion persona ciegas puedan lograr forma individual vida desarrollar potencialidades lograr objetivos basados igualdad oportunidades equiparacion condiciones inclusion plenum sociedad', 'www.ibc.gob.bo', NULL),
(1954, 'Consejo Nacional del Cine', 'CONACINE', 'lograr crecimiento cultura audiovisual marco diversidad social boliviana', 'http://www.conacinebolivia.com.bo/', NULL),
(1955, 'Consejo Nacional del Cine', 'CONACINE', 'lograr crecimiento cultura audiovisual marco diversidad social boliviana', 'http://www.conacinebolivia.com.bo/', NULL),
(1956, 'Ministerio de Obras Públicas Servicios y Vivienda', 'MINOPSV', 'promover gestionar acceso universal equitativo poblacion boliviana obras servicios calidad telecomunicaciones transportes vivienda armonia naturaleza', 'https://www.oopp.gob.bo/', NULL),
(1957, 'Ministerio de Obras Públicas Servicios y Vivienda', 'MINOPSV', 'promover gestionar acceso universal equitativo poblacion boliviana obras servicios calidad telecomunicaciones transportes vivienda armonia naturaleza', 'https://www.oopp.gob.bo/', NULL),
(1958, 'Ministerio de Obras Públicas Servicios y Vivienda', 'MINOPSV', 'promover gestionar acceso universal equitativo poblacion boliviana obras servicios calidad telecomunicaciones transportes vivienda armonia naturaleza', 'https://www.oopp.gob.bo/', NULL),
(1959, 'Ministerio de Obras Públicas Servicios y Vivienda', 'MINOPSV', 'promover gestionar acceso universal equitativo poblacion boliviana obras servicios calidad telecomunicaciones transportes vivienda armonia naturaleza', 'https://www.oopp.gob.bo/', NULL),
(1960, 'Ministerio de Medio Ambiente y Agua', 'MINMAA', 'ministerio medio ambiente agua promueve desarrollo equilibrio armonia madre tierra mediante gestion integral recursos hidricos acceso agua potable saneamiento riego seguridad alimentaria asi manejo integral medio ambiente ecosistemas enfoque cuencas generando condiciones equidad transparencia reciprocidad participacion actores vivir bien', 'www.mmaya.gob.bo', NULL),
(1961, 'Ministerio de Medio Ambiente y Agua', 'MINMAA', 'ministerio medio ambiente agua promueve desarrollo equilibrio armonia madre tierra mediante gestion integral recursos hidricos acceso agua potable saneamiento riego seguridad alimentaria asi manejo integral medio ambiente ecosistemas enfoque cuencas generando condiciones equidad transparencia reciprocidad participacion actores vivir bien', 'www.mmaya.gob.bo', NULL),
(1962, 'Ministerio de Medio Ambiente y Agua', 'MINMAA', 'ministerio medio ambiente agua promueve desarrollo equilibrio armonia madre tierra mediante gestion integral recursos hidricos acceso agua potable saneamiento riego seguridad alimentaria asi manejo integral medio ambiente ecosistemas enfoque cuencas generando condiciones equidad transparencia reciprocidad participacion actores vivir bien', 'www.mmaya.gob.bo', NULL),
(1963, 'Ministerio de Medio Ambiente y Agua', 'MINMAA', 'ministerio medio ambiente agua promueve desarrollo equilibrio armonia madre tierra mediante gestion integral recursos hidricos acceso agua potable saneamiento riego seguridad alimentaria asi manejo integral medio ambiente ecosistemas enfoque cuencas generando condiciones equidad transparencia reciprocidad participacion actores vivir bien', 'www.mmaya.gob.bo', NULL),
(1964, 'Instituto Boliviano de Metrología', 'IBMETRO', 'instituto boliviano metrologia ibmetro custodia patrones nacionales medicion referencia mediciones presta servicios promueven calidad sectores productivos apoyan defensa consumidores aportando vivir bien armonia madre tierra asi mismo reconoce competencia tecnica organismos evaluacion conformidad trave acreditacion', 'http://www.ibmetro.gob.bo', NULL),
(1965, 'Instituto Boliviano de Metrología', 'IBMETRO', 'instituto boliviano metrologia ibmetro custodia patrones nacionales medicion referencia mediciones presta servicios promueven calidad sectores productivos apoyan defensa consumidores aportando vivir bien armonia madre tierra asi mismo reconoce competencia tecnica organismos evaluacion conformidad trave acreditacion', 'http://www.ibmetro.gob.bo', NULL),
(1966, 'Instituto Boliviano de Metrología', 'IBMETRO', 'instituto boliviano metrologia ibmetro custodia patrones nacionales medicion referencia mediciones presta servicios promueven calidad sectores productivos apoyan defensa consumidores aportando vivir bien armonia madre tierra asi mismo reconoce competencia tecnica organismos evaluacion conformidad trave acreditacion', 'http://www.ibmetro.gob.bo', NULL),
(1967, 'Instituto Boliviano de Metrología', 'IBMETRO', 'instituto boliviano metrologia ibmetro custodia patrones nacionales medicion referencia mediciones presta servicios promueven calidad sectores productivos apoyan defensa consumidores aportando vivir bien armonia madre tierra asi mismo reconoce competencia tecnica organismos evaluacion conformidad trave acreditacion', 'http://www.ibmetro.gob.bo', NULL),
(1968, 'Instituto Boliviano de Metrología', 'IBMETRO', 'instituto boliviano metrologia ibmetro custodia patrones nacionales medicion referencia mediciones presta servicios promueven calidad sectores productivos apoyan defensa consumidores aportando vivir bien armonia madre tierra asi mismo reconoce competencia tecnica organismos evaluacion conformidad trave acreditacion', 'http://www.ibmetro.gob.bo', NULL),
(1969, 'Instituto Boliviano de Metrología', 'IBMETRO', 'instituto boliviano metrologia ibmetro custodia patrones nacionales medicion referencia mediciones presta servicios promueven calidad sectores productivos apoyan defensa consumidores aportando vivir bien armonia madre tierra asi mismo reconoce competencia tecnica organismos evaluacion conformidad trave acreditacion', 'http://www.ibmetro.gob.bo', NULL),
(1970, 'Agencia para el Desarrollo de la Sociedad de la Información en Bolivia', 'ADSIB', 'desarrollar politicas estrategias acciones brindar servicios fiables innovadores calidad ambito tecnologias informacion comunicacion avanzando soberania tecnologica inclusion poblacion uso informacion tecnologia', 'https://adsib.gob.bo/', NULL),
(1971, 'Agencia para el Desarrollo de la Sociedad de la Información en Bolivia', 'ADSIB', 'desarrollar politicas estrategias acciones brindar servicios fiables innovadores calidad ambito tecnologias informacion comunicacion avanzando soberania tecnologica inclusion poblacion uso informacion tecnologia', 'https://adsib.gob.bo/', NULL),
(1972, 'Ministerio de Trabajo Empleo y Previsión Social', 'MTEPS', 'garantizamos cumplimiento derechos obligaciones sociolaborales trabajadoras trabajadores servidoras servidores publicos promovemos defendemos trabajo empleo digno erradicando progresivamente toda forma explotacion exclusion discriminacion laboral marco construccion economia plural', 'http://www.mintrabajo.gob.bo', NULL),
(1973, 'Ministerio de Trabajo Empleo y Previsión Social', 'MTEPS', 'garantizamos cumplimiento derechos obligaciones sociolaborales trabajadoras trabajadores servidoras servidores publicos promovemos defendemos trabajo empleo digno erradicando progresivamente toda forma explotacion exclusion discriminacion laboral marco construccion economia plural', 'http://www.mintrabajo.gob.bo', NULL),
(1974, 'Ministerio de Trabajo Empleo y Previsión Social', 'MTEPS', 'garantizamos cumplimiento derechos obligaciones sociolaborales trabajadoras trabajadores servidoras servidores publicos promovemos defendemos trabajo empleo digno erradicando progresivamente toda forma explotacion exclusion discriminacion laboral marco construccion economia plural', 'http://www.mintrabajo.gob.bo', NULL),
(1975, 'Ministerio de Trabajo Empleo y Previsión Social', 'MTEPS', 'garantizamos cumplimiento derechos obligaciones sociolaborales trabajadoras trabajadores servidoras servidores publicos promovemos defendemos trabajo empleo digno erradicando progresivamente toda forma explotacion exclusion discriminacion laboral marco construccion economia plural', 'http://www.mintrabajo.gob.bo', NULL),
(1976, 'Autoridad de Fiscalización y Control Social de Bosques y Tierras', 'ABT', 'ejercer gobierno promoviendo sistemas desarrollo integral sustentables bosques tierras respetando derechos identidades culturales pueblo naciones viven trabajan bosques area rural bolivia concordancia objetivos plan nacional desarrollo preceptos constitucion politica', 'abt.gob.bo', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `procedures`
--

CREATE TABLE `procedures` (
  `procedure_id` int(11) NOT NULL,
  `organization_id` int(11) DEFAULT NULL,
  `descripcion_categoria` varchar(255) DEFAULT NULL,
  `continuo` tinyint(1) DEFAULT NULL,
  `primero_hora_ini` datetime DEFAULT NULL,
  `primero_hora_fin` datetime DEFAULT NULL,
  `segundo_hora_ini` datetime DEFAULT NULL,
  `segundo_hora_fin` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `procedures`
--

INSERT INTO `procedures` (`procedure_id`, `organization_id`, `descripcion_categoria`, `continuo`, `primero_hora_ini`, `primero_hora_fin`, `segundo_hora_ini`, `segundo_hora_fin`) VALUES
(256, 1, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '2012-10-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(257, 2, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(258, 3, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(259, 4, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(260, 5, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(261, 6, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(262, 7, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(263, 8, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(264, 9, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(265, 10, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(266, 11, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(267, 12, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(268, 13, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(269, 14, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(270, 15, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(271, 16, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(272, 17, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(273, 18, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(274, 19, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(275, 20, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(276, 21, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(277, 22, 'Cultura y Turismo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(278, 23, 'Cultura y Turismo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(279, 24, 'Identificación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(280, 25, 'Educación', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(281, 26, 'Gobierno', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(282, 27, 'Salud', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(283, 28, 'Cultura y Turismo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(284, 29, 'Cultura y Turismo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(285, 30, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(286, 31, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(287, 32, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(288, 33, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(289, 34, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(290, 35, 'Medio Ambiente', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(291, 36, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(292, 37, 'Medio Ambiente', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(293, 38, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(294, 39, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(295, 40, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(296, 41, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(297, 42, 'Transporte', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(298, 43, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(299, 44, 'Gobierno', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(300, 45, 'Gobierno', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(301, 46, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(302, 47, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(303, 48, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(304, 49, 'Económico-Productivo', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(305, 50, 'Gobierno', 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `organizations`
--
ALTER TABLE `organizations`
  ADD PRIMARY KEY (`organization_id`);

--
-- Indexes for table `procedures`
--
ALTER TABLE `procedures`
  ADD PRIMARY KEY (`procedure_id`),
  ADD KEY `organization_id` (`organization_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `organizations`
--
ALTER TABLE `organizations`
  MODIFY `organization_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1977;

--
-- AUTO_INCREMENT for table `procedures`
--
ALTER TABLE `procedures`
  MODIFY `procedure_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=306;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `procedures`
--
ALTER TABLE `procedures`
  ADD CONSTRAINT `procedures_ibfk_1` FOREIGN KEY (`organization_id`) REFERENCES `organizations` (`organization_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
