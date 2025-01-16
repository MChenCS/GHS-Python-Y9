def encrypt_decrypt(message, key, mode):
  """
  Encrypts or decrypts a message using a simple Caesar cipher.

  Args:
    message: The message to be encrypted or decrypted.
    key: The shift amount for the cipher.
    mode: 'encrypt' or 'decrypt'.

  Returns:
    The encrypted or decrypted message.
  """

  result = ""
  for char in message:
    if char.isalpha():
      if mode == 'encrypt':
        shift = key
      elif mode == 'decrypt':
        shift = -key
      else:
        raise ValueError("Invalid mode. Must be 'encrypt' or 'decrypt'.")

      if char.isupper():
        start = ord('A')
      else:
        start = ord('a')
      shifted_char = chr((ord(char) - start + shift) % 26 + start)
      result += shifted_char
    else:
      result += char
  return result

if __name__ == "__main__":
  mode = input("Enter mode (encrypt/decrypt): ").lower()
  key = int(input("Enter key: "))
  message = input("Enter message: ")

  if mode not in ('encrypt', 'decrypt'):
    print("Invalid mode.")
  else:
    result = encrypt_decrypt(message, key, mode)
    print(f"Result: {result}")