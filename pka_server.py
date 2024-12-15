import socket

host = "192.168.123.34"  # IP perangkat Anda
port = 6000

def generate_rsa_keys():
    """Fungsi sederhana untuk menghasilkan pasangan kunci RSA."""
    p = 11  # Bilangan prima pertama
    q = 13  # Bilangan prima kedua
    n = p * q
    phi = (p - 1) * (q - 1)

    # Cari e yang relatif prima dengan phi
    e = 7
    d = pow(e, -1, phi)  # Modular inverse
    return (e, n), (d, n)  # Public key, Private key

def pka_server_program():
    # Kunci RSA untuk PKA (n1)
    pka_public_key, pka_private_key = generate_rsa_keys()
    print(f"[PKA] Public Key PKA: {pka_public_key}, Private Key: {pka_private_key} (disimpan)")

    # Kunci RSA untuk client/server (n2)
    user_public_key, user_private_key = generate_rsa_keys()
    print(f"[PKA] Public Key User: {user_public_key}, Private Key: {user_private_key} (disimpan)")

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("[PKA] Menunggu koneksi...")

    while True:
        conn, address = server_socket.accept()
        print(f"[PKA] Koneksi diterima dari {address}")

        # Enkripsi public key user dengan private key PKA
        e, n = user_public_key
        encrypted_public_key = [str(pow(ord(char), pka_private_key[0], pka_private_key[1])) for char in f"{e},{n}"]
        encrypted_public_key = " ".join(encrypted_public_key)

        conn.send(encrypted_public_key.encode())
        print(f"[PKA] Public Key User terenkripsi dikirim ke {address}")
        conn.close()

if __name__ == '__main__':
    pka_server_program()
