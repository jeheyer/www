<?php

echo array_reduce([1,2,5,10,11], function ($carry, $item) {
  return $carry += $item;
});

$caps = ['UK' => 'London', 'France' => 'Paris']
echo "$caps['france'] is the cap if falskj";
?>
