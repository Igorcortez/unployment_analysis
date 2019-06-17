# [`Unemployment_analysis`]
> This project uses data from RAIS - MTE in order to understand what kind of factors are associated with unemployment in Brazi. This is an exercise that is done almost every day by the government and think tank institutions like IPEA - Instuto de Pesquisas Econômicas Aplicadas. What is new here, is the use of machine learning techniques to dive in the data and find insights the may or may not be already known.  


## Stakeholders

| Role                 | Responsibility         | Full name                | e-mail       |
| -----                | ----------------       | -----------              | ---------    |
| Data Scientist       | Author                 | [`Igor Cortez`]            | [`igorcortez@gmail.com`] |

## Usage
> Describe how to reproduce your model

Usage is standardized across models. There are two main things you need to know, the development workflow and the Makefile commands.

Both are made super simple to work with Git and Docker while versioning experiments and workspace.

All you'll need to have setup is Docker and Git, which you probably already have. If you don't, feel free to ask for help.h

Makefile commands can be accessed using `make help`.


Make sure that **docker** is installed.

Clone the project from the analytics Models repo.
```
git clone https://github.com/<@github_username>/unployment_analysis.git
cd unployment_analysis
```

## Documentation

* [project_specification.md](./docs/project_specification.md): gives a data-science oriented description of the project.

* [model_report.md](./docs/model_report.md): describes the modeling performed.


#### Folder structure
>Explain you folder strucure

* [docs](./docs): contains documentation of the project
* [analysis](./analysis/): contains notebooks of data and modeling experimentation.
* [tests](./tests/): contains files used for unit tests.
* [unployment_analysis](./unployment_analysis/): main Python package with source of the model.
