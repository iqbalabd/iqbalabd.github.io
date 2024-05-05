#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A script to help edit blog posts for grammar errors.
"""

import os
import re
from llama_cpp import Llama
import argparse
from dotenv import load_dotenv

from prompts import FIX_CONTENT_PROMPT, TRANSLATE_CONTENT_TO_JA

SEPERATOR = "<!-- EDPART -->"


def edit_content(text_list, n_ctx=5120, n_threads=8, use_gpu=False, translate=None):
    """Fixes the grammar of the given list of text

    n_ctx is the context window in tokens
    n_threads sets the amount of CPU threads to use
    use_gpu sets if GPU is to be used. If not set, CPU will be used
    translate sets if translation is to be done
    """

    if use_gpu:
        n_gpu = 1
        n_gpu_layers = -1
        use_gpu = True
    else:
        n_gpu = 0
        n_gpu_layers = 0
        use_gpu = False

    load_dotenv()
    model_path = os.environ.get("GGUF_FILE_PATH")
    llm = Llama(
        model_path=model_path,
        chat_format="chatml",
        n_ctx=n_ctx,
        n_threads=n_threads,
        n_gpu_layers=n_gpu_layers,
        n_gpu=n_gpu,
        use_gpu=use_gpu,
    )

    output_list = list()
    _cnt = 0
    for _part in text_list:

        messages = list()
        if translate == "ja":
            for m in TRANSLATE_CONTENT_TO_JA:
                messages.append(m)
        else:
            for m in FIX_CONTENT_PROMPT:
                messages.append(m)

        # The final_message is defined here because input_text is defined here
        final_message = {
            "role": "user",
            "content": f"{_part.strip()}",
        }
        messages.append(final_message)

        chat_output = llm.create_chat_completion(
            messages=messages,
            temperature=1.0,
            top_p=0.1,
            top_k=40,
        )
        try:
            _edited_output = chat_output["choices"][0]["message"]["content"]
            output_list.append(_edited_output)
            print(f"DONE {_cnt}/{len(text_list)}")
            _cnt += 1
        except Exception:
            pass

    _output = f"\n\n{SEPERATOR}\n\n".join(output_list)

    return _output.strip()


def process_file(input_file, output_file, translation=None, gpu=None):
    # Open the input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    content_parts = re.split(r"<!-- EDPART -->", content)

    if gpu and gpu.lower() == "y":
        processed_content = edit_content(
            content_parts, use_gpu=True, translate=translation
        )
    else:
        processed_content = edit_content(content_parts, translate=translation)

    # Write to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(processed_content)


def main():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Fix grammar and optionally translate a Markdown file."
    )

    # Add the arguments
    parser.add_argument("input_file", type=str, help="The input Markdown file")
    parser.add_argument("output_file", type=str, help="The output Markdown file")
    parser.add_argument("--gpu", type=str, help="Use GPU (optional)")
    parser.add_argument(
        "--translate", type=str, help="Language code for translation (optional)"
    )

    # Parse the arguments
    args = parser.parse_args()

    # Process the file
    process_file(args.input_file, args.output_file, args.translate, args.gpu)


if __name__ == "__main__":
    main()
