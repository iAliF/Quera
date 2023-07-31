import os
from argparse import ArgumentParser

NAME = {
    "cs": "Program.cs"
}
README_TEMPLATE = "# [{id}](https://quera.org/problemset/{id}/)"


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
            args.file_name or NAME.get(args.ext, f"{args.id}.{args.ext}"),
            ""
        )
    )

    for file_name, data in files_to_write:
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
    args = parser.parse_args()

    print(main())
