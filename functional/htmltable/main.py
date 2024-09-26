from functools import reduce


def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"

    return tagger


def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")

    return accumulate


tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


# don't touch above this line


def create_html_table(data_rows):
    rows = ""

    def create_table_headers(headers):
        nonlocal rows

        header_cells = map(lambda header: f"<th>{header}</th>", headers)
        header_row = "".join(header_cells)
        rows = f"<tr>{header_row}</tr>" + rows

        html_rows = "".join(
            map(lambda row: f"<tr>{''.join(map(lambda cell: f'<td>{cell}</td>', row))}</tr>", data_rows)
        )
        rows += html_rows

        return f"<table>{rows}</table>"

    return create_table_headers

