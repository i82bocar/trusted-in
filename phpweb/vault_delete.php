<?php
header("Content-type: application/json;charset=utf-8");
include __DIR__ . '/connector.php';
require_once __DIR__ . '/crypto.php';

$response = [
    'success' => false,
    'message' => 'Invalid request'
];

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['delete_item']) && $_POST['delete_item'] === 'true') {
    $email_plain = $_POST['user_email'] ?? '';
    $item_type_plain = $_POST['item_type'] ?? '';
    $item_name_plain = $_POST['item_name'] ?? '';
    $item_data_plain = $_POST['item_data'] ?? '';

    if (empty($email_plain) || empty($item_type_plain) || empty($item_name_plain) || empty($item_data_plain)) {
        $response['message'] = 'Email, type, name, and data are required.';
        echo json_encode($response);
        exit;
    }

    // Encrypt inputs to match how they're stored
    $user_email = encryptField($email_plain);
    $item_type = encryptField($item_type_plain);
    $item_name = encryptField($item_name_plain);
    $item_data = encryptField($item_data_plain);

    $stmt = mysqli_prepare(
        $con,
        "DELETE FROM vault_items 
         WHERE user_email = ? AND item_type = ? AND item_name = ? AND item_data = ?"
    );

    if (!$stmt) {
        $response['message'] = 'Database error: ' . mysqli_error($con);
        echo json_encode($response);
        exit;
    }

    mysqli_stmt_bind_param($stmt, 'ssss', $user_email, $item_type, $item_name, $item_data);

    if (mysqli_stmt_execute($stmt)) {
        $affected_rows = mysqli_stmt_affected_rows($stmt);
        if ($affected_rows > 0) {
            $response['success'] = true;
            $response['message'] = 'Item deleted successfully.';
        } else {
            $response['message'] = 'No matching item found.';
        }
    } else {
        $response['message'] = 'Delete failed: ' . mysqli_error($con);
    }

    mysqli_stmt_close($stmt);
}

echo json_encode($response);
?>