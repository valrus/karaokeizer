from setuptools import setup, find_namespace_packages

setup(
    name='karaokeizer',
    version='1.0',
    packages=find_namespace_packages(),
    entry_points={
        'console_scripts': [
            'karaokeize = karaokeizer.karaokeizer:main',
        ],
    },
    install_requires=[
        'aeneas',
        'doit',
        'lyricsgenius',
        'moviepy',
        'mutagen',
        'pydub',
        'spleeter',
        'youtube-dl',
    ]
)
