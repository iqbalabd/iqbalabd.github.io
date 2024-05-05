#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from llama_cpp import Llama
import argparse
from dotenv import load_dotenv

from prompts import FIX_CONTENT_PROMPT, TRANSLATE_CONTENT_TO_JA


def edit_content(text, n_ctx=5120, n_threads=8, use_gpu=False, translate=None):
    """Fixes the grammar of the given text

    n_ctx is the context window in tokens
    n_threads sets the amount of CPU threads to use
    n_gpu_layers sets the GPU acceleration to use
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
        "content": f"{text}",
    }
    messages.append(final_message)

    chat_output = llm.create_chat_completion(
        messages=messages,
        temperature=0.7,
        top_p=0.1,
        top_k=40,
    )
    try:
        _output = chat_output["choices"][0]["message"]["content"]
    except Exception:
        pass

    return _output.strip()


def process_file(input_file, output_file, translation=None, gpu=None):
    # Open the input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    if gpu:
        processed_content = edit_content(content, use_gpu=True, translate=translation)
    else:
        processed_content = edit_content(content, translate=translation)

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
