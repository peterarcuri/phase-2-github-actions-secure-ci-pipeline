
def health_check():
    return {
        "status": "ok",
        "service": "secure-ci-pipeline",
        "security": "enabled"
    }


def add_numbers(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(health_check())

