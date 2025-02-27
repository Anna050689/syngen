from syngen.security.data_encryptor import DataEncryptor

def test_data_encryptor_encrypt_decrypt():
    key = b"test_key_12345678"  # Example key, must be 16 bytes for AES
    encryptor = DataEncryptor(key)

    plaintext = "This is a test message."
    ciphertext = encryptor.encrypt(plaintext)
    decrypted_text = encryptor.decrypt(ciphertext)

    assert plaintext == decrypted_text

def test_data_encryptor_invalid_key():
    key = b"short_key"  # Invalid key length
    try:
        DataEncryptor(key)
    except ValueError as e:
        assert str(e) == "Key must be 16, 24, or 32 bytes long"

    key = b""  # Empty key
    try:
        DataEncryptor(key)
    except ValueError as e:
        assert str(e) == "Key must be 16, 24, or 32 bytes long"

def test_data_encryptor_invalid_decrypt():
    key = b"test_key_12345678"
    encryptor = DataEncryptor(key)

    invalid_ciphertext = b"invalid_ciphertext"
    try:
        encryptor.decrypt(invalid_ciphertext)
    except ValueError as e:
        assert "Decryption failed" in str(e)