<?php
header("Content-type: application/json;charset=utf-8");
include __DIR__ . '/connector.php';
require_once __DIR__ . '/crypto.php';

$response = [
    'success' => false,
    'message' => 'Invalid request',
    'uploaded' => 0
];

if (isset($_POST['upload_item']) || isset($_POST['upload_items'])) {
    $user_email = encryptField($_POST['user_email']);
    
    if (isset($_POST['upload_item'])) {
        // Single item upload
        $item_data = json_decode($_POST['item_data'], true);
        
        $encrypted_data = encryptField(json_encode($item_data));
        $item_type = encryptField($item_data['type'] ?? 'unknown');
        $item_name = encryptField($item_data['name'] ?? '');
        
        $stmt = mysqli_prepare(
            $con,
            "INSERT INTO vault_items 
            (user_email, item_type, item_name, item_data, created_at, updated_at)
            VALUES (?, ?, ?, ?, NOW(), NOW())
            ON DUPLICATE KEY UPDATE
            item_data = VALUES(item_data),
            updated_at = NOW()"
        );
        
        mysqli_stmt_bind_param($stmt, 'ssss', 
            $user_email,
            $item_type,
            $item_name,
            $encrypted_data
        );
        
        if (mysqli_stmt_execute($stmt)) {
            $response['success'] = true;
            $response['message'] = 'Item uploaded successfully';
            $response['uploaded'] = 1;
        } else {
            $response['message'] = 'Database error: ' . mysqli_error($con);
        }
        
        mysqli_stmt_close($stmt);
    } 
    elseif (isset($_POST['upload_items'])) {
        // Batch upload (for sync)
        $items = json_decode($_POST['items'], true);
        $uploaded = 0;
        
        mysqli_begin_transaction($con);
        
        try {
            $stmt = mysqli_prepare(
                $con,
                "INSERT INTO vault_items 
                (user_email, item_type, item_name, item_data, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON DUPLICATE KEY UPDATE
                item_data = VALUES(item_data),
                updated_at = VALUES(updated_at)"
            );
            
            foreach ($items as $item) {
                $encrypted_data = encryptField(json_encode($item));
                $item_type = encryptField($item['type'] ?? 'unknown');
                $item_name = encryptField($item['name'] ?? '');
                $created_at = $item['created_at'] ?? date('Y-m-d H:i:s');
                
                mysqli_stmt_bind_param($stmt, 'ssssss', 
                    $user_email,
                    $item_type,
                    $item_name,
                    $encrypted_data,
                    $created_at,
                    $created_at
                );
                
                if (mysqli_stmt_execute($stmt)) {
                    $uploaded++;
                }
            }
            
            mysqli_commit($con);
            $response['success'] = true;
            $response['message'] = "Uploaded $uploaded items";
            $response['uploaded'] = $uploaded;
        } catch (Exception $e) {
            mysqli_rollback($con);
            $response['message'] = 'Batch upload failed: ' . $e->getMessage();
        }
        
        mysqli_stmt_close($stmt);
    }
}

echo json_encode($response);
?>