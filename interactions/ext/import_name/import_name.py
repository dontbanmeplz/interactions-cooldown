"""
Change the file name to the name of the extension.
Technically, you can name it anything you want, but
it's best to use the same name as the extension import name.
"""

from interactions import Client, Extension
from typing import Optional  # just using it for typehinting


class ExtensionName(Extension):
    """
    This is the core of the extension.
    This is where you code your extension.
    Change the name to the name of your extension.
    """

    def __init__(self, client: Client, *args, **kwargs):
        """
        You can add code here to be run when the extension is loaded.
        """
        ...  # do stuff here

    ...  # add more stuff here if needed


def setup(client: Client, *args, **kwargs) -> Optional[Extension]:
    """
    This setup function will be run when the extension is loaded.
    Optionally, arguments can be inputted by the user when loading.
    ```py
    client.load("interactions.ext.import_name", ...)
    ```
    At the end, this function should initialize the extension,
    and either return it, return something else, or return nothing.
    """
    ...  # do stuff here
    return ExtensionName(client, *args, **kwargs)
