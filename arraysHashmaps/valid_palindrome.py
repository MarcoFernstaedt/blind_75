def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


# Test cases for is_palindrome function

tests = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("No lemon, no melon", True),
    ("Was it a car or a cat I saw?", True),
    ("12321", True),
    ("123421", False),
    ("Able , was I, eRe I saw eLba", True),
]

for text, expected in tests:
    result = is_palindrome(text)
    print(
        f"{text!r} -> {result}  ({'OK' if result == expected else 'FAIL, expected ' + str(expected)})"
    )
