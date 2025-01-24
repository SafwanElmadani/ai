
## Plotly
- pip install plotly ipywidgets 
- pip install pandas (optional)
- install JupyterLab extensions for plotly `jupyterlab-plotly` (NOT needed. Deprecated)
- set the default renderer to `plotly_mimetype`
    - ```python
        import plotly.io as pio
        # For JupyterLab
        # pio.renderers.default = 'plotly_mimetype'  # For JupyterLab
        pio.renderers.default = 'iframe'  # For JupyterLab

        ```

## JupyterLab
- pip install --upgrade jupyterlab-vim
    - vim motion
