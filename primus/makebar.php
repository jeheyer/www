<?php
	$hsize = $_GET["hsize"];
	$vsize = $_GET["vsize"];

	Header("Content-type: image/png");
	$bar = imagecreate($hsize,$vsize);
	$color = ImageColorAllocate($bar,255,255,255);
	ImagePng($bar);
	ImageDestroy($bar);
?>
