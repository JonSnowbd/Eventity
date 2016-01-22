from setuptools import setup

setup(
name="eventity",
version='0.1.0',
description="Easy event based ECS system",
keywords="event entity component system ecs",
url="www.todo.com",
author="Josiah P.",
author_email="vasti009@gmail.com",
license="MIT",
packages=["eventity"],
test_suite="nose2.collector",
tests_require=["nose2"],
zip_safe=False
)
