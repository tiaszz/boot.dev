from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document, edit_type, edit):
    match (edit_type):
        case EditType.NEWLINE:
            lines = document.split("\n")
            line_number = edit["line_number"]
            
            if line_number >= len(lines):
                raise Exception("Invalid line number")
            
            lines[line_number] += "\n"
            return "\n".join(lines)

        case EditType.SUBSTITUTE:
            insert_text = edit["insert_text"]
            line_number = edit["line_number"]
            start = edit["start"]
            end = edit["end"]
            lines = document.split("\n")

            if line_number >= len(lines):
                raise Exception("Invalid line number")

            modify = lines[line_number]

            if start > len(modify):
                raise Exception("Invalid start index")
            if end > len(modify) or end < start:
                raise Exception("Invalid end index")

            lines[line_number] = modify[:start] + insert_text + modify[end:]
            return "\n".join(lines)

        case EditType.INSERT:
            insert_text = edit["insert_text"]
            line_number = edit["line_number"]
            start = edit["start"]
            lines = document.split("\n")

            if line_number >= len(lines):
                raise Exception("Invalid line number")

            modify = lines[line_number]

            if start > len(modify):
                raise Exception("Invalid start index")

            lines[line_number] = modify[:start] + insert_text + modify[start:]
            return "\n".join(lines)
            
        case EditType.DELETE:
            line_number = edit["line_number"]
            start = edit["start"]
            end = edit["end"]
            lines = document.split("\n")

            if line_number >= len(lines):
                raise Exception("Invalid line number")

            modify = lines[line_number]


            if start > len(modify):
                raise Exception("Invalid start index")

            if end > len(modify) or end < start:
                raise Exception("Invalid end index")

            lines[line_number] = modify[:start] + "" + modify[end:]
            return "\n".join(lines)

        case _:
            raise Exception("Unknown edit type")
            
