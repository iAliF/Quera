import os
from argparse import ArgumentParser

TEST_FILE_TEMPLATE = """import unittest


class Test(unittest.TestCase):
    def test_one(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
"""
README_TEMPLATE = "# [{id}](https://quera.org/problemset/{id}/)"

DATA = {
    "cs": {
        "name": "Program.cs"
    },
    "py": {
        "name": lambda p_id: f"q_{p_id}.py",
        "extra": {
            "test.py": TEST_FILE_TEMPLATE
        }
    }
}


def main() -> str:
    s_id = str(args.id)
    if os.path.exists(s_id):
        return "Folder already exists"

    os.mkdir(s_id)

    files_to_write = (
        # File name, data
        (
            "README.md",
            README_TEMPLATE.format(id=args.id)
        ),
        (
            args.file_name or DATA.get(args.ext, {}).get("name", f"{args.id}.{args.ext}"),
            ""
        ),
        *(
            (
                (
                    key,
                    value
                ) for key, value in DATA.get(args.ext, {}).get("extra", {}).items()
            ) if args.with_extra else ()
        )
    )

    for file_name, data in files_to_write:
        if not isinstance(file_name, str):
            file_name = file_name(args.id)

        with open(
                os.path.join(s_id, file_name),
                "w"
        ) as file:
            file.write(data)

    return "Done"


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("id", type=int, help="problem-set ID")
    parser.add_argument("ext", type=str, help="source file extension")
    parser.add_argument("--file-name", type=str, help="Custom file name")
    parser.add_argument("--with-extra", action='store_true', help="Creating extra files")
    args = parser.parse_args()

    print(main())
