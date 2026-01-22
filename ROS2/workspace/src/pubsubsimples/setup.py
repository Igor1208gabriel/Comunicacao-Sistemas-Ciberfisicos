"Module docstring"
from setuptools import find_packages, setup

PACKAGE_NAME = "pubsubsimples"

setup(
    name=PACKAGE_NAME,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages",
         ["resource/" + PACKAGE_NAME]),
        ("share/" + PACKAGE_NAME, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="igo",
    maintainer_email="santos.igor1@escolar.ifrn.com.br",
    description="Pacote com Publisher e Subscriber simples",
    license="LICENSE",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "publisher = pubsubsimples.publisher:main",
            "subscriber = pubsubsimples.subscriber:main",
        ],
    },
)
