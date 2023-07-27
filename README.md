# sentimental

## Summary

The qualitative analysis component of a [Value Investing](https://www.investopedia.com/terms/v/valueinvesting.asp) approach. Apply natural language models to perform sentiment analysis on publicly-traded securities.

## Method

1. Employ an open source [Large Language Model (LLM)](https://www.nvidia.com/en-us/glossary/data-science/large-language-models/) like [LLaMA2](https://github.com/facebookresearch/llama) to review articles from business and financial reporters.
2. Using the model, score the sentiment in historical reports and articles towards various [quantitatively-filtered](https://github.com/computerise/stonks/) companies and compare the sentiment to historical stock performance.
3. Sources with the highest correlation between sentiment score and share price over time become **trusted sources**; the remainder become **candidate sources**.
4. Apply the algorithm to recent articles and reports from all sources and to obtain current sentiment towards the company stocks.
5. Iteratively reassess the source lists based on actual performance of the stocks by promoting candidate sources that outperformed trusted sources.
6. The sentiment scores, in conjunction with a quantitative evaluation of each company are used to assess the likelihood of stocks being over- or under-valued by the market.
7. Profit?
8. Repeat steps 4-8.

## Dependency Installation

"sentimental" requires an installation of python3.11 (tested on Python 3.11.3) and poetry (tested on Poetry 1.5.1).

### Python Installation

Instructions on how to set up and install python3.

#### Python Installation on Windows

Download and install the python3.11 [here](https://www.python.org/downloads/). Then add the parent directory of `python.exe` to the [System Environment Variables `Path` field](<https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)>). Where `<username>` is the name of the Windows user account, the default path for `python3.exe` is:

```text
C:\Users\<username>\AppData\Local\Programs\Python\Python311\
```

#### Python Installation on Debian-Based Linux Distributions

`python3` comes pre-installed on most modern distributions.

To manually install `python3.11` execute:

```bash
sudo add-apt-repository -y 'ppa:deadsnakes/ppa'
sudo apt-get install python3.11
```

### Poetry Installation

Instructions for installing poetry for dependency management and packaging.

#### Poetry Installation on Windows

To install poetry on Windows open PowerShell and execute:

```PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Then add the parent directory of `poetry.exe` to the [System Environment Variables `Path` field](<https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)>). Where `<username>` is the name of the Windows user account, the default path for `poetry.exe` is:

```text
C:\Users\<username>\AppData\Roaming\pypoetry\venv\Scripts\
```

#### Poetry Installation on Linux

To install poetry on Linux execute:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## Application Installation

### Dependencies

When using the launcher the application and dependencies are automatically installed.

To manually install the application from a Command Line Interface (CLI) on Windows or Linux, execute:

```shell
poetry install
```

## Configuration

The user input file must be a JSON file specified in `settings.toml` as `input_file`. By default `input_file` is `input.json`. All other application specific settings are specified in `settings.toml`. All necessary assumptions used for calculations are specified in `assumptions.toml`.

## Usage

### Windows Usage

Launch the application on Windows by double-clicking on `LAUNCH_WINDOWS.bat`. If Windows raises the warning `Windows protected your PC`, select `More info` then `Run anyway`.

Launch the application on Linux by executing:

### Linux Usage

```bash
./LAUNCH_LINUX.sh
```

## Development

To manually execute the application from a CLI, first activate a poetry virtual environment by executing:

```shell
poetry shell
```

Then launch the application by executing:

```shell
sentimental
```

The poetry shell session is exited by executing:

```shell
deactivate
```

Note that `sentimental` can be executed without entering a poetry shell session by prefixing all commands (where `<command>` is any command stated in `Usage` or `Test`) with:

```shell
poetry run <command>
```

## Test

To run unit tests from within a poetry shell session execute:

```shell
pytest
```

To see the code coverage report from within a poetry shell session execute:

```bash
coverage run -m pytest test/
coverage report --fail-under=55
```
