from interactions.ext import Base, build, Version, VersionAuthor

# gets the long description from the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# data for pypi
data = {
    "name": "interactions.ext.import_name",  # the name of the extension
    "description": "description",  # the short description of the extension
    "long_description": long_description,  # the long description of the extension, taken from README.md
    "version": Version(
        version="1.0.0",
        author=VersionAuthor(name="github_username_here", email="example@email.domain"),
    ),  # the version of the extension
    "link": "https://github.com/username/repo",  # the link to the extension's repo
}


class MyThirdParty(Base):
    def __init__(self):
        super().__init__(**data)


library = MyThirdParty()
build(library)
