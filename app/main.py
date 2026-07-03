
def copy_file(command: str) -> None:

    str_parts = command.strip().split(" ")

    if len(str_parts) == 3 and str_parts[0] == "cp":
        cmd, origin, destination = str_parts

        if origin != destination:
            try:
                with (open(origin, "r") as f,
                      open(destination, "w") as d):

                    d.write(f.read())

            except FileNotFoundError:
                pass
