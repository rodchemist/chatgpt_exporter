# Setting Up Dare FTP Manager with Conda

This guide will help you set up the Dare FTP Manager application using Conda for Python environment management.

## Prerequisites

- **Anaconda** or **Miniconda** installed
- Node.js 16.0.0 or higher
- npm (comes with Node.js)

## Setup Instructions

1. **Ensure Conda is Initialized**

   Make sure Conda is properly initialized in your command prompt. You can verify this by running:

   ```bash
   conda --version
   ```

   If you get an error, you may need to initialize Conda for your shell:
   ```bash
   conda init cmd.exe
   ```
   
   Then close and reopen your command prompt.

2. **Run the Setup Script**

   Copy the Conda setup script to your project directory and run it:

   ```bash
   cd C:\ai_repos\tempering_prediction
   python conda-setup-script.py
   ```

   This script will:
   - Create the necessary directory structure
   - Move and rename files to their correct locations
   - Create a Conda environment.yml file
   - Generate batch files for Conda-aware setup and execution

3. **Create Conda Environment and Install Dependencies**

   After running the setup script, execute the `setup.bat` file that was created:

   ```
   setup.bat
   ```

   This will:
   - Create a Conda environment named `dare_ftp_manager`
   - Install the required Python packages (pyftpdlib, psutil)
   - Install all the Node.js dependencies for the application

4. **Start the Application**

   To start the Dare FTP Manager application, run:

   ```
   start.bat
   ```

   This will activate the Conda environment and launch the Electron application.

5. **Build Distributable (Optional)**

   If you want to create an installable package of the application, run:

   ```
   build.bat
   ```

   The resulting installers will be placed in the `dist` directory.

## Conda Environment Details

The setup creates a Conda environment with:

- Python 3.9
- pyftpdlib (FTP server library)
- psutil (Process and system utilities)

You can manually activate the environment with:

```bash
conda activate dare_ftp_manager
```

## Troubleshooting

- **Conda Not Found**: Make sure Conda is in your PATH and initialized for your shell
- **Environment Creation Fails**: Check your internet connection and Conda installation
- **Node.js Missing**: Install Node.js and ensure it's in your PATH
- **Permission Issues**: Run the command prompt as administrator if needed
- **Script Errors**: Make sure all files are in the expected locations

## Manually Creating the Conda Environment

If the batch file doesn't work, you can manually create the environment:

```bash
cd C:\ai_repos\tempering_prediction
conda env create -f environment.yml
conda activate dare_ftp_manager
npm install
```

## Additional Notes

- The Conda environment only needs to be created once
- Always use the provided batch files to ensure the Conda environment is activated
- If you need to add more Python dependencies, edit the `environment.yml` file and run `conda env update -f environment.yml`

For any issues or questions, refer to the documentation or contact the IT department.
