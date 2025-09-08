<?php
header("Content-type: application/json;charset=utf-8");
include __DIR__ . '/connector.php';
require_once __DIR__ . '/crypto.php'; 

$data = [
    'pos_res' => 'none',
    'success' => false,
    'register_response' => ''
];

if (isset($_POST['register_user'])) {
    // Sanitize and encrypt input
    $first_name_raw = trim($_POST['first_name'] ?? '');
    $last_name_raw  = trim($_POST['last_name'] ?? '');
    $email_raw      = trim($_POST['email'] ?? '');
    $password       = trim($_POST['password_hash'] ?? '');

    if (empty($first_name_raw) || empty($last_name_raw) || empty($email_raw) || empty($password)) {
        $data['register_response'] = "Error: All fields are required.";
    } else {
        $first_name = encryptField($first_name_raw);
        $last_name  = encryptField($last_name_raw);
        $email      = encryptField($email_raw);

        // Use prepared statements to prevent SQL injection
        $stmtCheck = mysqli_prepare($con, "SELECT 1 FROM `users` WHERE `user_email` = ?");
        mysqli_stmt_bind_param($stmtCheck, 's', $email);
        mysqli_stmt_execute($stmtCheck);
        mysqli_stmt_store_result($stmtCheck);
        if (mysqli_stmt_num_rows($stmtCheck) > 0) {
            $data['register_response'] = "Error: User already exists.";
            mysqli_stmt_close($stmtCheck);
        } else {
            mysqli_stmt_close($stmtCheck);

            $stmtInsert = mysqli_prepare(
                $con,
                "INSERT INTO `users` (`first_name`, `last_name`, `user_email`, `password_hash`, `created_at`)
                 VALUES (?, ?, ?, ?, NOW())"
            );
            mysqli_stmt_bind_param($stmtInsert, 'ssss', $first_name, $last_name, $email, $password);

            if (mysqli_stmt_execute($stmtInsert)) {
                $data['success'] = true;
                $data['register_response'] = "Registration successful.";
                $data['pos_res'] = "reload";
            } else {
                $data['register_response'] = "Error inserting user: " . mysqli_error($con);
            }
            mysqli_stmt_close($stmtInsert);
        }
    }
}

echo json_encode($data);
?>
