from typing import List
from setuptools import setup ,find_packages


def requirement(file_path:str)->list[str]:
    requirement=[]
    with open(file_path, encoding='utf-8') as obj_file:
        requirement=obj_file().readlines()
        requirement=[req.strip() for req in requirement if req.strip() and not req.startswith('-e')]#first get all , pass on all req and get 1) req without ends/n 2)not start -e
        return requirement



setup(
    name="Parkinson Disease",
    description="artificial intelligence model (using classification algorithms) can predict whether a person has Parkinson's disease or not based on a set of characteristics.",
    author="MohamedNasser",
    author_email="mohamednasserabohamda",
    packages=find_packages(),
    install_require=requirement("requirement.txt")
)