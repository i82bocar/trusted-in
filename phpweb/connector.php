<?php

	// Database credentials
	$DB_HOST = "localhost:3306";      
	$DB_USER = "spinnco1_altern";   
	$DB_PASS = '.fYHXwgKT-$S';   
	$DB_NAME = "spinnco1_alternox";   

	// Create connection
	$con = mysqli_connect($DB_HOST, $DB_USER, $DB_PASS, $DB_NAME);

	// Check connection
	if (!$con) {
		http_response_code(500);
		echo json_encode([
			"success" => false,
			"error" => "Failed to connect to database: " . mysqli_connect_error()
		]);
		exit;
	}

	// Set charset to utf8mb4 for proper Unicode support
	mysqli_set_charset($con, "utf8mb4");
?>