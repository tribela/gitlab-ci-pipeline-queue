import setuptools

setuptools.setup(
    name='gitlab-ci-pipeline-queue',
    version='0.0.1',
    author='Kjwon15',
    author_email='kjwonmail@gmail.com',
    description='Lock job until older pipeline finished',
    install_requires=[
        'requests>=2.23.0',
    ],
    scripts=['gitlab-ci-pipeline-queue']
)
