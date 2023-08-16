### Prerequisites

* Setup terminal and pip
  ```sh
  python -m pip install --upgrade pip setuptools virtualenv
  ```
* Create virtual environment
  ```sh
  python -m virtualenv kivy_venv
  kivy_venv\Scripts\activate
  ```
* Kivy
  ```sh
  pip install "kivy[base]" kivy_examples
  ```
* PyTube
  ```sh
  pip install pytube
  ```
* Pyinstaller
  ```sh
  pip install pyinstaller==5.6.2
  ```

### Installation

```sh
python -m PyInstaller YTmusic.spec
```
