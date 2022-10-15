-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 13, 2022 at 10:52 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `docterapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `user_information`
--

CREATE TABLE `user_information` (
  `id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `disease` varchar(255) NOT NULL,
  `dob` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `status` varchar(100) NOT NULL,
  `stat` varchar(100) NOT NULL,
  `bp` varchar(100) NOT NULL,
  `he` varchar(100) NOT NULL,
  `we` varchar(100) NOT NULL,
  `med1` varchar(1000) NOT NULL,
  `med2` varchar(1000) NOT NULL,
  `med3` varchar(1000) NOT NULL,
  `medc` varchar(1000) NOT NULL,
  `exec` varchar(1000) NOT NULL,
  `wat` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_information`
--

INSERT INTO `user_information` (`id`, `first_name`, `last_name`, `age`, `gender`, `disease`, `dob`, `username`, `password`, `status`, `stat`, `bp`, `he`, `we`, `med1`, `med2`, `med3`, `medc`, `exec`, `wat`) VALUES
(14, 'Danish', 'Ali', '18', '', 'Delhi', 'Shastri Nagar ', 'masterprograming', 'Welcome@12', '', '', '', '', '', '', '', '', '', '', ''),
(15, 'aaa', 'aa', '213', '', 'trichy', 'trd', 'a', 'a', 'No', '', '', '', '', '', '', '', '', '', ''),
(16, 'ragu', 'ragu', '23', '', 'Trichy', 'Trichy', 'b', 'b', '', '', '', '', '', '', '', '', '', '', ''),
(17, 'Ramya', 'Ramya', '25', '', 'Fever', 'Trichy', 'ramya', '123', 'No', '', '', '', '', '', '', '', '', '', ''),
(18, 'neeraja', 'shanthi', '24', '', 'cancer', 'Trichy', 'neeraja', '123', 'No', '', '', '', '', '', '', '', '', '', ''),
(19, 'rv', 'rv', '45', '', 'fever', 'trichy', 'reva', '123', '', '', '', '', '', '', '', '', '', '', ''),
(20, 'nee', 'neea', '34', '', 'Fever', 'Trichy', 'nee', '123', 'No', 'Veg', 'A+', '5.5', '60', '', '', '', '', '', ''),
(21, 'aaa', 'aa', '12', '', 'asad', 'asdasd', 'asd', 'a', '', 'aa', 'a', 'a', 'a', '', '', '', '', '', ''),
(22, 'asda', 'sdasd', '3', '', 'da', 'sdasd', 'sd', 's', '', 'sdf', 'sdf', '', 'sdfsd', '', '', '', '', '', ''),
(23, 'a', 'a', '2', '', 's', 's', 's', 's', '', 's', 's', 's', 's', '', '', '', '', '', ''),
(24, 's', 's', '3', '', 'sddsf', '333', '33', '12', '', '33', '33', '2', '22', 'sd', 'sf', 'sdf', 'sdfds', 'sdfsdf', 'fdsdf'),
(25, 'ganesh', 'revathy', '25', '', 'Fever', '1-4-1985', 'gb', '123', '', 'Veg', 'B+', '5.5', '52', '8:00AM', '1:00PM', '10:00PM', 'Yoga', 'Exercise demo', '1Hr'),
(26, 'aa', 'aa', '12', '', 'xdc', 'xc', 'xcx', '1', '', 'xcx', 'xcx', 'cx', 'xc', 'xc', 'x', 'xc', 'xc', 'cx', 'xc'),
(27, 'ee', 'ee', '45', '', 'xdfsdf', 'sdfsad', 'fsdfsdf', '1', '', ' Non Veg', 'A-', '3', '3', 'ddd', 'dd', 'ddd', 'yo', 'ddd', 'ere'),
(28, 'rr', 'rrrr', '34', 'Male', 'sdfsdf', '1-4-2019', 'aa', '1', '', ' Non Veg', 'A-', '34', '34', 'cccc', 'ccc', 'ddd', 'sdds', 'sdsd', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `user_information`
--
ALTER TABLE `user_information`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user_information`
--
ALTER TABLE `user_information`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
