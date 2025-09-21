from static import ALFABET_POWER, OFFSET, SECRET_DATA


def encrypt(plaintext: str, k: int) -> str:
	char_codes: list[int] = [ord(char) for char in plaintext]

	ciphertext: str = ''.join(map(lambda code: chr((code + k) % ALFABET_POWER), char_codes))

	return ciphertext


def decrypt(ciphertext: str, k: int) -> str:
	char_codes: list[int] = [ord(char) for char in ciphertext]

	decoded_string: str = ''.join(map(lambda code: chr((code - k) % ALFABET_POWER), char_codes))

	return decoded_string


def main() -> None:
	"""Точка запуска файла."""

	print("Открытое сообщение: ", SECRET_DATA)
	print("Зашифрованные данные: ", encoded_data := encrypt(SECRET_DATA, OFFSET))
	print("Дешифрованные данные: ", decrypt(encoded_data, OFFSET))

	return None


if __name__ == "__main__":
	main()
