<?php

$command = escapeshellcmd('/home/administrator/print-schedule/main.py /home/administrator/print-schedule/test.json /home/administrator/print-schedule/outputs/out.png');
$output = shell_exec($command);
echo $output;

?>