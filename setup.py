from setuptools import setup

setup(
name="eventity",
version='0.3.1',
description="Easy event based ECS system",
keywords="event entity component system ecs",
url="https://github.com/JonSnowbd/Eventity",
author="Josiah P.",
author_email="vasti009@gmail.com",
license="MIT",
packages=["eventity"],
test_suite="nose2.collector",
tests_require=["nose2"],
zip_safe=False
)
