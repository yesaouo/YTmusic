<?php
  if (isset($_POST["download"])) {
    $command = 'sudo python ytmusic.py "1" "'.$_POST["folder-path"].'" "'.$_POST["url"].'"';
    $result = shell_exec($command);
    echo $result;
    header("Location: http://192.168.0.6");
    exit;
  }elseif (isset($_POST["path"]) && isset($_POST["file-path"])) {
    $command = 'sudo rm "'.$_POST["file-path"].'"';
    $result = shell_exec($command);
    echo $result;
    $command = 'sudo python ytmusic.py "2" "'.$_POST["path"].'"';
    $result = shell_exec($command);
    echo $result;
    header("Location: http://192.168.0.6");
    exit;
  }
?>