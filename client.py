import socket

host_pka = "192.168.123.34"  # IP PKA server
port_pka = 6000

host_server = "192.168.123.34"  # IP server utama
port_server = 5000

def modular_exponentiation(base, exp, mod):
    """Pemangkatan modular untuk enkripsi/dekripsi."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def decrypt_public_key(encrypted_key, pka_public_key):
    """Dekripsi public key yang diterima dari PKA."""
    decrypted_chars = [chr(modular_exponentiation(int(num), pka_public_key[0], pka_public_key[1])) for num in encrypted_key.split()]
    decrypted_key = "".join(decrypted_chars)
    e, n = map(int, decrypted_key.split(","))
    return e, n

def encrypt_key_des(des_key, private_key, public_key_receiver):
    """Enkripsi DES key dua kali: private sender, public receiver."""
    encrypted_once = modular_exponentiation(des_key, private_key[0], private_key[1])
    encrypted_twice = modular_exponentiation(encrypted_once, public_key_receiver[0], public_key_receiver[1])
    return encrypted_twice

def encrypt_message_des(message, des_key):
    """Enkripsi pesan menggunakan DES (simulasi XOR sederhana)."""
    return "".join([chr(ord(char) ^ des_key) for char in message])

def decrypt_message_des(encrypted_message, des_key):
    """Dekripsi pesan menggunakan DES (simulasi XOR sederhana)."""
    return "".join([chr(ord(char) ^ des_key) for char in encrypted_message])

def client_program():
    # Hubungkan ke PKA server
    pka_socket = socket.socket()
    pka_socket.connect((host_pka, port_pka))
    encrypted_key = pka_socket.recv(1024).decode()
    pka_socket.close()

    # Public key PKA (hardcoded untuk dekripsi)
    pka_public_key = (7, 143)  # Sesuai dengan kunci PKA di server
    user_public_key = decrypt_public_key(encrypted_key, pka_public_key)
    print(f"[CLIENT] Public Key diterima dari PKA: {user_public_key}")

    # DES key (simulasi: angka random kecil)
    des_key = 42
    print(f"[CLIENT] DES Key yang dihasilkan: {des_key}")

    # Hubungkan ke server utama
    client_socket = socket.socket()
    client_socket.connect((host_server, port_server))
    print("[CLIENT] Terhubung ke server utama")

    # Enkripsi DES key dua kali
    private_key_client = (7, 143)  # Contoh private key client
    encrypted_des_key = encrypt_key_des(des_key, private_key_client, user_public_key)
    client_socket.send(str(encrypted_des_key).encode())
    print(f"[CLIENT] DES Key terenkripsi dikirim: {encrypted_des_key}")

    # Komunikasi dua arah menggunakan DES key
    while True:
        message = input("Ketik pesan -> ")
        if message.lower() == 'bye':
            encrypted_message = encrypt_message_des(message, des_key)
            client_socket.send(encrypted_message.encode())
            print("[CLIENT] Mengakhiri koneksi...")
            break

        encrypted_message = encrypt_message_des(message, des_key)
        client_socket.send(encrypted_message.encode())
        print(f"[CLIENT] Pesan terenkripsi dikirim: {encrypted_message}")

        # Terima pesan dari server
        encrypted_response = client_socket.recv(1024).decode()
        response = decrypt_message_des(encrypted_response, des_key)
        print(f"[CLIENT] Balasan dari server: {response}")

    client_socket.close()

if __name__ == '__main__':
    client_program()
