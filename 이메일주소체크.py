import re

def is_valid_email(email):
    # 이메일 패턴 정규 표현식
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 샘플 이메일 주소
sample_emails = [
    "test.email@example.com",
    "valid.email@domain.co",
    "user.name+tag+sorting@example.com",
    "user_name@sub.domain.com",
    "email@domain.com",
    "invalid-email@domain",
    "email@domain..com",
    "email@.com",
    "email@domain.c",
    "plainaddress"
]

# 이메일 주소 유효성 검사
for email in sample_emails:
    print(f"'{email}': {'Valid' if is_valid_email(email) else 'Invalid'}")
