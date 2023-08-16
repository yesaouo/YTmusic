<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/yesaouo/YTmusic">
    <img src="Windows/resources/icon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">YTmusic</h3>

  <p align="center">
    An awesome YouTube music downloader to jumpstart your music player!
    <br />
    <a href="https://github.com/yesaouo/YTmusic"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/yesaouo/YTmusic/issues">Report Bug / Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#windows-mode-1">Windows mode</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#server-mode-1">Server mode</a>
      <ul>
        <li><a href="#prerequisites-1">Prerequisites</a></li>
        <li><a href="#installation-1">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
There are many great YouTube downloader available on GitHub; however, my project has some features that others don't. I want to create a music player that it can combine download and play functionality -- I think this is it.

<br />
<div align="center">
  <a href="https://github.com/yesaouo/YTmusic/tree/main/Windows">
    <img src="https://user-images.githubusercontent.com/88719692/214229445-3c902d42-140c-450a-a7ff-2e2aa071ad4d.png">
  </a>

  <h3 align="center">Windows mode</h3>

  <p align="center">
    Using Python Kivy library to develop GUI desktop applications.
    <br />
    <a href="https://github.com/yesaouo/YTmusic/tree/main/Windows"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>

<br />
<div align="center">
  <a href="https://github.com/yesaouo/YTmusic/tree/main/Raspberry_Pi">
    <img src="https://user-images.githubusercontent.com/88719692/214233621-7cc5fe2d-79ef-460d-b3f0-6dc155a8acf1.png">
  </a>

  <h3 align="center">Server mode</h3>

  <p align="center">
    Hosting a server with a Raspberry Pi.
    <br />
    <a href="https://github.com/yesaouo/YTmusic/tree/main/Raspberry_Pi"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>

* Windows mode allows users to easily download music on the computer and listen to local music on browser.
* Server mode allows users to download and store music using a server host.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Windows mode
Use Windows 10 as a demonstration.

### Installation
Download `Windows/dist/YTmusic/` and execute the exe file.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Server mode
Use Raspberry Pi 4 as a demonstration.
### Prerequisites

* Setup terminal and pip
  ```sh
  sudo apt-get update
  ```
  ```sh
  sudo apt-get install apache2
  ```
  ```sh
  sudo apt-get install python3
  ```
  ```sh
  sudo apt install python3-pip
  ```
* PyTube
  ```sh
  sudo -H pip install pytube
  ```

### Installation

1. ```sh
   cd /var/www/html
   ```
2. Clone files in `Raspberry_Pi`
3. Use `ifconfig` to find your ip
4. Open browser and enter your ip

<p align="right">(<a href="#readme-top">back to top</a>)</p>
