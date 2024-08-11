def list_files(current_filetree, current_path=""):
    file_path = []

    for key, value in current_filetree.items():
        if current_path:
            new_path = f"{current_path}/{key}"
        else:
            new_path = f"/{key}"
        
        if value is None:
            file_path.append(new_path)
        elif isinstance(value, dict):
            file_path.extend(list_files(value, new_path))

    return file_path

