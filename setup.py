import setuptools

setuptools.setup(
    name='github-webhooks',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
