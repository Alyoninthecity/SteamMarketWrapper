<?php $url = "https://sitoscuolamagnifica.altervista.org/TPSIT/index.php";
$page = file_get_contents($url);
$outfile = "copy.html";
file_put_contents($outfile, $page);
$outfile;