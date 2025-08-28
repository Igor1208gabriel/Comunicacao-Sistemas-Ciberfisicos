from setuptools import find_packages, setup

package_name = "webcam"

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
    maintainer="Igor Santos",
    maintainer_email="santos.igor1@escolar.ifrn.edu.br",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "publishercameraraw = webcam.capturar_webcam:main",
            "display = webcam.display_image:main",
        ],
    },
)
