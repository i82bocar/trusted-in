<?php
header("Content-type: application/json;charset=utf-8");
include __DIR__ . '/connector.php';
require_once __DIR__ . '/crypto.php';

$response = [
    'success' => false,
    'items' => [],
    'message' => 'Invalid request'
];

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['download_items']) && $_POST['download_items'] === 'true') {
    $email_plain = $_POST['user_email'] ?? '';

    if (empty($email_plain)) {
        $response['message'] = 'User email is required.';
        echo json_encode($response);
        exit;
    }

    $user_email = encryptField($email_plain); // Match encrypted email style

    $stmt = mysqli_prepare(
        $con,
        "SELECT id, item_type, item_name, item_data, created_at, updated_at 
         FROM vault_items 
         WHERE user_email = ?"
    );

    if (!$stmt) {
        $response['message'] = 'Database error: ' . mysqli_error($con);
        echo json_encode($response);
        exit;
    }

    mysqli_stmt_bind_param($stmt, 's', $user_email);

    if (mysqli_stmt_execute($stmt)) {
        $result = mysqli_stmt_get_result($stmt);
        $items = [];

        while ($row = mysqli_fetch_assoc($result)) {
            $decrypted_data = decryptField($row['item_data']);
            $decrypted_name = decryptField($row['item_name']);
            $decrypted_type = decryptField($row['item_type']);

            $items[] = [
                'id' => $row['item_id'],
                'type' => $decrypted_type,
                'name' => $decrypted_name,
                'data' => json_decode($decrypted_data, true), // decode JSON structure
                'created_at' => $row['created_at'],
                'updated_at' => $row['updated_at']
            ];
        }

        $response['success'] = true;
        $response['items'] = $items;
        $response['message'] = 'Vault items downloaded successfully.';
    } else {
        $response['message'] = 'Query failed: ' . mysqli_error($con);
    }

    mysqli_stmt_close($stmt);
}

echo json_encode($response);
?>
