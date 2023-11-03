# OAuth with Flask and TailwindCSS Demo

Instructions will be shown for PC and macOS/Linux when possible.


## Setting up (General steps)
- Open a terminal (e.g. Command Prompt, iTerm2, Terminal, Warp et al)
- Use `cd` to change into your repos folder
- Use `cd` to change into the project's folder
- Create a Python Virtual Environment
- Activate the Python venv
- Install the Requirements for the app
- Run the application
- Visit the application in a web browser
- Try authenticating with your GitHub account

We recommend updating your pip...

```shell
python -m pip install --upgrade pip
```


### How to get to your profile folder in a terminal:

- **PC Cmd**: `cd %userprofile%`
- **Mac/Linux**: `cd ~`

If you are "*lost*" then the appropriate choice from those two commands will put you at a starter point that will be familiar (or become familiar).

### PC Specific
We presume you have a "Source\Repos" folder for your repositories.
- Open CMD or Windows Terminal (Command Prompt)
- ```shell
  cd Source\Repos
  git clone https://github.com/AdyGCode/ICT50220-IP4RIoT-POR-Pt7-OAuth-Demo.git 
  cd ICT50220-IP4RIoT-POR-Pt7-OAuth-Demo
  python -m venv venv
  .\venv\Scripts\activate
  python -m pip install -r requirements.txt
  flask run --port=8192 --host=127.0.0.1 --reload
  ```
In a second terminal do the following:

- ```shell
  cd Source\Repos
  cd ICT50220-IP4RIoT-POR-Pt7-OAuth-Demo
  npm install
  npm update
  npx tailwindcss -i ./src/input.css -o ./static/css/site.css --watch
  ```
  
### PC Specific (TAFE)
Due to security restrictions at TAFE, we sometimes need to add extra steps to execute items such as NPM.

If you try running `npm` and it cannot be found then you are able to temporarily add nodejs to your path...

In the terminal you wish to run npm do the following, presuming that Laragon is installed, and you have NodeJS v18...

```shell
SET PATH=%PATH%;c:\laragon\bin\nodejs\node-v18 
```
In some labs you may find Laragon in `c:\ProgramData\Laragon`.


### MacOS Specific

These instructions need to be added.

Please feel free to propose the instructions required.

### Linux Specific

These instructions need to be added.

Please feel free to propose the instructions required.
