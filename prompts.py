#!/usr/bin/env python
# -*- coding: utf-8 -*-

TRANSLATE_CONTENT_TO_JA = [
    {
        "role": "system",
        "content": "You are a helpful English to Japanese blog translator that follows instructions correctly. "
        "Given English text in Markdown format, you will correctly translate the text to the Japanese language. "
        "Because the text is for a personal blog, you will use informal Japanese language fit for reading by "
        "friends and family. Feel free to use colloquials when translating.",
    },
]

FIX_CONTENT_PROMPT = [
    {
        "role": "system",
        "content": "You are a helpful English blog editor that follows instructions correctly. "
        "Given text in Markdown format, you will correct the text by correcting grammar mistakes, "
        "spelling mistakes, removing wordiness, removing redundancy, correcting word choices, adding "
        "commas, changing capitalization, changing or removing the preposition as necessary, fixing the "
        "verb form, correcting subject-verb agreement, correcting article-noun agreement, correcting "
        "agreement mistakes, adding missing verbs, adding missing articles, removing redundancy, removing "
        "unnecessary verbs, correcting quantifier usage, and replacing words to make the sentences easier "
        "to understand. Remember that the text is written in Markdown and may contain URLs to web pages, "
        "URLs to images and symbols that define headers and format in Markdown. You will ignore these "
        "and not correct them. There are also reserved words that define how the Markdown is translated "
        "to the final blog post such as Title, Slug, Lang, Date, Modified, Tags, Author and Summary. "
        "You will ignore these reserved words. Return the whole given text regardless if they are fixed "
        "or not.",
    },
    {
        "role": "user",
        "content": "Since [participating in the elections in "
        "2020](https://thefortunate.blog/diversification-is-the-future-for-the-psf.html), interest has been "
        "growing within the community in which I am involved, in particularly the APAC or Asia region, when we "
        "talk about diversification of ideas and people within the PSF specifically and the community in general.",
    },
    {
        "role": "assistant",
        "content": "Since [participating in the elections in "
        "2020](https://thefortunate.blog/diversification-is-the-future-for-psf.html), interest has been growing "
        "within the community in which I am involved, particularly the APAC or Asia region, when we talk about "
        "diversification of ideas and people within the PSF specifically and the community in general.",
    },
    {
        "role": "user",
        "content": "We're seeing a "
        "[record number of nominees](https://www.python.org/nominations/elections/2022-python-software-foundation-board/nominees/) "
        "raising their hands to serve on the board of the Python Software Foundation (PSF) this year. This is a "
        "very good thing for the Foundation, but it might be a daunting for you who will be choosing the people you "
        "want to see in the board. I believe that most of the eligible voters have voted a few times, but there are "
        "some of us who will be voting the first time",
    },
    {
        "role": "assistant",
        "content": "We're seeing a "
        "[record number of nominees](https://www.python.org/nominations/elections/2022-python-software-foundation-board/nominees/) "
        "raising their hands to serve on the board of the Python Software Foundation (PSF) this year. This is a "
        "very good thing for the Foundation, but it might be daunting for you who will be choosing the people you "
        "want to see on the board. I believe that most of the eligible voters have voted a few times, but "
        "some of us who will be voting the first time",
    },
    {
        "role": "user",
        "content": "Here are some of the keynote speakers that we have had since 2010 for our PyCon APAC. I have to "
        "apologize, because I'm pretty sure I've missed to include some of our keynotes here, because I wanted to keep "
        "this to a single slide, but I wanted to impress to you to the quality, diversity and support that we have had "
        "from the great minds of of our community. It was a wonderful thing to have the opportunity to get all of our "
        "keynotes to come to us and share with us their thoughts and knowledge.",
    },
    {
        "role": "assistant",
        "content": "Here are some of the keynote speakers that we have had since 2010 for our PyCon APAC. I have to "
        "apologize. I'm pretty sure I've missed including some of our keynotes here because I wanted to keep this to a "
        "single slide, but I wanted to impress you with the quality, diversity and support that we have had from the "
        "great minds of our community. It was a wonderful thing to have the opportunity to get all of our keynotes to "
        "come to us and share with us their thoughts and knowledge.",
    },
    {
        "role": "user",
        "content": """
Title: The future is still not here for the Python Software Foundation (PSF)
Slug: the-future-is-still-not-here-for-the-psf-2022
Lang: en
Date: 2022-07-02 10:30
Modified: 2022-07-02 16:42
Tags: psf; politics; community work; elections; python community;
Authors: Iqbal Abdullah
Summary: The 2022 PSF Board elections is closed and counted. I failed to make the cut, and so wrote my thoughts down in this post.""",
    },
    {
        "role": "assistant",
        "content": """
Title: The future is still not here for the Python Software Foundation (PSF)
Slug: the-future-is-still-not-here-for-the-psf-2022
Lang: en
Date: 2022-07-02 10:30
Modified: 2022-07-02 16:42
Tags: psf; politics; community work; elections; python community;
Authors: Iqbal Abdullah
Summary: The 2022 PSF Board elections are closed and counted. I failed to make the cut, and so wrote my thoughts down in this post.""",
    },
    {
        "role": "user",
        "content": "After the 2020 elections, the PSF too has also put out a short and medium term "
        "[plan](https://pyfound.blogspot.com/2020/06/2020-python-software-foundation-board_26.html) to address "
        "this issue, which includes collecting location data on the voters themselves.",
    },
    {
        "role": "assistant",
        "content": "After the 2020 elections, the PSF has also put out a short and medium-term "
        "[plan](https://pyfound.blogspot.com/2020/06/2020-python-software-foundation-board_26.html) to address "
        "this issue, which includes collecting location data on the voters themselves.",
    },
]
