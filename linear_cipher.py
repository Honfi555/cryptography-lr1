import math
from typing import Iterator

from static import ALFABET_POWER, LINEAR_KEY_A as KEY_A, LINEAR_KEY_B as KEY_B, SECRET_DATA


class Keys:
	__slots__ = ("a", "b")

	def __init__(self, a: int, b: int) -> None:
		if not self._is_valid_key(a, ALFABET_POWER):
			raise ValueError()
		self.a = int(a)
		self.b = int(b)

	def __iter__(self) -> Iterator[int]:
		yield self.a
		yield self.b

	def __repr__(self) -> str:
		return f"Keys(a={self.a}, b={self.b})"

	def _is_valid_key(self, a: int, n: int) -> bool:
		return math.gcd(n, a) == 1


def encrypt(plaintext: str, keys: Keys, n: int) -> str:
	cipher_text = ""
	for char in plaintext:
		cipher_text += chr((keys.a * ord(char) + keys.b) % n)
	return cipher_text


def decrypt(ciphertext: str, keys: Keys, n: int) -> str:
	keys = Keys(a=pow(keys.a, -1, n), b=keys.b)

	plaintext = ""
	for char in ciphertext:
		plaintext += chr((keys.a * (ord(char) - keys.b)) % n)
	return plaintext


def main() -> None:
	"""Точка запуска файла."""

	keys: Keys = Keys(a=KEY_A, b=KEY_B)

	print("Открытое сообщение: ", SECRET_DATA)
	print("Зашифрованные данные: ", ciphertext := encrypt(SECRET_DATA, keys, ALFABET_POWER))
	print("Дешифрованные данные: ", decrypt(ciphertext, keys, ALFABET_POWER))

	return None


if __name__ == "__main__":
	main()
