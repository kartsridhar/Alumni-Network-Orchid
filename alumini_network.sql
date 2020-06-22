-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 23, 2020 at 12:05 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alumini_network`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`name`) VALUES
('Country'),
('Subjects'),
('Universities');

-- --------------------------------------------------------

--
-- Table structure for table `subcategories`
--

CREATE TABLE `subcategories` (
  `name` varchar(255) NOT NULL,
  `parentcat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `subcategories`
--

INSERT INTO `subcategories` (`name`, `parentcat`) VALUES
('Australia', 'Country'),
('Busineess', 'Subjects'),
('Commerce', 'Subjects'),
('Computer Science', 'Subjects'),
('Economics', 'Subjects'),
('India', 'Country'),
('Ireland', 'Country'),
('Mathematics', 'Subjects'),
('New Zealand', 'Country'),
('Science', 'Subjects'),
('United Kingdom', 'Country'),
('United States', 'Country');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `email` varchar(255) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `user_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `confirmation_status` tinyint(1) NOT NULL,
  `confirmation_code` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`email`, `full_name`, `user_name`, `password`, `confirmation_status`, `confirmation_code`) VALUES
('alumni.net@yahoo.com', 'Trial', 'trial1', 'xyz123', 1, 'CJ59DcHko3q1yOuV'),
('bumlayirto@enayu.com', 'web1', 'tryw1', '12345', 1, 'MVDga7Q4tFJXXCPg'),
('nibas57206@jupiterm.com', 'NRR', 'web _trial', '12345', 1, 'lyLya5I4VgYRGZrz'),
('nishd268@gmail.com', 'Nishad Raisinghani', 'justnishad', 'yolo123', 1, 'vZYljStkfqz6XWUu'),
('nishd269@gmail.com', 'yolo123s', 'NR', 'jsNR', 1, '5010'),
('solmecutre@enayu.com', 'trya', 'yyyy', 'lmnooo', 1, 'ojOhW724dOsPU96V'),
('vimemod606@jupiterm.com', 'hjshsh', 'lolabcd', '123456', 1, 'kp4c3xv9CBp5UTuv'),
('wihibo7585@mailcupp.com', 'Nishad', 'nray', '12345', 1, '9bIo9NX8hKJO4g78');

-- --------------------------------------------------------

--
-- Table structure for table `user_profiles`
--

CREATE TABLE `user_profiles` (
  `email` varchar(255) NOT NULL,
  `cat1` varchar(255) NOT NULL,
  `cat2` varchar(255) NOT NULL,
  `cat3` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_profiles`
--

INSERT INTO `user_profiles` (`email`, `cat1`, `cat2`, `cat3`) VALUES
('alumni.net@yahoo.com', 'Computer Science', 'JSPM', 'USA'),
('bumlayirto@enayu.com', 'Computer Science', 'UK', 'USA'),
('nibas57206@jupiterm.com', 'UK', 'JSPM', 'USA'),
('nishd268@gmail.com', 'Computer Science', 'JSPM', 'USA'),
('nishd269@gmail.com', 'USA', 'UK', 'Computer Science'),
('solmecutre@enayu.com', 'Computer Science', 'UK', 'USA'),
('vimemod606@jupiterm.com', 'Computer Science', 'JSPM', 'USA'),
('wihibo7585@mailcupp.com', 'USA', 'Computer Science', 'JSPM');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `subcategories`
--
ALTER TABLE `subcategories`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `user_profiles`
--
ALTER TABLE `user_profiles`
  ADD PRIMARY KEY (`email`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
