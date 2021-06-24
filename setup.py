import setuptools

setuptools.setup(
    name='github-webhooks',
    version='2021.06.23',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
