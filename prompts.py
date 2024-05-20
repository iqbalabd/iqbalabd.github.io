#!/usr/bin/env python
# -*- coding: utf-8 -*-

TRANSLATE_CONTENT_TO_JA = [
    {
        "role": "system",
        "content": "You are a helpful English to Japanese blog translator that follows instructions correctly. "
        "Given English text in Markdown format, you will correctly translate the text to the Japanese language. "
        "Remember that the text is written in Markdown and may contain URLs to web pages, paths to files, URLs "
        "to images and symbols that define headers and format in Markdown. Do not translate these. "
        "There are also reserved words that define how the Markdown is presented defined as metadata such as "
        "Title, Slug, Lang, Date, Modified, Tags, Author and Summary. Do not translate these. "
        "Because the text is for a personal blog, you will use informal Japanese language fit for reading by "
        "friends and family. Feel free to use colloquials when translating.",
    },
    {
        "role": "user",
        "content": "Since 2019, I have been working on trying to get our Python community in "
        "East/South/South East Asia (collectively called APAC) to move towards a more coherent direction together. "
        "There were also plans for a poster session to introduce us to the wider North American and international "
        "community during the annual PyCon 2020 in Pittsburgh, but due to COVID-19, that unfortunately didn't "
        "happen. PyCon US is an annual Python programming language conference, which is organized by the "
        "Python Software Foundation (PSF) and at the same time is also its single biggest fundraising event.",
    },
    {
        "role": "assistant",
        "content": "2019年以降、私は東アジア、南アジア、東南アジア（まとめてAPACと呼ばれる）にあるPythonコミュニティ"
        "がより一貫した方向に進めるよう尽力してきた。 毎年北米で開催されるPyCon(今年はピッツバーグで開催)の期間中に、"
        "より広範な北米および国際コミュニティに 紹介するコミュニティブースも予定されていたが、"
        "COVID-19のため残念ながら中止になった。 PyCon US1 とはPythonソフトウェア財団（PSF）が主催する年に1度の"
        "プログラミング言語Pythonに関するカンファレンスで、 同時に唯一の大規模な資金調達イベントでもある。",
    },
    {
        "role": "user",
        "content": """
Title: Diversification is the future for the Python Software Foundation (PSF)
Slug: diversification-is-the-future-for-the-psf
Lang: en
Date: 2020-06-20 16:05
Modified: 2020-06-20 16:05
Tags: psf; politics; community; 2020;
Authors: Iqbal Abdullah
Summary: My thoughts after my failed attempt at running for the 2020 board of the Python Software Foundation (PSF).""",
    },
    {
        "role": "assistant",
        "content": """
Title: 多様化がPythonソフトウェア財団（PSF）の将来像
Slug: diversification-is-the-future-for-the-psf
Lang: ja
Date: 2020-06-20 16:05
Modified: 2020-06-20 16:05
Tags: psf; 政治; コミュニティ; 2020;
Authors: Iqbal Abdullah
Summary: Pythonソフトウェア財団（PSF）の2020年理事会選挙に立候補し落選して思うこと。""",
    },
]

FIX_CONTENT_PROMPT = [
    {
        "role": "system",
        "content": "You are a helpful English blog editor that follows instructions correctly. "
        "Given text in Markdown format, you will correct the text by correcting grammar mistakes, "
        "spelling mistakes, removing wordiness, removing redundancy, correcting word choices, adding "
        "commas, changing capitalization, changing or removing the preposition as necessary, "
        "correcting the verb form, correcting subject-verb agreement, change the wording, rephrase "
        "sentences, correcting the comma splice, correcting article-noun agreement, correcting "
        "agreement mistakes, adding missing verbs, rewrite sentences for clarity, adding missing "
        "articles, removing redundancy, removing unnecessary verbs, fixing the infinitive, correcting "
        "quantifier usage, and replacing words to make the sentences easier to understand. "
        "Remember that the text is written in Markdown and may contain URLs to web pages, "
        "paths to files, URLs to images and anotations that define headers and format in Markdown. "
        "Keep these as they are and do not change them. There are also reserved words that define "
        "how the Markdown is translated to the final blog post such as Title, Slug, Lang, Date, "
        "Modified, Tags, Author and Summary. You will ignore these reserved words. Make sure to "
        "return the whole given text regardless if there are corrections.",
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
    {
        "role": "user",
        "content": "Now I have transitioned to _'Aggresive Packing'_ where you get only essentials for your comfort "
        "and try get anything else that you'd need along the way.",
    },
    {
        "role": "assistant",
        "content": "Now I have transitioned to _'Aggresive Packing'_ where you get only essentials for your comfort "
        "and try get anything else that you'd need along the way.",
    },
    {
        "role": "user",
        "content": """
- [PyCon US 2024 in Pittsburgh](https://us.pycon.org/2024/) (From May 15th to May 19th)
- [Latitude59 in Tallinn](https://latitude59.ee) (From May 22nd to May 24th)""",
    },
    {
        "role": "assistant",
        "content": """
- [PyCon US 2024 in Pittsburgh](https://us.pycon.org/2024/) (From May 15th to May 19th)
- [Latitude59 in Tallinn](https://latitude59.ee) (From May 22nd to May 24th)""",
    },
]
