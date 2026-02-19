
def isPalindrome(text):
  text = text.lower()
  if text == text[::-1]:
    return True
  else:
    return False


def main():
  userInput = input("Dia algo ai: ")

  if (isPalindrome(userInput)):
    print(userInput + " é um palindrome!")
  else:
    print(userInput + " é um palindrome!")

if __name__ == "__main__":
    main()