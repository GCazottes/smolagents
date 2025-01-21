from setuptools import setup, find_packages

setup(
    name="smolagents_httpx",  # Nom du package
    version="0.1.0",    # Version du package
    description="smolagents library modified to be proxy-compatible",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Guillaume Cazottes",
    author_email="guillaume.cazottes@gmail.com",
    url="https://github.com/GCazottes/smolagents",
    packages=find_packages(),  # Trouve automatiquement les sous-packages
    install_requires=[],       # Liste des dépendances
    python_requires=">=3.6",
)
