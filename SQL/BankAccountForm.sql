CREATE TABLE `bank_account_form` (
  `form_type` varchar(50) DEFAULT NULL,
  `owner_first_name` varchar(50) NOT NULL,
  `owner_middle_initial` varchar(2) DEFAULT NULL,
  `owner_last_name` varchar(50) NOT NULL,
  `account_number` int NOT NULL AUTO_INCREMENT,
  `joint_owner_first_name` varchar(50) DEFAULT NULL,
  `joint_owner_middle_initial` varchar(2) DEFAULT NULL,
  `joint_owner_last_name` varchar(50) DEFAULT NULL,
  `party_name` varchar(100) DEFAULT NULL,
  `auth_person` varchar(100) DEFAULT NULL,
  `other_auth_person` varchar(100) DEFAULT NULL,
  `annual_income` varchar(50) DEFAULT NULL,
  `liquid_net_worth` varchar(50) DEFAULT NULL,
  `total_net_worth` varchar(50) DEFAULT NULL,
  `owner_signature_1` varchar(100) DEFAULT NULL,
  `date_1` varchar(50) DEFAULT NULL,
  `owner_signature_2` varchar(100) DEFAULT NULL,
  `date_2` varchar(50) DEFAULT NULL,
  `last_updated_ts` datetime DEFAULT NULL,
  PRIMARY KEY (`account_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;