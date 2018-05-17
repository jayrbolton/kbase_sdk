
## Project anatomy

## Development

Key files:

* `setup.py`
* `conda_recipe`

Install conda and miniconda

### Tests

```sh
conda create -n kbase_sdk
source activate kbase_sdk
pip install --editable .
make test
```

When you are done, be sure to `source deactivate`

#### Build

```
conda-build conda_recipe
```
