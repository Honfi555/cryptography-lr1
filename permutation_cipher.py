import math
from random import choice

from static import PERMUTATION_KEY as KEY, SECRET_DATA


def _normalize_key_indexation(key: list[int]) -> list[int]:
	return list(map(lambda i: i - 1, key))


def _inverse_key(key: list[int]) -> list[int]:
	inv = [0] * len(key)
	for j, k in enumerate(key):
		inv[k] = j
	return inv


def _normalize_plaintext_length(plaintext: str, len_cipher_text: int) -> str:
	return plaintext + choice(plaintext) * (len_cipher_text - len(plaintext))


def _core(main_text: list[str], depended_text: str, key: list[int]) -> str:
	len_key: int = len(key)
	for i in range(int(len(main_text) / len_key)):
		for j in range(len_key):
			main_text[i * len_key + j] = depended_text[i * len_key + key[j]]

	return ''.join(main_text)


def encrypt(plaintext: str, key: list[int]) -> str:
	key: list[int] = _normalize_key_indexation(key)

	cipher_text: list[str] = [""] * math.ceil(len(plaintext) / len(key)) * len(key)

	plaintext = _normalize_plaintext_length(plaintext, len(cipher_text))

	return ''.join(_core(cipher_text, plaintext, key))


def decrypt(ciphertext, key: list[int]) -> str:
	key: list[int] = _normalize_key_indexation(key)
	key: list[int] = _inverse_key(key)

	plaintext: list[str] = [""] * len(ciphertext)

	return ''.join(_core(plaintext, ciphertext, key))


def main() -> None:
	"""Точка запуска файла."""

	print("Открытое сообщение: ", SECRET_DATA)
	print("Зашифрованные данные: ", ciphertext := encrypt(SECRET_DATA, KEY))
	print("Дешифрованные данные: ", decrypt(ciphertext, KEY))

	return None


if __name__ == "__main__":
	main()
