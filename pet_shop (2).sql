-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2022 at 10:46 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pet_shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL,
  `feedback` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `rating` varchar(10) NOT NULL,
  `reg_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`feedback_id`, `feedback`, `date`, `rating`, `reg_id`) VALUES
(1, 'vokey', '2022-10-02', '5', 1),
(2, 'vokey', '2022-10-02', '5', 1),
(3, 'ytyytf', '2022-10-02', '3', 1);

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL,
  `user_name` varchar(10) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `price` int(11) NOT NULL,
  `card_number` int(11) NOT NULL,
  `cardholder_name` varchar(25) NOT NULL,
  `cvv` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`payment_id`, `date`, `price`, `card_number`, `cardholder_name`, `cvv`) VALUES
(1, '2022-10-02', 50, 0, '', 0),
(2, '2022-10-02', 50, 12345, 'sga', 72);

-- --------------------------------------------------------

--
-- Table structure for table `pet`
--

CREATE TABLE `pet` (
  `pet_id` int(11) NOT NULL,
  `pet_name` varchar(25) NOT NULL,
  `pet_type` varchar(25) NOT NULL,
  `description` varchar(100) NOT NULL,
  `price` int(11) NOT NULL,
  `image` varchar(100) NOT NULL,
  `age` int(11) NOT NULL,
  `quantity` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pet`
--

INSERT INTO `pet` (`pet_id`, `pet_name`, `pet_type`, `description`, `price`, `image`, `age`, `quantity`) VALUES
(1, 'sura', 'dog', 'tddyg', 10, 'WIN_20220821_17_05_46_Pro.mp4', 5, 0),
(2, 'sura', 'dog', 'healthy', 400000, '322868_1100-800x825.jpg', 5, 0),
(3, 'dog', 'dog', 'good', 150, '322868_1100-800x825.jpg', 6, 0),
(4, 'helo', 'cat', 'gkgiou', 10, '322868_1100-800x825.jpg', 10, 0),
(5, 'uuh', 'dog', 'u7u', 2147483647, '322868_1100-800x825.jpg', 5, 0),
(6, 'patti', 'dog', 'patti', 125, '322868_1100-800x825.jpg', 10, 0),
(7, 'pepatti', 'dog', 'fjhk', 175, '322868_1100-800x825.jpg', 25, 0),
(8, 'jjjjjjjjj', 'cat', 'vvvvvvvvv', 200, '322868_1100-800x825.jpg', 25, 0),
(9, 'bombey', 'dog', 'bombey waala', 5, '322868_1100-800x825.jpg', 10, 2),
(10, 'cat', 'cat', 'gggg', 25, '322868_1100-800x825.jpg', 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `pet_order`
--

CREATE TABLE `pet_order` (
  `petorder_id` int(11) NOT NULL,
  `pet_id` int(11) NOT NULL,
  `image` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `reg_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pet_order`
--

INSERT INTO `pet_order` (`petorder_id`, `pet_id`, `image`, `price`, `quantity`, `reg_id`) VALUES
(16, 1, '', 10, 1, 0),
(19, 10, '', 25, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL,
  `product_name` varchar(25) NOT NULL,
  `price` int(11) NOT NULL,
  `description` varchar(100) NOT NULL,
  `quantity` int(11) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `price`, `description`, `quantity`, `image`) VALUES
(1, 'water', 50, 'healthy', 5, 'WIN_20220821_17_05_46_Pro.mp4'),
(2, 'who', 100, 'good product', 1, 'WIN_20221008_16_11_47_Pro.jpg'),
(3, 'water', 12, 'aca', 2, 'WIN_20221008_16_11_47_Pro.jpg'),
(4, 'ugg', 12, 'ads', 1, 'WIN_20221008_16_11_47_Pro.jpg'),
(5, 'hh', 22, 'yfy', 48, '322868_1100-800x825.jpg'),
(6, 'zzzz', 25, 'zzzz', 2, '322868_1100-800x825.jpg'),
(7, 'pepsi', 100, 'pepsi', 10, '322868_1100-800x825.jpg'),
(8, 'glucose', 50, 'glucose', 22, '322868_1100-800x825.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `product_order`
--

CREATE TABLE `product_order` (
  `productorder_id` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `reg_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_order`
--

INSERT INTO `product_order` (`productorder_id`, `price`, `quantity`, `product_id`, `reg_id`) VALUES
(8, 12, 1, 4, 0),
(9, 12, 1, 3, 0),
(10, 25, 2, 6, 0);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `reg_id` int(11) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `user_name` varchar(10) NOT NULL,
  `password` varchar(8) NOT NULL,
  `conform_password` varchar(8) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `email` varchar(25) NOT NULL,
  `place` varchar(25) NOT NULL,
  `post` varchar(25) NOT NULL,
  `pin` int(11) NOT NULL,
  `phone` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`reg_id`, `first_name`, `last_name`, `user_name`, `password`, `conform_password`, `gender`, `email`, `place`, `post`, `pin`, `phone`) VALUES
(1, 'jhon', 'bosco', 'jhon', '1234', '1234', 'male', 'mshakir', 'patt', '6535', 46, 12349);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`feedback_id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`payment_id`);

--
-- Indexes for table `pet`
--
ALTER TABLE `pet`
  ADD PRIMARY KEY (`pet_id`);

--
-- Indexes for table `pet_order`
--
ALTER TABLE `pet_order`
  ADD PRIMARY KEY (`petorder_id`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `product_order`
--
ALTER TABLE `product_order`
  ADD PRIMARY KEY (`productorder_id`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`reg_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `feedback_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `login_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `payment_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `pet`
--
ALTER TABLE `pet`
  MODIFY `pet_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `pet_order`
--
ALTER TABLE `pet_order`
  MODIFY `petorder_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `product_order`
--
ALTER TABLE `product_order`
  MODIFY `productorder_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `reg_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
