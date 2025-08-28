from setuptools import find_packages, setup

package_name = "pubsubsimples"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
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
