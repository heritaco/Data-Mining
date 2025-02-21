**In terminal**
   
   ```bash
   conda activate Geo-DA
   ```

   ```bash
   conda install numpy
   ```

   ```bash
   conda deactivate
   ```

   ```bash
   conda install conda-forge::jupyter
   ```

   ```bash
   jupyter notebook
   ```

   Ya si quiero activar pandas? 
   Buscamos conda forge pandas

   ```bash
   conda install conda-forge::pandas
   ```
   
   
**Create an environment:**
   
   ```bash
   conda create --name GDA python=3.9
   ```

   ```bash
   conda create --prefix ./GDA python=3.9
   ```

**Activate an environment:**

   ```bash
   conda activate Geo-DA
   ```

   ```bash
   conda activate ./env
   ```

**Install a package (e.g., numpy):**

   ```bash
   conda install numpy
   ```

**Deactivate the environment:**

   ```bash
   conda deactivate
   ```

**List all environments:**

   ```bash
   conda env list
   ```

**Remove an environment:**

   ```bash
   conda remove --name mi_entorno --all
   ```

   ```bash
   conda env remove --prefix C:\Heri\GitHub\.Semester\Geospatial-Data-Analysis\Geo-DA
   ```

**Update conda:**

   ```bash
   conda update -n base -c defaults conda
   ```


**List all installed packages in an environment:**

   ```bash
   conda list
   ```

**Install a specific version of a package:**

   ```bash
   conda install numpy=1.21.0
   ```


**Update a specific package:**

   ```bash
   conda update numpy
   ```

**Check for outdated packages:**

   ```bash
   conda update --all
   ```


**Search for a package:**

   ```bash
   conda search pandas
   ```

**Clone an environment:**
 
   ```bash
   conda create --name GDA_clone --clone Geo-DA
   ```

**Deactivate a specific environment without using `conda deactivate`:**
   If you're already in an environment and want to go back to the base environment without deactivating, use:

   ```bash
   conda activate base
   ```

**Clean unused packages and caches:**

   ```bash
   conda clean --all
   ```

**Check the current conda configuration:**

   ```bash
   conda config --show
   ```

**Show information about the environment:**
   If you want detailed information about the currently active environment, use:

   ```bash
   conda info
   ```

   This will give you information such as the version of conda, active environment, and the locations of the installed environments.

**Export an environment to a file:**

   ```bash
   conda list --export > environment.txt
   ```

   ```bash
   conda env export > environment.yml
   ```


**Create an environment from an environment file:**

   ```bash
   conda create --name new_env --file environment.txt
   ```

   Or for a YAML file:

   ```bash
   conda env create -f environment.yml
   ```