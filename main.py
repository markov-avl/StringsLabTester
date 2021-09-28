from random import randint, choice
import string
import subprocess


TEST_PROGRAM = 'main.exe'
MAX_SOURCE_STRING_LENGTH = 50
LETTERS = (*string.ascii_lowercase, ' ')


def generate_random_string(length: int) -> str:
    return ''.join(choice(LETTERS) for _ in range(length))


def execute_test_program(source_string: str, to_replace: str, with_replace: str) -> str:
    command = [TEST_PROGRAM, source_string, to_replace, with_replace]
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    return proc.communicate()[0].decode("utf-8")


if __name__ == '__main__':
    successful = 0
    failed = 0

    while True:
        source_length = randint(0, MAX_SOURCE_STRING_LENGTH)
        source_string = generate_random_string(source_length)
        if randint(0, 100) >= 80:
            from_ = randint(1, MAX_SOURCE_STRING_LENGTH - 1)
            to_ = randint(from_, MAX_SOURCE_STRING_LENGTH)
            to_replace = source_string[from_: to_]
        else:
            to_replace_length = randint(0, MAX_SOURCE_STRING_LENGTH)
            to_replace = generate_random_string(to_replace_length)
        with_replace_length = randint(0, MAX_SOURCE_STRING_LENGTH)
        with_replace = generate_random_string(with_replace_length)

        try:
            if to_replace:
                python_result = str(source_string).replace(to_replace, with_replace)
            else:
                python_result = source_string
            cpp_result = execute_test_program(source_string, to_replace, with_replace)

            if python_result != cpp_result:
                print(f'Python result: "{python_result}"')
                print(f'C++ result: "{cpp_result}"')
                raise Exception('Results don\'t match')
            else:
                successful += 1

        except Exception as e:
            failed += 1
            print(f'{e.__class__.__name__}: {e}')
            print(f'Source string: "{source_string}"')
            print(f'To replace: "{to_replace}"')
            print(f'With replace: "{with_replace}"')
            print(f'Failed tests: {failed}')
            print(f'Successful tests: {successful}')
            print()
