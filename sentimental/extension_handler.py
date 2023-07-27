"""Extension handler utility."""

class ExtensionHandler:
    """Utility to handle file extensions."""

    def change_file_extension(path: str, new_extension: str) -> str:
        """Change the file extension of a file at the specified path."""
        extensionless_path = ExtensionHandler.remove_file_extension(path)
        new_path = ExtensionHandler.add_file_extension(extensionless_path, new_extension)
        return new_path

    def remove_file_extension(path: str) -> list[str]:
        """Remove the top-level extension from a file if the file has an extension."""
        if "." not in path:
            raise ValueError("Specified file does not have a file extension")
        return path.split(".")[0]

    def add_file_extension(path: str, new_extension: str) -> str:
        """Add any string to the end of a file path and prepend a dot if not supplied."""
        if new_extension[0] != ".":
            new_extension = "." + new_extension
        return path + new_extension
