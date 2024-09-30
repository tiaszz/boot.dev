from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match (status):
        case CSVExportStatus.PENDING:
            mapped_data = list(map(lambda inner_list: list(map(str, inner_list)), data))
            tup = ("Pending...", mapped_data)
            return tup
        case CSVExportStatus.PROCESSING:
            rows = map(lambda row: ",".join(row), data)
            csv_data = "\n".join(rows)
            tup = ("Processing...", csv_data)
            return tup
        case CSVExportStatus.SUCCESS:
            tup = ("Success!", data)
            return tup
        case CSVExportStatus.FAILURE:
            converted_data = list(
                map(lambda inner_list: list(map(str, inner_list)), data)
            )
            rows = map(lambda row: ",".join(row), converted_data)
            csv_data = "\n".join(rows)

            tup = ("Unknown error, retrying...", csv_data)
            return tup

        case _:
            raise Exception("Unknown export status")
