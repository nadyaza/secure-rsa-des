import socket

host = "192.168.0.101"  # IP server utama
port = 5000

def modular_exponentiation(base, exp, mod):
    """Pemangkatan modular untuk enkripsi/dekripsi."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def decrypt_key_des(encrypted_key, private_key_receiver, public_key_sender):
    """Dekripsi DES key dua kali: public sender, private receiver."""
    decrypted_once = modular_exponentiation(encrypted_key, public_key_sender[0], public_key_sender[1])
    decrypted_twice = modular_exponentiation(decrypted_once, private_key_receiver[0], private_key_receiver[1])
    return decrypted_twice

def encrypt_message_des(message, des_key):
    """Enkripsi pesan menggunakan DES (simulasi XOR sederhana)."""
    return "".join([chr(ord(char) ^ des_key) for char in message])

def decrypt_message_des(encrypted_message, des_key):
    """Dekripsi pesan menggunakan DES (simulasi XOR sederhana)."""
    return "".join([chr(ord(char) ^ des_key) for char in encrypted_message])

def server_program():
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    print("[SERVER] Menunggu koneksi client...")

    conn, address = server_socket.accept()
    print(f"[SERVER] Koneksi diterima dari {address}")

    # Terima DES key yang terenkripsi
    encrypted_des_key = int(conn.recv(1024).decode())
    print(f"[SERVER] DES Key terenkripsi diterima: {encrypted_des_key}")

    # Dekripsi DES key dua kali
    private_key_server = (7, 143)  # Contoh private key server
    public_key_client = (7, 143)  # Contoh public key client
    des_key = decrypt_key_des(encrypted_des_key, private_key_server, public_key_client)
    print(f"[SERVER] DES Key setelah dekripsi: {des_key}")

    # Komunikasi dua arah menggunakan DES key
    while True:
        # Terima pesan terenkripsi dari client
        encrypted_message = conn.recv(1024).decode()
        
        # ** Tambahkan log pesan terenkripsi **
        print(f"[SERVER] Pesan terenkripsi diterima: {encrypted_message}")

        # Dekripsi pesan
        message = decrypt_message_des(encrypted_message, des_key)
        print(f"[SERVER] Pesan dari client (setelah dekripsi): {message}")

        if message.lower() == 'bye':
            print("[SERVER] Mengakhiri koneksi...")
            break

        # Kirim balasan ke client
        response = input("Ketik balasan -> ")
        encrypted_response = encrypt_message_des(response, des_key)
        print(f"[SERVER] Balasan terenkripsi dikirim: {encrypted_response}")  # Log balasan terenkripsi
        conn.send(encrypted_response.encode())

    conn.close()

if __name__ == '__main__':
    server_program()
