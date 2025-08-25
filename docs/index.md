# Documentation

## Overview

This project is currently being developed to test **reward hacking behaviors** in large language models (LLMs).
The approach is to create coding tests with hidden malicious intents: if the LLM tries to pass the test by following those intents, it indicates that the model may be discarding its previously trained safety standards in order to maximize reward.

The goal is to observe and evaluate whether the LLM engages in harmful actions to optimize the reward signal during the test.

To achieve this, the project references and leverages the initial attack dataset of 120 harmful behavior prompts written in natural language, introduced in the work of **[Liu et al](https://www.usenix.org/conference/usenixsecurity24/presentation/liu-tong)**.

When running the project with the current *reward hacking*, the program will run all the prompts in the list.
If you prefer, you can fix a specific test prompt in **[`src/red_team_harness/prompts.py`](../src/red_team_harness/prompts.py)**.