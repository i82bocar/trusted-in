<?php
require_once __DIR__ . '/config.php';

function encryptField($plainText) {
    return openssl_encrypt($plainText, 'AES-256-CBC', ENCRYPTION_KEY, 0, ENCRYPTION_IV);
}

function decryptField($cipherText) {
    return openssl_decrypt($cipherText, 'AES-256-CBC', ENCRYPTION_KEY, 0, ENCRYPTION_IV);
}
